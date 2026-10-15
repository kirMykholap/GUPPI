"""`guppi pageread` — the `PreToolUse` hook on `Read` that reads a vault page without its
`## History`; `guppi pageread --after` — the `PostToolUse` hook that says where the History
starts (`rule-page-read`) (case 420.1).

Before. For a `Read` of a file under `vault/wiki/` whose input carries neither `offset` nor
`limit`, the hook finds the line of the page's own `## History` heading by
`pages.history_line` — the walk of `split_sections`, so a heading inside a render block does
not count — and prints `hookSpecificOutput.updatedInput`, the input with `limit` set to the
line before it, with no permission decision; the agent gets the frontmatter and the body.

After. Claude Code hands `PostToolUse` the input as the hook changed it (measured
2026-09-25, Claude Code 2.1.282, in the main agent and in a subagent). A `Read` of such a
file with no `offset` and `limit` one line short of the History heading was cut, and the
hook adds one line of `additionalContext`: the History is cut, its first and last line, and
a `Read` with `offset` at its first line shows it.

A call with its own `offset` or `limit`, a file with no `## History` — `brief.md`,
`sprint.md`, `glossary.md`, `log.md`, `case-schema.md` — a file outside `vault/wiki/`, any
other tool, or a payload the hook cannot read pass unchanged: exit 0, nothing printed. The
page on disk is never changed. The payload is read as UTF-8; the hook never raises. Rule
page: `vault/wiki/rules/rule-page-read.md`.
"""

import json
import os
import sys
from pathlib import Path

from guppi.event import project_root, read_payload
from guppi.pages import history_line, wiki_root

TOOL = "Read"


def inside(path: Path, folder: Path) -> bool:
    """Whether `path` lies under `folder`, the case of a Windows path ignored."""
    try:
        path = Path(os.path.normcase(os.path.abspath(path)))
        folder = Path(os.path.normcase(os.path.abspath(folder)))
    except (OSError, ValueError):
        return False
    return path == folder or folder in path.parents


def page_of(payload: dict, project_dir: Path) -> tuple[dict, Path, str] | None:
    """`(tool input, path, text)` of a `Read` of a file under `vault/wiki/`; None otherwise."""
    if payload.get("tool_name") != TOOL:
        return None
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict) or not tool_input.get("file_path"):
        return None
    path = Path(str(tool_input["file_path"]))
    if not path.is_absolute():
        path = project_dir / path
    if not inside(path, wiki_root(project_dir)) or not path.is_file():
        return None
    return tool_input, path, path.read_text(encoding="utf-8")


def before(payload: dict, project_dir: Path, stdout) -> int:
    found = page_of(payload, project_dir)
    if found is None:
        return 0
    tool_input, _, text = found
    if tool_input.get("offset") is not None or tool_input.get("limit") is not None:
        return 0
    line = history_line(text)
    if line is None or line < 2:
        return 0
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "updatedInput": {**tool_input, "limit": line - 1},
        }
    }
    print(json.dumps(output, ensure_ascii=False), file=stdout)
    return 0


def after(payload: dict, project_dir: Path, stdout) -> int:
    found = page_of(payload, project_dir)
    if found is None:
        return 0
    tool_input, path, text = found
    line = history_line(text)
    if line is None or tool_input.get("offset") is not None:
        return 0
    if tool_input.get("limit") != line - 1:
        return 0
    last = len(text.splitlines())
    try:
        name = path.relative_to(wiki_root(project_dir)).as_posix()
    except ValueError:  # the same folder spelled in another case
        name = path.name
    message = (
        f"pageread: the History of {name} is cut, lines {line}–{last}; a Read with offset "
        f"{line} shows how the page changed (rule-page-read)."
    )
    output = {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": message}}
    print(json.dumps(output, ensure_ascii=False), file=stdout)
    return 0


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        payload = read_payload(stdin)
        if not payload:
            return 0
        if "--after" in argv:
            return after(payload, project_dir, stdout)
        return before(payload, project_dir, stdout)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the call
        print(f"pageread: passed whole: {exc}", file=stderr)
        return 0
