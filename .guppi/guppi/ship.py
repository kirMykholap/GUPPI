"""`guppi ship <folder>` — the clean version of GUPPI that other people install.

Builds the clean version from the working tree into an empty folder (case 804.6): `.guppi/`,
the package `guppi` with its `pyproject.toml`, `uv.lock` and `.gitignore`, and its tests
`.guppi/tests/` (case 822); `.claude/`; the root files of `ROOT_FILES`, `CLAUDE.md`
and `.gitattributes`; the `schema.yaml` of each category, `vault/wiki/tags.md`, each page
but an Estimate that `is_core` of `.guppi/guppi/pages.py` accepts and each file that the
Render of such a page governs — but `LEFT_OUT`, the files of this project: the session files
of `SKELETONS` and `guppi.toml`, and this module, `.guppi/guppi/ship.py`, with its tests
`.guppi/tests/test_ship.py`, so that a project that installs GUPPI, which builds no clean
version, gets no command `ship` (case 820.5). The `pyproject.toml` and
`uv.lock` at the root of the repository of GUPPI, a development project, are not written
(case 819.3). A folder or a file of `SKIPPED_NAMES` — the Python environment `.guppi/.venv/`, a cache folder of Python, pytest or ruff — is neither
written nor judged. A file that a page without `core: true` renders in full is not written.
Of `.github/` it writes only `CI`, `.github/workflows/checks.yml`, the CI that runs the tests,
the vault checks and the style check of a project, judged and cleaned like each other file it
writes (case 822); nothing of `vault/raw/`, `vault/archive/` or the rest of `.github/`,
`.github/workflows/prod.yml` included, is read.

While a rule or an entity that `is_draft_core` of `.guppi/guppi/pages.py` accepts — a page
with `core: true` that is `draft` — stands, `drafts` gives a line `ship: <page>: a page with
core: true that is draft` for each, and the build prints them, writes nothing and exits 1,
before it reads a tag; the workflow that writes `prod` never passes `--allow-draft`. With
`--allow-draft` it prints those lines, which set no exit code, and writes the copy all the
same, for an install by hand from that folder (case 822).

In `CLAUDE.md` and in the Render of `rule-claude-md` that the copy holds, `blank_description`
writes `BLANK_DESCRIPTION` — the heading `# Project`, a blank line and the line `Project
description: not set yet.` — between the marker lines of `DESCRIPTION_MARKERS`,
`<!-- project-description -->` and `<!-- /project-description -->`, in place of the heading
and the description of this project; every other line stays, so `guppi render --check` over
the copy names no file that differs (case 822).

An Estimate is written when `ships` accepts it (case 822): its `status` is `passed`, its
`target`, read by `slug_of` of `.guppi/guppi/pages.py`, is a page with `core: true` that the
copy writes, and its `method` holds no match of `MAKE_TARGET` of `.guppi/guppi/lint.py`,
since the copy holds no `Makefile`; its own `core` is not read, since no Estimate of this
repository carries it. `shipped_page` writes `core: true` into the copy of such an Estimate,
so lint accepts its `origin`, and its `## Result` as one line, `RESULT_LINE`: the date of its
`checked` — else the date its Result opens with, by `READING_DATE` of
`.guppi/guppi/generate.py` — and that it passed in the repository of GUPPI. Its `status`,
`checked`, `purpose`, `method` and `## Criterion` stay, cleaned and judged as the text of any
page.

In place of the session files of this project it writes skeletons (case 822), after the
pages, over the clean folder: `vault/wiki/sprint.md` by `closed_form` of
`.guppi/guppi/sprint.py` for the sprint `SHIPPED`, so the first `/hi` of a new project starts
`/sprint-open`; `vault/wiki/backlog.md` and `vault/wiki/glossary.md` by `render` of
`.guppi/guppi/backlog.py` and of `.guppi/guppi/glossary.py`, which read the pages it wrote;
`vault/wiki/brief.md` from `BRIEF`, whose `Cases` of its Next session open with the line
that opens the next sprint, and `vault/wiki/log.md` from `LOG`, its heading and the
paragraph under it alone. No judgment of those writers stands here; an error of one is a
`ship:` line, and the file is not written.

It also makes the clean version a Claude Code plugin and its catalogue (case 816): it copies
`plugin/plugin.json`, the manifest of the plugin `guppi`, and `plugin/marketplace.json`, the
catalogue `guppi-marketplace`, into `.claude-plugin/`, by `PLUGIN_FILES`, and writes each
file under `plugin/skills/` to the same path under `skills/`, where Claude Code finds the
skills of a plugin, by `PLUGIN_SKILLS`, and judges and cleans it like each other file it
writes (case 818). No file of `plugin/` is written at its own
path. The manifest it writes takes as its `version` the number of the highest tag
`prod-x.y.z` in the history of the commit of the working tree, such as `0.2.0` for
`prod-0.2.0`; `VERSION_TAG` is the one judgment of the form of such a tag, and a tag of
another form, such as `prod-2`, gives no version. With no such tag it prints a line, exits 1
and writes nothing.

A pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its
id, each id of a list included — stands in a bracket of its own at the end of its sentence,
with the words that go with it (case 807.1). In each text file it writes it removes whole
each bracket that holds a pointer, with the space before it, and each `[[decision-case-N]]`
link; a bracket with no pointer stays. It writes each other `[[…]]` link of a Markdown file
to a page or a file it does not write as the slug in a code span, by `WIKILINK` of
`.guppi/guppi/lint.py`. A case id after `[case `, `#case-` or `:case ` — the form of a ledger line
or a mark — is no pointer, and neither is one in a code span or a fenced block of a Markdown
file or of the text of a `schema.yaml`; the example Case of `case-example.md` stands in such
a block, and the text around it is judged like any other (case 815). In a Python file under
`TESTS`, `.guppi/tests/`, it removes and judges only in the comments and the docstrings: each
other string is a sample, put aside with the code around it by `masked_strings` of
`.guppi/guppi/pointers.py`, so a case id in the data of a test is neither removed nor judged
(case 822). Each page it writes carries `origin` and `sprint` `SHIPPED`, the date
of the run in `created` and a `## History` of one line; its link fields, `LINK_FIELDS` of
`.guppi/guppi/lint.py`, keep only the pages it writes. The page is written by `write_page` of
`.guppi/guppi/generate.py`.

Then it reads what it wrote and prints `ship: <file>:<line>: <what>` for each pointer that
stands outside such a bracket and each marker line of `MARKER` of `.guppi/guppi/pages.py` that
opens or closes the section of a page without `core: true`; any such line exits 1, and a
Case rewords that text at its source. A case number with no word `case` before it is no
pointer and stays in the copy, but in a comment or a docstring of a Python file
`bare_numbers` prints it and exits 1 too: a bracket of case numbers alone, an opening of
one or more case numbers and a colon, a comment that is one or more case numbers alone, a
list joined in each shape alike (cases 808.1, 811); it reads the
file by `tokenize`, and a docstring by `python_strings` of `.guppi/guppi/pointers.py`, so no
code is judged. `--review` also prints each bracket it removes that
holds a word beside its pointers, which sets no exit code. `--check` judges in place each
file outside `vault/` that the copy takes, the files under `plugin/skills/` and the two
files of `plugin/`, the tests under `.guppi/tests/` and `.github/workflows/checks.yml`
included, and no other file of `.github/`, but `NOT_CLEANED`, `.guppi/uv.lock`, which the
copy writes as it stands, and this module and its tests, which the copy does not take; it
prints the same lines, writes nothing, reads no tag and does not judge the status of a page
(case 822); `guppi check` runs it. A folder that is not empty exits 2 with
nothing written. The judgment of a pointer — `outside`, and `masked`, `masked_strings` and
`removed` that it calls — lives in `.guppi/guppi/pointers.py`, which this module and
`.guppi/guppi/prespec.py` import; this module holds no copy of it (cases 820.5, 822).
Rule page: `vault/wiki/rules/rule-clean-branch.md`.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tokenize
from datetime import date, datetime
from io import StringIO
from pathlib import Path

from guppi import backlog, glossary
from guppi.caseid import ID
from guppi.event import project_root
from guppi.generate import READING_DATE, RESULT, write_page
from guppi.lint import LINK_FIELDS, MAKE_TARGET, RENDER, WIKILINK
from guppi.pages import (
    CATEGORIES,
    DRAFT_CORE,
    HISTORY,
    MARKER,
    SHIPPED,
    Page,
    is_core,
    is_draft_core,  # the one judgment of a draft page with `core: true` (case 822)
    read_vault,
    slug_of,
    wiki_root,
)
from guppi.pointers import (  # the one judgment of a pointer, shared with pre-spec (case 820.5)
    DECISION_LINK,
    masked,
    masked_strings,
    outside,
    python_strings,
    removed,
    unmasked,
)
from guppi.sprint import closed_form

ROOT_FILES = ("CLAUDE.md", ".gitattributes")
TREES = (".guppi", ".claude")
# the CI of the checks, the one file of `.github/` the copy takes; the workflow that writes
# `prod` stays here (case 822)
CI = ".github/workflows/checks.yml"
# the description of the project in `CLAUDE.md` and in the Render of its page: the copy
# writes `BLANK_DESCRIPTION` between the marker lines (case 822)
DESCRIBED_FILE, DESCRIBED_PAGE = "CLAUDE.md", "rule-claude-md"
DESCRIPTION_MARKERS = ("<!-- project-description -->", "<!-- /project-description -->")
BLANK_DESCRIPTION = ("# Project", "", "Project description: not set yet.")
# the session files of a project: the copy writes each as a skeleton, never the file of this
# project (case 822)
SPRINT, BACKLOG, GLOSSARY, BRIEF_FILE, LOG_FILE = (
    f"vault/wiki/{name}.md" for name in ("sprint", "backlog", "glossary", "brief", "log")
)
SKELETONS = (SPRINT, BACKLOG, GLOSSARY, BRIEF_FILE, LOG_FILE)
# the files of this project, and the module of this command with its tests, which only the
# repository of GUPPI runs (cases 820.5, 822)
LEFT_OUT = (
    *SKELETONS,
    "guppi.toml",
    ".guppi/guppi/ship.py",
    ".guppi/tests/test_ship.py",
)
# the tests: in a Python file here only the comments and the docstrings are cleaned and
# judged, and each other string is a sample (case 822)
TESTS = ".guppi/tests/"
# a folder or a file of these names, at any depth of a tree: the Python environment, the
# cache folders of Python, pytest and ruff, and the settings of one person
SKIPPED_NAMES = ("__pycache__", ".pytest_cache", ".ruff_cache", ".venv", "settings.local.json")
NOT_CLEANED = (".guppi/uv.lock",)  # a lock file is data of the package manager, not text of ours
TAGS = "vault/wiki/tags.md"
HISTORY_LINE = "- {day} shipped with GUPPI"
# the `## Result` of a shipped Estimate, with and without the date of its last reading
RESULT_LINE = "{day}, passed in the repository of GUPPI."
RESULT_UNDATED = "Passed in the repository of GUPPI."
# the skeletons of the brief and of the log (case 822): the brief opens the next sprint
BRIEF = f"""# Brief — GUPPI installed

