"""`guppi glossary [--check]` — `vault/wiki/glossary.md` written from the glossary page.

The glossary is a page: `vault/wiki/entities/entity-glossary.md`, whose `## Terms` is a
flat table `| term | meaning | where |`, one row per term in the order the person keeps,
`where` a `[[slug]]` to the live page that defines the term. This script writes
`vault/wiki/glossary.md` from it (case 306.4): `# Glossary`; one line naming the source;
then one group per parent MOC of the pages in `where` — `## [[<moc>]]`, in the order of
first appearance in the table; a page without a `parent` (a root MOC, or a placeholder
not yet placed) groups under itself — each group a table `| term | meaning | where |` in
the order of the table. A `where` with no live page, a row not of three cells, a term
twice, a `where` that is no wikilink, or no `## Terms`: one line on stderr, exit 1, the
file not written; no glossary page, or two: the same. `--check` renders in memory and
compares: one line on stdout — `glossary: vault/wiki/glossary.md differs from
entity-glossary` — and exit 1 when the file differs, silence and exit 0 when it is the
same, nothing written either way; `make lint` runs it after `sprint --check` (case 306.5).
Once the plain `guppi glossary` wrote the file and exits 0, it ticks every unticked task
line that opens with a code span holding `guppi glossary` in the `spec.md` of every unit
under `raw/` whose yaml is applied whole — the Spec's bookkeeping, never a tick in the
glossary itself; `--check` and an exit 1 tick nothing; the helper is
`render.tick_command_lines` (case 306.6). The librarian runs the script after `sprint`, before the
brief, and the governed-files hook refuses a hand edit (`governs` on `rule-glossary`);
a term changes by an `update` of `entity-glossary`. Rule page:
`vault/wiki/rules/rule-glossary.md`.
"""

import argparse
import re
import sys
from pathlib import Path

from guppi.event import project_root
from guppi.pages import Page, read_vault, wiki_root
from guppi.render import tick_command_lines

SLUG = "entity-glossary"
TERMS = "## Terms"
HEADER = ("| term | meaning | where |", "|---|---|---|")
WIKILINK = re.compile(r"^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$")
SOURCE_LINE = (
    "Written by `guppi glossary` from the `## Terms` of `entity-glossary`; "
    "a term changes by an `update` of that page."
)


def glossary_page(pages: dict[str, list[Page]]) -> Page | None:
    found = [p for p in pages["entities"] if p.slug == SLUG and not p.error]
    return found[0] if len(found) == 1 else None


def cells(line: str) -> list[str] | None:
    """The cells of a table row, or None for a line that is not one."""
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [c.strip() for c in stripped[1:-1].split("|")]


def rows(text: str) -> tuple[list[tuple[str, str, str]], str]:
    """`(rows, error)`: the `(term, meaning, where-slug)` of every row of the table under
    `## Terms`, the header and the separator passed by; the error names the first row
    that is not three cells, whose `where` is no wikilink, or whose term repeats."""
    out: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for line in text.splitlines():
        parts = cells(line)
        if parts is None:
            continue
        if parts == [c.strip() for c in HEADER[0][1:-1].split("|")]:
            continue
        if all(set(c) <= set("-: ") for c in parts):
            continue
        if len(parts) != 3:
            return [], f"glossary: a row of {len(parts)} cells, not three: {line.strip()}"
        term, meaning, where = parts
        match = WIKILINK.match(where)
        if not match:
            return [], f"glossary: {term}: where is not a [[slug]]: {where}"
        if term in seen:
            return [], f"glossary: {term}: stands twice"
        seen.add(term)
        out.append((term, meaning, match.group(1).strip()))
    return out, ""


def group_of(slug: str, by_slug: dict[str, Page]) -> str:
    """The parent MOC of the page a `where` names; a page without a parent — a root MOC,
    a placeholder not yet placed — groups under itself."""
    page = by_slug[slug]
    parent = page.props.get("parent")
    return str(parent) if parent else slug


def render(page: Page, by_slug: dict[str, Page]) -> tuple[str | None, str]:
    """`(text, error)`: the whole file, or the error line."""
    section = page.section(TERMS)
    if section is None:
        return None, f"glossary: {SLUG} has no {TERMS} section"
    table, error = rows(section)
    if error:
        return None, error
    groups: dict[str, list[tuple[str, str, str]]] = {}
    for term, meaning, where in table:
        if where not in by_slug:
            return None, f"glossary: {term}: where names {where}, which no live page carries"
        groups.setdefault(group_of(where, by_slug), []).append((term, meaning, where))
    parts = ["# Glossary", "", SOURCE_LINE, ""]
    for moc, terms in groups.items():
        parts += [f"## [[{moc}]]", "", *HEADER]
        parts += [f"| {term} | {meaning} | [[{where}]] |" for term, meaning, where in terms]
        parts.append("")
    return "\n".join(parts), ""


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi glossary", description=__doc__.split("\n\n")[1])
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
    page = glossary_page(pages)
    if page is None:
        print(f"glossary: no live {SLUG} page", file=stderr)
        return 1
    by_slug = {p.slug: p for category in pages.values() for p in category if not p.error}
    text, error = render(page, by_slug)
    if text is None:
        print(error, file=stderr)
        return 1
    target = wiki / "glossary.md"
    if args.check:  # compare, name, write nothing (case 306.5)
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current == text:
            return 0
        print(f"glossary: vault/wiki/glossary.md differs from {SLUG}", file=stdout)
        return 1
    target.write_text(text, encoding="utf-8", newline="\n")
    tick_command_lines(project_dir, "guppi glossary")  # the glossary lines of the applied Specs
    return 0
