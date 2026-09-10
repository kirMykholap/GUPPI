"""`guppi gate` — the `PreToolUse` hook on the `Skill` tool that refuses `/handoff` on a
dirty tree.

Reads the hook payload from stdin. When the tool is `Skill` and its input names the skill
`handoff`, and `git status --porcelain` is not empty, it exits 2 with the reason `commit
first`, which blocks the call once; a clean tree, another skill or another tool: exit 0.
The hook writes nothing and commits nothing. It sees only calls made through the `Skill`
tool, which is how the Retro skill calls `/handoff`; the handoff skill checks the tree
itself for the case where the person types it. Rule page:
`vault/wiki/rules/rule-retro-commit.md`.
"""

import subprocess
import sys
from pathlib import Path

from guppi.event import project_root, read_payload

TOOL = "Skill"
SKILL = "handoff"


def skill_of(payload: dict) -> str:
    if payload.get("tool_name") != TOOL:
        return ""
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return ""
    for key in ("skill", "name", "skill_name"):
        value = tool_input.get(key)
        if value:
            return str(value).strip().lstrip("/").split(" ", 1)[0]
    return ""


def dirty(project_dir: Path) -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=project_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, status=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        payload = read_payload(stdin)
        if skill_of(payload) != SKILL:
            return 0
        tree = dirty(project_dir) if status is None else status
        if not tree:
            return 0
        count = len(tree.splitlines())
        print(
            f"gate: /handoff refused — commit first. {count} path(s) uncommitted; the librarian's "
            "commit must be separate from the session's.",
            file=stderr,
        )
        return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"gate: not checked: {exc}", file=stderr)
        return 0