## Where things stand

- GUPPI is installed from its clean version; no session has run in this project yet.

## Flags

- none

## Next session

### Cases

- open the next sprint — no sprint is open since the close of {SHIPPED}

### Work

- none

### Ask the person

- none
"""
LOG = """# Log

Every page change, one line each, appended by a hook and never by an agent following an
instruction. The global feed; a page's own `## History` is the per-page view.
"""
# the manifest and the catalogue of the plugin: the path in the copy, and the path of its
# template in this repository
MANIFEST = ".claude-plugin/plugin.json"
PLUGIN_FILES = {
    MANIFEST: "plugin/plugin.json",
    ".claude-plugin/marketplace.json": "plugin/marketplace.json",
}
# each file under the first folder is written to the same path under the second
PLUGIN_SKILLS = ("plugin/skills", "skills")
# a tag of a version, `prod-x.y.z`; `prod-2` or `prod-0.2` is none
VERSION_TAG = re.compile(r"prod-((0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*))")

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
    judgment of a bare case number (case 808.1). A docstring is one of `python_strings` of
    `.guppi/guppi/pointers.py`, the one judgment of a docstring (case 822); a comment that
    only opens with a number, such as a count, is no finding. A text that does not tokenize
    gives none."""
    try:
        tokens = list(tokenize.generate_tokens(StringIO(text).readline))
    except (tokenize.TokenError, SyntaxError):
        return []
    out = []
    for token in tokens:
        if token.type == tokenize.COMMENT:
            body = token.string[1:]
            out += [(token.start[0], f"a bare case number: {n}") for _, n in bare_in(body)]
    for begin, end, docstring in python_strings(text):
        if not docstring:
            continue
        string = text[begin:end]
        quote = STRING_PREFIX.match(string)
        start = quote.end() if quote else 0
        line = text.count("\n", 0, begin) + 1
        out += [
            (line + string.count("\n", 0, start + at), f"a bare case number: {n}")
            for at, n in bare_in(string[start:])
        ]
    return sorted(out)


