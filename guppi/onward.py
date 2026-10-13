"""`guppi onward` — the `Stop` hook that sends the agent from the end of Retro to `/handoff`.

In Claude Code the end of a reply hands the turn to the person, and the ledger hook writes
the lines of a reply only when it ends; so Retro ends one reply with its `LEDGER` block, and
this hook sends the agent on in the same turn (case 531.9). It exits 2 when four things hold:
the event log of the session's window holds the mark `retro` of this session after its
`hi` — the mark `guppi gate` leaves at a call of `/retro` it lets through —,
`raw/<hi date>/<hi HHMM>/handoff.md` does not stand, its own refusal is not spent — `spent`:
its last refusal stands in the stretch, the transcript after the person's last message, and
no refusal of the ledger hook follows the same reply or a later one, by `ledger.refusals` —,
and the reply that ended does not open with `STOP:`. Its reason on stderr tells the agent to commit
the session folder and call `/handoff`, or, when a condition of
`vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person.

In every other case with no error of its own it exits 0 and prints nothing: without a `hi` of the session, before the
mark, once `handoff.md` stands, once its own refusal is spent, on a reply that
opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript. A
refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and
neither does the flag, which Claude Code keeps set from a refusal until the person's next
message (case 577.1). After a reply the ledger hook refused, it sends the agent on again at
the end of the reply that writes the refused lines again (case 596.1); the ledger hook tells
each refused line once a stretch, so it cannot loop. It counts nothing, reads no test result,
calls no model and writes nothing: its judgment is the mark, the file, the refusals in the
transcript and the first word of the reply. The session window, the stamp and
the folder are those of `guppi/ledger.py`. An error of its own after it has read the payload —
while it reads the reply, the session folder, the event log or the transcript — exits 2 with
the error on stderr and the advice to commit the session folder and call `/handoff` if Retro
has ended and `handoff.md` does not stand, before Retro too, at most once a stretch, judged by
its own refusal in the stretch alone, `told`, whatever the ledger hook refused after it; an
error while it reads the payload exits 0 (cases 555.3, 577.2, 596.3). Rule page:
`vault/wiki/rules/rule-retro-onward.md`.

`guppi onward --plan` — the `Stop` hook that sends the agent on in Plan Mode where no
person is needed after `/pre-spec`: in the loop after its findings, and from the
ratification of the Cases built again on them to the exit (cases 561.5, 696.2). Before
`/pre-spec` it stays silent, so the person speaks before `/pre-spec` runs (case 697). A reply
that carries a `LEDGER` block ends in that text, so the agent cannot go on in it. It exits 2
when all of these hold: the event log of the session's window holds a `hi` of this session
and, after it, a `prespec` line of this session, by `prespec.prespec_mark` — the one reading
of the line, through which `prespec.window` finds it too; `raw/<hi date>/<hi HHMM>/spec.md`
does not stand; `frontier.md` holds no open line under `## Cases`, by
`prespec.open_case_items`, the one judgment the check of `/pre-spec` reports; the reply
carries a `LEDGER` block, by `ledger.ledger_lines`, or the ledger hook refused the reply that
ended just before it, by `ledger.sent_back_last`, so the answer with no block to its reminder
is sent on too (case 696.2); no file under `cases/` was written after the last decision line
of its Case, or of a sub-case, in `ledger.md`, in any reply of the main agent in the
transcript at the moment of its record (`transcript_replies`) (cases 597.2, 604) or in that
block — a Case built again and not yet ratified is still out, while one ratified again with
lines the ledger already held counts as ratified for the rest of the session, after a later
message of the person too, and a Case that a `{supersedes:case N}` mark of those lines
retires, whole or sub-case by sub-case, is never out, judged by
`prespec.superseded_in_window` and `prespec.retired_whole`, no judgment of a mark written
here (case 696.1), nor is a file that holds nothing but blank space, the file of a dropped
Case, judged by `casecheck.dropped`, the one judgment of an empty Case file (case 701.1); its own refusal, `uv run guppi onward --plan`, is not spent, as above
(case 597.1), the flag counting only when the transcript cannot be read; and the reply does
not open with `STOP:`. When a file under `cases/` that holds more than blank space was
written after the last `prespec` line, its time read on the date of the event log that
holds it (`built_after`) (cases 686.1, 701.2),
it tells the agent that the Cases built again on the findings are ratified, to run
`uv run guppi prespec --check` on the plan file and call `ExitPlanMode` when it prints no
finding; when no such file was written after that line — a defer or a lesson in answer to
the report of `/pre-spec`, before any Case is built again, or only the emptied file of a
dropped Case — it sends the agent on with the loop
after the findings: to send each finding in a Case to its `case-guppi`, or, when no Case
goes back, to run the check and exit. After a reply the ledger hook sent back — a line it
refused or held, or its reminder of a lesson with no mark (cases 685.1, 688.7) — `spent`
lets it fire again at the next reply. Each reason adds that, when only the person can go
on, the agent opens its reply with `STOP:` and asks the person. The time of a line of
`ledger.md` is read on the `hi` date and rolls to the next date when it runs backwards, so a
session across midnight keeps its order; a decision line of the reply counts as written now.
It counts nothing, calls no model and writes nothing. An error of its own after it has read
the payload exits 2 with `onward: not checked: <error>` and the advice to go on with the
loop after the findings or to run the check and exit, never to call `/pre-spec`, at most
once a stretch, judged by its own refusal alone (case 597.1) — and only after `/pre-spec`:
before it, or when the `prespec` line cannot be read, it exits 0 (case 696.2). Rule page:
`vault/wiki/rules/rule-prespec-onward.md`.
"""

