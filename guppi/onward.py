"""`guppi onward` — the `Stop` hook that sends the agent from the end of Retro to `/handoff`.

In Claude Code the end of a reply hands the turn to the person, and the ledger hook writes
the lines of a reply only when it ends; so Retro ends one reply with its `LEDGER` block, and
this hook sends the agent on in the same turn (case 531.9). It exits 2 when four things hold:
the event log of the session's window holds the mark `retro` of this session after its
`hi` — the mark `guppi gate` leaves at a call of `/retro` it lets through —,
`raw/<hi date>/<hi HHMM>/handoff.md` does not stand, `stop_hook_active` is false, and the
reply that ended does not open with `STOP:`. Its reason on stderr tells the agent to commit
the session folder and call `/handoff`, or, when a condition of
`vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person.

In every other case with no error of its own it exits 0 and prints nothing: without a `hi` of the session, before the
mark, once `handoff.md` stands, on the reply that follows a refusal of a `Stop` hook, and on
a reply that opens with `STOP:`. It counts nothing, reads no test result, calls no model and
writes nothing: its judgment is the mark, the file, the flag and the first word of the reply,
so it fires at most once a turn and cannot loop. The session window, the stamp and the folder
are those of `guppi/ledger.py`. An error of its own after it has read the payload exits 2 with
the error on stderr and the advice to commit the session folder and call `/handoff` if Retro
has ended and `handoff.md` does not stand, before Retro too; an error while it reads the payload
exits 0 (case 555.3). Rule page: `vault/wiki/rules/rule-retro-onward.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import reply_text, session_dir, session_event_logs

MARK = "retro"
STOP = "STOP:"
REASON = (
    "onward: Retro has ended and handoff.md does not stand. Commit the session folder and "
    "call /handoff now. If a condition of vault/wiki/where-to-stop.md holds, open your reply "
    "with STOP: and ask the person instead."
)


def retro_marked(logs: list[tuple[str, str]], stamp: str) -> bool:
    """True when the mark `retro` of this stamp follows the first `hi` of this stamp that
    follows its first `session-start`, over the `(date, text)` logs in date order — the
    window `ledger.hi_moment` opens."""
    started = opened = False
    for _, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 3)
            if len(parts) < 4 or parts[0] != "-" or parts[2] != stamp:
                continue
            event = parts[3].split(" ", 1)[0]
            if event == "session-start":
                started = True
            elif event == "hi" and started:
                opened = True
            elif event == MARK and opened:
                return True
    return False


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
    except Exception as exc:  # noqa: BLE001 — no payload, no way to tell a re-fire (case 555.3)
        print(f"onward: not checked: {exc}", file=stderr)
        return 0
    if not payload or payload.get("stop_hook_active"):
        return 0
    try:
        if reply_text(payload).lstrip().startswith(STOP):
            return 0
        stamp = session_stamp(None, payload)
        folder = session_dir(project_dir, now, stamp)
        if folder is None or (folder / "handoff.md").exists():
            return 0
        if not retro_marked(session_event_logs(project_dir, now, stamp), stamp):
            return 0
        print(REASON, file=stderr)
        return 2
    except Exception as exc:  # noqa: BLE001 — shown to the agent, not swallowed (case 555.3)
        print(
            f"onward: not checked: {exc}. If Retro has ended and handoff.md does not stand, "
            "commit the session folder and call /handoff.",
            file=stderr,
        )
        return 2
