"""Draft one `wiki/rules/` page per vault-facing family, from the cleanup verdicts.

WHO WRITES AND WHO ANSWERS. The librarian is the only writer of `wiki/`, and this script does not
change that: it drafts, the librarian is dispatched once, reads the output WHOLE, repairs it and
answers for it. The owner ratified that split on 2026-08-30 against the librarian authoring the
pages by hand, on the ground that the clauses are already machine content - a title and a slug
lifted out of frontmatter - so writing them by hand means retyping the output of the script that
collected them.

WHAT A CLAUSE IS. The title of the decision, plus a link to it. Only two of the 295 prohibitions
carry a `# The rule text` section, so there is no written rule text to lift; the title is what
names the claim, which is why titles in this store are sentences.

WHICH SLUG THE PAGE TAKES. The `authority:` of ONE of the family's decisions - the earliest-decided
one, which is the answer that opened the question. That is mechanical on purpose: any other pick is
a judgement made 18 times by a script, and the librarian can move it. The same decision is named in
`decided_by:`, which this folder requires.

Usage:  python scripts/build-family-rules.py [--dry-run]
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VAULT = REPO / "job_hunt_ai_vault"
REGISTER = VAULT / "authority.md"
RULES = VAULT / "wiki" / "rules"
VERDICTS = REPO / "docs" / "vault-cleanup-verdicts.md"

# The LOCAL date, and the linter is silenced rather than obeyed - every date in this store is a
# calendar day of the owner's rather than an instant, so UTC would stamp yesterday on a page written
# late in his evening. Same reason and same spelling as `scripts/vault-measure.py`.
TODAY = date.today().isoformat()  # noqa: DTZ011


def families() -> list[tuple[str, str, list[str]]]:
    text = REGISTER.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"^- group: (.+?)\n(.*?)(?=^- group: |\Z)", text, re.MULTILINE | re.DOTALL):
        name = m.group(1).strip()
        body = m.group(2)
        dm = re.search(r"^  definition: (.*?)(?=\n  slugs:|\n  aliases:|\Z)", body, re.MULTILINE | re.DOTALL)
        definition = " ".join(dm.group(1).split()) if dm else ""
        sm = re.search(r"^  slugs: \[(.*?)\]", body, re.MULTILINE | re.DOTALL)
        slugs = [s.strip() for s in sm.group(1).replace("\n", " ").split(",") if s.strip()] if sm else []
        out.append((name, definition, slugs))
    return out


def decisions_by_slug() -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = {}
    for path in sorted((VAULT / "wiki" / "decisions").glob("*.md")):
        head = path.read_text(encoding="utf-8")[:4000]
        page = {"file": path.stem}
        for key in ("title", "authority", "binding", "decided", "tags"):
            m = re.search(rf"^{key}:\s*(.+?)\s*$", head, re.MULTILINE)
            page[key] = m.group(1).strip().strip('"').strip("'") if m else ""
        if page["binding"] != "prohibition" or not page["authority"]:
            continue
        out.setdefault(page["authority"], []).append(page)
    return out


def verdicts() -> dict[str, str]:
    out = {}
    for line in VERDICTS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- (.+?):\s*(\S.*)$", line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


# RULE 10 OF THE GATE: no title and no filename carries a measurable quantity, and the rule is
# unconditional - there is no way for a page to declare itself exempt, and the `quantity:` field
# that once carried such a declaration was withdrawn after two of them turned out to be false.
# `one` and `first` are exempt, measured rather than assumed. A family name that counts something
# therefore cannot be used as a title unchanged, and the fix is to NAME what is counted.
QUANTITY = re.compile(
    r"\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d+)\b", re.IGNORECASE
)
TITLE_OVERRIDES = {
    # "the tag dictionary and the two languages" counts the languages. Named instead of counted.
    "the tag dictionary and the two languages": "The tag dictionary, and the question asked in "
    "one language of a corpus written in another",
}


def slugify(name: str) -> str:
    s = name.lower().replace("`", "").replace("’", "").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def title_of(name: str) -> str:
    """The family question as a rule title, refused rather than written if it counts something."""
    if name in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[name]
    clean = name.replace("`", "").strip()
    title = clean[0].upper() + clean[1:]
    if QUANTITY.search(title):
        raise SystemExit(
            f"build-family-rules: the title for '{name}' carries a quantity and rule 10 of the "
            "gate is unconditional. Add an entry to TITLE_OVERRIDES that names what is counted."
        )
    return title


def pick_tags(members: list[dict[str, str]]) -> list[str]:
    """2 to 4 tags, taken from the family's own decisions so every one is already registered."""
    counter: Counter[str] = Counter()
    for member in members:
        for tag in re.findall(r"[a-z0-9-]+", member["tags"]):
            counter[tag] += 1
    picked = [tag for tag, _ in counter.most_common(3)]
    return picked or ["vault"]