def clean(
    text: str, sample: bool, known: set[str] | None = None, strings: bool = False
) -> tuple[str, list[tuple[int, str]]]:
    """The text as the copy holds it, and the brackets `--review` lists: each bracket that
    holds a pointer and each `[[decision-case-N]]` link removed; with `known`, each other
    `[[…]]` link to a slug outside it written as the slug in a code span (case 807.1); with
    `strings`, a test file, each string but a docstring kept as a sample (case 822)."""
    body, spans = masked_strings(text) if strings else masked(text, sample)
    body, review = removed(DECISION_LINK.sub("", body), keep_lines=False)
    if known is not None:

        def link(match: re.Match) -> str:
            slug = match.group(1).strip()
            return match.group(0) if slug in known else f"`{slug}`"

        body = WIKILINK.sub(link, body)
    return unmasked(body, spans), [(n, unmasked(b, spans)) for n, b in review]


def leftovers(
    text: str, sample: bool, loose: set[str], python: bool = False, strings: bool = False
) -> list[tuple[int, str]]:
    """`(line, what)` for each pointer outside a bracket, and each marker of a page in
    `loose`, the page slugs without `core`, that the copy must not hold; with `python`, each
    bare case number of `bare_numbers` too; with `strings`, a test file, no pointer in a
    string but a docstring (case 822)."""
    out = []
    for number, line in enumerate(text.split("\n"), start=1):
        marker = MARKER.match(line.strip())
        if marker and marker.group(2) in loose:
            out.append((number, f"a section of {marker.group(2)}, a page without core: true"))
    if python:
        out += bare_numbers(text)
    return sorted(out + outside(text, sample, strings))


