"""`guppi ship <folder>` — the clean version of GUPPI that other people install.

Builds the clean version from the working tree into an empty folder (case 804.6): `guppi/`,
`.claude/`, the root files of `ROOT_FILES`, the `schema.yaml` of each category,
`vault/wiki/tags.md`, each page that `is_core` of `guppi/pages.py` accepts and each file
that the Render of such a page governs — but `LEFT_OUT`, the files of this project:
`sprint.md`, `backlog.md` and `guppi.toml`. A file that a page without `core: true` renders
in full is not written; nothing of `vault/raw/`, `vault/archive/` or `.github/` is read.

In each text file it writes it removes a parenthesis that holds only references to cases,
the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link.
A case id after `[case `, `#case-` or `:case ` — the form of a ledger line or a mark — is
no reference, and neither is one inside a code span of a Markdown file. Each page it writes
carries `origin` and `sprint` `SHIPPED`, the date of the run in `created` and a `## History`
of one line; its link fields, `LINK_FIELDS` of `guppi/lint.py`, keep only the pages it
writes. The page is written by `write_page` of `guppi/generate.py`.

Then it reads what it wrote and prints `ship: <file>:<line>: <what>` for each reference to
a case or a decision, each `[[link]]` of a Markdown file to a page or a file it does not
write — by `WIKILINK` and `CODE_SPAN` of `guppi/lint.py`, the patterns of `links_of` —,
each mention of a session of this repository by its id, and each marker line of `MARKER`
of `guppi/pages.py` that opens or closes the section of a page without `core: true`; any
such line exits 1, and a Case rewords that text at its source. A folder that is not empty
exits 2 with nothing written.
Rule page: `vault/wiki/rules/rule-clean-branch.md`.
"""

import argparse
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

from guppi.caseid import ID
from guppi.event import project_root
from guppi.generate import write_page
from guppi.lint import CODE_SPAN, LINK_FIELDS, WIKILINK
from guppi.pages import (
    CATEGORIES,
    HISTORY,
    MARKER,
    SHIPPED,
    Page,
    is_core,
    read_vault,
    wiki_root,
)

ROOT_FILES = ("CLAUDE.md", "Makefile", "pyproject.toml", "uv.lock", ".gitattributes")
TREES = ("guppi", ".claude")
LEFT_OUT = ("vault/wiki/sprint.md", "vault/wiki/backlog.md", "guppi.toml")
SKIPPED_NAMES = ("__pycache__", "settings.local.json")
NOT_CLEANED = ("uv.lock",)  # a lock file is data of the package manager, not text of ours
TAGS = "vault/wiki/tags.md"
HISTORY_LINE = "- {day} shipped with GUPPI"

# a reference to a case: the word `case` or `cases`, either case, and one or more ids of
# `ID`, joined by a comma, a semicolon or `and`; not the form of a line after `[`, `#` or
# `:`, and not part of a longer word
REFS = re.compile(
    rf"(?<![\[#:\w-])[Cc]ases?\s+{ID}(?:(?:\s*[,;]\s*|\s+and\s+)(?:[Cc]ases?\s+)?{ID})*\b"
)
PARENTHESIS = re.compile(r"([ \t]?)\(([^()\n]*)\)")
DANGLING = re.compile(r"\s*[,;]\s*(?=[,;]|$)")
DECISION_LINK = re.compile(rf"[ \t]?\[\[decision-case-{ID}(?:[|#][^\]]*)?\]\]")
DECISION = re.compile(rf"\bdecision-case-{ID}")
SESSION = re.compile(r"\b[Ss]essions?\s+(?:\d{4}-\d\d-\d\d/)?\d{4}\b")
MASK = "\x00{}\x00"
MASKED = re.compile(r"\x00(\d+)\x00")


def clean_parenthesis(match: re.Match) -> str:
    space, inner = match.groups()
    if not REFS.search(inner):
        return match.group(0)
    rest = DANGLING.sub("", REFS.sub("", inner))
    rest = re.sub(r"^\s*[,;]?\s*", "", rest).rstrip()
    return f"{space}({rest})" if rest else ""


def masked(text: str, markdown: bool) -> tuple[str, list[str]]:
    """The text with each code span of a Markdown file put aside, and the spans."""
    if not markdown:
        return text, []
    spans: list[str] = []

    def keep(match: re.Match) -> str:
        spans.append(match.group(0))
        return MASK.format(len(spans) - 1)

    return CODE_SPAN.sub(keep, text), spans


def unmasked(text: str, spans: list[str]) -> str:
    return MASKED.sub(lambda m: spans[int(m.group(1))], text)


def clean(text: str, markdown: bool) -> str:
    """The references to cases and the links to decisions removed (case 804.6)."""
    body, spans = masked(text, markdown)
    body = DECISION_LINK.sub("", body)
    body = PARENTHESIS.sub(clean_parenthesis, body)
    return unmasked(body, spans)


