"""`guppi event <name> [--session ID] [detail ...]` — the event log.

One line per hook event, appended to `vault/raw/<date>/event_log.md`. The log is
debugging material, not traceability: gitignored, written by hooks rather than by
instructions, so it still fills when the agent deviates or crashes. Rule page:
`vault/wiki/rules/rule-event-log.md`.

Line format: `- HH:MM:SS <first 8 of session_id | --------> <event> <detail>`.

The hook never fails the session. Every error goes to stderr and the exit code is 0.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

UNKNOWN_SESSION = "--------"
DETAIL_LIMIT = 80


def read_text(stream) -> str:
    """Everything on the stream, taken as bytes and decoded as UTF-8 where the stream has a
    byte layer underneath. A hook's stdin on Windows is a text wrapper in the locale's code
    page with `surrogateescape` (measured 2026-09-09: cp1252), which turns a UTF-8 payload
    into mojibake and lone surrogates that no UTF-8 file will take."""
    buffer = getattr(stream, "buffer", None)
    if buffer is not None:
        return buffer.read().decode("utf-8", errors="replace")
    return stream.read()


def read_payload(stream) -> dict:
    """The hook's JSON from stdin; `{}` when there is none or it is not JSON."""
    try:
        text = read_text(stream)
    except (OSError, ValueError):
        return {}
    if not text or not text.strip():
        return {}
    try:
        data = json.loads(text)
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


def session_stamp(session: str | None, payload: dict) -> str:
    """Eight characters of the session id, from the option first, the payload second."""
    value = session or payload.get("session_id") or ""
    value = str(value).strip()
    return value[:8].ljust(8, "-") if value else UNKNOWN_SESSION


def one_line(text: str, limit: int = DETAIL_LIMIT) -> str:
    return " ".join(str(text).split())[:limit]


def tool_detail(payload: dict) -> str:
    """`<tool>: <the most telling field of its input>`, or just the tool name."""
    tool = payload.get("tool_name")
    if not tool:
        return ""
    tool_input = payload.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        return str(tool)
    for key in ("command", "subagent_type", "skill", "file_path", "pattern", "description"):
        value = tool_input.get(key)
        if value:
            return f"{tool}: {one_line(value)}"
    return str(tool)


def event_detail(name: str, payload: dict, words: list[str]) -> str:
    if words:
        return one_line(" ".join(words))
    if name == "session-start":
        return one_line(payload.get("source") or payload.get("session_start_type") or "")
    if name == "tool":
        return tool_detail(payload)
    return ""


def format_line(name: str, payload: dict, words: list[str], session: str | None, now) -> str:
    parts = [f"- {now.strftime('%H:%M:%S')}", session_stamp(session, payload), name]
    detail = event_detail(name, payload, words)
    if detail:
        parts.append(detail)
    return " ".join(parts)


def log_path(project_dir: Path, now) -> Path:
    return project_dir / "vault" / "raw" / now.date().isoformat() / "event_log.md"


def append(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi event", description=__doc__.split("\n\n")[1])
    p.add_argument("name", help="the event, e.g. session-start, tool, hi")
    p.add_argument("--session", default=None, help="session id; overrides the payload's")
    p.add_argument("words", nargs="*", help="free detail; replaces what the payload would give")
    return p


def project_root() -> Path:
    import os

    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
        payload = read_payload(stdin)
        line = format_line(args.name, payload, args.words, args.session, now)
        append(log_path(project_dir, now), line)
    except SystemExit as exc:  # argparse: a bad invocation still must not fail the session
        if exc.code not in (None, 0):
            print("guppi event: bad arguments, nothing written", file=stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"guppi event: event_log.md not written: {exc}", file=stderr)
    return 0
