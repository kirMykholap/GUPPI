"""`guppi render [--check]` — the harness written from its Rule pages.

Every page under `vault/wiki/rules/` with `enforcement: render` carries the text of a
harness file in its `## Render` section, between `<!-- slug -->` and `<!-- /slug -->`.
A `full` page's text becomes the whole file named by `governs`, without those outer
markers; a lone `<!-- child -->` line in it is replaced by the child's text, markers kept,
in the order of `children`, one blank line between blocks. A `partial` page whose file no
`full` page owns is spliced into the existing file between its markers, which stay.
`--check` renders in memory, names every file that differs, exits 1 and writes nothing.
Rule page: `vault/wiki/rules/rule-render-harness.md`.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from guppi.event import project_root
from guppi.pages import Page, read_category, wiki_root

RENDER = "## Render"


class RenderError(Exception):
    pass


@dataclass
class Unit:
    page: Page
    governs: str
    mode: str
    text: str  # between the page's own markers, exclusive


def marker(slug: str, close: bool = False) -> str:
    return f"<!-- {'/' if close else ''}{slug} -->"


def own_text(page: Page) -> str:
    section = page.section(RENDER)
    if section is None:
        raise RenderError(f"{page.slug}: no {RENDER} section")
    lines = section.splitlines()
    opening, closing = marker(page.slug), marker(page.slug, close=True)
    if lines[:1] != [opening] or lines[-1:] != [closing]:
        raise RenderError(f"{page.slug}: {RENDER} is not wrapped in {opening} … {closing}")
    return "\n".join(lines[1:-1])


def block(unit: Unit) -> str:
    """The unit's text with its own markers around it: how a child or a partial lands."""
    return "\n".join([marker(unit.page.slug), unit.text, marker(unit.page.slug, close=True)])


def render_units(pages: list[Page]) -> dict[str, Unit]:
    units: dict[str, Unit] = {}
    for page in pages:
        if page.error:
            continue
        if page.props.get("enforcement") != "render":
            continue
        governs, mode = page.props.get("governs"), page.props.get("render_mode")
        if not governs or mode not in ("full", "partial"):
            raise RenderError(f"{page.slug}: a render page needs governs and render_mode")
        units[page.slug] = Unit(page, str(governs), str(mode), own_text(page))
    return units


def join_blocks(lines: list[str]) -> str:
    """Two adjacent blocks are separated by one blank line."""
    out: list[str] = []
    for line in lines:
        if out and re.match(r"^<!-- [^/].* -->$", line) and re.match(r"^<!-- /.* -->$", out[-1]):
            out.append("")
        out.append(line)
    return "\n".join(out)


def render_full(unit: Unit, units: dict[str, Unit]) -> str:
    children = unit.page.props.get("children") or []
    lines: list[str] = []
    replaced: set[str] = set()
    for line in unit.text.splitlines():
        match = re.match(r"^<!-- ([^/\s]+) -->$", line)
        child = match.group(1) if match else None
        if child in children:
            other = units.get(child)
            if other is None:
                raise RenderError(f"{unit.page.slug}: child {child} is not a render page")
            if other.governs != unit.governs:
                raise RenderError(f"{unit.page.slug}: child {child} governs another file")
            lines.extend(block(other).splitlines())
            replaced.add(child)
        else:
            lines.append(line)
    missing = [child for child in children if child not in replaced]
    if missing:
        raise RenderError(f"{unit.page.slug}: no marker line for child {missing[0]}")
    return join_blocks(lines) + "\n"


def render_partial(unit: Unit, current: str | None, path: str) -> str:
    if current is None:
        raise RenderError(f"{unit.page.slug}: {path} does not exist, nothing to splice into")
    opening, closing = marker(unit.page.slug), marker(unit.page.slug, close=True)
    lines = current.splitlines()
    if opening not in lines or closing not in lines:
        raise RenderError(f"{unit.page.slug}: {path} has no {opening} … {closing} markers")
    start, end = lines.index(opening), lines.index(closing)
    if end < start:
        raise RenderError(f"{unit.page.slug}: {path} closes {closing} before it opens")
    lines[start : end + 1] = block(unit).splitlines()
    return "\n".join(lines) + "\n"


def plan(project_dir: Path, units: dict[str, Unit]) -> dict[str, str]:
    """`governs` → the text the file must hold. Full pages first, then the partials no full
    page owns, in slug order; a file is read from disk at most once."""
    outputs: dict[str, str] = {}
    fulls = {u.governs: u for u in units.values() if u.mode == "full"}
    seen: dict[str, str] = {}
    for unit in sorted(units.values(), key=lambda u: u.page.slug):
        if unit.mode == "full":
            if unit.governs in seen:
                raise RenderError(
                    f"{unit.page.slug}: {unit.governs} is also rendered in full by {seen[unit.governs]}"
                )
            seen[unit.governs] = unit.page.slug
            outputs[unit.governs] = render_full(unit, units)
    for unit in sorted(units.values(), key=lambda u: u.page.slug):
        if unit.mode != "partial":
            continue
        owner = fulls.get(unit.governs)
        if owner is not None:
            if unit.page.slug not in (owner.page.props.get("children") or []):
                raise RenderError(
                    f"{unit.page.slug}: {unit.governs} is owned by {owner.page.slug}, "
                    "which does not list it as a child"
                )
            continue
        path = project_dir / unit.governs
        current = outputs.get(unit.governs)
        if current is None and path.exists():
            current = path.read_text(encoding="utf-8")
        outputs[unit.governs] = render_partial(unit, current, unit.governs)
    return outputs


def differing(project_dir: Path, outputs: dict[str, str]) -> list[str]:
    stale = []
    for governs, text in outputs.items():
        path = project_dir / governs
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            stale.append(governs)
    return stale


def write_all(project_dir: Path, outputs: dict[str, str]) -> None:
    for governs, text in outputs.items():
        path = project_dir / governs
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi render", description=__doc__.split("\n\n")[1])
    p.add_argument("--check", action="store_true", help="report files that differ; write nothing")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        args = parser().parse_args(argv)
        pages = read_category(wiki_root(project_dir), "rules")
        outputs = plan(project_dir, render_units(pages))
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    except RenderError as exc:
        print(f"render: {exc}", file=stderr)
        return 1
    if args.check:
        stale = differing(project_dir, outputs)
        for governs in stale:
            print(f"render: {governs} differs from its Rule page", file=stdout)
        return 1 if stale else 0
    write_all(project_dir, outputs)
    return 0
