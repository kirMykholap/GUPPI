"""`guppi sprint [--check | --hi]` — `vault/wiki/sprint.md` written from the sprint page.

The sprint is a page: the one live Entity under `vault/wiki/entities/` whose slug starts
with `entity-sprint-`; its `estimates` are the Definition of done, its `## Milestones` the
Slices in order, its `## Backlog` the items without a turn, each item a wikilink to a page
or a plain line — shown by `guppi backlog` in `vault/wiki/backlog.md`, never rendered here. This script writes `vault/wiki/sprint.md` from it:
`# Sprint`; `## <id>`, the slug without `entity-sprint-`, so `sprint_id` and the archive
path read what they read before; the `## Purpose` text as it is; `**Done when**`, one line
per Estimate of the page — `- [x]` when `passed`, `- [ ]` otherwise, the Estimate's
`purpose` and its status; then `## Milestones` — the current milestone, the first `### `
with an item not done or with no item, whole: its heading `### [ ] <name>` and each item
`- [[slug]] — <text>` as `- [x]` when every page it names before the first ` — ` is
`built`, `passed` or `archived`, `- [ ]` otherwise, their statuses in the order of the
slugs and, when present, their `deferred_by` after ` · `; a wikilink after the ` — ` is
text and holds no tick back; a closed
milestone — every item `[x]`, at least one — as one line `### [x] <name>`; every later one
as one line `### [ ] <name> — N items: ` and its items by name, the pages it names or the
text itself, without a tick or a status; a blank line follows every `### `
line, collapsed or whole, so each heading stands between blank lines; a line
naming no page before the
` — ` is a note — a task not yet cut into pages: `- [ ] <text>`, never ticked, so a
milestone holding one stays open, and it leaves only by the `update` of the Case that cuts
it; then the `## Closed` section copied as it is. An item of `## Milestones` or
an Estimate whose slug has no live or archived page, or two sprint pages: one line on
stderr, exit 1, the file not written; the `## Backlog` is not read, so a slug there without
a page is no error.

With no live sprint page, after the close of a sprint, the script writes the closed form
and exits 0: `# Sprint`, the heading `## <id> — closed` and the line `No
sprint is open since the close of <id>.`, `<id>` the id the first `## ` heading of the file
named before, read by `sprint_id` of `guppi/materialize.py`, so a file already marked closed
keeps its id and `sprint_id` reads it from the closed heading. `closed_heading` is the one
form of the mark: `closed_form` writes it and `closed_id` judges a heading by it. No live
sprint page and no file: one line on stderr, exit 1, nothing written.

`--hi` is the `UserPromptSubmit` hook of `rule-skill-sprint-open`: it reads the
payload on stdin, and when the prompt is `/hi` by `is_hi_prompt` of `guppi/event.py` and
`closed_id` finds the mark on the first heading of `vault/wiki/sprint.md`, it prints into the
agent's context one line that names the closed sprint and tells the agent to start the
skill `/sprint-open` before the Frontier. Any other prompt, an open heading and a missing
file print nothing; the hook writes no file, exits 0 in every case, and an error of its own
is one line on stderr.

`--check` renders in memory and compares: one line on stdout — `sprint:
vault/wiki/sprint.md differs from entity-sprint-<id>`, or `… differs from the closed form of
<id>` with no live sprint page — and exit 1 when the file differs,
silence and exit 0 when it is the same, nothing written either way; `make lint` runs it
after `render --check`. Once the plain `guppi sprint` wrote the file and exits
0, it ticks every unticked task line that opens with a code span holding `guppi sprint` —
never a `read` line that names the command later, nor a line whose code span holds `guppi
sprint-close`, which that command ticks itself — in the `spec.md` of every unit under
`raw/` whose yaml is applied whole, a carried-over unit passed by; `--check` and an exit 1
tick nothing; the helper is `render.tick_command_lines`. The file holds
nothing beyond this: the librarian runs the script after `cleanup` and `render`, and the
governed-files hook refuses a hand edit (`governs` on `rule-sprint`). Rule page:
`vault/wiki/rules/rule-sprint.md`.
"""

