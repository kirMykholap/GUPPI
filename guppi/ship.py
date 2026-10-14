"""`guppi ship <folder>` — the clean version of GUPPI that other people install.

Builds the clean version from the working tree into an empty folder (case 804.6): `guppi/`,
`.claude/`, the root files of `ROOT_FILES`, the `schema.yaml` of each category,
`vault/wiki/tags.md`, each page that `is_core` of `guppi/pages.py` accepts and each file
that the Render of such a page governs — but `LEFT_OUT`, the files of this project:
`sprint.md`, `backlog.md` and `guppi.toml`. A file that a page without `core: true` renders
in full is not written; nothing of `vault/raw/`, `vault/archive/` or `.github/` is read.

A pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its
id, each id of a list included — stands in a bracket of its own at the end of its sentence,
with the words that go with it (case 807.1). In each text file it writes it removes whole
each bracket that holds a pointer, with the space before it, and each `[[decision-case-N]]`
link; a bracket with no pointer stays. It writes each other `[[…]]` link of a Markdown file
to a page or a file it does not write as the slug in a code span, by `WIKILINK` of
`guppi/lint.py`. A case id after `[case `, `#case-` or `:case ` — the form of a ledger line
or a mark — is no pointer, and neither is one in a code span or a fenced block of a Markdown
file or of the text of a `schema.yaml`; the example Case of `case-example.md` stands in such
a block, and the text around it is judged like any other (case 815). Each page it writes carries `origin` and `sprint` `SHIPPED`, the date
of the run in `created` and a `## History` of one line; its link fields, `LINK_FIELDS` of
`guppi/lint.py`, keep only the pages it writes. The page is written by `write_page` of
`guppi/generate.py`.

Then it reads what it wrote and prints `ship: <file>:<line>: <what>` for each pointer that
stands outside such a bracket and each marker line of `MARKER` of `guppi/pages.py` that
opens or closes the section of a page without `core: true`; any such line exits 1, and a
Case rewords that text at its source. A case number with no word `case` before it is no
pointer and stays in the copy, but in a comment or a docstring of a Python file
`bare_numbers` prints it and exits 1 too: a bracket of case numbers alone, an opening of
one or more case numbers and a colon, a comment that is one or more case numbers alone, a
list joined in each shape alike (cases 808.1, 811); it reads the
file by `tokenize`, so no code is judged. `--review` also prints each bracket it removes that
holds a word beside its pointers, which sets no exit code. `--check` judges in place each
file outside `vault/` that the copy takes, but `NOT_CLEANED`, prints the same lines and
writes nothing; `make lint` runs it. A folder that is not empty exits 2 with nothing
written. `outside` is the one judgment of a pointer, which `guppi/prespec.py` imports.
Rule page: `vault/wiki/rules/rule-clean-branch.md`.
"""

import argparse
import re
import shutil
import sys
import tokenize
from datetime import date, datetime
from io import StringIO
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
DECISION_LINK = re.compile(rf"[ \t]?\[\[decision-case-{ID}(?:[|#][^\]]*)?\]\]")
DECISION = re.compile(rf"\bdecision-case-{ID}")
# a mention of a session by its id, each id of a list included, as `REFS` takes a list
SESSION_ID = r"(?:\d{4}-\d\d-\d\d/)?\d{4}"
SESSION = re.compile(
    rf"\b[Ss]essions?\s+{SESSION_ID}"
    rf"(?:(?:\s*[,;]\s*|\s+and\s+)(?:[Ss]essions?\s+)?{SESSION_ID})*\b"
)
POINTERS = (
    ("a reference to a case", REFS),
    ("a reference to a decision", DECISION),
    ("a mention of a session", SESSION),
)
# a bracket with no bracket inside it, on one line or across lines, and the space before it;
# a bracket that opens a line and a mark of punctuation follows takes the line break before
# it, so the mark joins the line above and does not stand alone
BRACKET = re.compile(r"(\n[ \t]*(?=\([^()]*\)[.,;:])|[ \t]?)\(([^()]*)\)")
# a case number with no word before it, in a comment or a docstring of a Python file
# (cases 808.1, 811): `NUMBERS`, one or more case numbers joined by a comma, a semicolon,
# `and` or a dash, serves each shape — a bracket that holds only such a list, and not opened
# right after a name, as a call is; a comment or a docstring that opens with such a list and
# a colon; a comment that is such a list alone. A date is no case number.
NUMBER = rf"(?!\d{{4}}-\d\d-\d\d){ID}"
NUMBERS = rf"{NUMBER}(?:\s*(?:[,;]|\band\b|[-–])\s*{NUMBER})*"
BARE_BRACKET = re.compile(rf"(?<![\w.\])])\(\s*{NUMBERS}\s*\)")
BARE_OPENING = re.compile(rf"^\s*{NUMBERS}:")
BARE_ALONE = re.compile(rf"^\s*{NUMBERS}\s*$")
STRING_PREFIX = re.compile(r"^[rRbBuU]*('''|\"\"\"|'|\")")
STATEMENT_START = {
    tokenize.NEWLINE,
    tokenize.NL,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.ENCODING,
}
SEPARATORS = re.compile(r"[\s,;]+|\band\b")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
MASK = "\x00{}\x00"
MASKED = re.compile(r"\x00(\d+)\x00")


