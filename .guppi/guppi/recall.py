"""`guppi recall` — the `SessionStart` hook on `compact`: what a working session reads back
after the client compacted its context (case 287).

`/hi` loads the session's texts once, through the `@` lines of its skill; a compaction keeps
`CLAUDE.md` and a capped part of the skill's body, and the rest survives only in the summary.
This hook is registered on `SessionStart` with the matcher `compact` (`rule-hook-registry`)
and prints, on stdout, what to read before the next reply — paths, not texts: a hook's
stdout over 10,000 characters is saved to a file and the agent gets a preview.

Reads the payload from stdin. With a `source` other than `compact`, or without a `hi` in
the session's window — `session_dir` of `.guppi/guppi/ledger.py`, the ledger hook's own — it
prints nothing. Otherwise stdout holds one header line naming the time and the session's
folder, then one path per line: the `@` lines of `.claude/skills/hi/SKILL.md` in their
order — the list is the skill file's, never a copy here, so a file added to
`rule-internal-context` is in it without a change — then the folder's `frontier.md` when it
exists, then the Spec: `spec.md` of the folder, or before the approval the plan file the
event log names last under `.claude/plans/`, as `guppi gate` finds it (case 122); then the
line `Frontier:` and the text of `frontier.md` as it stands. Exit 0 always; an error prints
nothing and blocks nothing; the hook writes no file and no event line — `session-start
compact` is `guppi event`'s. Rule page: `vault/wiki/rules/rule-compact-recall.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import plan_path, session_dir, session_event_logs

SKILL = Path(".claude") / "skills" / "hi" / "SKILL.md"
SOURCE = "compact"


def import_lines(skill: Path) -> list[str]:
    """The paths of the `@` lines of the hi skill file, in order; none without the file."""
    try:
        text = skill.read_text(encoding="utf-8")
    except OSError:
        return []
    return [line.strip()[1:] for line in text.splitlines() if line.strip().startswith("@")]


def spec_of(folder: Path, logs: list[tuple[str, str]], stamp: str) -> Path | None:
    """`spec.md` of the session's folder, or the plan file the event log names last; None
    when neither exists on disk."""
    spec = folder / "spec.md"
    if spec.is_file():
        return spec
    plan = plan_path(logs, stamp)
    if plan is not None and plan.is_file():
        return plan
    return None


def relative(path: Path, project_dir: Path) -> str:
    """The path as the agent reads it: relative to the project when it lies inside."""
    try:
        return path.resolve().relative_to(project_dir.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def recall(project_dir: Path, payload: dict, now) -> str:
    """The text for stdout; empty when nothing is due."""
    if str(payload.get("source") or "") != SOURCE:
        return ""
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    if folder is None:
        return ""
    logs = session_event_logs(project_dir, now, stamp)
    session = folder.relative_to(project_dir / "vault").as_posix() + "/"
    header = (
        f"recall: the context was compacted at {now.strftime('%H:%M:%S')}; the session is "
        f"{session}. Read before the next reply:"
    )
    lines = [header]
    lines.extend(import_lines(project_dir / SKILL))
    frontier = folder / "frontier.md"
    if frontier.is_file():
        lines.append(relative(frontier, project_dir))
    spec = spec_of(folder, logs, stamp)
    if spec is not None:
        lines.append(relative(spec, project_dir))
    if frontier.is_file():
        lines.append("Frontier:")
        lines.append(frontier.read_text(encoding="utf-8").rstrip("\n"))
    return "\n".join(lines) + "\n"


def run(argv, *, stdin=None, stdout=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        text = recall(project_dir, read_payload(stdin), now)
    except Exception:  # noqa: BLE001 — a hook that raises would fail the session; nothing is due
        return 0
    if text:
        stdout.write(text)
    return 0
