"""`guppi caseid --next [--session <id>]` — the one grammar of a Case id, and the next id.

A Case id of a sprint opened after sprint ids came in is the sprint id, a hyphen and the
number of the Case in that sprint, from 1, with a dot for each sub-case level:
`kir-plugin-12.1` (case 788). A sprint id holds lower-case letters, digits and hyphens and no
dot, so the number is the last run of digits after the last hyphen ahead of the first dot. An
id with no sprint part, such as `785.1`, is a Case from before sprint ids, and the sprints of
`PLAIN_SPRINTS`, opened before sprint ids came in, keep that form to their close (case 788.2). Every reader of a Case id — the
ledger's `parse_line` and `_case_of` of `guppi/materialize.py`, `top_case`, `case_file`,
`case_number` and `new_number` of `guppi/casecheck.py`, `held_number` of
`guppi/ratified.py`, `ORIGIN_CASE` and `DEFERRED_LINE` of `guppi/lint.py`, `case_key` of
`guppi/gate.py` and the History links of `guppi/box.py` — reads it by `ID` or `parse` here,
and `tests/test_caseid.py` runs each over both forms.

`next_id` is the one count of the next free id (case 788.4): one above the highest number of
the sprint among the ids it is given — the Decision pages live and archived, the decision
lines of the session's ledger, the keys of the store `<plan>.checked.json` and the files under
the session's `cases/` — or above the highest plain number for a sprint of `PLAIN_SPRINTS`.
`new_number` of `guppi/casecheck.py` calls it for a Case built again, and the command calls
it for a new Case.

The command takes the open sprint from the `create` decision line of a sprint page in the
session's `ledger.md` (`opened_sprint` of `guppi/materialize.py`), else from the first heading
of `vault/wiki/sprint.md` (`sprint_id`), prints the next id, and holds it in the store under
that id with no `agent_id` and no text, so that the next run prints the id after it. With no
session folder or no plan file it prints the id and holds nothing.

Rule page: `vault/wiki/rules/rule-ratification.md`.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import NamedTuple

SPRINT = r"[a-z0-9]+(?:-[a-z0-9]+)*"
ID = rf"(?:{SPRINT}-)?\d+(?:\.\d+)*"  # a Case id in either form, for a larger pattern
WHOLE = re.compile(rf"^(?:({SPRINT})-)?(\d+)((?:\.\d+)*)$")
TOP_ID = rf"(?:{SPRINT}-)?\d+"  # the id of a top-level Case
CASE_FILE = re.compile(rf"^case-({TOP_ID})\.md$")  # the name `case_file` gives
DECISION_PAGE = re.compile(rf"^decision-case-({ID})\.md$")
# the sprints opened before sprint ids came in, whose Cases keep a plain id to their close
# (case 788)
PLAIN_SPRINTS = ("migration", "plugin")


class CaseId(NamedTuple):
    sprint: str | None
    number: int
    levels: tuple[int, ...]


def parse(case) -> CaseId | None:
    """The sprint, the number and the sub-case levels of a Case id; None for any other text."""
    match = WHOLE.match(str(case).strip())
    if match is None:
        return None
    sprint, number, rest = match.groups()
    levels = tuple(int(p) for p in rest.split(".")[1:]) if rest else ()
    return CaseId(sprint, int(number), levels)


def top(case) -> str:
    """The id of the top-level Case: `452` of `452.1`, `kir-plugin-12` of `kir-plugin-12.1`.
    A sprint id holds no dot, so the first dot opens the sub-case levels."""
    return str(case).split(".", 1)[0]


def sort_key(case) -> tuple:
    """`12.3` after `9` and before `12.10`; the ids of a sprint together, the plain ids first."""
    parsed = parse(case)
    if parsed is None:
        return ("", 0)
    return (parsed.sprint or "", parsed.number, *parsed.levels)


def is_plain(sprint: str | None) -> bool:
    """Whether the Cases of `sprint` take a plain id: no sprint, or one of `PLAIN_SPRINTS`."""
    return sprint is None or sprint in PLAIN_SPRINTS


def next_id(sprint: str | None, ids) -> str:
    """One above the highest number of `sprint` among `ids` — of the plain ids when the
    sprint keeps them (case 788.4)."""
    plain = is_plain(sprint)
    numbers = [
        parsed.number
        for case in ids
        if (parsed := parse(top(case))) is not None
        and (parsed.sprint is None if plain else parsed.sprint == sprint)
    ]
    number = max(numbers, default=0) + 1
    return str(number) if plain else f"{sprint}-{number}"


def page_ids(project_dir: Path) -> list[str]:
    """The ids of the Decision pages, under `vault/wiki/decisions/` and in a folder
    `decisions/` under `vault/archive/`."""
    vault = project_dir / "vault"
    paths = list((vault / "wiki" / "decisions").glob("decision-case-*.md"))
    archive = vault / "archive"
    if archive.is_dir():
        paths += [p for p in archive.rglob("decision-case-*.md") if p.parent.name == "decisions"]
    return [m.group(1) for p in paths if (m := DECISION_PAGE.match(p.name))]


def file_ids(folder: Path | None) -> list[str]:
    """The ids of the Case files under the session folder's `cases/`."""
    if folder is None or not (folder / "cases").is_dir():
        return []
    return [m.group(1) for p in (folder / "cases").iterdir() if (m := CASE_FILE.match(p.name))]


def known_ids(project_dir: Path, folder: Path | None, records: list[dict], store: dict) -> list:
    """Every id the next id must stand above: the Decision pages, the decision lines of the
    session's ledger `records`, the keys of the store and the Case files (case 788.4)."""
    from guppi.casecheck import key_case  # it imports this module

    ids = [str(r["case"]) for r in records if r.get("record") == "decision"]
    ids += [key_case(key) for key in store]
    return ids + page_ids(project_dir) + file_ids(folder)


def open_sprint(project_dir: Path, folder: Path | None) -> str:
    """The sprint of a new Case: the sprint the session's ledger opens, else the first heading
    of `vault/wiki/sprint.md`."""
    from guppi.materialize import opened_sprint, sprint_id

    if folder is not None and (folder / "ledger.md").is_file():
        lines = (folder / "ledger.md").read_text(encoding="utf-8").splitlines()
        opened = opened_sprint(lines)
        if opened:
            return opened
    return sprint_id(project_dir)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi caseid", description=__doc__.splitlines()[0])
    p.add_argument("--next", action="store_true", required=True, help="print the next id")
    p.add_argument("--session", default=None, help="the stamp of the hi: line")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    from guppi.casecheck import held_store, ledger_of, ledger_records, write_store
    from guppi.event import project_root, session_stamp
    from guppi.ledger import plan_path, session_dir, session_event_logs

    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    args = parser().parse_args(argv)
    stamp = session_stamp(args.session, {})
    folder = session_dir(project_dir, now, stamp)
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    store = held_store(plan) if plan is not None and plan.is_file() else {}
    records = ledger_records(ledger_of(folder))
    case = next_id(open_sprint(project_dir, folder), known_ids(project_dir, folder, records, store))
    if plan is not None and plan.is_file():
        store[case] = {"stored": now.isoformat()}  # held: no agent_id, no text (case 788.2)
        write_store(plan, store)
    else:
        print("caseid: no plan file of the session — the id is not held", file=stderr)
    print(case, file=stdout)
    return 0
