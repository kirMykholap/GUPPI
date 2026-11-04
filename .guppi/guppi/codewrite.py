"""`guppi codewrite` — the `PostToolUse` hook on `Edit`, `Write` and `MultiEdit` that names a
pointer outside its bracket under `.guppi/` at the write (`rule-clean-branch`).

A pointer to a case in a comment or a docstring under `.guppi/` stands in a bracket of its own
at the end of its sentence, so that `guppi ship` removes it whole from the clean version; the
test of the live code in `.guppi/tests/test_ship.py` checks it, but only inside the full test
run. After each call of `Edit`, `Write` or `MultiEdit`, this hook reads the file the call
wrote, as it stands now, and runs over it `live_code` of `.guppi/guppi/ship.py`, the same
judgment the test of the live code takes its lines from. Each line it finds — a pointer
outside a bracket of its own, a bare case number in a comment or a docstring — goes to the
agent with one line on the fix, as one `hookSpecificOutput.additionalContext`, the shape in
which the stdout of a `PostToolUse` hook reaches the agent beside the result of the tool.

A file with no such line, a file outside `.guppi/`, a file of `LEFT_OUT` or `NOT_CLEANED` of
`.guppi/guppi/ship.py` and a call of another tool print nothing. The hook refuses no call and
exits 0; a payload or a file it cannot read gives one line on stderr. It serves only the build
of the clean version: the copy holds neither this module nor its registration, as
`.guppi/guppi/ship.py` sets it. Rule page: `vault/wiki/rules/rule-clean-branch.md`.
"""

import json
import sys
from pathlib import Path

from guppi.event import project_root, read_payload
from guppi.ship import live_code

TOOLS = ("Edit", "Write", "MultiEdit")
FIX = (
    "codewrite: put each pointer to a case in a bracket of its own at the end of its"
    " sentence, such as `(as set in case N)`, or write the sample `case N`; a bare case"
    " number in a comment or a docstring fails the test of the live code."
)


def relative(file_path: str, project_dir: Path) -> str | None:
    """The path of the written file relative to the project, in the form `/`; None for a
    file outside the project."""
    path = Path(file_path)
    if not path.is_absolute():
        path = project_dir / path
    try:
        return path.resolve().relative_to(project_dir.resolve()).as_posix()
    except ValueError:
        return None


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        payload = read_payload(stdin)
    except Exception:  # noqa: BLE001 — a hook that raises would fail the call
        payload = {}
    if not payload:  # `read_payload` gives {} for no payload and for one that is not JSON
        print("codewrite: payload not readable, nothing checked", file=stderr)
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    tool_input = payload.get("tool_input")
    file_path = tool_input.get("file_path") if isinstance(tool_input, dict) else None
    if not file_path:
        return 0
    name = relative(str(file_path), project_dir)
    if name is None or not name.startswith(".guppi/"):
        return 0
    try:
        text = (project_dir / name).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"codewrite: {name} not checked: {exc}", file=stderr)
        return 0
    found = live_code(name, text)
    if found:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "\n".join([*found, FIX]),
            }
        }
        print(json.dumps(output, ensure_ascii=False), file=stdout)
    return 0
