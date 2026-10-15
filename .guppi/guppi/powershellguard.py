"""`guppi powershellguard` — the `PreToolUse` hook on the `PowerShell` tool that refuses a
here-string piped into an interpreter.

A script fed inline to Python rewrote a source file in three sessions, and `Path.write_text`
left CRLF line endings in it. `guppi bashguard` refuses such a heredoc before a Bash call; a
here-string piped into an interpreter is the same script in PowerShell, and no check saw it
before the call. A lesson the agent has to remember is not a rule; a `PreToolUse` hook
cannot be skipped (case 796.2).

`uv run --project .guppi guppi powershellguard` runs on `PreToolUse` of `PowerShell`. It reads
`tool_input.command` and finds every here-string: the text from a line that ends with `@'`
or `@"` to a line that opens with `'@` or `"@`. A closing line that pipes the here-string
into an interpreter — judged by `interpreter` of `.guppi/guppi/bashguard.py`, the one judgment the
Bash guard calls, so this module keeps no list of its own — exits 2 with the reason on
stderr — `powershellguard: here-string refused — it is piped into <interpreter>. Write a
whole file with the Write tool and change a file with Edit, never through PowerShell; only
a script goes into the scratchpad, written with the Write tool and run by path. The refusal
is this guard working as designed, not an event of the session: do not report it at
Retro.` — which blocks the call; one line `powershellguard refused: <reason>` goes to
`vault/raw/<date>/event_log.md` before that. A here-string not piped into an interpreter,
a command without a here-string, any other tool, or a payload the hook cannot read: exit 0,
the last with one line on stderr. A quoted string, a variable or the output of a command
piped into an interpreter, a script run by path and a script passed by `-c` or `-e` pass.
The hook never raises. Rule page: `vault/wiki/rules/rule-powershell-guard.md`.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.bashguard import interpreter
from guppi.event import append, format_line, log_path, project_root, read_payload

TOOL = "PowerShell"
OPENING = re.compile(r"@['\"]\s*$")
CLOSING = re.compile(r"^\s*(['\"])@(.*)$")


def closing_lines(command: str) -> list[str]:
    """What follows the closing `'@` or `"@` of every here-string in the command, in order;
    a here-string that nothing closes gives none."""
    found: list[str] = []
    quote = None
    for line in command.split("\n"):
        if quote is None:
            match = OPENING.search(line.rstrip("\r"))
            if match:
                quote = match.group(0).strip()[1]
            continue
        match = CLOSING.match(line.rstrip("\r"))
        if match and match.group(1) == quote:
            found.append(match.group(2))
            quote = None
    return found


def refusal(command: str) -> str | None:
    """The first reason to refuse the command, or None."""
    for rest in closing_lines(command):
        if not rest.lstrip().startswith("|"):
            continue
        fed = interpreter(rest.lstrip()[1:])
        if fed:
            return f"it is piped into {fed}"
    return None


def log_refusal(project_dir: Path, payload: dict, reason: str, now, stderr) -> None:
    """A blocked call has no `PostToolUse`, so a refusal the hook does not write is nowhere.
    A log it cannot write never changes the refusal."""
    try:
        line = format_line("powershellguard", payload, ["refused:", reason], None, now)
        append(log_path(project_dir, now), line)
    except Exception as exc:  # noqa: BLE001 — the refusal stands whatever the log does
        print(f"powershellguard: refusal not logged: {exc}", file=stderr)


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("powershellguard: payload not readable, check skipped", file=stderr)
            return 0
        if payload.get("tool_name") != TOOL:
            return 0
        tool_input = payload.get("tool_input") or {}
        command = tool_input.get("command") if isinstance(tool_input, dict) else None
        if not command or "@" not in str(command):
            return 0
        reason = refusal(str(command))
        if reason is None:
            return 0
        log_refusal(project_dir, payload, reason, now, stderr)
        print(
            f"powershellguard: here-string refused — {reason}. Write a whole file with the "
            "Write tool and change a file with Edit, never through PowerShell; only a script "
            "goes into the scratchpad, written with the Write tool and run by path. The "
            "refusal is this guard working as designed, not an event of the session: do not "
            "report it at Retro.",
            file=stderr,
        )
        return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"powershellguard: not checked: {exc}", file=stderr)
        return 0