def is_sample_file(name: str) -> bool:
    """Whether the code spans and fenced blocks of a file hold samples: Markdown, and the
    text of a `schema.yaml`."""
    return name.endswith(".md") or Path(name).name == "schema.yaml"


def is_test_file(name: str) -> bool:
    """Whether a file is a Python file of the tests, whose strings but the docstrings are
    samples (case 822)."""
    return name.startswith(TESTS) and name.endswith(".py")


def tree_files(project_dir: Path, top: str) -> list[str]:
    root = project_dir / top
    if not root.is_dir():
        return []
    found = []
    for folder, dirs, files in os.walk(root):
        here = Path(folder).relative_to(project_dir)
        # a skipped folder is not walked, so the Python environment costs nothing
        dirs[:] = [d for d in dirs if d not in SKIPPED_NAMES]
        found += [
            (here / f).as_posix()
            for f in files
            if f not in SKIPPED_NAMES and not f.endswith(".pyc")
        ]
    return sorted(found)


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


def ships(estimate: Page, written: set[str]) -> bool:
    """Whether the copy writes an Estimate (case 822): `passed`, its `target`, read by
    `slug_of`, in `written`, the pages with `core: true` the copy writes, and no target of the
    `Makefile` in its `method`, by `MAKE_TARGET`, since the copy holds no `Makefile`."""
    return (
        estimate.props.get("status") == "passed"
        and slug_of(estimate.props.get("target")) in written
        and not MAKE_TARGET.search(str(estimate.props.get("method") or ""))
    )


def result_line(estimate: Page) -> str:
    """The `## Result` of an Estimate in the copy (case 822): the date of its `checked`, else
    the date its Result opens with, by `READING_DATE`, and that it passed here."""
    day = estimate.props.get("checked")
    if not day:
        match = READING_DATE.match(estimate.sections.get(RESULT) or "")
        day = match.group(1) if match else None
    return RESULT_LINE.format(day=day) if day else RESULT_UNDATED


def blank_description(text: str) -> str:
    """The text with `BLANK_DESCRIPTION` — the heading `# Project`, a blank line and a line
    that says the description is not set yet — in place of each line between the marker
    lines of `DESCRIPTION_MARKERS`, which stay; every other line as it is, and a text without
    both marker lines, or with the closing one first, as it is. The one writer of the blank
    description, over `CLAUDE.md` and over the Render of `rule-claude-md` that the copy holds
    (case 822)."""
    lines = text.split("\n")
    opening, closing = DESCRIPTION_MARKERS
    if opening not in lines or closing not in lines[lines.index(opening) :]:
        return text
    start = lines.index(opening)
    end = lines.index(closing, start)
    return "\n".join(lines[: start + 1] + list(BLANK_DESCRIPTION) + lines[end:])


