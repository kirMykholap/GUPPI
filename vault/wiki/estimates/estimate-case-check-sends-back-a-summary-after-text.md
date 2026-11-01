---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of case-guppi sends back an answer that holds a Built line after a first line of other text, once per text, and leaves a summary that opens with Built, a round, a Fact answer and a Dropped answer alone
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k summary_after_text
origin: raw/2026-11-01/0141/ledger.md#case-981.1
sprint: plugin
created: 2026-11-01
tags: [hooks, harness, workflow]
---

## Criterion

When:
`case-guppi` stops after it wrote or edited a file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the `SubagentStop` hook `guppi casecheck --subagent` of `.guppi/guppi/casecheck.py`, registered in `.claude/settings.json`, reads its newest output.

Then:
An output whose first line that is not blank does not open with `**Built:**`, and that holds a later line opening with `**Built:**`, its indent set aside, gets a finding that quotes its first line and tells the agent to answer with the summary alone, its first line `**Built:**`, and the hook exits 2.
**＋** That finding is sent back in the same exit 2 as the findings on the file and on the `**Case:**` line.
**＋** A summary is known by `is_summary`, a round by `is_round` and a `**Fact:**` answer by `is_fact` of `.guppi/guppi/casecheck.py`, the one test of each that the other checks call, and a `**Dropped:**` answer by its first line that is not blank opening with one constant of that module.
**－** An output whose text an earlier output of the subagent already holds, trailing spaces aside, is not sent back again for it.
**－** An output whose first line that is not blank opens with `**Built:**`, a round, a `**Fact:**` answer, a `**Dropped:**` answer and an output with no line opening with `**Built:**` get no such finding.
**－** A subagent that wrote no file of `cases/` gets no such finding.

## Result

2026-11-01, Retro of session 0141: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k summary_after_text 8 passed, 234 deselected

## History

- 2026-11-01 created · [[decision-case-981.1]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/0141/ledger.md#L13
