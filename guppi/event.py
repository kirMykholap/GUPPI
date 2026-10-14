"""`guppi event <name> [--session ID] [detail ...]` — the event log.

One line per hook event, appended to `vault/raw/<date>/event_log.md`. The log is
debugging material, not traceability: gitignored, written by hooks rather than by
instructions, so it still fills when the agent deviates or crashes. Rule page:
`vault/wiki/rules/rule-event-log.md`.

Line format: `- HH:MM:SS <first 8 of session_id | --------> <event> <detail>`.

`guppi event prompt`, the `UserPromptSubmit` hook, is the one event with a filter: it
writes `hi` with the session's stamp when the prompt is `/hi` (arguments allowed) and no
`hi` of this session follows its first `session-start` yet; any other prompt, a second
`/hi`, or a payload without a session id writes nothing. On `/hi` it also
prints one line on stdout, which Claude Code adds to the context: `hi: HH:MM:SS <stamp> →
raw/<date>/<HHMM>/` for the line it wrote, `hi: already recorded at HH:MM:SS → raw/<date>/
<HHMM>/` for the one that exists; the `/hi` skill takes the session's folder from it.

`/hi` opens a working session only in plan mode. A `/hi` whose `permission_mode`
is not `plan` — `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, or the
field missing or empty, a second `/hi` included — writes no line, prints nothing on stdout and
exits 2 with a reason on stderr that tells the person to turn plan mode on and type `/hi`
again; Claude Code blocks the prompt, and the skill does not run. `hi_refusal` is the one
judgment; any other prompt is not judged, and its `permission_mode` is not read.

The hook never fails the session on an error: every error goes to stderr and the exit code is
0. Its one exit 2 is the refusal of a `/hi` outside plan mode.
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
    into mojibake and lone surrogates that no UTF-8 file will take. A leading BOM is dropped:
    Windows PowerShell 5.1 puts one in front of a piped payload (measured 2026-09-12), and
    `json.loads` refuses it."""
    buffer = getattr(stream, "buffer", None)
    if buffer is not None:
        return buffer.read().decode("utf-8-sig", errors="replace")
    return stream.read().lstrip("\ufeff")


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


HI_PROMPT = "/hi"


PLAN_MODE = "plan"
HI_REFUSED = (
    "hi: /hi opens a working session only in plan mode, and this prompt came in permission "
    "mode {mode}. Turn plan mode on and type /hi again."
)


def is_hi_prompt(prompt) -> bool:
    text = str(prompt or "").strip()
    return text == HI_PROMPT or text.startswith(HI_PROMPT + " ")


def hi_refusal(payload: dict) -> str | None:
    """The reason a `/hi` payload is refused, or None when it passes: the one judgment of a
    `/hi` by its `permission_mode`. Only `plan` passes; any other value, and a
    field missing or empty, is refused — a second `/hi` too. Any other prompt is not judged,
    and its `permission_mode` is not read."""
    if not is_hi_prompt(payload.get("prompt")):
        return None
    mode = payload.get("permission_mode")
    if mode == PLAN_MODE:
        return None
    return HI_REFUSED.format(mode=f"'{mode}'" if mode else "not given")


def hi_written(project_dir: Path, now, stamp: str) -> bool:
    """True when a `hi` of this stamp already follows the first `session-start` of this
    stamp in the logs the ledger hook walks: one session, one `hi` line."""
    return hi_of(project_dir, now, stamp) is not None


def hi_of(project_dir: Path, now, stamp: str) -> tuple[str, str] | None:
    """`(date, HH:MM:SS)` of the first `hi` of this stamp after its first `session-start`
    in the logs the ledger hook walks; None when there is none."""
    from guppi.ledger import session_event_logs  # ledger imports this module

    ours = False
    for day, text in session_event_logs(project_dir, now, stamp):
        for line in text.splitlines():
            parts = line.split(" ", 3)
            if len(parts) < 4 or parts[0] != "-" or parts[2] != stamp:
                continue
            event = parts[3].split(" ", 1)[0]
            if event == "session-start":
                ours = True
            elif event == "hi" and ours:
                return day, parts[1]
    return None


def folder_of(day: str, time: str) -> str:
    """`raw/<date>/<HHMM>/`, the session's folder, as the `hi:` line names it."""
    return f"raw/{day}/{time[:2] + time[3:5]}/"


def hi_context(payload: dict, session: str | None, project_dir: Path, now) -> str | None:
    """The line the `UserPromptSubmit` hook prints into the context on `/hi`:
    `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/` when it wrote the `hi` line, `hi: already
    recorded at HH:MM:SS → raw/<date>/<HHMM>/` when one of this session exists; None on
    any other prompt or without a session id."""
    if not is_hi_prompt(payload.get("prompt")):
        return None
    stamp = session_stamp(session, payload)
    if stamp == UNKNOWN_SESSION:
        return None
    existing = hi_of(project_dir, now, stamp)
    if existing is not None:
        day, time = existing
        return f"hi: already recorded at {time} → {folder_of(day, time)}"
    time = now.strftime("%H:%M:%S")
    return f"hi: {time} {stamp} → {folder_of(now.date().isoformat(), time)}"


def prompt_line(payload: dict, session: str | None, project_dir: Path, now) -> str | None:
    """The `hi` line a `UserPromptSubmit` payload earns, or None: the prompt must be `/hi`
    (arguments allowed), the session id known, and no `hi` of this session written yet. Any other prompt writes nothing."""
    if not is_hi_prompt(payload.get("prompt")):
        return None
    stamp = session_stamp(session, payload)
    if stamp == UNKNOWN_SESSION or hi_written(project_dir, now, stamp):
        return None
    return format_line("hi", payload, [], session, now)


def log_path(project_dir: Path, now) -> Path:
    return project_dir / "vault" / "raw" / now.date().isoformat() / "event_log.md"


def append(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi event", description=__doc__.split("\n\n")[1])
    p.add_argument("name", help="the event, e.g. session-start, tool, prompt, hi")
    p.add_argument("--session", default=None, help="session id; overrides the payload's")
    p.add_argument("words", nargs="*", help="free detail; replaces what the payload would give")
    return p


def project_root() -> Path:
    import os

    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
        payload = read_payload(stdin)
        if args.name == "prompt":
            refusal = hi_refusal(payload)
            if refusal is not None:  # no line, nothing on stdout; Claude Code blocks the prompt
                print(refusal, file=stderr)
                return 2
            context = hi_context(payload, args.session, project_dir, now)
            line = prompt_line(payload, args.session, project_dir, now)
            if line is not None:
                append(log_path(project_dir, now), line)
            if context is not None:
                print(context, file=stdout)  # stdout of UserPromptSubmit reaches the context
            return 0
        else:
            line = format_line(args.name, payload, args.words, args.session, now)
        append(log_path(project_dir, now), line)
    except SystemExit as exc:  # argparse: a bad invocation still must not fail the session
        if exc.code not in (None, 0):
            print("guppi event: bad arguments, nothing written", file=stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"guppi event: event_log.md not written: {exc}", file=stderr)
    return 0
