---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the check of case-guppi sends back a summary that does not name the top-level Case as its file heads it
method: uv run pytest tests/test_casecheck.py -k summary_names_the_case
origin: raw/2026-10-05/1616/ledger.md#case-662.3
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
`case-guppi` stops after it wrote or edited a file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the `SubagentStop` hook `guppi casecheck --subagent` of `guppi/casecheck.py`, registered in `.claude/settings.json`, reads its newest output: a summary whose first line that is not blank opens with `**Built:**`.

Then:
A summary with no line `**Case:**` for the top-level Case of a file it wrote, or with one whose id and name differ from the heading `## Case N — name` of that file, gets a finding that names the file and the line to write, and the hook exits 2.
**＋** A summary whose `**Case:**` line gives the same id and the same name as the heading of each such file, trailing spaces aside, gets no finding on its line.
**＋** A finding on the summary is sent back in the same exit 2 as the findings on the file.
**＋** A summary sent back once is sent back again when the heading of its file has changed since, even if an earlier output holds its text.
**－** A summary whose text an earlier output of the subagent already holds, trailing spaces aside, is not sent back again for its line while the heading of its file is the same as when it was sent back.
**－** A round, a `**Fact:**` answer, and an answer with no file written are not judged for the line.

## History

- 2026-10-05 created · [[decision-case-662.3]]
