"""`guppi pretask` — the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-task` has run in this session.

Reads the event log the way the ledger hook does: the session is a working one when a
`hi` follows its last `session-start`. In a working session with no `pretask` line after
that `hi`, the hook exits 2 with the reason on stderr, which Claude Code shows the agent
and which blocks the tool; the agent runs `/pre-task` (whose skill records the line) and
exits Plan Mode again. An ordinary session — no `hi` — is not gated: no governance applies
there. Any other tool: exit 0. Rule page: `vault/wiki/rules/rule-pretask-hook.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import log_path, project_root, read_payload, session_stamp

TOOL = "ExitPlanMode"


def window(event_log: str, stamp: str) -> tuple[bool, bool]:
    """`(hi, pretask)`: whether this session's window holds a `hi`, and a `pretask` after it."""
    ours = seen_hi = seen_pretask = False
    for line in event_log.splitlines():
        parts = line.split(" ", 3)
        if len(parts) < 4 or parts[0] != "-":
            continue
        session, event = parts[2], parts[3].split(" ", 1)[0]
        if event == "session-start" and session != stamp:
            ours = seen_hi = seen_pretask = False
        elif event == "session-start":
            ours = True
        elif event == "hi" and ours:
            seen_hi = True
        elif event == "pretask" and seen_hi:
            seen_pretask = True
    return seen_hi, seen_pretask


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if payload.get("tool_name") != TOOL:
            return 0
        stamp = session_stamp(None, payload)
        log = log_path(project_dir, now)
        event_log = log.read_text(encoding="utf-8") if log.exists() else ""
        hi, done = window(event_log, stamp)
        if hi and not done:
            print(
                f"pretask: Plan Mode is closing without /pre-task in session {stamp}. "
                "Run /pre-task, then exit Plan Mode again.",
                file=stderr,
            )
            return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"pretask: check skipped: {exc}", file=stderr)
    return 0
