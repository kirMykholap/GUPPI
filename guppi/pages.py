"""Reading vault pages: frontmatter, `## ` sections, and the folders they live in.

Shared by `render`, `lint`, `generate`, `cleanup`, `prespec`, `archive` and `pageread`. A page is a
Markdown file under `vault/wiki/<category>/`, its properties in a YAML block between `---`
lines, its body in H2 sections. A ref field — `REF_FIELDS` — holds its slugs as quoted
wikilinks, `"[[slug]]"`, so Obsidian's graph, backlinks and Bases see them; `read_page`
strips the brackets, so every reader sees the bare slug, and a page written without them
reads the same (case 148.1). Nothing here writes.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

CATEGORIES = ("entities", "rules", "estimates", "lessons", "insights", "decisions")
SECTION = "## "
HISTORY = "## History"  # the record of a page's changes, its last section
MARKER = re.compile(r"^<!-- (/?)([^\s]+) -->$")
REF_FIELDS = (  # the fields whose values are slugs of pages (case 148.1)
    "parent",
    "children",
    "estimates",
    "target",
    "insight",
    "addressed_by",
    "deferred_by",
    "create",
    "update",
    "delete",
    "defer",
    "supersedes",
    "superseded_by",
    "applies_to",  # the edge Rule → Entity (case 305)
    "rules",  # its backlink, computed by generate (case 305.3)
)
WIKILINK_VALUE = re.compile(r"^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$")


def slug_of(value):
    """The slug inside a `[[slug]]` value; any other value as it is."""
    if isinstance(value, str):
        match = WIKILINK_VALUE.match(value.strip())
        if match:
            return match.group(1).strip()
    return value


def strip_refs(props: dict) -> dict:
    """The props with every ref field read through its brackets, in place."""
    for key in REF_FIELDS:
        value = props.get(key)
        if isinstance(value, list):
            props[key] = [slug_of(v) for v in value]
        elif isinstance(value, str):
            props[key] = slug_of(value)
    return props


@dataclass
class Page:
    category: str
    slug: str
    path: Path
    props: dict = field(default_factory=dict)
    sections: dict[str, str] = field(default_factory=dict)
    error: str | None = None

    def section(self, name: str) -> str | None:
        return self.sections.get(name)


def wiki_root(project_dir: Path) -> Path:
    return project_dir / "vault" / "wiki"


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """`(yaml block, body)`; the block is None when the file does not open with `---`."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1 :])
    return None, text


def section_starts(lines: list[str]) -> set[int]:
    """The indexes of the lines that open an H2 section of the page. A heading inside a
    `<!-- slug -->` … `<!-- /slug -->` block belongs to the block: a render section may carry
    the headings of the file it produces. The one walk of `split_sections` and
    `history_line`."""
    starts: set[int] = set()
    closed = {m.group(2) for m in map(MARKER.match, lines) if m and m.group(1)}
    open_markers: list[str] = []
    for index, line in enumerate(lines):
        match = MARKER.match(line)
        if match:
            closing, name = match.groups()
            if closing:
                if open_markers and open_markers[-1] == name:
                    open_markers.pop()
            elif name in closed:  # a lone child marker in a frame opens nothing
                open_markers.append(name)
        if line.startswith(SECTION) and not open_markers:
            starts.add(index)
    return starts


def split_sections(body: str) -> dict[str, str]:
    """H2 heading → the text under it, leading and trailing blank lines removed; the
    headings by `section_starts`."""
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []

    def close():
        if current is not None:
            sections[current] = "\n".join(buffer).strip("\n")

    lines = body.splitlines()
    starts = section_starts(lines)
    for index, line in enumerate(lines):
        if index in starts:
            close()
            current = line.strip()
            buffer = []
        elif current is not None:
            buffer.append(line)
    close()
    return sections


def history_line(text: str) -> int | None:
    """The 1-based line of the page's own `## History` heading in the whole file, frontmatter
    included, by the walk of `split_sections`; None when the page has none (case 420.1)."""
    lines = text.splitlines()
    for index in sorted(section_starts(lines)):
        if lines[index].strip() == HISTORY:
            return index + 1
    return None


def read_page(path: Path, category: str) -> Page:
    page = Page(category=category, slug=path.stem, path=path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        page.error = f"unreadable: {exc}"
        return page
    block, body = split_frontmatter(text)
    if block is None:
        page.error = "no frontmatter"
    else:
        try:
            props = yaml.safe_load(block) or {}
        except yaml.YAMLError as exc:
            page.error = f"frontmatter is not YAML: {exc}"
            props = {}
        if not isinstance(props, dict):
            page.error = "frontmatter is not a mapping"
            props = {}
        page.props = strip_refs(props)
    page.sections = split_sections(body)
    return page


def read_category(wiki: Path, category: str) -> list[Page]:
    folder = wiki / category
    if not folder.is_dir():
        return []
    pages = [read_page(p, category) for p in sorted(folder.glob("*.md")) if p.stem != "schema"]
    return pages


def read_vault(wiki: Path) -> dict[str, list[Page]]:
    return {category: read_category(wiki, category) for category in CATEGORIES}