def drafts(project_dir: Path) -> list[str]:
    """A line `ship: <page>: a page with core: true that is draft` for each page of the vault
    that `is_draft_core` of `.guppi/guppi/pages.py` accepts, by its path (case 822)."""
    vault = read_vault(wiki_root(project_dir))
    return [
        f"ship: vault/wiki/{page.category}/{page.slug}.md: {DRAFT_CORE}"
        for category in CATEGORIES
        for page in vault[category]
        if not page.error and is_draft_core(page)
    ]


def shipped_page(page: Page, slugs: set[str], day: date) -> tuple[dict, dict]:
    """The props and sections of a page as the copy holds it (case 804.6); an Estimate gets
    `core: true` and a `## Result` of one line (case 822)."""
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
    if page.slug == DESCRIBED_PAGE and RENDER in sections:
        sections[RENDER] = blank_description(sections[RENDER])
    if page.category == "estimates":
        props["core"] = True
        sections[RESULT] = result_line(page)
    sections[HISTORY] = HISTORY_LINE.format(day=day)
    return props, sections


def version(project_dir: Path) -> str | None:
    """The number of the highest tag `prod-x.y.z` in the history of the commit of the working
    tree, such as `0.2.0` for `prod-0.2.0`; None when there is none, or no git history."""
    result = subprocess.run(
        ["git", "tag", "--list", "prod-*", "--merged", "HEAD"],
        cwd=project_dir,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    if result.returncode != 0:
        return None
    found = [VERSION_TAG.fullmatch(tag.strip()) for tag in result.stdout.splitlines()]
    numbers = [match.group(1) for match in found if match]
    if not numbers:
        return None
    return max(numbers, key=lambda number: tuple(int(part) for part in number.split(".")))


def plan(project_dir: Path) -> tuple[dict[str, str], list[Page], set[str], set[str]]:
    """The files the copy takes from the tree, each path in the copy mapped to its path in the
    tree, the pages it writes — each page but an Estimate with `core: true`, then each
    Estimate that `ships` accepts — the slugs and hub names a link of the copy may name, and
    the page slugs it does not write."""
    vault = read_vault(wiki_root(project_dir))
    pages = [page for category in CATEGORIES for page in vault[category]]
    core = [
        page for page in pages if page.category != "estimates" and is_core(page) and not page.error
    ]
    written = {page.slug for page in core}
    core += [page for page in vault["estimates"] if not page.error and ships(page, written)]
    slugs = {page.slug for page in core}
    loose = {page.slug for page in pages} - slugs
    written_governed, refused = governed(pages)

    names = [name for name in ROOT_FILES if (project_dir / name).is_file()]
    names.append(CI)
    for top in TREES:
        names += tree_files(project_dir, top)
    names += [f"vault/wiki/{category}/schema.yaml" for category in CATEGORIES]
    names.append(TAGS)
    names += sorted(written_governed)
    taken = {name: name for name in names}
    taken.update(PLUGIN_FILES)
    skills, target = PLUGIN_SKILLS
    taken.update((target + name[len(skills) :], name) for name in tree_files(project_dir, skills))
    files = {
        name: source
        for name, source in taken.items()
        if name not in refused and name not in LEFT_OUT and (project_dir / source).is_file()
    }
    names = list(files) + [f"vault/wiki/{page.category}/{page.slug}.md" for page in core]
    hubs = {Path(name).stem for name in names if Path(name).parent.as_posix() == "vault/wiki"}
    known = slugs | hubs | {f"{p.category}/{p.slug}" for p in core}
    return files, core, known, loose


def judged(name: str, text: str, known: set[str], loose: set[str]) -> tuple[str, list, list]:
    """The text of a file as the copy holds it, and its `ship:` lines and `--review` lines by
    the lines of `text`; a file of `NOT_CLEANED` is not judged."""
    if name in NOT_CLEANED:
        return text, [], []
    sample, strings = is_sample_file(name), is_test_file(name)
    cleaned, review = clean(text, sample, known if name.endswith(".md") else None, strings)
    python = name.endswith(".py")
    found = leftovers(text, sample, loose, python, strings)
    lines = [f"ship: {name}:{n}: {what}" for n, what in found]
    reviewed = [f"ship: {name}:{n}: a bracket with words: {' '.join(b.split())}" for n, b in review]
    return cleaned, lines, reviewed


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def manifest(template: str, number: str) -> str:
    """The manifest of the plugin as the copy holds it: its template with `version` after
    `name`."""
    props = json.loads(template)
    shipped = {"name": props.pop("name")} if "name" in props else {}
    shipped["version"] = number
    shipped.update(props)
    return json.dumps(shipped, indent=2, ensure_ascii=False) + "\n"


def ship(project_dir: Path, folder: Path, day: date, number: str) -> tuple[list[str], list[str]]:
    """Writes the clean version into `folder`, its manifest with the version `number`; the
    lines of what remains, empty when clean, and the lines of `--review`."""
    files, core, known, loose = plan(project_dir)
    slugs = {page.slug for page in core}
    for name, source in files.items():
        target = folder / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(project_dir / source, target)
    if DESCRIBED_FILE in files:
        path = folder / DESCRIBED_FILE
        text = path.read_text(encoding="utf-8")
        if blank_description(text) != text:
            path.write_text(blank_description(text), encoding="utf-8", newline="\n")
    if MANIFEST in files:
        path = folder / MANIFEST
        text = manifest(path.read_text(encoding="utf-8"), number)
        path.write_text(text, encoding="utf-8", newline="\n")
    names = list(files)
    for page in core:
        props, sections = shipped_page(page, slugs, day)
        name = f"vault/wiki/{page.category}/{page.slug}.md"
        write_page(folder / name, props, sections, page.category)
        names.append(name)

    out, review = settled(folder, names, known, loose)
    # the skeletons read the pages as the copy holds them, so they come after the cleaning
    texts, errors = skeletons(folder)
    for name, text in texts.items():
        (folder / name).write_text(text, encoding="utf-8", newline="\n")
    lines, reviewed = settled(folder, list(texts), known, loose)
    return out + errors + lines, review + reviewed


def settled(
    folder: Path, names: list[str], known: set[str], loose: set[str]
) -> tuple[list[str], list[str]]:
    """Cleans in place each file of `names` the copy wrote, and gives its `ship:` lines and
    its `--review` lines."""
    out, review = [], []
    for name in names:
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


def skeletons(folder: Path) -> tuple[dict[str, str], list[str]]:
    """The session files of the copy in `folder`, each by its own writer over the pages the
    copy holds, and a `ship:` line for each writer that refuses (case 822)."""
    pages = read_vault(wiki_root(folder))
    by_slug = {p.slug: p for category in pages.values() for p in category if not p.error}
    terms = glossary.glossary_page(pages)
    rendered = {
        BACKLOG: backlog.render(folder, pages),
        GLOSSARY: (
            glossary.render(terms, by_slug)
            if terms is not None
            else (None, f"glossary: no live {glossary.SLUG} page")
        ),
    }
    texts = {SPRINT: closed_form(SHIPPED), BRIEF_FILE: BRIEF, LOG_FILE: LOG}
    errors = []
    for name, (text, error) in rendered.items():
        if text is None:
            errors.append(f"ship: {name}: {error}")
        else:
            texts[name] = text
    return texts, errors


def check(project_dir: Path) -> tuple[list[str], list[str]]:
    """The lines of `ship` for each file outside `vault/` that the copy takes, judged in
    place in the working tree, at its path there; no tag is read and nothing is written."""
    files, _, known, loose = plan(project_dir)
    out, review = [], []
    for name, source in files.items():
        if name.startswith("vault/"):
            continue
        text = read_text(project_dir / source)
        if text is None:
            continue
        _, lines, reviewed = judged(source, text, known, loose)
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
    p.add_argument(
        "--allow-draft",
        action="store_true",
        help="write the copy while a page with core: true is draft, for an install by hand",
    )
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    args = parser().parse_args(argv)
    if args.check:  # the status of a page is not judged here (case 822)
        lines, review = check(project_dir)
    elif args.folder is None:
        print("ship: name an empty folder, or pass --check", file=stderr)
        return 2
    else:
        folder = Path(args.folder)
        if folder.exists() and any(folder.iterdir()):
            print(f"ship: {folder} is not empty; nothing written", file=stderr)
            return 2
        # a draft page with `core: true` stops the build before it writes; with
        # `--allow-draft` its line is printed and sets no exit code (case 822)
        draft = drafts(project_dir)
        for line in draft:
            print(line, file=stdout)
        if draft and not args.allow_draft:
            return 1
        number = version(project_dir)
        if number is None:
            print("ship: no tag prod-x.y.z in the history of HEAD; nothing written", file=stderr)
            return 1
        folder.mkdir(parents=True, exist_ok=True)
        lines, review = ship(project_dir, folder, now.date(), number)
    for line in lines + (review if args.review else []):
        print(line, file=stdout)
    return 1 if lines else 0
