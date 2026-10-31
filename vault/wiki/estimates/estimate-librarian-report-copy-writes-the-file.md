---
type: estimate
kind: QA
status: passed
target: "[[rule-librarian-report-copy]]"
purpose: Whether the SubagentStop hook writes the last output of librarian-guppi, a text or a handback message, into report.md of the session folder, writes it again at a second fire, and writes nothing for another agent or with no transcript, output or folder
method: uv run --project .guppi guppi test, which runs .guppi/tests/test_libreport.py
origin: raw/2026-10-31/0431/ledger.md#case-965
sprint: plugin
created: 2026-10-31
tags: [hooks, harness, librarian]
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

2026-10-31, Retro of session 0431, uv run --project .guppi guppi test: 1830 passed, 6 skipped, 1 deselected, .guppi/tests/test_libreport.py 8 passed — the last text and the last handback message written whole, a file that stands replaced, a second fire written again, another agent writes nothing, no transcript, no output or no session folder writes nothing with one line on stderr

## History

- 2026-10-31 created · [[decision-case-965]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/0431/ledger.md#L39