def leftovers(text: str, markdown: bool, known: set[str], loose: set[str]) -> list[tuple[int, str]]:
    """`(line, what)` for each reference, link, session or marker the copy must not hold:
    `known` the slugs and hub names it writes, `loose` the page slugs without `core`."""
    out = []
    for number, line in enumerate(text.splitlines(), start=1):
        marker = MARKER.match(line.strip())
        if marker and marker.group(2) in loose:
            out.append((number, f"a section of {marker.group(2)}, a page without core: true"))
            continue
        plain = CODE_SPAN.sub("", line) if markdown else line
        for match in REFS.finditer(plain):
            out.append((number, f"a reference to a case: {match.group(0)}"))
        for match in DECISION.finditer(plain):
            out.append((number, f"a reference to a decision: {match.group(0)}"))
        for match in SESSION.finditer(plain):
            out.append((number, f"a mention of a session: {match.group(0)}"))
        if markdown:
            for slug in WIKILINK.findall(plain):
                if slug.strip() not in known:
                    out.append((number, f"a link to {slug.strip()}, which the copy leaves out"))
    return out


def tree_files(project_dir: Path, top: str) -> list[str]:
    root = project_dir / top
    if not root.is_dir():
        return []
    return sorted(
        path.relative_to(project_dir).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and not any(part in SKIPPED_NAMES for part in path.parts)
        and path.suffix != ".pyc"
    )


def governed(pages: list[Page]) -> tuple[set[str], set[str]]:
    """The files the Render of a page with `core: true` governs, and those a page without
    it renders in full."""
    written, refused = set(), set()
    for page in pages:
        governs, mode = page.props.get("governs"), page.props.get("render_mode")
        if page.props.get("enforcement") != "render" or not governs:
            continue
        if is_core(page):
            written.add(str(governs))
        elif mode == "full":
            refused.add(str(governs))
    return written - refused, refused


def shipped_page(page: Page, slugs: set[str], day: date) -> tuple[dict, dict]:
    """The props and sections of a page as the copy holds it (case 804.6)."""
    props = dict(page.props)
    for field in LINK_FIELDS:
        value = props.get(field)
        if isinstance(value, list):
            kept = [v for v in value if v in slugs]
            if kept or field == "estimates" or not value:
                props[field] = kept
            else:
                del props[field]
        elif value is not None and value not in slugs:
            del props[field]
    props["origin"], props["sprint"], props["created"] = SHIPPED, SHIPPED, day
    sections = dict(page.sections)
    sections[HISTORY] = HISTORY_LINE.format(day=day)
    return props, sections


def ship(project_dir: Path, folder: Path, day: date) -> list[str]:
    """Writes the clean version into `folder`; the lines of what remains, empty when clean."""
    vault = read_vault(wiki_root(project_dir))
    pages = [page for category in CATEGORIES for page in vault[category]]
    core = [page for page in pages if is_core(page) and not page.error]
    slugs = {page.slug for page in core}
    loose = {page.slug for page in pages} - slugs
    written_governed, refused = governed(pages)

    files = [name for name in ROOT_FILES if (project_dir / name).is_file()]
    for top in TREES:
        files += tree_files(project_dir, top)
    files += [f"vault/wiki/{category}/schema.yaml" for category in CATEGORIES]
    files.append(TAGS)
    files += sorted(written_governed)
    files = [
        name
        for name in dict.fromkeys(files)
        if name not in refused and name not in LEFT_OUT and (project_dir / name).is_file()
    ]
    for name in files:
        target = folder / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(project_dir / name, target)
    for page in core:
        props, sections = shipped_page(page, slugs, day)
        name = f"vault/wiki/{page.category}/{page.slug}.md"
        write_page(folder / name, props, sections, page.category)
        files.append(name)

    hubs = {Path(name).stem for name in files if Path(name).parent.as_posix() == "vault/wiki"}
    known = slugs | hubs | {f"{p.category}/{p.slug}" for p in core}
    out = []
    for name in files:
        if Path(name).name in NOT_CLEANED:
            continue
        path = folder / name
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        markdown = path.suffix == ".md"
        cleaned = clean(text, markdown)
        if cleaned != text:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
        for number, what in leftovers(cleaned, markdown, known, loose):
            out.append(f"ship: {name}:{number}: {what}")
    return out


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi ship")
    p.add_argument("folder", help="an empty folder for the clean version")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    args = parser().parse_args(argv)
    folder = Path(args.folder)
    if folder.exists() and any(folder.iterdir()):
        print(f"ship: {folder} is not empty; nothing written", file=stderr)
        return 2
    folder.mkdir(parents=True, exist_ok=True)
    lines = ship(project_dir, folder, now.date())
    for line in lines:
        print(line, file=stdout)
    return 1 if lines else 0
