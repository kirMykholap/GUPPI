"""`guppi ledger` — the `Stop` hook that lifts ratified lines out of the finished reply.

Every line of the reply that starts with `- decision[`, `- estimate[` or `- lesson[` inside
a fenced block opened with the `LEDGER` tag goes into `vault/raw/<hi date>/<hi HHMM>/ledger.md`
— the session's folder, the same across midnight (case 103.1) — its text verbatim,
prefixed with the time of writing. A line anywhere else — bare, or in a
block with another tag or none — is a preview (a Case shows its lines in `then` before they
are ratified); only a LEDGER block is a record. Rule page:
`vault/wiki/rules/rule-ledger-write.md`.

The hook first asks the event log whether this is a working session: a `hi` line of
this session's id must follow its first `session-start` (case 111.3); a start of another
session changes nothing, an unstamped `hi` does not count. The log it reads is `raw/<date>/event_log.md` of every date from today back to the
first that holds a `session-start` of this session, joined in date order, so a session that
crosses midnight keeps its window (case 55.1). Without a `hi`, and with lines to write, the
hook exits 2 and says why on stderr, so the person is told rather than left believing the
lines were recorded. An error of the hook itself after it has read the payload — an
exception while it reads the transcript, the event log or the ledger, or judges or appends
the lines — exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent
sees it at the end of that reply; a line not yet appended waits for the next `Stop`. An error
while it reads the payload exits 0 with the error on stderr, since the hook cannot tell its
own refusal then (cases 552.4, 577.4).

The hook writes and judges the lines whether `stop_hook_active` is set or not (case 577.3):
Claude Code keeps the flag set from the first refusal of any `Stop` hook until the person's
next message, so a run that a hook sends on — Plan Mode into Work Mode and Retro — would
otherwise write nothing until the person writes. It guards its own loop by its refusals in
the stretch, read by `own_refusals`: the stderr line of a refused line is printed, with exit
2, only when it does not already stand in a refusal of the hook since the person's last
message, so each faulty line is told once and a repeat of it stays silent; no `hi` and an
error of its own exit 2 only when no refusal of the hook stands in the stretch. With the flag
set and a transcript it cannot read, it writes the lines of the reply and exits 0. A refusal
of a hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and
holds a line opening with `[<command>]: `.

The person's message is judged once, by `user_kind` (case 592): a `user` record whose
`origin.kind` is `human` is the person's message, one whose `origin.kind` is
`task-notification` a returned answer of a subagent, any other record neither. The stretch
starts after the last person's message, and a returned answer does not end it; the turn of
the reply that `guppi/casecheck.py` reads starts after the last record of either kind, and
`guppi/context.py` counts from the start of the turn. Both import `user_kind`; `guppi onward`
reaches it through `own_refusals`; no other module judges `origin.kind`. A transcript with
neither kind is read whole as the stretch and as the turn.

The hook runs on `Stop`, not on `MessageDisplay`, which can neither block nor speak
(measured 2026-08-29). The ledger is not created at session start; it comes into being with
its first line. `compact` and `resume` of the same session do not close the window of the
event log — `SessionStart` fires on both, and neither changes the person, the branch or the
agenda (case 14) — and a `hi` with the id `--------` never counts (case 136.3). A block in a
text followed by a tool call reaches the ledger at the next `Stop` of the session, measured
on Claude Code 2.1.269–2.1.272 (case 224.1); `guppi gate` holds a skill call back while an
item of the Spec has no ledger line, so the reply that ends in text lands the block first
(cases 122, 169.1, 174). A hook-written line is told from a hand-written one by its time.

A line the grammar does not read is not written (case 552.2): `parse_line` of
`guppi/materialize.py` gives None for it, and `materialize` would put it under `unparsed`,
the record it holds lost. It is judged before the other refusals and gets no other; the hook
exits 2 with one stderr line per such line only when it stands in the reply just finished,
skips an older one without a word, and writes the other lines as before.

The lines come from every assistant message of the session in `transcript_path`, in order,
plus the reply that just finished (`last_assistant_message`), so a reply that ended in a
tool call — which has no `Stop` of its own — reaches the ledger at the next `Stop` of the
session (case 55.2). A subagent's message (`isSidechain`) is skipped: only the main agent
writes ledger lines. A line whose text is already in any `ledger.md` under `raw/`, at the
date level or in a session folder, whatever its time, is not appended twice.

What a session changes, it does not measure (case 428.1). An `estimate[<slug>]` line is not
written when a decision line `create` or `update` of `<slug>` stands in the session's ledger
or among the lines of the same `Stop`, each line read by `parse_line` of
`guppi/materialize.py`; a reading of the old slug of a page an `update` renames falls under
the same rule, since the decision line names the old slug. The judgment reads the ledger
alone and holds the whole session, so a refused line of the transcript is refused again at
every `Stop`: the hook exits 2 with one stderr line per refused line only when the line
stands in the reply just finished, and skips an older one without a word. The other lines
are written as before.

A lesson names its category (case 460.5). A fresh `lesson[<slug>]` line whose slug
`category_of` of `guppi/materialize.py` does not put under `lessons` — a slug that does not
open with `lesson-` — is not written, since `materialize` sends a lesson line to `lessons/`
by its record, not by its slug. As for a refused reading, the hook exits 2 with one stderr
line per refused line only when the line stands in the reply just finished, and skips an
older one without a word. A line already in a ledger is not fresh and is not judged again;
`estimate` and `decision` lines are not judged by their prefix.

A mark names a decision line before it (case 497.1). A fresh `lesson[...]` line whose
`{addressed_by:case N}` has no decision line of Case N before it — in the session's ledger,
or earlier among the lines of the same `Stop` — is not written, since `materialize` links a
lesson only to a decision line of that Case earlier in the unit, and a Case with sub-cases
has no line of its own. The judgment is `marks_without_decision` of `guppi/materialize.py`,
the one `materialize` makes, over the session's ledger followed by the fresh lines. The
prefix is judged first: a line refused for its prefix is not judged for its mark. The hook
exits 2 with one stderr line per refused line only when the line stands in the reply just
finished, naming the decision lines of the sub-cases of N that stand in the session, when
there are any. A refused line from an earlier text is judged again at every `Stop`, without
a word, and is written at the first `Stop` where a decision line of its Case stands in the
ledger before it.

No sprint, no decision (case 628.3). While no live page `vault/wiki/entities/entity-sprint-<id>.md`
stands — after the close of a sprint — a fresh decision line other than a `defer` is not
written until the session's ledger or the lines of the same `Stop` hold a `create` decision
line of an `entity-sprint-` slug, so the session after a close opens the next sprint first.
Readings and lessons pass. The hook exits 2 with one stderr line per refused line only when
it stands in the reply just finished, and the line is written at the first `Stop` after the
`create` stands. Judged by `refused_without_sprint`, over lines read by `parse_line`.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp

PREFIXES = ("- decision[", "- estimate[", "- lesson[")
TIMED = re.compile(r"^- (?:\d\d:\d\d:\d\d )?(.*)$")
BRACKET = re.compile(r"\[([^\]]*)\]")
LEDGER_TAG = "ledger"
PLAN_TOOLS = ("Write", "Edit", "MultiEdit")
REFUSAL_HEAD = "Stop hook feedback:"
COMMAND = "uv run guppi ledger"


def reply_text(payload: dict) -> str:
    """The finished reply: `last_assistant_message` (measured 2026-09-09, Slice 1 probe)."""
    return str(payload.get("last_assistant_message") or "")


def is_main(record) -> bool:
    """A record of the main agent's conversation: a JSON object, not a subagent's
    (`isSidechain`). The one judgment of the ledger and of `guppi context` (case 392.1)."""
    return isinstance(record, dict) and not record.get("isSidechain")


def read_records(path) -> list[dict] | None:
    """Every JSON object of the JSONL file at `path`, in order; a line that is not JSON is
    skipped. None when the path is absent or unreadable. The one reading of a transcript, the
    main agent's and a subagent's alike (case 434). The transcript is JSONL: one object per
    API block, `type: assistant`, `message.content` a list of blocks (measured 2026-09-11,
    session H)."""
    if not path:
        return None
    try:
        raw = Path(str(path)).read_text(encoding="utf-8")
    except (OSError, ValueError):
        return None
    records: list[dict] = []
    for line in raw.splitlines():
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if isinstance(record, dict):
            records.append(record)
    return records


def record_text(record: dict) -> str:
    """The text of a record's message: a string, or its text blocks joined by newlines."""
    content = (record.get("message") or {}).get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(
            str(b.get("text") or "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return ""


HUMAN = "human"  # the `origin.kind` of the person's message
NOTIFICATION = "task-notification"  # the `origin.kind` of a record that brings an answer back
PERSON, ANSWER = "person", "answer"


def user_kind(record: dict) -> str | None:
    """The kind of a `user` record of the transcript, by its `origin.kind` (case 592): the
    person's message (`PERSON`) when it is `human`, a returned answer of a subagent
    (`ANSWER`) when it is `task-notification`, and None for any other record — a record with
    no `origin`, such as the local command that clears the session, a `peer` message of
    another Claude session, a refusal marked `isMeta`, a tool result. The one judgment of the
    person's message: the turn of `guppi/casecheck.py` starts after either kind, the stretch
    of `own_refusals` after the person's message alone, and `guppi/context.py` counts from the
    start of the turn; no other module judges `origin.kind`."""
    if record.get("type") != "user":
        return None
    origin = record.get("origin")
    kind = origin.get("kind") if isinstance(origin, dict) else None
    return {HUMAN: PERSON, NOTIFICATION: ANSWER}.get(kind)


def opens_turn(record: dict) -> bool:
    """Whether a record opens a turn: the person's message or a returned answer (case 592)."""
    return user_kind(record) is not None


def stretch(payload: dict) -> list[dict] | None:
    """The stretch: the main-agent records of `transcript_path` after the last person's
    message, by `user_kind` — a `user` record whose `origin.kind` is `human`; a returned
    answer does not end it (case 592). None when the transcript cannot be read. The one
    judgment of the stretch, which the ledger hook and `guppi onward` call (cases 577.1,
    577.3, 597.2): Claude Code keeps `stop_hook_active` set from a refusal until the
    person's next message, so a hook guards its own loop by the transcript, not by the flag."""
    records = read_records(payload.get("transcript_path"))
    if records is None:
        return None
    main = [r for r in records if is_main(r)]
    start = 0
    for index, record in enumerate(main):
        if user_kind(record) == PERSON:
            start = index + 1
    return main[start:]


def refusals(payload: dict, *commands: str) -> dict[str, list[tuple[int, str]]] | None:
    """For each `Stop` hook `command`, its refusals in the stretch, in order, each with the
    reply of the agent it follows: the index in the stretch of the last `assistant` record
    before it, -1 when none — the refusals of one end of a reply share it, and a refusal of a
    later reply has a greater one (case 596.1). A refusal is a `user` record marked `isMeta`
    whose text opens with `Stop hook feedback:` and holds a line that opens with
    `[<command>]: `; its text is what follows that prefix (measured on session 1237 and 1441,
    Claude Code 2.1.282). None when the transcript cannot be read. The one judgment of the
    refusals, which `guppi onward` uses for its own and for those of the ledger hook."""
    records = stretch(payload)
    if records is None:
        return None
    found: dict[str, list[tuple[int, str]]] = {command: [] for command in commands}
    reply = -1
    for index, record in enumerate(records):
        if record.get("type") == "assistant":
            reply = index
            continue
        if record.get("type") != "user" or not record.get("isMeta"):
            continue
        text = record_text(record)
        if not text.startswith(REFUSAL_HEAD):
            continue
        for command in commands:
            prefix = f"[{command}]: "
            at = text.find("\n" + prefix)
            if at >= 0:
                found[command].append((reply, text[at + 1 + len(prefix) :]))
    return found


def own_refusals(payload: dict, command: str) -> list[str] | None:
    """The text of each refusal of the `Stop` hook `command` in the stretch, by `refusals`;
    None when the transcript cannot be read (cases 577.1, 577.3)."""
    found = refusals(payload, command)
    return None if found is None else [text for _, text in found[command]]


def transcript_records(payload: dict) -> list[dict]:
    """The main-agent records of `transcript_path`, in order. Empty when the path is absent
    or unreadable."""
    return [r for r in read_records(payload.get("transcript_path")) or [] if is_main(r)]


def transcript_texts(payload: dict) -> list[str]:
    """The text of every main-agent assistant message in `transcript_path`, in order."""
    texts: list[str] = []
    for record in transcript_records(payload):
        if record.get("type") != "assistant":
            continue
        content = (record.get("message") or {}).get("content")
        if isinstance(content, str):
            texts.append(content)
        elif isinstance(content, list):
            parts = [
                b.get("text") for b in content if isinstance(b, dict) and b.get("type") == "text"
            ]
            if parts:
                texts.append("\n".join(str(t) for t in parts if t))
    return texts


def session_lines(payload: dict) -> list[str]:
    """Every record line of the session: the transcript's messages first, the finished reply
    last, each line once, in first-seen order."""
    seen: set[str] = set()
    lines: list[str] = []
    for text in [*transcript_texts(payload), reply_text(payload)]:
        for line in ledger_lines(text):
            if body(line) not in seen:
                seen.add(body(line))
                lines.append(line)
    return lines


def ledger_lines(text: str) -> list[str]:
    """The record lines of a reply, in order: prefixed, inside a fence tagged LEDGER. The
    fence is judged by `fence_opening` and `closes_fence` of `guppi/materialize.py`, the one
    judgment (case 444.1); imported here, since `materialize` imports this module."""
    from guppi.materialize import closes_fence, fence_opening

    lines: list[str] = []
    opening: tuple[str, int, str] | None = None
    for line in text.splitlines():
        if opening is None:
            opening = fence_opening(line)
            continue
        if closes_fence(line, opening):
            opening = None
            continue
        if opening[2] == LEDGER_TAG and line.startswith(PREFIXES):
            lines.append(line.rstrip())
    return lines


def body(line: str) -> str:
    """A ledger line without its `- ` and its time, if any: what makes two lines the same."""
    match = TIMED.match(line.rstrip())
    return match.group(1) if match else line.rstrip()


def timed(line: str, now) -> str:
    """The line as written into the ledger: the time of writing between the dash and the text."""
    return f"- {now.strftime('%H:%M:%S')} {body(line)}"


def hi_recorded(event_log: str, stamp: str) -> bool:
    """True when a `hi` line of this session's stamp follows its first `session-start`
    (case 111.3). The `hi` is written by the `UserPromptSubmit` hook with the session id,
    so a start of another session — before, between, after — changes nothing, and a `hi`
    of another stamp does not count. A further start of the same session — `compact`,
    `resume` — does not close the window either (case 14). A `--------` `hi` never counts
    (case 136.3)."""
    return hi_moment([("", event_log)], stamp) is not None


def ledger_path(project_dir: Path, now, stamp: str) -> Path | None:
    """`raw/<hi date>/<hi HHMM>/ledger.md`, the session's ledger (case 103.1); None without
    a `hi`, which `hi_recorded` has already refused by then."""
    folder = session_dir(project_dir, now, stamp)
    return None if folder is None else folder / "ledger.md"


def session_event_logs(project_dir: Path, now, stamp: str) -> list[tuple[str, str]]:
    """`(date, text)` of the event log of every date from today back to the first holding a
    `session-start` of this session, in date order (case 55.1). With no such date, every
    log up to today is returned and the window check fails on its own."""
    raw = project_dir / "vault" / "raw"
    today = now.date().isoformat()
    marker = f" {stamp} session-start"
    chosen: list[tuple[str, str]] = []
    if raw.is_dir():
        dates = sorted(
            (d.name for d in raw.iterdir() if d.name <= today and d.is_dir()), reverse=True
        )
        for name in dates:
            log = raw / name / "event_log.md"
            if not log.exists():
                continue
            text = log.read_text(encoding="utf-8")
            chosen.append((name, text))
            if marker in text:
                break
    return list(reversed(chosen))


def hi_moment(logs: list[tuple[str, str]], stamp: str) -> tuple[str, str] | None:
    """`(date, time)` of the `hi` that opens this session's window: the first `hi` of this
    stamp after its first `session-start`, over the `(date, text)` logs of
    `session_event_logs` in date order; lines of other sessions are skipped (case 111.3).
    A stamped `hi` is the one opener: the fallback of case 111.6 — a `--------` `hi` bound
    by position, for the sessions opened before the hook — was removed once those sessions
    had closed (case 136.3)."""
    ours = False
    for day, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 3)
            if len(parts) < 4 or parts[0] != "-" or parts[2] != stamp:
                continue
            time, event = parts[1], parts[3].split(" ", 1)[0]
            if event == "session-start":
                ours = True
            elif event == "hi" and ours:
                return (day, time)
    return None


def session_dir(project_dir: Path, now, stamp: str) -> Path | None:
    """The session's folder `vault/raw/<hi date>/<hi HHMM>/` (case 73): the date and the
    time of the `hi` line that opens this session's window, over the event logs the ledger
    hook walks; None without a `hi`. Lives here rather than in `event.py` because this
    module imports `event.py` and the walk is the ledger's."""
    hi = hi_moment(session_event_logs(project_dir, now, stamp), stamp)
    if hi is None:
        return None
    day, time = hi
    return project_dir / "vault" / "raw" / day / (time[:2] + time[3:5])


def is_plan_file(path: Path) -> bool:
    """A plan file: a `.md` file under `.claude/plans/` — the one judgment of `plan_path` and
    of the guard `guppi ratified --guard` (case 445.1)."""
    return (
        path.suffix == ".md"
        and path.parent.name == "plans"
        and path.parent.parent.name == ".claude"
    )


def plan_path(logs: list[tuple[str, str]], stamp: str) -> Path | None:
    """The plan file of the session: the path of the last `tool Write:` / `tool Edit:` /
    `tool MultiEdit:` line of this session's stamp that names a plan file by `is_plan_file`
    (cases 122, 445.1). None when no such line exists; a path the log truncated does not
    exist and is skipped by the caller. Lives here beside the window it reads, so that
    `gate`, `recall` and `ratified` import one reading (case 387.2)."""
    last = None
    for _, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 4)
            if len(parts) < 5 or parts[0] != "-" or parts[2] != stamp or parts[3] != "tool":
                continue
            tool, sep, path = parts[4].partition(": ")
            if not sep or tool not in PLAN_TOOLS:
                continue
            candidate = Path(path.strip())
            if is_plan_file(candidate):
                last = candidate
    return last