def holds_pointer(text: str) -> bool:
    return any(pattern.search(text) for _, pattern in POINTERS)


def masked(text: str, sample: bool) -> tuple[str, list[str]]:
    """The text with each sample put aside, and the samples: with `sample`, each code span,
    each line of a fenced block. A line keeps its place, so the lines of the text keep their
    numbers."""
    spans: list[str] = []

    def keep(part: str) -> str:
        spans.append(part)
        return MASK.format(len(spans) - 1)

    if not sample:
        return text, spans
    lines, fence = text.split("\n"), None
    for number, line in enumerate(lines):
        opener = FENCE.match(line)
        if fence is None and opener:
            fence = opener.group(1)
            lines[number] = keep(line)
        elif fence is not None:
            if opener and opener.group(1)[0] == fence[0] and len(opener.group(1)) >= len(fence):
                fence = None
            lines[number] = keep(line)
        else:
            lines[number] = CODE_SPAN.sub(lambda m: keep(m.group(0)), line)
    return "\n".join(lines), spans


def unmasked(text: str, spans: list[str]) -> str:
    return MASKED.sub(lambda m: spans[int(m.group(1))], text)


def words_beside(inner: str) -> bool:
    """Whether a bracket holds a word beside its pointers."""
    rest = inner
    for _, pattern in POINTERS:
        rest = pattern.sub("", rest)
    return bool(SEPARATORS.sub("", rest))


def removed(body: str, keep_lines: bool = True) -> tuple[str, list[tuple[int, str]]]:
    """`body` with each bracket that holds a pointer removed whole, and `(line, bracket)`
    for each removed bracket that holds a word beside its pointers. With `keep_lines` a
    removed bracket leaves its line breaks, so the lines keep their numbers."""
    review = []

    def drop(match: re.Match) -> str:
        if not holds_pointer(match.group(2)):
            return match.group(0)
        if words_beside(match.group(2)):
            line = body.count("\n", 0, match.start(2)) + 1
            review.append((line, f"({match.group(2)})"))
        return "\n" * match.group(0).count("\n") if keep_lines else ""

    return BRACKET.sub(drop, body), review


def outside(text: str, sample: bool = True) -> list[tuple[int, str]]:
    """`(line, what)` for each pointer that stands outside a bracket of its own: the one
    judgment of a pointer, which `guppi/prespec.py` runs over the new text of a page."""
    body, _ = masked(text, sample)
    body, _ = removed(DECISION_LINK.sub("", body))
    out = []
    for number, line in enumerate(body.split("\n"), start=1):
        for what, pattern in POINTERS:
            out += [(number, f"{what}: {m.group(0)}") for m in pattern.finditer(line)]
    return out


def bare_in(body: str) -> list[tuple[int, str]]:
    """`(offset, number)` for each bare case number of the text of one comment or docstring."""
    found = [(m.start(), m.group(0)) for m in BARE_BRACKET.finditer(body)]
    opening = BARE_ALONE.match(body) or BARE_OPENING.match(body)
    if opening:
        found.append((opening.start(), opening.group(0).strip()))
    return sorted(found)


def bare_numbers(text: str) -> list[tuple[int, str]]:
    """`(line, what)` for each case number with no word before it in a comment or a docstring
    of the Python source `text`, read by `tokenize`, so that no code is judged: the one
    judgment of a bare case number (case 808.1). A docstring is a string that a statement is
    alone; a comment that only opens with a number, such as a count, is no finding. A text
    that does not tokenize gives none."""
    try:
        tokens = list(tokenize.generate_tokens(StringIO(text).readline))
    except (tokenize.TokenError, SyntaxError):
        return []
    skipped = (tokenize.COMMENT, tokenize.NL)
    out, at_start = [], True
    for index, token in enumerate(tokens):
        if token.type == tokenize.COMMENT:
            body = token.string[1:]
            out += [(token.start[0], f"a bare case number: {n}") for _, n in bare_in(body)]
            continue
        if token.type == tokenize.STRING and at_start:
            after = next((t for t in tokens[index + 1 :] if t.type not in skipped), None)
            if after is None or after.type in (tokenize.NEWLINE, tokenize.ENDMARKER):
                quote = STRING_PREFIX.match(token.string)
                start = quote.end() if quote else 0
                body = token.string[start:]
                out += [
                    (
                        token.start[0] + token.string.count("\n", 0, start + at),
                        f"a bare case number: {n}",
                    )
                    for at, n in bare_in(body)
                ]
        if token.type not in skipped:
            at_start = token.type in STATEMENT_START
    return out


