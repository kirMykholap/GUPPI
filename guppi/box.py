"""`guppi box --check <folder> --session <id>` — whether a conserved Spec can run now, and
the judgment whether an approved plan names one.

A conserved Spec is a session folder `vault/raw/<date>/<HHMM>/` that `/carry` marked with
`carry.md` and gave the branch `spec/<date>-<HHMM>` (case 591.1). A later session takes it
whole at the Frontier and names its `spec.md` in the title line of its plan file (case
593.1); `conserved_spec_named` finds that folder in the approved plan, and the hook of
`rule-spec-capture` then leads the agent to `/box` in place of the fork (case 591.3).

`check` is the first step of `/box` (case 593.3). It prints one line per reason the Spec
cannot run now and exits 1 when it prints any; with no reason it prints nothing and exits 0:

- the folder is not marked — `is_carried_over` of `guppi/materialize.py`, the one judgment
  of the mark — or no branch `spec/<date>-<HHMM>` exists;
- the current branch is `main`: the shared branch is never `main`;
- the ledger window of the session, read the way `guppi prespec --check` reads it, holds a
  decision line other than a `defer`: a box session ratifies no Case of its own in this
  first part (case 591);
- a live page that an `update`, `delete` or `defer` item of the folder's `spec.md` names has
  a History line that names the Decision page of a later Case, read by `guppi/caseid.py`
  (`later_case`, case 788.5): a plain id whose whole number is higher than that of every Case
  of that Spec with a plain id, when the Spec holds one; an id of a sprint whose number is
  higher than that of every Case of that Spec of the same sprint; or an id of a sprint the
  Spec holds no Case of, on a History line dated on or after the date of the folder — a later
  decision changed the page after the Spec was conserved; the line names the page and that
  Decision page;
- a slug that a `create` item of that Spec names is carried by a live page.

The items are read by `split_cases` and `then_blocks` of `guppi/materialize.py`, the parser
`guppi materialize` uses. The check writes nothing, switches no branch and opens no page
beyond those the Spec names. Rule page: `vault/wiki/rules/rule-spec-box.md`.
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from guppi.caseid import ID as CASE_ID
from guppi.caseid import parse, top
from guppi.event import project_root, session_stamp
from guppi.materialize import category_of, is_carried_over, split_cases, then_blocks

SPEC_PATH = re.compile(r"vault/raw/(\d{4}-\d\d-\d\d)/(\d{4})/spec\.md")
DECISION_LINK = re.compile(rf"\[\[decision-case-({CASE_ID})")  # either form (case 788.5)
HISTORY_DATE = re.compile(r"^- (\d{4}-\d\d-\d\d)\b")
NAMED_KINDS = ("update", "delete", "defer")
SHARED_NEVER = "main"


def conserved_spec_named(plan: str, project_dir: Path) -> Path | None:
    """The folder `vault/raw/<date>/<HHMM>/` whose `spec.md` the title line of the plan names
    and that `is_carried_over` judges marked by `carry.md`; None for any other plan."""
    title = next((line for line in plan.splitlines() if line.startswith("# ")), "")
    match = SPEC_PATH.search(title.replace("\\", "/"))
    if match is None:
        return None
    unit = f"{match.group(1)}/{match.group(2)}"
    if not is_carried_over(project_dir, unit):
        return None
    return project_dir / "vault" / "raw" / match.group(1) / match.group(2)


def unit_of(folder: Path, project_dir: Path) -> str | None:
    """`<date>/<HHMM>` of a folder under `vault/raw/`, or None when it is not one."""
    path = folder if folder.is_absolute() else project_dir / folder
    try:
        parts = path.resolve().relative_to((project_dir / "vault" / "raw").resolve()).parts
    except ValueError:
        return None
    if len(parts) != 2 or not re.fullmatch(r"\d{4}-\d\d-\d\d", parts[0]):
        return None
    if not re.fullmatch(r"\d{4}", parts[1]):
        return None
    return f"{parts[0]}/{parts[1]}"


def git(project_dir: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=project_dir,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    return result.stdout if result.returncode == 0 else ""


def history_cases(page: Path) -> list[tuple[str, str]]:
    """`(date, id)` of each Decision page the `## History` of a page names, the id of its
    top-level Case read by `guppi/caseid.py` in either form, the date of its History line
    (case 788.5)."""
    text = page.read_text(encoding="utf-8")
    at = text.find("\n## History")
    if at < 0:
        return []
    found: list[tuple[str, str]] = []
    for line in text[at:].splitlines():
        date = HISTORY_DATE.match(line.strip())
        for case in DECISION_LINK.findall(line):
            found.append((date.group(1) if date else "", top(case)))
    return found


def later_case(case: str, date: str, spec_cases: list[str], folder_date: str) -> bool:
    """Whether the Decision page of top-level `case`, on a History line dated `date`, is of a
    Case later than the Spec of `spec_cases`, conserved on `folder_date` (case 788.5): a plain
    id whose number is higher than every plain id of the Spec, when it holds one; an id of a
    sprint whose number is higher than every id of that sprint in the Spec; an id of a sprint
    the Spec holds no Case of, on a line dated on or after the folder."""
    parsed = parse(case)
    if parsed is None:
        return False
    own = [p.number for c in spec_cases if (p := parse(c)) and p.sprint == parsed.sprint]
    if own:
        return parsed.number > max(own)
    if parsed.sprint is None:
        return False
    return bool(date) and date >= folder_date


def spec_items(spec: str) -> tuple[list[str], list[tuple[str, str]]]:
    """The ids of the top-level Cases of a Spec, and `(kind, slug)` of each decision item."""
    numbers: list[str] = []
    items: list[tuple[str, str]] = []
    for case, lines in split_cases(spec).items():
        head = top(case)
        if parse(head) is not None and head not in numbers:
            numbers.append(head)
        block, _ = then_blocks(lines)
        for kind in ("create", *NAMED_KINDS):
            for item in block.get(kind) or []:
                if isinstance(item, dict) and item.get("slug"):
                    items.append((kind, str(item["slug"])))
    return numbers, items


def own_decisions(project_dir: Path, now, session: str) -> list[str]:
    """The Cases of the decision lines other than a `defer` in the session's ledger window,
    read the way `guppi prespec --check` reads them."""
    from guppi.ledger import hi_moment, session_event_logs
    from guppi.prespec import session_decisions, window_lines

    hi = hi_moment(session_event_logs(project_dir, now, session), session)
    if hi is None:
        return []
    lines = window_lines(project_dir, hi, now.date().isoformat())
    cases: list[str] = []
    for record in session_decisions(lines):
        if record.get("kind") != "defer" and record.get("case") not in cases:
            cases.append(str(record.get("case")))
    return cases


def check(project_dir: Path, folder: Path, session: str, now=None) -> list[str]:
    """Each reason the conserved Spec of `folder` cannot run now, one line per reason."""
    now = datetime.now().astimezone() if now is None else now
    unit = unit_of(folder, project_dir)
    if unit is None:
        return [f"box: {folder} is no session folder vault/raw/<date>/<HHMM>/"]
    reasons: list[str] = []
    date, hhmm = unit.split("/")
    branch = f"spec/{date}-{hhmm}"
    if not is_carried_over(project_dir, unit):
        reasons.append(f"box: vault/raw/{unit}/ holds no carry.md — no conserved Spec")
    if not git(project_dir, "branch", "--list", branch).strip():
        reasons.append(f"box: no branch {branch}")
    if git(project_dir, "branch", "--show-current").strip() == SHARED_NEVER:
        reasons.append(f"box: the current branch is {SHARED_NEVER} — the shared branch never is")
    for case in own_decisions(project_dir, now, session):
        reasons.append(
            f"box: case {case} of this session holds a decision line — "
            "a box session ratifies no Case of its own"
        )
    spec = project_dir / "vault" / "raw" / unit / "spec.md"
    if not spec.is_file():
        reasons.append(f"box: vault/raw/{unit}/spec.md is missing")
        return reasons
    numbers, items = spec_items(spec.read_text(encoding="utf-8"))
    wiki = project_dir / "vault" / "wiki"
    seen: set[tuple[str, str]] = set()
    for kind, slug in items:
        if (kind, slug) in seen:
            continue
        seen.add((kind, slug))
        category = category_of(slug)
        page = wiki / category / f"{slug}.md" if category else None
        if kind == "create":
            if page is not None and page.is_file():
                reasons.append(f"box: {slug} — the Spec creates it, and a live page carries it")
            continue
        if page is None or not page.is_file():
            continue
        later = dict.fromkeys(
            case for day, case in history_cases(page) if later_case(case, day, numbers, date)
        )
        for number in later:
            reasons.append(
                f"box: {slug} — changed after the Spec was conserved, by decision-case-{number}"
            )
    return reasons


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi box", description=__doc__.splitlines()[0])
    p.add_argument("--check", metavar="FOLDER", required=True, help="the conserved Spec")
    p.add_argument("--session", required=True, help="the stamp of the hi: line")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    args = parser().parse_args(argv)
    reasons = check(project_dir, Path(args.check), session_stamp(args.session, {}), now)
    for line in reasons:
        print(line, file=stdout)
    return 1 if reasons else 0
