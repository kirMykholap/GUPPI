"""`guppi ledger` — the `Stop` hook that lifts ratified lines out of the finished reply.

Every line of the reply that starts with `- decision[`, `- estimate[` or `- lesson[` at
column zero and is not inside a fenced block goes verbatim into
`vault/raw/<date>/ledger.md`. A fenced line is a preview (a Case shows its lines in `then`
before they are ratified); a bare line is a record. Rule page:
`vault/wiki/rules/rule-ledger-write.md`.

The hook first asks the event log whether this is a working session: a `hi` line must
follow the last `session-start` of this session's id, with no other session's start in
between. Without it, and with lines to write, the hook exits 2 and says why on stderr, so
the person is told rather than left believing the lines were recorded. On the re-fire after
a block (`stop_hook_active`) it exits 0 and writes nothing, so it cannot loop. A line already
in today's ledger, verbatim, is not appended twice.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import log_path, project_root, read_payload, session_stamp

PREFIXES = ("- decision[", "- estimate[", "- lesson[")
FENCE = re.compile(r"^ {0,3}(```|~~~)")


def reply_text(payload: dict) -> str:
    """The finished reply: `last_assistant_message` (measured 2026-09-09, Slice 1 probe)."""
    return str(payload.get("last_assistant_message") or "")


def ledger_lines(text: str) -> list[str]:
    """The record lines of a reply, in order: prefixed at column zero, outside any fence."""
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None and line.startswith(PREFIXES):
            lines.append(line.rstrip())
    return lines


def hi_recorded(event_log: str, stamp: str) -> bool:
    """True when a `hi` follows the last `session-start` of this session, with no other
    session's start in between. The `hi` line carries no session id (`/hi` cannot see
    one), which is why the window is tied to the starts around it."""
    ours = False
    seen_hi = False
    for line in event_log.splitlines():
        parts = line.split(" ", 3)
        if len(parts) < 4 or parts[0] != "-":
            continue
        session, event = parts[2], parts[3].split(" ", 1)[0]
        if event == "session-start":
            ours = session == stamp
            seen_hi = False
        elif event == "hi" and ours:
            seen_hi = True
    return seen_hi


def ledger_path(project_dir: Path, now) -> Path:
    return log_path(project_dir, now).with_name("ledger.md")


def existing_lines(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()}


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
        seen = existing_lines(path)
        fresh = []
        for line in lines:
            if line not in seen:
                fresh.append(line)
                seen.add(line)
        if fresh:
            append(path, fresh)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"ledger: ledger.md not written: {exc}", file=stderr)
    return 0
