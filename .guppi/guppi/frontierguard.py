"""`guppi frontierguard` — the `PreToolUse` hook that refuses an edit of the Frontier which leaves
an open box beside a closer.

The main agent closes a line of a session's `frontier.md` by its box and its closer together,
such as `- [x] C3 — … · backlog · case N`. An `Edit` that matches only the tail of the line
appends the closer and leaves the box `[ ]`, and `/pre-spec` then reads the line as open
(case 1012). On `Edit`, `Write` or `MultiEdit` of a file `vault/raw/<date>/<HHMM>/frontier.md`, the
date and the `HHMM` judged by `generate.DAY` and `generate.SESSION` as `casecheck.is_case_file`
judges a session folder, the hook works out the whole text the call would leave by
`text_after` of `.guppi/guppi/ratified.py`, the one computation `builder_write` shares, and
reads its lines by `open_box_closers` of `.guppi/guppi/prespec.py`, the one judgment of a box
line whose box is `[ ]` while its last segment after ` · ` is a closer by `CLOSERS`. When one
or more such lines stand, under any heading, it exits 2 with each item and its closer on
stderr, which Claude Code shows the agent and which blocks the call; one line goes to the
day's `event_log.md` first, since a blocked call has no `PostToolUse` (case 91). A text whose
open lines carry no closer, any other file, any other tool, a text that cannot be made — an
old string missing or found more than once without `replace_all`, a file to edit that does
not exist — and a payload the hook cannot read exit 0, the last with one line on stderr. The
hook never raises. It runs as `uv run --project .guppi guppi frontierguard`, on `PreToolUse`
with the matcher `Edit|Write|MultiEdit`. The check of the Frontier in `/pre-spec` stays as it
is, so a box written by a shell call still shows there.
Rule page: `vault/wiki/rules/rule-frontier-hook.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import append, format_line, log_path, project_root, read_payload
from guppi.generate import DAY, SESSION
from guppi.prespec import open_box_closers
from guppi.ratified import text_after

TOOLS = ("Edit", "Write", "MultiEdit")
FRONTIER = "frontier.md"


def is_frontier(path) -> bool:
    """A path `vault/raw/<date>/<HHMM>/frontier.md`, whatever it stands under."""
    parts = Path(str(path)).parts
    return (
        len(parts) >= 5
        and parts[-1] == FRONTIER
        and SESSION.match(parts[-2]) is not None
        and DAY.match(parts[-3]) is not None
        and parts[-4] == "raw"
        and parts[-5] == "vault"
    )


def log_refusal(project_dir: Path, payload: dict, path: str, now, stderr) -> None:
    """A blocked call has no `PostToolUse`, so a refusal the hook does not write is nowhere
    (case 91). A log it cannot write never changes the refusal."""
    tool = str(payload.get("tool_name") or "a tool")
    try:
        line = format_line("frontierguard", payload, ["refused", tool, path], None, now)
        append(log_path(project_dir, now), line)
    except Exception as exc:  # noqa: BLE001 — the refusal stands whatever the log does
        print(f"frontierguard: refusal not logged: {exc}", file=stderr)


def refusal(path: str, found: list[tuple[str, str]]) -> str:
    """The reason on stderr: each item with its closer, and how the line is closed."""
    items = ", ".join(f"{item} (· {closer})" for item, closer in found)
    return (
        f"frontierguard: {path}: {items} keeps the box [ ] beside a closer; write the box and "
        "the closer in one edit of the whole line, [x] for an item ended and [-] for an item "
        "put off"
    )


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("frontierguard: payload not readable, check skipped", file=stderr)
            return 0
        if payload.get("tool_name") not in TOOLS:
            return 0
        tool_input = payload.get("tool_input")
        file_path = tool_input.get("file_path") if isinstance(tool_input, dict) else None
        if not file_path or not is_frontier(file_path):
            return 0
        path = Path(str(file_path))
        if not path.is_absolute():
            path = project_dir / path
        text, _ = text_after(payload, path)
        if text is None:
            return 0  # the tool fails the call itself
        found = open_box_closers(text)
        if found:
            log_refusal(project_dir, payload, str(file_path), now, stderr)
            print(refusal(str(file_path), found), file=stderr)
            return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"frontierguard: check skipped: {exc}", file=stderr)
    return 0
