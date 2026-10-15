"""`guppi backlog [--check]` — `vault/wiki/backlog.md`, every deferred item in one file.

The file is not a document: this script writes it from what the vault already stores
(case 451.4). `# Backlog`; the line `N items`; then `## Conserved Specs` — each unit under
`vault/raw/` that holds `carry.md`, one line naming its `spec.md` and its Cases, and under
it one line per item of its `then` blocks, the kind, the slug and the Case, read by the
Spec reader of `.guppi/guppi/materialize.py` (`read_specs`, `then_blocks`); then `## Deferred` —
one line per item: each live page whose `deferred_by` is not empty, each Insight whose
`status` is `open`, each line of the `## Backlog` of each sprint page `entity-sprint-<id>`
— the live one, then each under `vault/archive/`, so the Backlog of a closed sprint stays in
the list (case 628.12) — read by the item reader of `.guppi/guppi/sprint.py`. A slug of a line of
the Backlog of an archived sprint page does not stand when the live sprint page names it in
its `## Milestones` or its `## Backlog`, or when its page stands `built`, `passed` or
`archived` by `item_statuses` and `is_done` of `.guppi/guppi/sprint.py`, imported; a line of an
archived Backlog that names no page does not stand when the live sprint page holds a line of
the same text (case 743.4). A line holds the slug in a code span, the
page's `purpose` — for an Insight its `pattern` and `severity` — and the count; a line of
the Backlog that names no page stands by its text, and a slug there without a live page
by the text after its ` — `. The count of an item is the number of sessions whose
`frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line naming its slug
in a code span of its title — read by `generate.frontiers` and `generate.frontier_marks`,
held in no second copy here (`rule-one-judgment-one-implementation`). `N` counts the
conserved Specs and the lines of `## Deferred`; a slug under a conserved Spec does not
stand again under `## Deferred`, and a slug of two sources stands once, by its first
source in the order above. A folder whose `carry.md` is gone shows nothing. A Spec of a
conserved unit that does not parse — a Case in two files, a `then` block not YAML — is
one line on stderr, exit 1, the file not written. The script writes no file but
`vault/wiki/backlog.md`. `--check` renders in memory and compares: one line on stdout —
`backlog: vault/wiki/backlog.md differs from its sources` — and exit 1 when the file
differs, silence and exit 0 when it is the same, nothing written either way; `guppi check`
runs it after `sprint --check` (case 451.5). The librarian runs the script after
`guppi sprint`, `carry` after it writes `carry.md`, and the governed-files hook refuses a
hand edit (`governs` on `rule-backlog`). Rule page: `vault/wiki/rules/rule-backlog.md`.
"""

import argparse
import sys
from pathlib import Path

from guppi.event import project_root
from guppi.generate import frontier_marks, frontiers
from guppi.ledger import SPRINT_PAGE
from guppi.lint import archived_slugs, as_list
from guppi.materialize import (
    DECISION_KINDS,
    MaterializeError,
    read_specs,
    spec_files,
    then_blocks,
    units_with,
)
from guppi.pages import Page, read_page, read_vault, wiki_root
from guppi.sprint import DASH, is_done, item_slugs, item_statuses, sprint_page

TARGET = "backlog.md"
CARRY = "carry.md"
PUT_OFF = "-"  # the box of a Frontier line put off (case 451.1)

Sessions = list[tuple[tuple[str, str], list[tuple[str, set[str]]]]]


def one_line(value) -> str:
    """A field's value on one line: its whitespace collapsed."""
    return " ".join(str(value or "").split())


def plural(count: int, word: str) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def sessions_of(project_dir: Path) -> Sessions:
    """Every Frontier of `raw/` and the archive, keyed by its session, as the marks of its
    lines by `generate.frontiers` and `generate.frontier_marks`, read once."""
    return [(key, frontier_marks(path)) for key, path in frontiers(project_dir)]


def put_off_count(slugs: set[str], sessions: Sessions) -> int:
    """The number of sessions whose Frontier holds a `[-]` line naming one of `slugs` in a
    code span of its title (case 451.4); none for an item that names no slug."""
    return len(
        {
            key
            for key, marks in sessions
            if any(box == PUT_OFF and named & slugs for box, named in marks)
        }
    )


def conserved(project_dir: Path) -> tuple[list[list[str]], set[str], str]:
    """`(blocks, slugs, error)`: one block of lines per unit under `raw/` holding
    `carry.md` — the line naming its Spec and Cases, then one line per item of its `then`
    blocks; the slugs those items name; the first parse error, else empty."""
    blocks: list[list[str]] = []
    slugs: set[str] = set()
    for unit in units_with(project_dir, CARRY):
        files = spec_files(project_dir, unit)
        if not files:
            blocks.append([f"- `vault/raw/{unit}/` — no spec.md"])
            continue
        try:
            cases, found = read_specs(project_dir, unit)
        except MaterializeError as exc:
            return [], set(), f"backlog: vault/raw/{unit}: {exc}"
        names = ", ".join(f"`{p.relative_to(project_dir).as_posix()}`" for p in files)
        top = [case for case in cases if "." not in case]
        block = [f"- {names} — Cases {', '.join(top)}" if top else f"- {names} — no Case"]
        for case, lines in cases.items():
            merged, errors = then_blocks(lines)
            if errors:
                return [], set(), f"backlog: {found[case]}: Case {case}: {errors[0]}"
            for kind in DECISION_KINDS:
                for item in merged.get(kind) or []:
                    slug = item.get("slug") if isinstance(item, dict) else None
                    if slug:
                        block.append(f"  - {kind} `{slug}` · case {case}")
                        slugs.add(str(slug))
        blocks.append(block)
    return blocks, slugs, ""


