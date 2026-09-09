"""`guppi spec` — the `PostToolUse ExitPlanMode` hook that copies the approved plan into
`vault/raw/<date>/spec.md`.

The plan arrives whole in `tool_response.plan` (measured 2026-09-09, Slice 1 probe). It is
appended after a `---` separator when the file already has content, under a stamp line
with the time and the session; a plan whose text is already in the file is not appended
again. Any other tool, or a payload without a plan: nothing. Without a `hi` recorded for
this session — the same check the ledger makes — the hook exits 2 with the reason, so the
person is told rather than left believing the Spec was copied. Rule page:
`vault/wiki/rules/rule-spec-capture.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import log_path, project_root, read_payload, session_stamp
from guppi.ledger import hi_recorded

TOOL = "ExitPlanMode"


def plan_text(payload: dict) -> str:
    if payload.get("tool_name") != TOOL:
        return ""
    response = payload.get("tool_response")
    if not isinstance(response, dict):
        return ""
    return str(response.get("plan") or "")


def spec_path(project_dir: Path, now) -> Path:
    return log_path(project_dir, now).with_name("spec.md")


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
        log = log_path(project_dir, now)
        event_log = log.read_text(encoding="utf-8") if log.exists() else ""
        if not hi_recorded(event_log, session):
            print(
                f"spec: the approved plan was not copied to spec.md — no /hi recorded for "
                f"session {session}. Tell the person; copy the plan by hand, or run /hi and "
                "approve again.",
                file=stderr,
            )
            return 2
        append_plan(spec_path(project_dir, now), plan, now, session)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"spec: spec.md not written: {exc}", file=stderr)
    return 0
