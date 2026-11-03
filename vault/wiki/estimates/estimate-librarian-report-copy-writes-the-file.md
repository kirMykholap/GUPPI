---
type: estimate
kind: QA
status: passed
target: "[[rule-librarian-report-copy]]"
purpose: Whether the SubagentStop hook writes the last output of librarian-guppi, a text or a handback message, into report.md of the session folder, writes it again at a second fire, and writes nothing for another agent or with no transcript, output or folder
method: uv run --project .guppi guppi test, which runs .guppi/tests/test_libreport.py
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, librarian]
core: true
---

## Criterion

When:
`SubagentStop` fires at the end of an agent, and `uv run --project .guppi guppi libreport` of `.guppi/guppi/libreport.py` reads its payload.

Then:
For `librarian-guppi`, the hook writes the last output of the agent in its `agent_transcript_path`, a text or the `message` of a `SubagentHandback` call, whole into `report.md` in the session folder `vault/raw/<hi date>/<hi HHMM>/`, and replaces a file that stands there.
**＋** A second `SubagentStop` of the same run writes the file again from the last output at that moment.
**＋** The hook reads the outputs by `subagent_outputs` of `.guppi/guppi/casecheck.py` and the folder by `session_dir` of `.guppi/guppi/ledger.py`.
**－** For any other agent, the hook writes nothing.
**－** The hook blocks nothing and exits 0; with no readable transcript, no output or no session folder it writes nothing and prints one line on stderr.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
