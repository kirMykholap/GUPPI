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
lines were recorded. On the re-fire after a block (`stop_hook_active`) it exits 0 and writes
nothing, so it cannot loop.

The lines come from every assistant message of the session in `transcript_path`, in order,
plus the reply that just finished (`last_assistant_message`), so a reply that ended in a
tool call — which has no `Stop` of its own — reaches the ledger at the next `Stop` of the
session (case 55.2). A subagent's message (`isSidechain`) is skipped: only the main agent
writes ledger lines. A line whose text is already in any `ledger.md` under `raw/`, at the
date level or in a session folder, whatever its time, is not appended twice.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp

PREFIXES = ("- decision[", "- estimate[", "- lesson[")
FENCE = re.compile(r"^ {0,3}(```|~~~)\s*(\S*)")
TIMED = re.compile(r"^- (?:\d\d:\d\d:\d\d )?(.*)$")
LEDGER_TAG = "ledger"


def reply_text(payload: dict) -> str:
    """The finished reply: `last_assistant_message` (measured 2026-09-09, Slice 1 probe)."""
    return str(payload.get("last_assistant_message") or "")


def transcript_texts(payload: dict) -> list[str]:
    """The text of every main-agent assistant message in `transcript_path`, in order. Empty
    when the path is absent or unreadable; a line that is not JSON is skipped. The transcript
    is JSONL: one object per API block, `type: assistant`, `message.content` a list of blocks
    (measured 2026-09-11, session H)."""
    path = payload.get("transcript_path")
    if not path:
        return []
    try:
        raw = Path(str(path)).read_text(encoding="utf-8")
    except (OSError, ValueError):
        return []
    texts: list[str] = []
    for line in raw.splitlines():
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if not isinstance(record, dict) or record.get("type") != "assistant":
            continue
        if record.get("isSidechain"):
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
    """The record lines of a reply, in order: prefixed, inside a fence tagged LEDGER."""
    lines: list[str] = []
    fence: str | None = None
    recording = False
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker, tag = match.groups()
            if fence is None:
                fence = marker
                recording = tag.lower() == LEDGER_TAG
            elif marker == fence:
                fence = None
                recording = False
            continue
        if recording and line.startswith(PREFIXES):
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
    `resume` — does not close the window either (case 14). With no stamped `hi` at all, a
    `--------` `hi` counts by the rule before 111.3 (case 111.6)."""
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
    With no stamped `hi` at all, the rule before 111.3 applies to the `--------` lines the
    old skill line wrote: a `hi` after a `session-start` of this session with no other
    session's start in between (case 111.6, the sessions opened before the hook)."""
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
    return unstamped_hi_moment(logs, stamp)


def unstamped_hi_moment(logs: list[tuple[str, str]], stamp: str) -> tuple[str, str] | None:
    """The rule before case 111.3, kept as the fallback of case 111.6: the first `--------`
    `hi` after a `session-start` of this session with no other session's start in between;
    a foreign start closes the window, a further start of our own does not (case 14)."""
    from guppi.event import UNKNOWN_SESSION

    ours = False
    for day, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 3)
            if len(parts) < 4 or parts[0] != "-":
                continue
            time, session, event = parts[1], parts[2], parts[3].split(" ", 1)[0]
            if event == "session-start":
                ours = session == stamp
            elif event == "hi" and ours and session == UNKNOWN_SESSION:
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
        if payload.get("stop_hook_active"):
            return 0
        seen = existing_bodies(project_dir)
        fresh = [timed(line, now) for line in session_lines(payload) if body(line) not in seen]
        if not fresh:
            return 0
        stamp = session_stamp(None, payload)
        if not hi_recorded(session_event_log(project_dir, now, stamp), stamp):
            print(
                f"ledger: {len(fresh)} line(s) not written — no /hi recorded for session "
                f"{stamp}. Tell the person; run /hi, then repeat the lines.",
                file=stderr,
            )
            return 2
        path = ledger_path(project_dir, now, stamp)
        if path is None:
            raise RuntimeError("no session folder for the hi")
        append(path, fresh)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"ledger: ledger.md not written: {exc}", file=stderr)
    return 0
