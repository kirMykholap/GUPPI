"""`guppi libreport` — the `SubagentStop` hook that keeps the librarian's report in the
session folder (`rule-librarian-report-copy`).

Claude Code refused the librarian's `Write` of `report.md` with the message that subagents
return findings as text and write no report files, so the file is written here, by
the hook's own code, and no `Write` call of a subagent is made. For a payload that names
`librarian-guppi` as `agent_type`, the hook takes the outputs of the agent in its
`agent_transcript_path` by `subagent_outputs` of `.guppi/guppi/casecheck.py` — each text
block and the `message` of each `SubagentHandback` call — and writes the last one that holds
text whole into `report.md` of the session folder `vault/raw/<hi date>/<hi HHMM>/`, which
`session_dir` of `.guppi/guppi/ledger.py` gives from the `hi` line of the session's stamp. A
file that stands there is replaced: `SubagentStop` may fire twice in one run, before and
after the handback, and each fire writes the file again from the last output at that moment.

For any other agent the hook writes nothing and prints nothing. It blocks nothing and exits 0;
with no readable transcript, no output or no session folder it writes nothing and prints one
line on stderr, and so does an error. Rule page:
`vault/wiki/rules/rule-librarian-report-copy.md`.
"""

import sys
from datetime import datetime
from pathlib import Path

from guppi.casecheck import subagent_outputs
from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import session_dir

AGENT = "librarian-guppi"
REPORT = "report.md"


def last_output(payload: dict) -> str | None:
    """The last output of the subagent that holds text; "" when it gave none, None when its
    transcript is not readable."""
    texts = subagent_outputs(payload)
    if texts is None:
        return None
    held = [text for text in texts if text.strip()]
    return held[-1] if held else ""


def copy(payload: dict, project_dir: Path, now, stderr) -> int:
    if payload.get("agent_type") != AGENT:
        return 0
    text = last_output(payload)
    if text is None:
        print(
            "libreport: the transcript of the librarian is not readable, no report.md written",
            file=stderr,
        )
        return 0
    if not text:
        print("libreport: the librarian gave no output, no report.md written", file=stderr)
        return 0
    folder = session_dir(project_dir, now, session_stamp(None, payload))
    if folder is None or not folder.is_dir():
        print("libreport: no session folder, no report.md written", file=stderr)
        return 0
    path = folder / REPORT
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    return 0


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("libreport: payload not readable, no report.md written", file=stderr)
            return 0
        return copy(payload, project_dir, now, stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the agent's end
        print(f"libreport: no report.md written: {exc}", file=stderr)
        return 0
