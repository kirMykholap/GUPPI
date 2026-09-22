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
`- [[slug]] — <text>` as `- [x]` when every page it names before the first ` — ` is
`built`, `passed` or `archived`, `- [ ]` otherwise, their statuses in the order of the
slugs and, when present, their `deferred_by` after ` · `; a wikilink after the ` — ` is
text and holds no tick back (case 313); a closed
milestone — every item `[x]`, at least one — as one line `### [x] <name>`; every later one
as one line `### [ ] <name> — N items: ` and its items by name, the pages it names or the
text itself, without a tick or a status (case 236); a line naming no page before the
` — ` is a note — a task not yet cut into pages: `- [ ] <text>`, never ticked, so a
milestone holding one stays open, and it leaves only by the `update` of the Case that cuts
it (case 313); then `## Backlog`, each item a
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
WIKILINK = re.compile(r"\[\[([^\]|#]+)\]\]")
DASH = " — "
SLICE = re.compile(r"^### (.+)$")


def sprint_page(pages: dict[str, list[Page]]) -> Page | None:
    found = [p for p in pages["entities"] if p.slug.startswith(PREFIX) and not p.error]
    return found[0] if len(found) == 1 else None


def tick(done: bool) -> str:
    return "[x]" if done else "[ ]"


def item_slugs(body: str) -> list[str]:
    """The pages of an item: every `[[slug]]` before the first ` — ` (case 313). An empty
    list means a note — a task not yet cut into pages."""
    return [s.strip() for s in WIKILINK.findall(body.split(DASH)[0])]


def plain_or_item(
    line: str, by_slug: dict[str, Page], archived: set[str]
) -> tuple[str | None, str | None]:
    """`(rendered, missing)`: an item by the statuses of every page it names before the
    first ` — ` — `[x]` when each is `built`, `passed` or `archived`, the statuses after
    ` · ` in the order of the slugs; a line naming none there is a note, `- [ ] <text>`,
    never ticked (case 313). `missing` is the first slug without a page."""
    if not line.startswith("- "):
        return line, None
    body = line[2:]
    slugs = item_slugs(body)
    if not slugs:
        return f"- [ ] {body}", None
    statuses: list[str] = []
    deferred: list[str] = []
    for slug in slugs:
        page = by_slug.get(slug)
        if page is not None:
            statuses.append(str(page.props.get("status") or ""))
            deferred += as_list(page.props.get("deferred_by"))
        elif slug in archived:
            statuses.append("archived")
        else:
            return None, slug
    rendered = f"- {tick(all(s in DONE for s in statuses))} {body} · " + ", ".join(statuses)
    if deferred:
        rendered += " · " + ", ".join(deferred)
    return rendered, None


def item_name(line: str) -> str:
    """The name of an item on a collapsed milestone line (case 236): the pages it names, as
    they stand, for an item; the text itself for a note; no tick, no status."""
    body = line[2:]
    head = body.split(DASH)[0].strip()
    return head if item_slugs(body) else body


def milestone_blocks(text: str) -> list[tuple[str | None, list[str]]]:
    """`(heading line, lines)` of `## Milestones` in order, the text before the first `### `
    under `None`; blank lines kept, so `generate`'s move (case 354) writes an untouched block
    back as it stood. The one parse of the section: `split_milestones` reads it too."""
    blocks: list[tuple[str | None, list[str]]] = [(None, [])]
    for raw in text.splitlines():
        line = raw.rstrip()
        if SLICE.match(line):
            blocks.append((line, []))
        else:
            blocks[-1][1].append(line)
    return blocks


def split_milestones(text: str) -> list[tuple[str, list[str]]]:
    """`(name, item lines)` per `### <name>` heading, in order; a line before the first
    heading is dropped."""
    return [
        (SLICE.match(heading).group(1), [line for line in lines if line])
        for heading, lines in milestone_blocks(text)
        if heading is not None
    ]


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
