"""The tags a check holds listed — the one reading of `vault/wiki/tags.md` and of the tag
lines of the Cases of a session (cases 703.1, 703.2).

`registered_tags` reads the rows of `tags.md` by `TAG_ROW`, the header row left out; it gives
None when the file does not stand, and a check then judges no tag. `declared_tags` gives the
tags of the `new_tags` of a `then` block, the entries that the tag lines of a Case make by
`read_tasks` of `.guppi/guppi/ratified.py` (case 702). `ratified_tags` gives the tags that the tag
lines of the Cases stored in `<plan>.checked.json` declare, for each stored Case whose family
holds a decision line among the given ledger records: a Case ratified in the session, whose
tags `tags.md` gains at the librarian's run. The check of the file of a Case in
`.guppi/guppi/casecheck.py`, the ledger hook in `.guppi/guppi/ledger.py` and `register_tags` of
`.guppi/guppi/generate.py` share these functions; none of them reads `tags.md` another way. Rule
pages: `vault/wiki/rules/rule-case-check.md`, `vault/wiki/rules/rule-ledger-write.md`.
"""

import re
from pathlib import Path

TAG_ROW = re.compile(r"^\|\s*([\w-]+)\s*\|")  # a row of `tags.md`, its tag the first cell
HEADER = "tag"  # the first cell of the header row, which is no tag


def tags_file(project_dir: Path) -> Path:
    return Path(project_dir) / "vault" / "wiki" / "tags.md"


def rows_of(text: str) -> set[str]:
    """The tags of the rows of the text of `tags.md`."""
    known = {m.group(1) for m in map(TAG_ROW.match, text.splitlines()) if m}
    return {tag for tag in known if tag != HEADER and tag.strip("-")}  # no header, no rule row


def registered_tags(path: Path) -> set[str] | None:
    """The tags of the rows of `tags.md` at `path`; None when the file does not stand, so no
    tag is judged (cases 703.1, 703.2)."""
    path = Path(path)
    if not path.is_file():
        return None
    return rows_of(path.read_text(encoding="utf-8"))


def declared_tags(block: dict | None) -> set[str]:
    """The tags of the `new_tags` of a `then` block — the entries the tag lines of a Case make
    (case 702)."""
    found: set[str] = set()
    for item in (block or {}).get("new_tags") or []:
        tag = str(item.get("tag") or "").strip() if isinstance(item, dict) else ""
        if tag:
            found.add(tag)
    return found


def ratified_tags(store: dict | None, records: list[dict]) -> set[str]:
    """The tags that the tag lines of the Cases of `store` declare, for each entry under its
    number alone whose top-level Case has a decision line among `records` — a Case ratified in
    the session. Each entry is read by `ratified.case_section`, the one reading of the Spec
    hook; imported here, since those modules import the checks that import this one."""
    from guppi.casecheck import AGENT_KEY, top_case
    from guppi.materialize import split_cases, then_blocks
    from guppi.ratified import case_section, headings

    tops = {
        top_case(str(r.get("case", "")))
        for r in records
        if isinstance(r, dict) and r.get("record") == "decision"
    }
    found: set[str] = set()
    for key, entry in (store or {}).items():
        key = str(key)
        if AGENT_KEY in key or top_case(key) not in tops or not isinstance(entry, dict):
            continue
        text = entry.get("text")
        if not isinstance(text, str):
            continue
        chat = split_cases(text).get(key)
        if chat is None:
            continue
        section, _ = case_section(key, headings(text).get(key, ""), chat, {})
        if section:
            found |= declared_tags(then_blocks(section)[0])
    return found
