"""`guppi spec` — the `PostToolUse ExitPlanMode` hook that copies the approved plan into
the session's folder, `vault/raw/<hi date>/<hi HHMM>/spec.md`, and prints the fork.

The plan arrives whole in `tool_response.plan` (measured 2026-09-09, Slice 1 probe). It is
appended after a `---` separator when the file already has content, under a stamp line
with the time and the session; a plan whose text is already in the file is not appended
again. Any other tool, or a payload without a plan: nothing. The folder is named by the
`hi` line that opens this session's window — its date, then its time as `HHMM` — found
the way the ledger hook finds it, across the event logs of the window (case 73.2); the
folder is created when missing. Without a `hi` recorded for this session the hook exits 2
with the reason, so the person is told rather than left believing the Spec was copied.

The file has three writers: this hook, once per approval; the `Stop` hook of
`rule-spec-write`, which, once the file stands, writes each Case ratified after the approval
— its sections replaced, or placed — removes a superseded Case, and writes a defer-only Case
under `## Deferred` (cases 421.1, 441, 542); and Work Mode, which ticks the boxes of the
`tasks` blocks.

Written or already there, the hook then prints one JSON object on stdout —
`{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": <line>}}` —
the one shape in which the stdout of a `PostToolUse` hook reaches the agent: plain stdout
with exit 0 goes to the client's debug log and never to the context (case 255). The line is
the fork the person chooses at — `/work`, Work Mode on the Spec, or `/carry` to conserve it
for a later session — naming the session folder and the Spec file (case 190.5). A
`PostToolUse` hook cannot block: the tool has run; the agent asks by `AskUserQuestion` with
the two options, the person picks, nothing starts until the answer, and the agent then calls
the skill picked (cases 190.2, 479.1). When the approved plan names the `spec.md` of a
conserved Spec — a folder under `vault/raw/` that holds `carry.md`, by `conserved_spec_named`
of `guppi/box.py` — the line in place of the fork names that folder and tells the agent to
call `/box` with it and to ask the person nothing: the person took that Spec at the Frontier
(case 591.3). Rule page: `vault/wiki/rules/rule-spec-capture.md`.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

from guppi.box import conserved_spec_named
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


def fork_line(path: Path, project_dir: Path) -> str:
    """The one line the agent reads after the Spec is in place (cases 190.5, 479.1): the
    fork between `/work` and `/carry`, asked by `AskUserQuestion`, with the session folder
    and the Spec file; the agent then calls the skill picked."""
    try:
        spec = path.relative_to(project_dir).as_posix()
    except ValueError:
        spec = path.as_posix()
    folder = spec.rsplit("/", 1)[0]
    return (
        f"spec: the Spec is in {spec}. Ask the person which end this session takes by "
        "AskUserQuestion with two options, and start nothing until it is answered: /work, "
        "Work Mode on the Spec now — or /carry, which conserves it for a later session (the "
        f"brief rewritten, {folder}/carry.md as the mark, a commit, nothing else run). Then "
        "call the skill picked."
    )


def box_line(path: Path, folder: Path, project_dir: Path) -> str:
    """The line in place of the fork when the approved plan names a conserved Spec (case
    591.3): the person took it at the Frontier, so the agent calls `/box` with its folder and
    asks nothing."""
    try:
        spec = path.relative_to(project_dir).as_posix()
        conserved = folder.relative_to(project_dir).as_posix()
    except ValueError:
        spec, conserved = path.as_posix(), folder.as_posix()
    return (
        f"spec: the Spec is in {spec}. The plan takes the conserved Spec of {conserved}/: "
        f"call /box with {conserved}/ as its argument, and ask the person nothing — the "
        "person took that Spec at the Frontier."
    )


def fork_output(path: Path, project_dir: Path, plan: str = "") -> str:
    """`fork_line`, or `box_line` for a plan that names a conserved Spec by
    `conserved_spec_named` of `guppi/box.py`, wrapped as `hookSpecificOutput.additionalContext`,
    the JSON a `PostToolUse` hook prints so that the client adds the line to the context
    (case 255)."""
    folder = conserved_spec_named(plan, project_dir)
    line = fork_line(path, project_dir) if folder is None else box_line(path, folder, project_dir)
    return json.dumps(
        {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": line}},
        ensure_ascii=False,
    )


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
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
        print(fork_output(path, project_dir, plan), file=stdout)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"spec: spec.md not written: {exc}", file=stderr)
    return 0
