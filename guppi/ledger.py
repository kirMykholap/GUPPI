"""`guppi ledger` — the `Stop` hook that lifts ratified lines out of the finished reply.

Every line of the reply that starts with `- decision[`, `- estimate[` or `- lesson[` inside
a fenced block opened with the `LEDGER` tag goes into `vault/raw/<date>/ledger.md`, its
text verbatim, prefixed with the time of writing. A line anywhere else — bare, or in a
block with another tag or none — is a preview (a Case shows its lines in `then` before they
are ratified); only a LEDGER block is a record. Rule page:
`vault/wiki/rules/rule-ledger-write.md`.

The hook first asks the event log whether this is a working session: a `hi` line must
follow the last `session-start` of this session's id, with no other session's start in
between. The log it reads is `raw/<date>/event_log.md` of every date from today back to the
first that holds a `session-start` of this session, joined in date order, so a session that
crosses midnight keeps its window (case 55.1). Without a `hi`, and with lines to write, the
hook exits 2 and says why on stderr, so the person is told rather than left believing the
lines were recorded. On the re-fire after a block (`stop_hook_active`) it exits 0 and writes
nothing, so it cannot loop.

The lines come from every assistant message of the session in `transcript_path`, in order,
plus the reply that just finished (`last_assistant_message`), so a reply that ended in a
tool call — which has no `Stop` of its own — reaches the ledger at the next `Stop` of the
session (case 55.2). A subagent's message (`isSidechain`) is skipped: only the main agent
writes ledger lines. A line whose text is already in any `raw/<date>/ledger.md`, whatever
its time, is not appended twice.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import log_path, project_root, read_payload, session_stamp

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
    """True when a `hi` follows a `session-start` of this session, with no other session's
    start in between. The `hi` line carries no session id (`/hi` cannot see one), which is
    why the window is tied to the starts around it. A further start of the same session —
    `compact`, `resume` — does not close the window (case 14): the person, branch and
    agenda are unchanged, and the `hi` already happened."""
    ours = False
    seen_hi = False
    for line in event_log.splitlines():
        parts = line.split(" ", 3)
        if len(parts) < 4 or parts[0] != "-":
            continue
        session, event = parts[2], parts[3].split(" ", 1)[0]
        if event == "session-start" and session != stamp:
            ours = False
            seen_hi = False
        elif event == "session-start":
            ours = True
        elif event == "hi" and ours:
            seen_hi = True
    return seen_hi


def ledger_path(project_dir: Path, now) -> Path:
    return log_path(project_dir, now).with_name("ledger.md")


def session_event_log(project_dir: Path, now, stamp: str) -> str:
    """The event logs of every date from today back to the first holding a `session-start`
    of this session, joined in date order (case 55.1). With no such date, every log up to
    today is joined and the window check fails on its own."""
    raw = project_dir / "vault" / "raw"
    today = now.date().isoformat()
    marker = f" {stamp} session-start"
    chosen: list[str] = []
    if raw.is_dir():
        dates = sorted(
            (d.name for d in raw.iterdir() if d.name <= today and d.is_dir()), reverse=True
        )
        for name in dates:
            log = raw / name / "event_log.md"
            if not log.exists():
                continue
            text = log.read_text(encoding="utf-8")
            chosen.append(text)
            if marker in text:
                break
    return "".join(reversed(chosen))


def existing_bodies(project_dir: Path) -> set[str]:
    """The bodies of every line in every `raw/<date>/ledger.md`."""
    raw = project_dir / "vault" / "raw"
    bodies: set[str] = set()
    if raw.is_dir():
        for path in raw.glob("*/ledger.md"):
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
        append(ledger_path(project_dir, now), fresh)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"ledger: ledger.md not written: {exc}", file=stderr)
    return 0