import argparse
import re
import sys
from pathlib import Path

from guppi.event import is_hi_prompt, project_root, read_payload
from guppi.ledger import SPRINT_PAGE, is_sprint_page
from guppi.lint import archived_slugs, as_list
from guppi.materialize import sprint_id
from guppi.pages import Page, read_vault, wiki_root
from guppi.render import tick_command_lines

DONE = {"built", "passed", "archived"}
WIKILINK = re.compile(r"\[\[([^\]|#]+)\]\]")
DASH = " — "
CLOSED = DASH + "closed"
SLICE = re.compile(r"^### (.+)$")


def sprint_pages_live(pages: dict[str, list[Page]]) -> list[Page]:
    return [p for p in pages["entities"] if is_sprint_page(p.slug) and not p.error]


def sprint_page(pages: dict[str, list[Page]]) -> Page | None:
    found = sprint_pages_live(pages)
    return found[0] if len(found) == 1 else None


def closed_heading(sprint: str) -> str:
    """The heading of a closed sprint: the one form, which `closed_form` writes
    and `closed_id` judges by, and which the hook of `rule-skill-sprint-open` reads."""
    return f"## {sprint}{CLOSED}"


def closed_form(sprint: str) -> str:
    """The whole file with no live sprint page, after the close of `sprint`."""
    return (
        f"# Sprint\n\n{closed_heading(sprint)}\n\nNo sprint is open since the close of {sprint}.\n"
    )


def closed_id(text: str) -> str | None:
    """The id of the closed sprint when the first `## ` heading of `text` carries the mark,
    else None."""
    for line in text.splitlines():
        if line.startswith("## "):
            sprint = line[3:].split(" ", 1)[0].strip()
            return sprint if line.rstrip() == closed_heading(sprint) else None
    return None


def tick(done: bool) -> str:
    return "[x]" if done else "[ ]"


def item_slugs(body: str) -> list[str]:
    """The pages of an item: every `[[slug]]` before the first ` — `. An empty
    list means a note — a task not yet cut into pages."""
    return [s.strip() for s in WIKILINK.findall(body.split(DASH)[0])]


def item_statuses(
    slugs: list[str], by_slug: dict[str, Page], archived: set[str]
) -> tuple[list[str], str | None]:
    """`(statuses, missing)`: the status of each page an item names, `archived` for a slug
    found only in the archive; `missing` is the first slug with no page, and stops the walk.
    The one judgment of an item's pages: `backlog.py` imports it."""
    statuses: list[str] = []
    for slug in slugs:
        page = by_slug.get(slug)
        if page is not None:
            statuses.append(str(page.props.get("status") or ""))
        elif slug in archived:
            statuses.append("archived")
        else:
            return statuses, slug
    return statuses, None


def is_done(statuses: list[str]) -> bool:
    """An item is done when each of its pages is `built`, `passed` or `archived`."""
    return all(s in DONE for s in statuses)


def plain_or_item(
    line: str, by_slug: dict[str, Page], archived: set[str]
) -> tuple[str | None, str | None]:
    """`(rendered, missing)`: an item by the statuses of every page it names before the
    first ` — ` — `[x]` when each is `built`, `passed` or `archived`, the statuses after
    ` · ` in the order of the slugs; a line naming none there is a note, `- [ ] <text>`,
    never ticked. `missing` is the first slug without a page."""
    if not line.startswith("- "):
        return line, None
    body = line[2:]
    slugs = item_slugs(body)
    if not slugs:
        return f"- [ ] {body}", None
    statuses, missing = item_statuses(slugs, by_slug, archived)
    if missing:
        return None, missing
    deferred = [
        slug
        for name in slugs
        if name in by_slug
        for slug in as_list(by_slug[name].props.get("deferred_by"))
    ]
    rendered = f"- {tick(is_done(statuses))} {body} · " + ", ".join(statuses)
    if deferred:
        rendered += " · " + ", ".join(deferred)
    return rendered, None