import re
import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import COMMAND as LEDGER
from guppi.ledger import (
    ledger_lines,
    own_refusals,
    record_text,
    refusals,
    reply_text,
    sent_back_last,
    session_dir,
    session_event_logs,
    silenced,
    transcript_records,
)

TIME_HEAD = re.compile(r"^- \d\d:\d\d:\d\d ")

MARK = "retro"
STOP = "STOP:"
PLAN_FLAG = "--plan"
COMMAND = "uv run guppi onward"
PLAN_COMMAND = f"{COMMAND} {PLAN_FLAG}"
REASON = (
    "onward: Retro has ended and handoff.md does not stand. Commit the session folder and "
    "call /handoff now. If a condition of vault/wiki/where-to-stop.md holds, open your reply "
    "with STOP: and ask the person instead."
)
ONLY_THE_PERSON = (
    " If only the person can go on — a Case still out with its case-guppi, or a question the "
    "person must answer — open your reply with STOP: and ask the person instead."
)
TO_EXIT = (
    "onward: the Cases built again on the findings of /pre-spec are ratified. Run uv run "
    "guppi prespec --check on the plan file with --session <id>, fix what it prints, and "
    "call ExitPlanMode when it prints no finding." + ONLY_THE_PERSON
)
TO_LOOP = (
    "onward: no Case has been built again on the findings of /pre-spec yet. Go on with the "
    "loop after its findings: send each finding in a Case to its case-guppi; when no Case "
    "goes back, run uv run guppi prespec --check on the plan file with --session <id>, fix "
    "what it prints, and call ExitPlanMode when it prints no finding." + ONLY_THE_PERSON
)
CASE_FILE = "case-"


def retro_mark(logs: list[tuple[str, str]], stamp: str) -> tuple[str, str] | None:
    """`(date, time)` of the first mark `retro` of this stamp that follows the first `hi` of
    this stamp that follows its first `session-start`, over the `(date, text)` logs in date
    order — the window `ledger.hi_moment` opens; None when no such mark stands."""
    started = opened = False
    for day, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 3)
            if len(parts) < 4 or parts[0] != "-" or parts[2] != stamp:
                continue
            event = parts[3].split(" ", 1)[0]
            if event == "session-start":
                started = True
            elif event == "hi" and started:
                opened = True
            elif event == MARK and opened:
                return day, parts[1]
    return None


def retro_marked(logs: list[tuple[str, str]], stamp: str) -> bool:
    """True when the mark `retro` of this stamp stands in the window, by `retro_mark`."""
    return retro_mark(logs, stamp) is not None


def retro_moment(logs: list[tuple[str, str]], stamp: str) -> datetime | None:
    """The moment of the mark of `retro_mark`, its time read on the date of its log in the
    local zone; None when no mark stands or its time cannot be read."""
    mark = retro_mark(logs, stamp)
    if mark is None:
        return None
    try:
        day, clock = date.fromisoformat(mark[0]), time.fromisoformat(mark[1])
        return datetime.combine(day, clock).astimezone()
    except ValueError:
        return None


def case_root(case: str) -> str:
    """The top-level Case of an id: `561` of `561.9`."""
    return case.split(".", 1)[0]


def transcript_replies(payload: dict) -> list[tuple[float, list[str]]]:
    """The record lines of each main-agent reply of the transcript, by
    `ledger.transcript_records` — the reading the ledger hook makes — and
    `ledger.ledger_lines`, each with the moment of its record, read by `moment` of
    `guppi/casecheck.py`. A reply before the person's last message counts like one after it,
    so a re-ratification with lines the ledger already held counts for the rest of the
    session (cases 597.2, 604). A record whose time cannot be read counts none of its lines,
    and a transcript that cannot be read gives none."""
    from guppi.casecheck import moment

    replies: list[tuple[float, list[str]]] = []
    for record in transcript_records(payload):
        if record.get("type") != "assistant":
            continue
        lines = ledger_lines(record_text(record))
        when = moment(record.get("timestamp"))
        if lines and when is not None:
            replies.append((when.timestamp(), lines))
    return replies


