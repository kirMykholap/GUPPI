"""`guppi index [--check]` — one line per live page, per category.

Writes `vault/wiki/<category>-index.md` for entities, rules, estimates, lessons and
insights: `slug: text`, sorted by slug, the file present even when empty. The text is
`purpose` for entities and rules, `root_cause` for lessons, `pattern` for insights, and the
`## Criterion` section collapsed to one line for estimates. Archived pages and decisions
have no line. `--check` renders in memory, names every stale file, exits 1 and writes
nothing. Rule page: `vault/wiki/rules/rule-index.md`.
"""

import argparse
import sys
from pathlib import Path

from guppi.event import project_root
from guppi.pages import Page, read_category, wiki_root

INDEXED = {
    "entities": ("prop", "purpose"),
    "rules": ("prop", "purpose"),
    "estimates": ("section", "## Criterion"),
    "lessons": ("prop", "root_cause"),
    "insights": ("prop", "pattern"),
}


def one_line(text) -> str:
    return " ".join(str(text or "").split())


def line_text(page: Page, category: str) -> str:
    source, name = INDEXED[category]
    if source == "prop":
        return one_line(page.props.get(name))
    return one_line(page.section(name))


def index_text(pages: list[Page], category: str) -> str:
    lines = [
        f"{page.slug}: {line_text(page, category)}" for page in sorted(pages, key=lambda p: p.slug)
    ]
    return "".join(line + "\n" for line in lines)


def index_path(wiki: Path, category: str) -> Path:
    return wiki / f"{category}-index.md"


def plan(wiki: Path) -> dict[Path, str]:
    return {
        index_path(wiki, category): index_text(read_category(wiki, category), category)
        for category in INDEXED
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi index", description=__doc__.split("\n\n")[1])
    p.add_argument("--check", action="store_true", help="report stale indexes; write nothing")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    wiki = wiki_root(project_dir)
    try:
        outputs = plan(wiki)
    except Exception as exc:  # noqa: BLE001 — report, never traceback
        print(f"index: cannot read the vault: {exc}", file=stderr)
        return 1
    if args.check:
        stale = [
            path
            for path, text in outputs.items()
            if not path.exists() or path.read_text(encoding="utf-8") != text
        ]
        for path in stale:
            print(f"index: {path.relative_to(project_dir).as_posix()} is stale", file=stdout)
        return 1 if stale else 0
    wiki.mkdir(parents=True, exist_ok=True)
    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8", newline="\n")
    return 0