def session_event_log(project_dir: Path, now, stamp: str) -> str:
    """The logs of `session_event_logs`, joined."""
    return "".join(text for _, text in session_event_logs(project_dir, now, stamp))


def existing_bodies(project_dir: Path) -> set[str]:
    """The bodies of every line in every `ledger.md` under `raw/`, at any depth."""
    raw = project_dir / "vault" / "raw"
    bodies: set[str] = set()
    if raw.is_dir():
        for path in raw.rglob("ledger.md"):
            bodies |= {body(line) for line in path.read_text(encoding="utf-8").splitlines()}
    return bodies


def changed_by_session(lines: list[str]) -> dict[str, str]:
    """Each slug a decision line `create` or `update` of these lines names, with its Case
    (case 428.1). The lines are read by `parse_line` of `guppi/materialize.py`, the one
    parse of a ledger line; imported here, since `materialize` imports this module."""
    from guppi.materialize import parse_line

    changed: dict[str, str] = {}
    for line in lines:
        record = parse_line(f"- {body(line)}")
        if record and record["record"] == "decision" and record["kind"] in ("create", "update"):
            changed.setdefault(record["slug"], record["case"])
    return changed


def unreadable(lines: list[str]) -> list[str]:
    """Each line that `parse_line` of `guppi/materialize.py` cannot read: `materialize` would
    put it under `unparsed`, and the record it holds would be lost (case 552.2)."""
    from guppi.materialize import parse_line

    return [line for line in lines if parse_line(f"- {body(line)}") is None]