def item_name(line: str) -> str:
    """The name of an item on a collapsed milestone line: the pages it names, as
    they stand, for an item; the text itself for a note; no tick, no status."""
    body = line[2:]
    head = body.split(DASH)[0].strip()
    return head if item_slugs(body) else body


def milestone_blocks(text: str) -> list[tuple[str | None, list[str]]]:
    """`(heading line, lines)` of `## Milestones` in order, the text before the first `### `
    under `None`; blank lines kept, so `generate`'s move writes an untouched block
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
    """The lines of `## Milestones`: the current one whole, a closed one and a
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
            out += [f"### [x] {name}", ""]
        else:  # a later one: the count, then its items by name
            count = f"{len(lines)} item{'' if len(lines) == 1 else 's'}"
            names = ", ".join(item_name(line) for line in items)
            out += [f"### [ ] {name} — {count}" + (f": {names}" if names else ""), ""]
    while out and out[-1] == "":
        out.pop()
    return out, None


def render(page: Page, by_slug: dict[str, Page], archived: set[str]) -> tuple[str | None, str]:
    """`(text, error)`: the whole file, or the error line."""
    parts = ["# Sprint", "", f"## {page.slug[len(SPRINT_PAGE) :]}", ""]
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
    closed = (page.section("## Closed") or "").strip()
    if closed:
        parts += ["## Closed", "", closed, ""]
    return "\n".join(parts), ""


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi sprint", description=__doc__.split("\n\n")[1])
    p.add_argument(
        "--check", action="store_true", help="name the file when it differs; write nothing"
    )
    p.add_argument(
        "--hi", action="store_true", help="the UserPromptSubmit hook: name a closed sprint at /hi"
    )
    return p


def hi_hook(project_dir: Path, stdin, stdout, stderr) -> int:
    """At `/hi`, a first heading that carries the closed mark prints one line that tells
    the agent to start `/sprint-open`; anything else prints nothing. Exit 0."""
    try:
        if not is_hi_prompt(read_payload(stdin).get("prompt")):
            return 0
        target = wiki_root(project_dir) / "sprint.md"
        closed = closed_id(target.read_text(encoding="utf-8")) if target.is_file() else None
        if closed:
            print(
                f"sprint: no sprint is open since the close of {closed}: start the skill "
                "/sprint-open before the Frontier",
                file=stdout,
            )
    except Exception as exc:  # noqa: BLE001 — a hook error is one line, never a block
        print(f"sprint --hi: {exc}", file=stderr)
    return 0


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None):
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    args = parser().parse_args(argv)
    if args.hi:
        return hi_hook(project_dir, stdin, stdout, stderr)
    wiki = wiki_root(project_dir)
    target = wiki / "sprint.md"
    pages = read_vault(wiki)
    found = sprint_pages_live(pages)
    if len(found) > 1:
        print(f"sprint: {len(found)} live {SPRINT_PAGE}<id> pages", file=stderr)
        return 1
    if not found:  # after the close, the closed form
        if not target.is_file():
            print(
                f"sprint: no live {SPRINT_PAGE}<id> page and no vault/wiki/sprint.md", file=stderr
            )
            return 1
        closed = sprint_id(project_dir)
        text, source = closed_form(closed), f"the closed form of {closed}"
    else:
        page = found[0]
        by_slug = {p.slug: p for category in pages.values() for p in category if not p.error}
        text, error = render(page, by_slug, archived_slugs(wiki))
        if text is None:
            print(error, file=stderr)
            return 1
        source = page.slug
    if args.check:  # compare, name, write nothing
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current == text:
            return 0
        print(f"sprint: vault/wiki/sprint.md differs from {source}", file=stdout)
        return 1
    target.write_text(text, encoding="utf-8", newline="\n")
    tick_command_lines(project_dir, "guppi sprint")  # the sprint lines of the applied Specs
    return 0
