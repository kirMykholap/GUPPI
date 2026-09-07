"""Build the cleanup review table from the authority register and the live corpus.

The table is DERIVED and reproducible: rerun this rather than editing its output. The one
thing written by hand is the verdict per family, and it does NOT live in the output file -
it lives in `docs/vault-cleanup-verdicts.md`, which this script reads. That split exists
because this script overwrites its output whole: a verdict written into the table would be
destroyed by the next regeneration, and a generator that parses its own previous output to
recover one breaks silently instead.

The output is English because it is a document under `docs/`, which the forward-only English
rule reaches with the FILE as its unit - and regenerating the file touches all of it.

Usage:  python scripts/build-families-table.py
"""

from __future__ import annotations

import re
import subprocess
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VAULT = REPO / "job_hunt_ai_vault"
REGISTER = VAULT / "authority.md"
WIKI = VAULT / "wiki"
VERDICTS = REPO / "docs" / "vault-cleanup-verdicts.md"
OUT = REPO / "docs" / "vault-cleanup-families.md"

FOLDERS = ("decisions", "concepts", "entities", "proposals", "lessons", "rules")

# The three verdicts a family of part one may take. Written into the verdicts file by hand;
# anything else there is reported as unknown rather than silently accepted.
LEGAL_VERDICTS = ("vault-facing", "harness-facing", "none")


def read_families() -> list[tuple[str, str, list[str]]]:
    """Return (name, definition, slugs) per group, in register order."""
    text = REGISTER.read_text(encoding="utf-8")
    out: list[tuple[str, str, list[str]]] = []
    for match in re.finditer(r"^- group: (.+?)\n(.*?)(?=^- group: |\Z)", text, re.MULTILINE | re.DOTALL):
        name = match.group(1).strip()
        body = match.group(2)
        definition = ""
        dm = re.search(r"^  definition: (.*?)(?=\n  slugs:|\n  aliases:|\Z)", body, re.MULTILINE | re.DOTALL)
        if dm:
            definition = " ".join(dm.group(1).split())
        slugs: list[str] = []
        sm = re.search(r"^  slugs: \[(.*?)\]", body, re.MULTILINE | re.DOTALL)
        if sm:
            slugs = [s.strip() for s in sm.group(1).replace("\n", " ").split(",") if s.strip()]
        out.append((name, definition, slugs))
    return out


def read_pages() -> list[dict[str, str]]:
    """Frontmatter of every live page under wiki/, one dict per page."""
    pages: list[dict[str, str]] = []
    for folder in FOLDERS:
        for path in sorted((WIKI / folder).glob("*.md")):
            head = path.read_text(encoding="utf-8")[:4000]
            page = {"slug": path.stem, "folder": folder}
            for key in ("title", "authority", "binding", "status"):
                m = re.search(rf"^{key}:\s*(.+?)\s*$", head, re.MULTILINE)
                page[key] = m.group(1).strip().strip('"').strip("'") if m else ""
            pages.append(page)
    return pages


def read_verdicts() -> dict[str, str]:
    """Family name -> verdict, from the hand-written file. Absent file means no verdicts yet."""
    if not VERDICTS.exists():
        return {}
    verdicts: dict[str, str] = {}
    for line in VERDICTS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- (.+?):\s*(\S.*)$", line)
        if m:
            verdicts[m.group(1).strip()] = m.group(2).strip()
    return verdicts


def head_commit() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return "unknown"


def entry(page: dict[str, str], mark: str = "") -> str:
    prefix = f"**{mark}** " if mark else ""
    return f"- {prefix}{page['title']}  \n  `{page['slug']}` — `{page['authority']}`"


def verdict_line(name: str, verdicts: dict[str, str], legal: bool) -> str:
    value = verdicts.get(name, "")
    if not value:
        return "**verdict:**"
    if legal and value not in LEGAL_VERDICTS:
        return f"**verdict:** {value}  ← NOT ONE OF {', '.join(LEGAL_VERDICTS)}"
    return f"**verdict:** {value}"


