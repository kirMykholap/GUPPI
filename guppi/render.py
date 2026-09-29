"""`guppi render [--check | --sync]` — the harness written from its Rule pages.

Every page under `vault/wiki/rules/` with `enforcement: render` carries the text of a
harness file in its `## Render` section, between `<!-- slug -->` and `<!-- /slug -->`.
A `full` page's text becomes the whole file named by `governs`, without those outer
markers; a lone `<!-- child -->` line in it is replaced by the child's text, markers kept,
in the order of `children`, one blank line between blocks. A file that cannot hold a
comment — today a `.json` target — takes the child's text bare, since the markers would
make it unparsable; the owner is then named by the `<!-- child -->` line of the parent's
body, and `--check` compares the whole file, so nothing is lost but the label (case 85.1). A child that is not a render
page — a script the frame calls by name — contributes nothing and needs no marker; a
marker line for it is an error. A `partial` page whose file no
`full` page owns is spliced into the existing file between its markers, which stay.
A Render may write `{{documentation_lang}}` and `{{chat_lang}}`: the render puts in the name
of the language whose code the `## Render` of `rule-guppi-config` sets for the key, by the
table of `guppi/config.py`, and the page keeps the placeholder, so the next render after a
changed code writes the new name. The codes come from that Render, never from `guppi.toml`,
which is its own output. A placeholder whose name is not a key, a key missing from
`rule-guppi-config` or a code the table does not hold stops the run with nothing written,
the page and the placeholder or key on stderr; a run in which no Render holds a placeholder
reads no `rule-guppi-config` (case 476.1).
`--check` renders in memory, names every file that differs, exits 1 and writes nothing.
`--sync`, the `SessionStart` hook and, since case 115, the `Render:` line of `/hi` after the
pull, prints a unified diff for each file that differs — the file as it is, then the
rendered text — and writes it, so the agent's first turn shows what the render changed: the
pages the librarian updated, or a hand edit that is now gone and may deserve a Case. An
identical file gets neither; a render error goes to stderr and nothing is written. `--sync`
always exits 0, since a `SessionStart` hook cannot block and its stdout is added to the
agent's context.
Claude Code reads the agent files under `.claude/agents/` at session start, so an agent the
librarian renders can be called from the next session (case 139.1): the librarian's render
is its last step before the commit. The rendered files are committed by the librarian, in its own commit
(case 89.2).
Every `.json` target is parsed before anything is written; one that does not parse stops
the whole write and names the file and its page on stderr (case 89.4).
Once the plain `guppi render` wrote the files and exits 0, it ticks — in the `spec.md` of
every unit under `vault/raw/` whose `materialize.yaml` is applied whole, a carried-over
unit passed by — every unticked task line that opens with a code span holding `guppi
render` (cases 226.2, 235; a `read` line that names the command later is not one);
`--check`, `--sync` and an exit 1 tick nothing, and nothing is said either way. A yaml is
applied whole when every entry carries `applied` or `superseded_by` and none `failed`, as
`guppi archive` counts it (case 250.1). The tick is `tick_command_lines`, shared with
`guppi sprint`, which ticks its own lines the same way (case 250.2).
Rule page: `vault/wiki/rules/rule-render-harness.md`.
"""

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from guppi import config
from guppi.event import project_root
from guppi.materialize import is_carried_over, load_yaml, units_with, yaml_path
from guppi.pages import Page, read_category, wiki_root

RENDER = "## Render"
PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")


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


def fill_placeholders(units: dict[str, Unit]) -> None:
    """Case 476.1: each `{{key}}` of a unit's text becomes the name of the language whose
    code the Render of `rule-guppi-config` sets for the key. No placeholder, no read of that
    page; an unknown placeholder, a missing key or an unknown code is a `RenderError`."""
    holders = [unit for unit in units.values() if PLACEHOLDER.search(unit.text)]
    if not holders:
        return
    settings_unit = units.get(config.SETTINGS_PAGE)
    if settings_unit is None:
        raise RenderError(
            f"{holders[0].page.slug}: a placeholder needs the Render of "
            f"{config.SETTINGS_PAGE}, and there is none"
        )
    try:
        settings = config.parse(settings_unit.text, config.SETTINGS_PAGE)
    except config.ConfigError as exc:
        raise RenderError(str(exc)) from exc
    for unit in holders:
        for key in PLACEHOLDER.findall(unit.text):
            if key not in config.KEYS:
                raise RenderError(
                    f"{unit.page.slug}: placeholder {{{{{key}}}}} is not a key of "
                    f"{config.SETTINGS_PAGE}"
                )
        unit.text = PLACEHOLDER.sub(
            lambda match: config.name_of(settings[match.group(1)]), unit.text
        )


