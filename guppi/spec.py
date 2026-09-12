"""`guppi spec` — the `PostToolUse ExitPlanMode` hook that copies the approved plan into
the session's folder, `vault/raw/<hi date>/<hi HHMM>/spec.md`.

The plan arrives whole in `tool_response.plan` (measured 2026-09-09, Slice 1 probe). It is
appended after a `---` separator when the file already has content, under a stamp line
with the time and the session; a plan whose text is already in the file is not appended
again. Any other tool, or a payload without a plan: nothing. The folder is named by the
`hi` line that opens this session's window — its date, then its time as `HHMM` — found
the way the ledger hook finds it, across the event logs of the window (case 73.2); the
folder is created when missing. Without a `hi` recorded for this session the hook exits 2
with the reason, so the person is told rather than left believing the Spec was copied.
Rule page: `vault/wiki/rules/rule-spec-capture.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import session_dir

TOOL = "ExitPlanMode"


def plan_text(payload: dict) -> str:
    if payload.get("tool_name") != TOOL:
        return ""
    response = payload.get("tool_response")
    if not isinstance(response, dict):
        return ""
    return str(response.get("plan") or "")


def spec_path(project_dir: Path, now, session: str) -> Path | None:
    """`<session folder>/spec.md`, or None when no `hi` opens this session's window."""
    folder = session_dir(project_dir, now, session)
    return None if folder is None else folder / "spec.md"


def stamp(now, session: str) -> str:
    return f"<!-- approved {now.strftime('%H:%M:%S')} · session {session} -->"


def append_plan(path: Path, plan: str, now, session: str) -> bool:
    """True when the plan was written; False when the file already holds its text."""
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    body = plan.strip("\n")
    if body in current:
        return False
    parts = []
    if current:
        parts.append("\n---\n\n" if current.endswith("\n") else "\n\n---\n\n")
    parts += [stamp(now, session), "\n\n", body, "\n"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("".join(parts))
    return True


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        plan = plan_text(payload)
        if not plan.strip():
            return 0
        session = session_stamp(None, payload)
        path = spec_path(project_dir, now, session)
        if path is None:
            print(
                f"spec: the approved plan was not copied to spec.md — no /hi recorded for "
                f"session {session}. Tell the person; copy the plan by hand, or run /hi and "
                "approve again.",
                file=stderr,
            )
            return 2
        append_plan(path, plan, now, session)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"spec: spec.md not written: {exc}", file=stderr)
    return 0