def last_decisions(
    ledger: str, hi_date: str, reply: list[str], now, replies=()
) -> dict[str, float]:
    """Top-level Case → the moment, as a timestamp, of its last decision line, its sub-cases
    included: the timed lines of `ledger.md` read on the `hi` date, rolled to the next date
    when the time runs backwards, the decision lines of each reply of the transcript at the
    moment of its record (cases 597.2, 604), and the decision lines of the reply as written
    now."""
    from guppi.materialize import parse_line

    moments: dict[str, float] = {}
    for at, lines in replies:
        for line in lines:
            record = parse_line(line)
            if record and record["record"] == "decision":
                root = case_root(str(record["case"]))
                moments[root] = max(moments.get(root, at), at)
    day, previous = date.fromisoformat(hi_date), None
    for line in ledger.splitlines():
        if not TIME_HEAD.match(line):
            continue
        clock = time.fromisoformat(line[2:10])
        if previous is not None and clock < previous:
            day += timedelta(days=1)
        previous = clock
        record = parse_line(line)
        if record and record["record"] == "decision":
            moment = datetime.combine(day, clock, tzinfo=now.tzinfo).timestamp()
            root = case_root(str(record["case"]))
            moments[root] = max(moments.get(root, moment), moment)
    for line in reply:
        record = parse_line(line)
        if record and record["record"] == "decision":
            moments[case_root(str(record["case"]))] = now.timestamp()
    return moments


def session_decisions(ledger: str, reply: list[str], replies=()) -> list[dict]:
    """The decision records, by `parse_line`, of the timed lines of `ledger.md`, of each reply
    of the transcript and of the reply that ended — the lines `last_decisions` reads."""
    from guppi.materialize import parse_line

    lines = [line for line in ledger.splitlines() if TIME_HEAD.match(line)]
    lines += [line for _, block in replies for line in block] + list(reply)
    return [r for r in map(parse_line, lines) if r and r["record"] == "decision"]


def case_out(folder: Path, reply: list[str], now, payload: dict | None = None) -> bool:
    """Whether a file under `cases/` was written after the last decision line of its Case or
    of a sub-case, in `ledger.md`, in a reply of the transcript or in the reply that ended — a
    Case built and not yet ratified (cases 561.5, 597.2, 604). A Case that a
    `{supersedes:case N}` mark of those lines retires, whole or sub-case by sub-case, is never
    out, by `superseded_in_window` and `retired_whole` of `guppi/prespec.py`; no judgment of a
    mark is written here (case 696.1). A file that holds nothing but blank space, the file of
    a dropped Case, is never out, by `dropped` of `guppi/casecheck.py` (case 701.1)."""
    from guppi.casecheck import dropped
    from guppi.prespec import retired_whole, superseded_in_window

    cases = folder / "cases"
    if not cases.is_dir():
        return False
    ledger = folder / "ledger.md"
    text = ledger.read_text(encoding="utf-8") if ledger.exists() else ""
    replies = transcript_replies(payload) if payload else []
    moments = last_decisions(text, folder.parent.name, reply, now, replies)
    records = session_decisions(text, reply, replies)
    superseded = superseded_in_window(records)
    for path in cases.glob(f"{CASE_FILE}*.md"):
        case = path.stem.removeprefix(CASE_FILE)
        if dropped(path) or retired_whole(case, superseded, records):
            continue
        if case not in moments or path.stat().st_mtime > moments[case]:
            return True
    return False


def plan_onward(payload: dict, project_dir: Path, now) -> str | None:
    """The reason `--plan` refuses the end of a reply with, or None (case 561.5)."""
    from guppi.prespec import open_case_items, prespec_mark

    reply = reply_text(payload)
    if reply.lstrip().startswith(STOP):
        return None
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    if folder is None or (folder / "spec.md").exists():
        return None
    frontier = folder / "frontier.md"
    if not frontier.exists() or open_case_items(frontier.read_text(encoding="utf-8")):
        return None
    mark = prespec_mark(session_event_logs(project_dir, now, stamp), stamp)
    if mark is None:  # before /pre-spec the person speaks first (case 697)
        return None
    lines = ledger_lines(reply)
    if not lines and not sent_back_last(payload, LEDGER):
        return None
    if case_out(folder, lines, now, payload):
        return None
    return TO_EXIT if built_after(folder, mark, now) else TO_LOOP