def refused_readings(lines: list[str], changed: dict[str, str]) -> list[tuple[str, str]]:
    """`(line, case)` of each `estimate[<slug>]` line whose slug a decision line of the
    session creates or updates: what a session changes, it does not measure (case 428.1)."""
    from guppi.materialize import parse_line

    refused: list[tuple[str, str]] = []
    for line in lines:
        record = parse_line(f"- {body(line)}")
        if record and record["record"] == "estimate" and record["slug"] in changed:
            refused.append((line, changed[record["slug"]]))
    return refused


def refused_lessons(lines: list[str]) -> list[tuple[str, str]]:
    """`(line, slug)` of each `lesson[...]` line whose slug `category_of` of
    `guppi/materialize.py` does not put under `lessons`: a lesson slug starts with `lesson-`
    (case 460.5). The lines are read by `parse_line`, the one parse of a ledger line, and
    judged by `category_of`, the one table of prefixes; imported here, since `materialize`
    imports this module."""
    from guppi.materialize import category_of, parse_line

    refused: list[tuple[str, str]] = []
    for line in lines:
        record = parse_line(f"- {body(line)}")
        if record and record["record"] == "lesson" and category_of(record["slug"]) != "lessons":
            refused.append((line, record["slug"]))
    return refused


def refused_marks(
    fresh: list[str], written: list[str], skip: set[str]
) -> list[tuple[str, str, str, list[str]]]:
    """`(line, slug, case, sub-cases)` of each fresh `lesson[...]` line whose
    `{addressed_by:case N}` has no decision line of Case N before it, over the session's
    ledger `written` followed by `fresh` (case 497.1); a line in `skip`, refused for its
    prefix, is not judged. The sub-cases are the Cases `N.<m>` whose decision lines stand in
    the session, in the order first seen. Judged by `marks_without_decision` of
    `guppi/materialize.py`, the one judgment of the mark; imported here, since `materialize`
    imports this module."""
    from guppi.materialize import marks_without_decision, parse_line

    ordered = written + fresh
    records = [parse_line(f"- {body(line)}") for line in ordered]
    cases = [r["case"] for r in records if r and r["record"] == "decision"]
    refused: list[tuple[str, str, str, list[str]]] = []
    for index in marks_without_decision([f"- {body(line)}" for line in ordered]):
        if index < len(written) or ordered[index] in skip:
            continue
        record = records[index]
        mark = record["addressed_by"]
        subs = list(dict.fromkeys(c for c in cases if c.startswith(f"{mark}.")))
        refused.append((ordered[index], record["slug"], mark, subs))
    return refused


