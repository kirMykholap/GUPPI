"""`guppi ledger` — the `Stop` hook that lifts ratified lines out of the finished reply.

Every line of the reply that starts with `- decision[`, `- estimate[` or `- lesson[` inside
a fenced block opened with the `LEDGER` tag goes into `vault/raw/<date>/ledger.md`, its
text verbatim, prefixed with the time of writing. A line anywhere else — bare, or in a
block with another tag or none — is a preview (a Case shows its lines in `then` before they
are ratified); only a LEDGER block is a record. Rule page:
`vault/wiki/rules/rule-ledger-write.md`.

The hook first asks the event log whether this is a working session: a `hi` line must
follow the last `session-start` of this session's id, with no other session's start in
between. Without it, and with lines to write, the hook exits 2 and says why on stderr, so
the person is told rather than left believing the lines were recorded. On the re-fire after
a block (`stop_hook_active`) it exits 0 and writes nothing, so it cannot loop. A line whose
text is already in today's ledger, whatever its time, is not appended twice.
"""

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


def existing_bodies(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {body(line) for line in path.read_text(encoding="utf-8").splitlines()}


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
        lines = ledger_lines(reply_text(payload))
        if not lines:
            return 0
        stamp = session_stamp(None, payload)
        log = log_path(project_dir, now)
        event_log = log.read_text(encoding="utf-8") if log.exists() else ""
        if not hi_recorded(event_log, stamp):
            print(
                f"ledger: {len(lines)} line(s) not written — no /hi recorded for session "
                f"{stamp}. Tell the person; run /hi, then repeat the lines.",
                file=stderr,
            )
            return 2
        path = ledger_path(project_dir, now)
        seen = existing_bodies(path)
        fresh = []
        for line in lines:
            if body(line) not in seen:
                fresh.append(timed(line, now))
                seen.add(body(line))
        if fresh:
            append(path, fresh)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"ledger: ledger.md not written: {exc}", file=stderr)
    return 0
