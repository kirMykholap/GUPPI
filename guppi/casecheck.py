"""`guppi casecheck --subagent` — the `SubagentStop` hook that checks the Case `case-guppi`
answers with before the main agent sees it (case 419.3); `guppi casecheck` — the `Stop` hook
that compares each Case the main agent shows with the one the check stored (case 419.4).

The check. For an answer of `case-guppi` (`agent_type`), the hook reads the Cases of
`last_assistant_message` in the chat form, builds the section of each in the Spec in memory
by `ratified.case_section` — the one reading of the Spec hook — and runs `prespec.judge` over
them, the decision lines of each `ratification` fence standing for the ledger; the Frontier,
the ratified copy and the grammar of the window stay with `/pre-spec`. It checks besides the
chat form: the sections in the order of the schema; the ones a Case needs — a parent's
`context` and `problem`, and `when`, `then`, `tasks` and `ratification` of a Case with no
sub-cases (`given` too, unless it is a sub-case); and a `ratification` of one untagged fence of
ledger lines and nothing else. A count in a story section is not checked: no script tells a
count from other words. Each Case of the answer is stored with its findings in
`<plan>.checked.json` beside the plan file of the session, a later answer for the same id
replacing it. A finding exits 2 with the findings on stderr, and Claude Code sends the agent
back (measured 2026-09-25, session 0051); on the re-fire (`stop_hook_active`) the findings are
stored and the hook exits 0. An answer with no Case heading is a question: nothing is checked
or stored. With no plan file of the session nothing is stored.

The comparison. On `Stop`, each Case the reply shows under its heading with at least one of
its sections is compared with the Case of the same id in the store — the heading and its
lines up to the horizontal rule that opens the agent's own text, line ends and trailing
spaces made the same. A parent shown with its sub-cases is compared part by part. A Case the
store does not hold, one that differs, or one stored with findings exits 2 with the reason on
stderr. A heading with no section — the acknowledging reply — a fence tagged `DIFF`, and a
deferred decision in the short form — `context`, `problem` and a fence tagged `then` with
`defer` items, no `given` and no `when` — are not compared. On the re-fire exit 0; outside a
working session — no `hi` — nothing is done.

The payload is read as UTF-8; the hook never raises. Rule page:
`vault/wiki/rules/rule-case-check.md`.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import plan_path, reply_text, session_dir, session_event_logs
from guppi.materialize import parse_line, split_cases, tagged_blocks
from guppi.prespec import FINDING_CASE, judge
from guppi.ratified import CHAT_SECTIONS, case_section, headings, quoted_sections

AGENT = "case-guppi"
STORE_SUFFIX = ".checked.json"
RULE = "---"  # the horizontal rule after which the agent's own text stands
LEDGER_LINE = ("- decision[", "- estimate[", "- lesson[")


def store_of(plan: Path) -> Path:
    return plan.with_name(plan.stem + STORE_SUFFIX)


def read_store(plan: Path | None) -> dict:
    if plan is None:
        return {}
    try:
        data = json.loads(store_of(plan).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def shown_text(heading: str, lines: list[str]) -> str:
    """The Case as compared: its heading and lines up to the horizontal rule, each line's
    trailing spaces and the blank lines at both ends removed."""
    kept: list[str] = []
    for line in lines:
        if line.strip() == RULE:
            break
        kept.append(line.rstrip())
    return "\n".join([heading.rstrip(), *kept]).strip("\n")


def is_short_form(lines: list[str]) -> bool:
    """A deferred decision in the short form: no `given`, no `when`, a `then` fence with
    `defer` items."""
    sections = quoted_sections(lines, CHAT_SECTIONS)
    if "given" in sections or "when" in sections:
        return False
    return any(block.lstrip().startswith("defer:") for block in tagged_blocks(lines, "then"))


def has_sub_cases(case: str, cases: dict) -> bool:
    return any(other.startswith(case + ".") for other in cases)


def form_findings(case: str, lines: list[str], cases: dict) -> list[str]:
    """The chat form of one Case: the order of its sections, the ones it needs, and what
    `ratification` holds."""
    sections = quoted_sections(lines, CHAT_SECTIONS)
    names = list(sections)
    findings: list[str] = []
    if names != sorted(names, key=CHAT_SECTIONS.index):
        findings.append(f"case {case}: sections out of the order of the schema: {', '.join(names)}")
    if has_sub_cases(case, cases):
        needed = ("context", "problem")
    elif "." in case:
        needed = ("when", "then", "tasks", "ratification")
    else:
        needed = ("given", "when", "then", "tasks", "ratification")
    missing = [name for name in needed if name not in sections]
    if missing:
        findings.append(f"case {case}: missing section {', '.join(missing)}")
    if "ratification" in sections:
        body = [line.strip() for line in sections["ratification"].splitlines() if line.strip()]
        if not (
            len(body) >= 3
            and body[0] == "```"
            and body[-1] == "```"
            and all(line.startswith(LEDGER_LINE) for line in body[1:-1])
        ):
            findings.append(
                f"case {case}: ratification holds one untagged fence of ledger lines and "
                "nothing else"
            )
    return findings


def ratification_records(cases: dict) -> list[dict]:
    """The decision records of every `ratification` fence of the answer."""
    records: list[dict] = []
    for lines in cases.values():
        text = quoted_sections(lines, ("ratification",)).get("ratification", "")
        for line in text.splitlines():
            record = parse_line(line.strip())
            if record and record.get("record") == "decision":
                records.append(record)
    return records


def check_answer(text: str, project_dir: Path) -> dict[str, list[str]]:
    """Case id → its findings, for every Case of an answer of `case-guppi`."""
    cases = split_cases(text)
    heads = headings(text)
    records = ratification_records(cases)
    refs = {
        (r["case"], r["slug"]): r["ref"]
        for r in records
        if r.get("kind") == "create" and r.get("ref")
    }
    found: dict[str, list[str]] = {case: [] for case in cases}
    spec: list[str] = ["# the answer of case-guppi", ""]
    for case, lines in cases.items():
        found[case] += form_findings(case, lines, cases)
        section, errors = case_section(case, heads[case], lines, refs)
        found[case] += [f"case {case}: {error}" for error in errors]
        spec += section or [heads[case], ""]
    for finding in judge("\n".join(spec) + "\n", project_dir, records):
        match = FINDING_CASE.match(finding)
        case = match.group(1) if match else ""
        found[case if case in found else next(iter(cases))].append(finding)
    return found


def subagent(payload: dict, project_dir: Path, now, stderr) -> int:
    if payload.get("agent_type") != AGENT:
        return 0
    text = str(payload.get("last_assistant_message") or "")
    cases = split_cases(text)
    if not cases:
        return 0
    found = check_answer(text, project_dir)
    stamp = session_stamp(None, payload)
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    if plan is not None and plan.is_file():
        store = read_store(plan)
        heads = headings(text)
        for case, lines in cases.items():
            store[case] = {"text": shown_text(heads[case], lines), "findings": found[case]}
        store_of(plan).write_text(
            json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8", newline=""
        )
    findings = [f for case in cases for f in found[case]]
    if findings and not payload.get("stop_hook_active"):
        print("casecheck: " + "; ".join(findings), file=stderr)
        return 2
    return 0


def stop(payload: dict, project_dir: Path, now, stderr) -> int:
    if payload.get("stop_hook_active"):
        return 0
    stamp = session_stamp(None, payload)
    if session_dir(project_dir, now, stamp) is None:
        return 0
    reply = reply_text(payload)
    cases = split_cases(reply)
    heads = headings(reply)
    shown = {
        case: lines
        for case, lines in cases.items()
        if quoted_sections(lines, CHAT_SECTIONS) and not is_short_form(lines)
    }
    if not shown:
        return 0
    store = read_store(plan_path(session_event_logs(project_dir, now, stamp), stamp))
    problems: list[str] = []
    for case, lines in shown.items():
        entry = store.get(case)
        if not isinstance(entry, dict):
            problems.append(f"case {case}: not built and checked by case-guppi — dispatch it")
        elif entry.get("findings"):
            problems.append(
                f"case {case}: its check found {'; '.join(entry['findings'])} — send them to "
                "case-guppi"
            )
        elif entry.get("text") != shown_text(heads[case], lines):
            problems.append(
                f"case {case}: differs from the answer of case-guppi — show that answer unchanged"
            )
    if problems:
        print("casecheck: " + "; ".join(problems), file=stderr)
        return 2
    return 0


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("casecheck: payload not readable, nothing checked", file=stderr)
            return 0
        if "--subagent" in argv:
            return subagent(payload, project_dir, now, stderr)
        return stop(payload, project_dir, now, stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"casecheck: not checked: {exc}", file=stderr)
        return 0