def describe(page: Page | None, fallback: str) -> str:
    """What an item is about: an Insight's `pattern` and `severity`, another page's
    `purpose`, and `fallback` for a slug without a live page."""
    if page is None:
        return fallback
    if page.category == "insights":
        return f"{one_line(page.props.get('pattern'))} · severity {page.props.get('severity', '')}"
    return one_line(page.props.get("purpose"))


def archived_sprint_pages(project_dir: Path) -> list[Page]:
    """Each sprint page `entity-sprint-<id>` under `vault/archive/`, at any depth, in path
    order: a closed sprint keeps its `## Backlog` in the list (case 628.12)."""
    root = project_dir / "vault" / "archive"
    if not root.is_dir():
        return []
    found = [read_page(p, "entities") for p in sorted(root.rglob(f"entities/{SPRINT_PAGE}*.md"))]
    return [p for p in found if not p.error]


def sprint_pages(pages: dict[str, list[Page]], archived: list[Page]) -> list[Page]:
    """The live sprint page, by `.guppi/guppi/sprint.py`, then each archived one."""
    live = sprint_page(pages)
    return ([live] if live is not None else []) + list(archived)


def item_bodies(text: str | None) -> list[str]:
    """The body of each `- ` line of a section, its marker cut."""
    lines = (raw.strip() for raw in (text or "").splitlines())
    return [line[2:] for line in lines if line.startswith("- ")]


def taken_by(current: Page | None) -> tuple[set[str], set[str]]:
    """`(slugs, notes)` the live sprint page names in its `## Milestones` and `## Backlog`:
    the slugs of its items and the text of its notes (case 743.4)."""
    slugs: set[str] = set()
    notes: set[str] = set()
    if current is None:
        return slugs, notes
    for section in ("## Milestones", "## Backlog"):
        for body in item_bodies(current.section(section)):
            named = item_slugs(body)
            slugs.update(named)
            if not named:
                notes.add(body)
    return slugs, notes


def finished(slug: str, by_slug: dict[str, Page], gone: set[str]) -> bool:
    """A slug whose page stands `built`, `passed` or `archived`, by the one judgment of
    `.guppi/guppi/sprint.py` (case 743.4)."""
    statuses, missing = item_statuses([slug], by_slug, gone)
    return missing is None and is_done(statuses)


def deferred(
    pages: dict[str, list[Page]],
    shown: set[str],
    sessions: Sessions,
    archived: list[Page] = (),
    gone: set[str] = frozenset(),
) -> list[str]:
    """The lines of `## Deferred`: each live page with `deferred_by`, each open Insight,
    each line of the `## Backlog` of each sprint page, live or under `vault/archive/` (case
    628.12), but a line of a closed sprint the live sprint takes or whose page is finished
    (case 743.4); `gone` holds the slugs of the archive; a slug in `shown` — under a
    conserved Spec or of an earlier source — is passed by."""
    live = [p for category in pages.values() for p in category if not p.error]
    by_slug = {p.slug: p for p in live}
    items: list[tuple[str | None, str]] = []  # (slug, description); no slug for a note
    for page in live:
        is_open = page.category == "insights" and page.props.get("status") == "open"
        if as_list(page.props.get("deferred_by")) or is_open:
            items.append((page.slug, describe(page, "")))
    current = sprint_page(pages)
    taken_slugs, taken_texts = taken_by(current)
    for sprint in sprint_pages(pages, archived):
        closed = sprint is not current
        for body in item_bodies(sprint.section("## Backlog")):
            slugs = item_slugs(body)
            if not slugs:
                if not (closed and body in taken_texts):
                    items.append((None, body))
                continue
            text = body.split(DASH, 1)[1].strip() if DASH in body else ""
            for slug in slugs:
                if closed and (slug in taken_slugs or finished(slug, by_slug, gone)):
                    continue  # taken by the live sprint, or its page finished (case 743.4)
                items.append((slug, describe(by_slug.get(slug), text)))
    out: list[str] = []
    seen = set(shown)
    for slug, text in items:
        if slug is None:
            out.append(f"- {text} · put off in {plural(0, 'session')}")
            continue
        if slug in seen:
            continue
        seen.add(slug)
        count = put_off_count({slug}, sessions)
        head = f"`{slug}` — {text}" if text else f"`{slug}`"
        out.append(f"- {head} · put off in {plural(count, 'session')}")
    return out


def render(project_dir: Path, pages: dict[str, list[Page]]) -> tuple[str | None, str]:
    """`(text, error)`: the whole file, or the error line."""
    blocks, slugs, error = conserved(project_dir)
    if error:
        return None, error
    lines = deferred(
        pages,
        slugs,
        sessions_of(project_dir),
        archived_sprint_pages(project_dir),
        archived_slugs(wiki_root(project_dir)),
    )
    parts = [
        "# Backlog",
        "",
        plural(len(blocks) + len(lines), "item"),
        "",
        "## Conserved Specs",
        "",
    ]
    for block in blocks:
        parts += block
    if blocks:
        parts.append("")
    parts += ["## Deferred", ""]
    if lines:
        parts += lines + [""]
    return "\n".join(parts), ""


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi backlog", description=__doc__.split("\n\n")[1])
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
    text, error = render(project_dir, read_vault(wiki))
    if text is None:
        print(error, file=stderr)
        return 1
    target = wiki / TARGET
    if args.check:  # compare, name, write nothing (case 451.5)
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current == text:
            return 0
        print("backlog: vault/wiki/backlog.md differs from its sources", file=stdout)
        return 1
    target.write_text(text, encoding="utf-8", newline="\n")
    return 0