def bare_splice(governs: str) -> bool:
    """A file that cannot carry a comment takes a child's text without its markers."""
    return Path(governs).suffix == ".json"


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
            text = other.text if bare_splice(unit.governs) else block(other)
            lines.extend(text.splitlines())
            replaced.add(child)
        else:
            lines.append(line)
    missing = [child for child in children if child not in replaced and child in units]
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


def check_json(outputs: dict[str, str], units: dict[str, Unit]) -> None:
    """Every `.json` target parses, or nothing is written: a file that does not load
    unregisters every hook it carries, and the render is the only writer (case 89.4)."""
    owners = {u.governs: u.page.slug for u in units.values() if u.mode == "full"}
    for governs, text in sorted(outputs.items()):
        if Path(governs).suffix != ".json":
            continue
        try:
            json.loads(text)
        except ValueError as exc:
            owner = owners.get(governs, "no full page")
            raise RenderError(f"{owner}: {governs} does not parse as JSON: {exc}") from exc


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


def command_line(command: str) -> re.Pattern[str]:
    """An unticked task line that opens with the code span holding `command`; a `read`
    line that names the command in a later span is not one (case 235)."""
    return re.compile(r"^- \[ \] `[^`]*" + re.escape(command) + r"[^`]*`")


def applied_whole(data: dict | None) -> bool:
    """A yaml whose every entry carries `applied` or `superseded_by` and none `failed`, as
    `guppi archive` counts it (case 250.1); an empty or absent yaml is not one."""
    if not data:
        return False
    entries = [e for e in data.get("entries") or [] if isinstance(e, dict)]
    return bool(entries) and all(
        (e.get("applied") or e.get("superseded_by")) and not e.get("failed") for e in entries
    )


def tick_command_lines(project_dir: Path, command: str) -> int:
    """Cases 226.2, 250.2: in the `spec.md` of every unit under `raw/` whose yaml is
    applied whole — a carried-over unit passed by — every unticked task line that opens
    with a code span holding `command` becomes `- [x]` (case 235). `render` calls it with
    `guppi render`, `sprint` with `guppi sprint`. The count of lines ticked; nothing is
    said."""
    pattern = command_line(command)
    ticked = 0
    for unit in units_with(project_dir, "materialize.yaml"):
        if is_carried_over(project_dir, unit):
            continue
        if not applied_whole(load_yaml(yaml_path(project_dir, unit))):
            continue
        spec = yaml_path(project_dir, unit).parent / "spec.md"
        if not spec.is_file():
            continue
        lines = spec.read_text(encoding="utf-8").split("\n")
        changed = False
        for index, line in enumerate(lines):
            if pattern.match(line):
                lines[index] = "- [x]" + line[len("- [ ]") :]
                changed = True
                ticked += 1
        if changed:
            spec.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return ticked


def sync(project_dir: Path, outputs: dict[str, str], stdout) -> None:
    """For each file that differs: its unified diff to the rendered text, then the write.
    A missing file diffs against nothing; an identical one is neither printed nor written."""
    stale = differing(project_dir, outputs)
    for governs in stale:
        path = project_dir / governs
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        diff = difflib.unified_diff(
            current.splitlines(keepends=True),
            outputs[governs].splitlines(keepends=True),
            fromfile=f"{governs} (file)",
            tofile=f"{governs} (rendered)",
        )
        for line in diff:
            stdout.write(line if line.endswith("\n") else line + "\n")
    write_all(project_dir, {governs: outputs[governs] for governs in stale})


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi render", description=__doc__.split("\n\n")[1])
    mode = p.add_mutually_exclusive_group()
    mode.add_argument(
        "--check", action="store_true", help="report files that differ; write nothing"
    )
    mode.add_argument(
        "--sync",
        action="store_true",
        help="print a diff for each file that differs, then write it; always exit 0",
    )
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    try:
        pages = read_category(wiki_root(project_dir), "rules")
        units = render_units(pages)
        fill_placeholders(units)
        outputs = plan(project_dir, units)
        check_json(outputs, units)
        if args.sync:
            sync(project_dir, outputs, stdout)
            return 0
    except RenderError as exc:
        print(f"render: {exc}", file=stderr)
        return 0 if args.sync else 1
    except Exception as exc:  # as a SessionStart hook, --sync must not raise
        if not args.sync:
            raise
        print(f"render: sync skipped: {exc}", file=stderr)
        return 0
    if args.check:
        stale = differing(project_dir, outputs)
        for governs in stale:
            print(f"render: {governs} differs from its Rule page", file=stdout)
        return 1 if stale else 0
    write_all(project_dir, outputs)
    tick_command_lines(project_dir, "guppi render")  # the render lines of the applied Specs
    return 0