def main() -> None:
    families = read_families()
    pages = read_pages()
    verdicts = read_verdicts()

    # A slug may be carried by MORE THAN ONE page since 2026-08-30 - rule 3 of the gate compares
    # slugs within a type, and a shared slug across types is the route a reader walks. A dict
    # keyed by slug silently drops the second page, which cost two prohibitions on the first run.
    by_slug: dict[str, list[dict[str, str]]] = {}
    for page in pages:
        if page["authority"]:
            by_slug.setdefault(page["authority"], []).append(page)
    definitions = {name: definition for name, definition, _ in families}

    prohibitions: dict[str, list[dict[str, str]]] = {}
    concepts: dict[str, list[dict[str, str]]] = {}
    entities: dict[str, list[dict[str, str]]] = {}
    for name, _, slugs in families:
        for slug in slugs:
            for page in by_slug.get(slug, []):
                if page["folder"] == "decisions" and page["binding"] == "prohibition":
                    prohibitions.setdefault(name, []).append(page)
                elif page["folder"] == "concepts":
                    concepts.setdefault(name, []).append(page)
                elif page["folder"] == "entities":
                    entities.setdefault(name, []).append(page)

    ungrouped = sorted(
        {p["authority"] for p in pages if p["authority"]} - {s for _, _, ss in families for s in ss}
    )

    total_prohibitions = sum(len(v) for v in prohibitions.values())
    lines: list[str] = []
    add = lines.append

    add("# Cleanup review table — the families")
    add("")
    add(
        # The LOCAL date - every date in this store is a calendar day of the owner's rather than
        # an instant, so UTC would stamp yesterday on a table built late in his evening.
        f"Built {date.today().isoformat()} at `{head_commit()}` by "  # noqa: DTZ011
        "`scripts/build-families-table.py`, which reads `job_hunt_ai_vault/authority.md`, the "
        "frontmatter of every live page under `wiki/`, and the hand-written verdicts in "
        "`docs/vault-cleanup-verdicts.md`. This file is derived: rerun the script rather than "
        "editing its output. Nothing here is written by hand."
    )
    add("")
    add("## How to read it")
    add("")
    add(
        "**Part one — the prohibitions.** Each family of `authority.md` collects the pages "
        "answering one question. One verdict per family, applied to all its pages at once:"
    )
    add("")
    add(
        "- **vault-facing** — the family's text is addressed to pages of the vault itself, so it "
        "becomes one page in `wiki/rules/` under `render: authority`, carrying the `authority:` "
        "of one of its decisions, and the clauses are the titles below;"
    )
    add(
        "- **harness-facing** — the text belongs in a harness file and needs `governs:` with a "
        "written region, which is a different kind of work; nothing is built for it now and its "
        "decisions stay where they are;"
    )
    add("- **none** — the family produces no rule, and its decisions stay where they are.")
    add("")
    add(
        "**Only a `vault-facing` family releases its decisions to `archive/`.** The repeal frees "
        "a prohibition once the family rule carrying its clause exists, and the other two "
        "verdicts produce no such rule."
    )
    add("")
    add(
        "**Part two — `concepts` and `entities`.** The same families, a different question: "
        "`concepts` become non-functional requirements and `entities` functional ones. The "
        "verdict says what stays in the pair and what goes."
    )
    add("")
    add("## What was measured, and with what")
    add("")
    add(
        f"- **{total_prohibitions} pages** carry `binding: prohibition` in `wiki/decisions/` — "
        "`grep -l '^binding: prohibition' job_hunt_ai_vault/wiki/decisions/*.md | wc -l`"
    )
    add(
        f"- they sit in **{len(prohibitions)} families** of the {len(families)} registered in "
        "`authority.md`"
    )
    add(
        f"- `concepts` and `entities` sit in **{len(set(concepts) | set(entities))} families**"
    )
    add(
        f"- **{len(ungrouped)} slugs** are carried by a page and grouped by no family"
        + (f": {', '.join(f'`{s}`' for s in ungrouped)}" if ungrouped else "")
    )
    add("")
    add("---")
    add("")
    add("# Part one — the prohibitions")
    add("")

    for name in sorted(prohibitions, key=lambda n: (-len(prohibitions[n]), n)):
        add(f"## {name}")
        add("")
        if definitions.get(name):
            add(f"*{definitions[name]}*")
            add("")
        add(f"Prohibitions: {len(prohibitions[name])}.")
        add("")
        add(verdict_line(name, verdicts, legal=True))
        add("")
        for page in sorted(prohibitions[name], key=lambda p: p["title"]):
            add(entry(page))
        add("")

    add("---")
    add("")
    add("# Part two — `concepts` and `entities`")
    add("")
    add(
        "Families that already hold a pair come first: there the work is only to name which of "
        "the two is the functional requirement. Then the ones holding concepts alone, which is "
        "the imbalance this part was opened for."
    )
    add("")

    paired = sorted(set(concepts) & set(entities))
    only_c = sorted(set(concepts) - set(entities))
    only_e = sorted(set(entities) - set(concepts))

    for heading, group in (
        (f"Families with a pair ({len(paired)})", paired),
        (f"Concepts only ({len(only_c)})", only_c),
        (f"Entities only ({len(only_e)})", only_e),
    ):
        add(f"## {heading}")
        add("")
        for name in group:
            add(f"### {name}")
            add("")
            if definitions.get(name):
                add(f"*{definitions[name]}*")
                add("")
            add(verdict_line(name, verdicts, legal=False))
            add("")
            for page in sorted(concepts.get(name, []), key=lambda p: p["title"]):
                add(entry(page, "C"))
            for page in sorted(entities.get(name, []), key=lambda p: p["title"]):
                add(entry(page, "E"))
            add("")

    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"build-families-table: wrote {OUT.relative_to(REPO)}, {len(lines)} lines")
    print(f"  {total_prohibitions} prohibitions in {len(prohibitions)} families")
    print(f"  {len(paired)} paired, {len(only_c)} concepts-only, {len(only_e)} entities-only")
    print(f"  {len(verdicts)} verdict(s) read from {VERDICTS.relative_to(REPO)}")
    if ungrouped:
        print(f"  WARNING: {len(ungrouped)} ungrouped slug(s): {', '.join(ungrouped)}")


if __name__ == "__main__":
    main()
