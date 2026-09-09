"""`guppi probe` — a throwaway hook that records what a hook event is really handed.

Writes stdin, verbatim, to `vault/raw/<date>/probe-<event>-<n>.json` (gitignored). Exists
for one measurement (Slice 1, Case 10: does `Stop` carry `last_assistant_message`; does
`PostToolUse ExitPlanMode` carry the plan) and is deleted in the commit that uses the
reading. The old vault's lesson: read the documentation, then measure anyway.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        text = stdin.read()
        payload = read_payload(__import__("io").StringIO(text))
        name = str(payload.get("hook_event_name") or "unknown")
        folder = project_dir / "vault" / "raw" / now.date().isoformat()
        folder.mkdir(parents=True, exist_ok=True)
        n = 1
        while (folder / f"probe-{name}-{n}.json").exists():
            n += 1
        (folder / f"probe-{name}-{n}.json").write_text(text, encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 — a probe must never fail the session
        print(f"guppi probe: nothing written: {exc}", file=stderr)
    return 0