def page_text(name: str, definition: str, members: list[dict[str, str]], anchor: dict[str, str]) -> str:
    tags = ", ".join(pick_tags(members))
    lines = [
        "---",
        f'title: "{title_of(name)}"',
        "type: rule",
        "status: current",
        f"authority: {anchor['authority']}",
        "render: authority",
        "basis: human",
        "sprint: S3",
        f"created: {TODAY}",
        'sources: ["docs/vault-cleanup-families.md", "job_hunt_ai_vault/authority.md"]',
        f"decided_by: [[{anchor['file']}]]",
        f"tags: [{tags}]",
        "---",
        "",
        f"# {title_of(name)}",
        "",
    ]
    if definition:
        lines += [definition, ""]
    lines += [
        (
            "**This rule is written into no file.** It is found by its `authority:` slug, by "
            "`.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each "
            "clause below is the claim of a decision discharged into this page and moved to "
            "`archive/`; the decision is where the reasoning and the rejected alternative stayed."
        ),
        "",
        "# The rule text",
        "",
    ]
    for member in sorted(members, key=lambda m: m["title"]):
        lines.append(f"- {member['title']} ([[{member['file']}]])")
    lines += [
        "",
        "# How this page was written",
        "",
        (
            f"Drafted {TODAY} by `scripts/build-family-rules.py` from the family *{name}* of "
            f"`job_hunt_ai_vault/authority.md`, which held {len(members)} pages carrying "
            f"`binding: prohibition`. The slug is the one carried by [[{anchor['file']}]], the "
            "earliest-decided of them, and that decision is named in `decided_by:` for the same "
            "reason. The clause of each member is its title, because a written rule text of its "
            "own is something almost no prohibition in this corpus ever carried."
        ),
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    dry = "--dry-run" in sys.argv
    verdict = verdicts()
    by_slug = decisions_by_slug()

    # Which slugs a LIVE concept or entity already carries. These are the convergence targets: a
    # rule taking one of them shares it with a page that stays in `wiki/`, so the hook matches.
    live_kinds: dict[str, str] = {}
    for folder in ("concepts", "entities"):
        for path in sorted((VAULT / "wiki" / folder).glob("*.md")):
            m = re.search(r"^authority:\s*(.+?)\s*$", path.read_text(encoding="utf-8")[:4000], re.MULTILINE)
            if m:
                live_kinds[m.group(1).strip().strip('"').strip("'")] = folder

    written, index_lines = 0, []

    for name, definition, slugs in families():
        if verdict.get(name) != "vault-facing":
            continue
        members = [page for slug in slugs for page in by_slug.get(slug, [])]
        if not members:
            print(f"  SKIP {name}: no prohibition members")
            continue
        anchor = min(members, key=lambda m: (m["decided"] or "9999-99-99", m["file"]))
        # THE FILENAME IS SLUGIFIED FROM THE TITLE AND NOT FROM THE FAMILY NAME, so a title fixed
        # for rule 10 carries the filename with it. Rule 10's filename half is an advisory rather
        # than a red verdict - a filename is an address and repairing one moves every inbound link
        # - which is exactly why it is got right before the page exists rather than after.
        target = RULES / f"{slugify(title_of(name))}.md"
        if target.exists():
            print(f"  SKIP {target.name}: already exists, refusing to clobber")
            continue
        text = page_text(name, definition, members, anchor)
        if not dry:
            target.write_text(text, encoding="utf-8", newline="\n")
        written += 1
        index_lines.append(f"- [[{target.stem}]] — `{anchor['authority']}`")
        # THE SLUG IS THE ADDRESS THE WHOLE DELIVERY MATCHES ON, so the mechanical pick is printed
        # WITH ITS ALTERNATIVES rather than presented as settled. A slug already carried by a live
        # concept or entity of the same family is the better choice where one exists: the rule and
        # that page then share it from the day it is written, which is the convergence the owner
        # ruled for, and the hook has something to match on rather than nothing.
        live = [f"{s} ({live_kinds[s]})" for s in slugs if s in live_kinds]
        print(f"  {target.name}  {len(members)} clause(s)  authority: {anchor['authority']}")
        if live:
            print(f"      slug also carried by a live page: {', '.join(live)}")

    print(f"\nbuild-family-rules: {'would write' if dry else 'wrote'} {written} page(s)")
    print("\nLines for index.md - THE LIBRARIAN writes them, not this script:")
    for line in index_lines:
        print(f"  {line}")


if __name__ == "__main__":
    main()
