"""`guppi guard` — the `PreToolUse` hook that refuses a hand edit of a governed harness file.

Every live Rule page under `vault/wiki/rules/` with a `governs` field owns the text of one
harness file; the renderer keeps the page and the file one text, so an edit to the file
alone is lost at the next render and was ratified for nobody. On `Edit`, `Write` or
`MultiEdit` the hook takes `tool_input.file_path`, resolves it against the project root and
compares it with every governed path. A match exits 2 with the rule's slug and the file on
stderr, which Claude Code shows the agent and which blocks the tool. One line goes to the
day's `event_log.md` first: a blocked call has no `PostToolUse`, so a refusal the hook does
not write is nowhere. Any other tool, a path
no page governs, or a payload the hook cannot read: exit 0, the last with one line on
stderr. The hook never raises. Rule page: `vault/wiki/rules/rule-governed-files-hook.md`.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import append, format_line, log_path, project_root, read_payload
from guppi.pages import Page, read_category, wiki_root

TOOLS = ("Edit", "Write", "MultiEdit")
NOT_LIVE = ("archived", "deleted")


def key(path: str) -> str:
    """One spelling for a relative path: separators and, on Windows, case folded."""
    return os.path.normcase(os.path.normpath(path))


def owner_first(page: Page) -> tuple[bool, str]:
    """A `full` page owns its file; a partial only splices into it. Full pages first, then
    slug order, so the refusal names the page one would update."""
    return page.props.get("render_mode") != "full", page.slug


def governed(pages: list[Page]) -> dict[str, tuple[str, str]]:
    """Normalized governed path → `(relative POSIX path, slug of the page governing it)`."""
    out: dict[str, tuple[str, str]] = {}
    for page in sorted(pages, key=owner_first):
        if page.error or page.props.get("status") in NOT_LIVE:
            continue
        governs = page.props.get("governs")
        if not governs or not isinstance(governs, str):
            continue
        out.setdefault(key(governs), (Path(governs).as_posix(), page.slug))
    return out


def relative(file_path: str, project_dir: Path) -> str | None:
    """`file_path` as a path relative to the project root; None when it lies outside."""
    path = Path(file_path)
    if not path.is_absolute():
        path = project_dir / path
    try:
        return path.resolve().relative_to(project_dir.resolve()).as_posix()
    except ValueError:
        return None


def log_refusal(project_dir: Path, payload: dict, path: str, slug: str, now, stderr) -> None:
    """A blocked call has no `PostToolUse`, so a refusal the hook does not write is nowhere. A log it cannot write never changes the refusal."""
    tool = str(payload.get("tool_name") or "a tool")
    try:
        line = format_line("guard", payload, ["refused", tool, path, f"({slug})"], None, now)
        append(log_path(project_dir, now), line)
    except Exception as exc:  # noqa: BLE001 — the refusal stands whatever the log does
        print(f"guard: refusal not logged: {exc}", file=stderr)


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("guard: payload not readable, check skipped", file=stderr)
            return 0
        if payload.get("tool_name") not in TOOLS:
            return 0
        tool_input = payload.get("tool_input") or {}
        file_path = tool_input.get("file_path") if isinstance(tool_input, dict) else None
        if not file_path:
            return 0
        rel = relative(str(file_path), project_dir)
        if rel is None:
            return 0
        hit = governed(read_category(wiki_root(project_dir), "rules")).get(key(rel))
        if hit is not None:
            path, slug = hit
            log_refusal(project_dir, payload, path, slug, now, stderr)
            print(
                f"guard: {path} is rendered from {slug}; change the Rule page through a decision",
                file=stderr,
            )
            return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"guard: check skipped: {exc}", file=stderr)
    return 0