SPRINT_PREFIX = "entity-sprint-"


def refused_without_sprint(project_dir: Path, fresh: list[str], written: list[str]) -> list[str]:
    """Each fresh decision line but a `defer` while no live sprint page stands, until the
    session's ledger or the lines of the same `Stop` hold a `create` decision line of an
    `entity-sprint-` slug: the session after the close of a sprint opens the next sprint
    first (case 628.3). Readings and lessons pass. The lines are read by `parse_line` of
    `guppi/materialize.py`, the one parse of a ledger line."""
    from guppi.materialize import parse_line

    entities = project_dir / "vault" / "wiki" / "entities"
    if entities.is_dir() and any(entities.glob(f"{SPRINT_PREFIX}*.md")):
        return []
    records = [(line, parse_line(f"- {body(line)}")) for line in written + fresh]
    decisions = [(line, r) for line, r in records if r and r["record"] == "decision"]
    if any(r["kind"] == "create" and r["slug"].startswith(SPRINT_PREFIX) for _, r in decisions):
        return []
    return [line for line, r in decisions if line in fresh and r["kind"] != "defer"]


def append(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for line in lines:
            handle.write(line + "\n")


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
    except Exception as exc:  # noqa: BLE001 — no payload, no way to tell its own refusal (552.4, 577.4)
        print(f"ledger: ledger.md not written: {exc}", file=stderr)
        return 0
    told: list[str] | None = None
    try:
        told = own_refusals(payload, COMMAND)
        seen = existing_bodies(project_dir)
        fresh = [timed(line, now) for line in session_lines(payload) if body(line) not in seen]
        if not fresh:
            return 0
        stamp = session_stamp(None, payload)
        if not hi_recorded(session_event_log(project_dir, now, stamp), stamp):
            if silenced(told, payload):
                return 0
            print(
                f"ledger: {len(fresh)} line(s) not written — no /hi recorded for session "
                f"{stamp}. Tell the person; run /hi, then repeat the lines.",
                file=stderr,
            )
            return 2
        path = ledger_path(project_dir, now, stamp)
        if path is None:
            raise RuntimeError("no session folder for the hi")
        written = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
        broken = unreadable(fresh)  # case 552.2: judged first, no other refusal
        fresh = [line for line in fresh if line not in broken]
        refused = refused_readings(fresh, changed_by_session(written + fresh))
        lessons = refused_lessons(fresh)
        marks = refused_marks(fresh, written, {line for line, _ in lessons})  # case 497.1
        unopened = refused_without_sprint(project_dir, fresh, written)  # case 628.3
        out = (
            {line for line, _ in refused}
            | {line for line, _ in lessons}
            | {line for line, _, _, _ in marks}
            | set(unopened)
        )
        fresh = [line for line in fresh if line not in out]
        if fresh:
            append(path, fresh)
        finished = {body(line) for line in ledger_lines(reply_text(payload))}
        messages = [
            "ledger: line not written — the grammar of a ledger line does not read it: "
            f"{body(line)}. Write it again in the form of the table in ratification.md."
            for line in broken
            if body(line) in finished
        ]
        for line, case in refused:
            if body(line) in finished:
                slug = BRACKET.search(line).group(1)
                messages.append(
                    f"ledger: estimate[{slug}] not written — case {case} creates or updates "
                    f"{slug} in this session; what a session changes it does not measure: take "
                    "the reading in a later session and name it in the handoff."
                )
        for line, slug in lessons:
            if body(line) in finished:
                messages.append(
                    f"ledger: lesson[{slug}] not written — a lesson slug starts with lesson-, "
                    "then the area, then the cause: write the line again with the prefix."
                )
        for line, slug, case, subs in marks:
            if body(line) in finished:
                named = (
                    "; its sub-cases have " + ", ".join(f"case {s}" for s in subs) if subs else ""
                )
                messages.append(
                    f"ledger: lesson[{slug}] not written — {{addressed_by:case {case}}} names "
                    f"no decision line before it in this session{named}: write the line again "
                    "after the decision line of the Case that closed the cause, naming that Case."
                )
        for line in unopened:
            if body(line) in finished:
                messages.append(
                    f"ledger: line not written — no sprint is open: {body(line)}. Open the next "
                    "sprint first: ratify the Case that creates entity-sprint-<id>, then repeat "
                    "the line; a defer, a reading and a lesson pass."
                )
        loud = untold(messages, told, payload)  # case 577.3: each refused line once a stretch
        for message in loud:
            print(message, file=stderr)
        if loud:
            return 2
    except Exception as exc:  # noqa: BLE001 — shown to the agent, not swallowed (case 552.4)
        if silenced(told, payload):
            return 0
        print(f"ledger: ledger.md not written: {exc}", file=stderr)
        return 2
    return 0


def silenced(told: list[str] | None, payload: dict) -> bool:
    """Whether a refusal that stands once a stretch — no `hi`, an error of the hook — is
    silent: a refusal of the hook already stands in the stretch, or `stop_hook_active` is set
    and the transcript cannot be read, so the hook cannot tell (cases 577.3, 577.4)."""
    if told is None:
        return bool(payload.get("stop_hook_active"))
    return bool(told)


def untold(messages: list[str], told: list[str] | None, payload: dict) -> list[str]:
    """The stderr lines of the refused lines not yet told in the stretch: a line that already
    stands in a refusal of the hook stays silent, so a repeat of a faulty line cannot loop;
    with `stop_hook_active` set and a transcript that cannot be read, none (case 577.3)."""
    if told is None:
        return [] if payload.get("stop_hook_active") else messages
    said = "\n".join(told)
    return [message for message in messages if message not in said]
