"""`guppi sprint [--check]` — `vault/wiki/sprint.md` written from the sprint page.

The sprint is a page: the one live Entity under `vault/wiki/entities/` whose slug starts
with `entity-sprint-`; its `estimates` are the Definition of done, its `## Milestones` the
Slices in order, its `## Backlog` the items without a turn, each item a wikilink to a page
or a plain line. This script writes `vault/wiki/sprint.md` from it (cases 209.1, 229.2):
`# Sprint`; `## <id>`, the slug without `entity-sprint-`, so `sprint_id` and the archive
path read what they read before; the `## Purpose` text as it is; `**Done when**`, one line
per Estimate of the page — `- [x]` when `passed`, `- [ ]` otherwise, the Estimate's
`purpose` and its status; then `## Milestones` — the current milestone, the first `### `
with an item not done or with no item, whole: its heading `### [ ] <name>` and each item
`- [[slug]] — <text>` as `- [x]` when the page `slug` is `built`, `passed` or `archived`,
`- [ ]` otherwise, its status and, when present, its `deferred_by` after ` · `; a closed
milestone — every item `[x]`, at least one — as one line `### [x] <name>`; every later one
as one line `### [ ] <name> — N items: ` and its items by name, `[[slug]]` or the plain
text, without a tick or a status (case 236); a plain item `- <text>` renders `- [ ] <text>`
and is never ticked, so a milestone holding one stays open; then `## Backlog`, each item a
line the same way; the `## Closed` section copied as it is. An item whose slug has no
live or archived page, or no sprint page, or two: one line on stderr, exit 1, the file
not written. `--check` renders in memory and compares: one line on stdout — `sprint:
vault/wiki/sprint.md differs from entity-sprint-<id>` — and exit 1 when the file differs,
silence and exit 0 when it is the same, nothing written either way; `make lint` runs it
after `render --check` (case 227). Once the plain `guppi sprint` wrote the file and exits
0, it ticks every unticked task line that opens with a code span holding `guppi sprint` —
never a `read` line that names the command later — in the `spec.md` of every unit under
`raw/` whose yaml is applied whole, a carried-over unit passed by; `--check` and an exit 1
tick nothing (case 250.2; the helper is `render.tick_command_lines`). The file holds
nothing beyond this: the librarian runs the script after `cleanup` and `render`, and the
governed-files hook refuses a hand edit (`governs` on `rule-sprint`). Rule page:
`vault/wiki/rules/rule-sprint.md`.
"""

import argparse
import re
import sys
from pathlib import Path

from guppi.event import project_root
from guppi.lint import archived_slugs, as_list
from guppi.pages import Page, read_vault, wiki_root
from guppi.render import tick_command_lines

PREFIX = "entity-sprint-"
DONE = {"built", "passed", "archived"}
ITEM = re.compile(r"^- \[\[([^\]|#]+)\]\](.*)$")
SLICE = re.compile(r"^### (.+)$")


def sprint_page(pages: dict[str, list[Page]]) -> Page | None:
    found = [p for p in pages["entities"] if p.slug.startswith(PREFIX) and not p.error]
    return found[0] if len(found) == 1 else None


def tick(done: bool) -> str:
    return "[x]" if done else "[ ]"


def item_line(slug: str, text: str, by_slug: dict[str, Page], archived: set[str]) -> str | None:
    page = by_slug.get(slug)
    if page is not None:
        status = str(page.props.get("status") or "")
        deferred = as_list(page.props.get("deferred_by"))
    elif slug in archived:
        status, deferred = "archived", []
    else:
        return None
    line = f"- {tick(status in DONE)} [[{slug}]]{text} · {status}"
    if deferred:
        line += " · " + ", ".join(deferred)
    return line


def plain_or_item(
    line: str, by_slug: dict[str, Page], archived: set[str]
) -> tuple[str | None, str | None]:
    """`(rendered, missing)`: a wikilink item by the status of its page, a plain item
    `- <text>` as `- [ ] <text>`, never ticked; `missing` the slug without a page."""
    item = ITEM.match(line)
    if item:
        rendered = item_line(item.group(1).strip(), item.group(2), by_slug, archived)
        return (rendered, None) if rendered is not None else (None, item.group(1).strip())
    if line.startswith("- "):
        return f"- [ ] {line[2:]}", None
    return line, None


def item_name(line: str) -> str:
    """The name of an item on a collapsed milestone line (case 236): `[[slug]]` for a
    wikilink item, the text itself for a plain one; no tick, no status."""
    item = ITEM.match(line)
    return f"[[{item.group(1).strip()}]]" if item else line[2:]


