"""`guppi bashguard` — the `PreToolUse` hook on the `Bash` tool that refuses a heredoc
whose body carries a backslash, or one that writes a file.

On this Windows machine the tool's shell layer interprets backslash escapes inside a
heredoc body before the interpreter reads it, whatever the quoting of the marker; three
sessions (H, L, M) broke edit scripts that way with the lesson live, and a heredoc that
writes a file fails on quotes in its body. A lesson the agent has to remember is not a
rule; a `PreToolUse` hook cannot be skipped (case 127).

The hook reads `tool_input.command`, finds every heredoc (`<<` or `<<-`, the marker quoted
or not) and its body up to the closing line. A body with a backslash, or a marker line that
redirects into a file (`>` or `>>` to a path other than `/dev/null`, or `tee`), exits 2 with
the reason on stderr — `bashguard: heredoc refused — <reason>. Write a whole file with the
Write tool and change a file with Edit, never through Bash; only a script goes into the
scratchpad, written with the Write tool and run by path. The refusal is this guard working
as designed, not an event of the session: do not report it at Retro.` (case 530.2) —
which blocks the call (case 384); one line `bashguard refused: <reason>` goes to
`vault/raw/<date>/event_log.md` before that (case 91). A `<<<` here-string, a heredoc without a backslash whose output goes to a
pipe or the screen, a command without a heredoc, any other tool, or a payload the hook
cannot read: exit 0, the last with one line on stderr. The hook never raises. Rule page:
`vault/wiki/rules/rule-bash-guard.md`.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import append, format_line, log_path, project_root, read_payload

TOOL = "Bash"
MARKER = re.compile(r"(?<!<)<<(?!<)(-?)\s*(?:'([^']+)'|\"([^\"]+)\"|\\?(\w+))")
REDIRECT = re.compile(r"(?<![<>&\d])\d?>{1,2}\s*(\S+)")
NULL = "/dev/null"


def heredocs(command: str) -> list[tuple[str, str]]:
    """`(marker line, body)` of every heredoc in the command, in order. The body runs from
    the line after the marker to the closing line — the marker word alone, leading tabs
    stripped for `<<-` — or to the end of the command when nothing closes it."""
    lines = command.split("\n")
    found: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        markers = [
            (m.group(1) == "-", m.group(2) or m.group(3) or m.group(4))
            for m in MARKER.finditer(line)
        ]
        i += 1
        for dash, word in markers:
            body: list[str] = []
            while i < len(lines):
                candidate = lines[i].lstrip("\t") if dash else lines[i]
                if candidate == word:
                    i += 1
                    break
                body.append(lines[i])
                i += 1
            found.append((line, "\n".join(body)))
    return found


def file_write(marker_line: str) -> str | None:
    """The path a marker line writes into — a `>`/`>>` target other than `/dev/null`, or the
    file after `tee` — or None."""
    line = MARKER.sub(" ", marker_line)
    for match in REDIRECT.finditer(line):
        target = match.group(1)
        if target != NULL and not target.startswith("&"):
            return target
    tee = re.search(r"\btee\b\s+(?:-a\s+)?(\S+)", line)
    if tee and tee.group(1) != NULL:
        return tee.group(1)
    return None


def refusal(command: str) -> str | None:
    """The first reason to refuse the command, or None."""
    for marker_line, body in heredocs(command):
        if "\\" in body:
            return "a backslash in its body"
        path = file_write(marker_line)
        if path:
            return f"it writes {path}"
    return None


def log_refusal(project_dir: Path, payload: dict, reason: str, now, stderr) -> None:
    """A blocked call has no `PostToolUse`, so a refusal the hook does not write is nowhere
    (case 91). A log it cannot write never changes the refusal."""
    try:
        line = format_line("bashguard", payload, ["refused:", reason], None, now)
        append(log_path(project_dir, now), line)
    except Exception as exc:  # noqa: BLE001 — the refusal stands whatever the log does
        print(f"bashguard: refusal not logged: {exc}", file=stderr)


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("bashguard: payload not readable, check skipped", file=stderr)
            return 0
        if payload.get("tool_name") != TOOL:
            return 0
        tool_input = payload.get("tool_input") or {}
        command = tool_input.get("command") if isinstance(tool_input, dict) else None
        if not command or "<<" not in str(command):
            return 0
        reason = refusal(str(command))
        if reason is None:
            return 0
        log_refusal(project_dir, payload, reason, now, stderr)
        print(
            f"bashguard: heredoc refused — {reason}. Write a whole file with the Write tool and "
            "change a file with Edit, never through Bash; only a script goes into the "
            "scratchpad, written with the Write tool and run by path. The refusal is this "
            "guard working as designed, not an event of the session: do not report it at Retro.",
            file=stderr,
        )
        return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"bashguard: not checked: {exc}", file=stderr)
        return 0
