"""`guppi sprint` — `vault/wiki/sprint.md` written from the sprint page.

The sprint is a page: the one live Entity under `vault/wiki/entities/` whose slug starts
with `entity-sprint-`; its `estimates` are the Definition of done, its `## Backlog` the open
Slices, each item a wikilink to a page. This script writes `vault/wiki/sprint.md` from it
(case 209.1): `# Sprint`; `## <id>`, the slug without `entity-sprint-`, so `sprint_id` and
the archive path read what they read before; the `## Purpose` text as it is; `**Done when**`,
one line per Estimate of the page — `- [x]` when `passed`, `- [ ]` otherwise, the Estimate's
`purpose` and its status; then the `## Backlog` — each `### <Slice>` as a heading, each item
`- [[slug]] — <text>` as `- [x]` when the page `slug` is `built`, `passed` or `archived`,
`- [ ]` otherwise, its status and, when present, its `deferred_by` after ` · `; a Slice whose
every item is ticked gets `[x]` in its heading, a Slice without items stays open; the
`## Closed` section copied as it is. An item whose slug has no live or archived page, or no
sprint page, or two: one line on stderr, exit 1, the file not written. The file holds
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


def render_backlog(
    backlog: str, by_slug: dict[str, Page], archived: set[str]
) -> tuple[list[str], str | None]:
    """The lines of `## Backlog` with a tick per item and per Slice; the first slug without
    a page, else None."""
    out: list[str] = []
    slice_start: int | None = None
    slice_done = True
    slice_items = 0

    def close_slice():
        if slice_start is not None:
            heading = out[slice_start]
            out[slice_start] = f"### {tick(slice_items > 0 and slice_done)} {heading[4:]}"

    for raw in backlog.splitlines():
        line = raw.rstrip()
        heading = SLICE.match(line)
        item = ITEM.match(line)
        if heading:
            close_slice()
            out.append(line)
            slice_start, slice_done, slice_items = len(out) - 1, True, 0
        elif item:
            rendered = item_line(item.group(1).strip(), item.group(2), by_slug, archived)
            if rendered is None:
                return out, item.group(1).strip()
            out.append(rendered)
            slice_items += 1
            slice_done = slice_done and rendered.startswith("- [x]")
        else:
            out.append(line)
    close_slice()
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
    return argparse.ArgumentParser(prog="guppi sprint", description=__doc__.split("\n\n")[1])


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None):
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    parser().parse_args(argv)
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
    (wiki / "sprint.md").write_text(text, encoding="utf-8", newline="\n")
    return 0