def split_milestones(text: str) -> list[tuple[str, list[str]]]:
    """`(name, item lines)` per `### <name>` heading, in order; a line before the first
    heading is dropped."""
    out: list[tuple[str, list[str]]] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        heading = SLICE.match(line)
        if heading:
            out.append((heading.group(1), []))
        elif out and line:
            out[-1][1].append(line)
    return out


def render_milestones(
    text: str, by_slug: dict[str, Page], archived: set[str]
) -> tuple[list[str], str | None]:
    """The lines of `## Milestones` (case 229.2): the current one whole, a closed one and a
    later one as one line each; the first slug without a page, else None."""
    milestones = split_milestones(text)
    rendered: list[list[str]] = []
    for _name, items in milestones:
        lines: list[str] = []
        for line in items:
            out, missing = plain_or_item(line, by_slug, archived)
            if missing:
                return [], missing
            lines.append(str(out))
        rendered.append(lines)
    current: int | None = None
    for index, lines in enumerate(rendered):
        if not lines or any(not line.startswith("- [x]") for line in lines):
            current = index
            break
    out: list[str] = []
    for index, ((name, items), lines) in enumerate(zip(milestones, rendered, strict=True)):
        closed = bool(lines) and all(line.startswith("- [x]") for line in lines)
        if index == current:
            out += [f"### [ ] {name}", ""] + lines + ([""] if lines else [])
        elif closed:
            out.append(f"### [x] {name}")
        else:  # a later one: the count, then its items by name (case 236)
            count = f"{len(lines)} item{'' if len(lines) == 1 else 's'}"
            names = ", ".join(item_name(line) for line in items)
            out.append(f"### [ ] {name} — {count}" + (f": {names}" if names else ""))
    while out and out[-1] == "":
        out.pop()
    return out, None


def render_backlog(
    backlog: str, by_slug: dict[str, Page], archived: set[str]
) -> tuple[list[str], str | None]:
    """The lines of `## Backlog`: each item a line, never a tick on a plain one; the first
    slug without a page, else None."""
    out: list[str] = []
    for raw in backlog.splitlines():
        line = raw.rstrip()
        rendered, missing = plain_or_item(line, by_slug, archived)
        if missing:
            return out, missing
        out.append(str(rendered))
    return out, None


def render(page: Page, by_slug: dict[str, Page], archived: set[str]) -> tuple[str | None, str]:
    """`(text, error)`: the whole file, or the error line."""
    parts = ["# Sprint", "", f"## {page.slug[len(PREFIX) :]}", ""]
    purpose = (page.section("## Purpose") or "").strip()
    if purpose:
        parts += [purpose, ""]
    parts += ["**Done when**", ""]
    for slug in as_list(page.props.get("estimates")):
        estimate = by_slug.get(slug)
        if estimate is None:
            return None, f"sprint: {slug}: no live or archived page"
        status = str(estimate.props.get("status") or "")
        parts.append(f"- {tick(status == 'passed')} {estimate.props.get('purpose', '')} · {status}")
    parts.append("")
    milestones = (page.section("## Milestones") or "").strip()
    lines, missing = render_milestones(milestones, by_slug, archived)
    if missing:
        return None, f"sprint: {missing}: no live or archived page"
    parts += ["## Milestones", ""] + lines + [""]
    backlog = (page.section("## Backlog") or "").strip()
    lines, missing = render_backlog(backlog, by_slug, archived)
    if missing:
        return None, f"sprint: {missing}: no live or archived page"
    parts += ["## Backlog", ""] + lines + [""]
    closed = (page.section("## Closed") or "").strip()
    if closed:
        parts += ["## Closed", "", closed, ""]
    return "\n".join(parts), ""


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi sprint", description=__doc__.split("\n\n")[1])
    p.add_argument(
        "--check", action="store_true", help="name the file when it differs; write nothing"
    )
    return p


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None):
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    args = parser().parse_args(argv)
    wiki = wiki_root(project_dir)
    pages = read_vault(wiki)
    page = sprint_page(pages)
    if page is None:
        print(f"sprint: no live {PREFIX}<id> page", file=stderr)
        return 1
    by_slug = {p.slug: p for category in pages.values() for p in category if not p.error}
    text, error = render(page, by_slug, archived_slugs(wiki))
    if text is None:
        print(error, file=stderr)
        return 1
    target = wiki / "sprint.md"
    if args.check:  # case 227: compare, name, write nothing
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current == text:
            return 0
        print(f"sprint: vault/wiki/sprint.md differs from {page.slug}", file=stdout)
        return 1
    target.write_text(text, encoding="utf-8", newline="\n")
    tick_command_lines(project_dir, "guppi sprint")  # the sprint lines of the applied Specs
    return 0