def after_prespec(payload: dict, project_dir: Path, now) -> bool:
    """Whether `prespec.prespec_mark` reads a `prespec` line of this session after its `hi`;
    False when it cannot be read, so an error of the hook before `/pre-spec` sends no reply
    back (case 696.2)."""
    from guppi.prespec import prespec_mark

    try:
        stamp = session_stamp(None, payload)
        return prespec_mark(session_event_logs(project_dir, now, stamp), stamp) is not None
    except Exception:  # noqa: BLE001 — a line it cannot read counts as none
        return False


def built_after(folder: Path, mark: tuple[str, str], now) -> bool:
    """Whether a file under `cases/` was written after the `prespec` line at `mark`, its time
    read on the date of its log in the zone of `now`, as `last_decisions` reads the times of
    `ledger.md` (case 686.1): a Case built again on the findings. A mark whose time cannot be
    read counts as none built, and so does a file that holds nothing but blank space, the
    file of a dropped Case, by `dropped` of `guppi/casecheck.py` (case 701.2)."""
    from guppi.casecheck import dropped

    cases = folder / "cases"
    try:
        day, clock = date.fromisoformat(mark[0]), time.fromisoformat(mark[1])
    except ValueError:
        return False
    moment = datetime.combine(day, clock, tzinfo=now.tzinfo).timestamp()
    return cases.is_dir() and any(
        path.stat().st_mtime > moment and not dropped(path)
        for path in cases.glob(f"{CASE_FILE}*.md")
    )


def told(payload: dict, command: str = COMMAND) -> bool:
    """Whether the error path of the hook `command` stays silent for its loop: its own
    refusal stands in the stretch, whatever the ledger hook refused after it, or
    `stop_hook_active` is set and the transcript cannot be read — the judgment `silenced` of
    `guppi/ledger.py`, the one the ledger hook makes (cases 577.1, 596.3). An error while
    reading counts as a transcript it cannot read."""
    try:
        own = own_refusals(payload, command)
    except Exception:  # noqa: BLE001 — judged as a transcript it cannot read
        own = None
    return silenced(own, payload)


def spent(payload: dict, command: str = COMMAND) -> bool:
    """Whether the hook `command` stays silent for its loop: its last refusal stands in the
    stretch and no refusal of the ledger hook follows the same reply of the agent or a later
    one, by `ledger.refusals` — so after a reply the ledger hook refused, it sends the agent
    on again at the end of the reply that writes the refused lines again. The ledger hook
    tells each refused line once a stretch, so this cannot loop. A refusal of another hook and
    `stop_hook_active` count for nothing, but with the flag set and a transcript it cannot
    read it is silent (cases 596.1, 597.1). An error while reading counts as a transcript it
    cannot read."""
    try:
        found = refusals(payload, command, LEDGER)
    except Exception:  # noqa: BLE001 — judged as a transcript it cannot read
        found = None
    if found is None:
        return bool(payload.get("stop_hook_active"))
    if not found[command]:
        return False
    last = found[command][-1][0]
    return not any(reply >= last for reply, _ in found[LEDGER])


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
    except Exception as exc:  # noqa: BLE001 — no payload, no way to tell its own refusal (cases 555.3, 577.2)
        print(f"onward: not checked: {exc}", file=stderr)
        return 0
    if not payload:
        return 0
    if PLAN_FLAG in (argv or []):
        try:
            reason = plan_onward(payload, project_dir, now)
            if reason is not None and spent(payload, PLAN_COMMAND):
                return 0
        except Exception as exc:  # noqa: BLE001 — shown to the agent after /pre-spec
            if not after_prespec(payload, project_dir, now) or told(payload, PLAN_COMMAND):
                return 0
            print(
                f"onward: not checked: {exc}. If no Case is left out, go on with the loop "
                "after the findings, or run the check and exit Plan Mode.",
                file=stderr,
            )
            return 2
        if reason is None:
            return 0
        print(reason, file=stderr)
        return 2
    try:
        if reply_text(payload).lstrip().startswith(STOP):
            return 0
        stamp = session_stamp(None, payload)
        folder = session_dir(project_dir, now, stamp)
        if folder is None or (folder / "handoff.md").exists():
            return 0
        if not retro_marked(session_event_logs(project_dir, now, stamp), stamp):
            return 0
        if spent(payload):
            return 0
        print(REASON, file=stderr)
        return 2
    except Exception as exc:  # noqa: BLE001 — shown to the agent, not swallowed (case 555.3)
        if told(payload):
            return 0
        print(
            f"onward: not checked: {exc}. If Retro has ended and handoff.md does not stand, "
            "commit the session folder and call /handoff.",
            file=stderr,
        )
        return 2