def clean(
    text: str, sample: bool, known: set[str] | None = None
) -> tuple[str, list[tuple[int, str]]]:
    """The text as the copy holds it, and the brackets `--review` lists: each bracket that
    holds a pointer and each `[[decision-case-N]]` link removed; with `known`, each other
    `[[…]]` link to a slug outside it written as the slug in a code span (case 807.1)."""
    body, spans = masked(text, sample)
    body, review = removed(DECISION_LINK.sub("", body), keep_lines=False)
    if known is not None:

        def link(match: re.Match) -> str:
            slug = match.group(1).strip()
            return match.group(0) if slug in known else f"`{slug}`"

        body = WIKILINK.sub(link, body)
    return unmasked(body, spans), [(n, unmasked(b, spans)) for n, b in review]


def leftovers(
    text: str, sample: bool, loose: set[str], python: bool = False
) -> list[tuple[int, str]]:
    """`(line, what)` for each pointer outside a bracket, and each marker of a page in
    `loose`, the page slugs without `core`, that the copy must not hold; with `python`, each
    bare case number of `bare_numbers` too."""
    out = []
    for number, line in enumerate(text.split("\n"), start=1):
        marker = MARKER.match(line.strip())
        if marker and marker.group(2) in loose:
            out.append((number, f"a section of {marker.group(2)}, a page without core: true"))
    if python:
        out += bare_numbers(text)
    return sorted(out + outside(text, sample))


def is_sample_file(name: str) -> bool:
    """Whether the code spans and fenced blocks of a file hold samples: Markdown, and the
    text of a `schema.yaml`."""
    return name.endswith(".md") or Path(name).name == "schema.yaml"


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


def plan(project_dir: Path) -> tuple[list[str], list[Page], set[str], set[str]]:
    """The files the copy takes from the tree, the pages it writes, the slugs and hub names
    a link of the copy may name, and the page slugs without `core`."""
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
    names = files + [f"vault/wiki/{page.category}/{page.slug}.md" for page in core]
    hubs = {Path(name).stem for name in names if Path(name).parent.as_posix() == "vault/wiki"}
    known = slugs | hubs | {f"{p.category}/{p.slug}" for p in core}
    return files, core, known, loose


def judged(name: str, text: str, known: set[str], loose: set[str]) -> tuple[str, list, list]:
    """The text of a file as the copy holds it, and its `ship:` lines and `--review` lines by
    the lines of `text`; a file of `NOT_CLEANED` is not judged."""
    if Path(name).name in NOT_CLEANED:
        return text, [], []
    sample = is_sample_file(name)
    cleaned, review = clean(text, sample, known if name.endswith(".md") else None)
    python = name.endswith(".py")
    lines = [f"ship: {name}:{n}: {what}" for n, what in leftovers(text, sample, loose, python)]
    reviewed = [f"ship: {name}:{n}: a bracket with words: {' '.join(b.split())}" for n, b in review]
    return cleaned, lines, reviewed


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def ship(project_dir: Path, folder: Path, day: date) -> tuple[list[str], list[str]]:
    """Writes the clean version into `folder`; the lines of what remains, empty when clean,
    and the lines of `--review`."""
    files, core, known, loose = plan(project_dir)
    slugs = {page.slug for page in core}
    for name in files:
        target = folder / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(project_dir / name, target)
    for page in core:
        props, sections = shipped_page(page, slugs, day)
        name = f"vault/wiki/{page.category}/{page.slug}.md"
        write_page(folder / name, props, sections, page.category)
        files.append(name)

    out, review = [], []
    for name in files:
        path = folder / name
        text = read_text(path)
        if text is None:
            continue
        cleaned, lines, reviewed = judged(name, text, known, loose)
        if cleaned != text:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
        out += lines
        review += reviewed
    return out, review


def check(project_dir: Path) -> tuple[list[str], list[str]]:
    """The lines of `ship` for each file outside `vault/` that the copy takes, judged in
    place in the working tree; nothing is written."""
    files, _, known, loose = plan(project_dir)
    out, review = [], []
    for name in files:
        if name.startswith("vault/"):
            continue
        text = read_text(project_dir / name)
        if text is None:
            continue
        _, lines, reviewed = judged(name, text, known, loose)
        out += lines
        review += reviewed
    return out, review


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi ship")
    p.add_argument("folder", nargs="?", help="an empty folder for the clean version")
    p.add_argument(
        "--review", action="store_true", help="also list the brackets with words it removes"
    )
    p.add_argument("--check", action="store_true", help="judge the files outside vault/ in place")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    args = parser().parse_args(argv)
    if args.check:
        lines, review = check(project_dir)
    elif args.folder is None:
        print("ship: name an empty folder, or pass --check", file=stderr)
        return 2
    else:
        folder = Path(args.folder)
        if folder.exists() and any(folder.iterdir()):
            print(f"ship: {folder} is not empty; nothing written", file=stderr)
            return 2
        folder.mkdir(parents=True, exist_ok=True)
        lines, review = ship(project_dir, folder, now.date())
    for line in lines + (review if args.review else []):
        print(line, file=stdout)
    return 1 if lines else 0
