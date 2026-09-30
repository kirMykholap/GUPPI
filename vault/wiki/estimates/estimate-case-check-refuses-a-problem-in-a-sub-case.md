---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of each answer of case-guppi sends back a sub-case that carries its own problem
method: "pytest tests/test_casecheck.py -k problem: a sub-case with problem, a parent without problem, a Case with no sub-cases"
checked: 2026-09-30
origin: raw/2026-09-30/1306/ledger.md#case-544.4
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case that has sub-cases, and `uv run guppi casecheck --subagent` checks the chat form of each Case of the answer.

Then:
A sub-case of the answer that carries a `problem` section is a finding of that sub-case from `form_findings` of `guppi/casecheck.py`, sent back to `case-guppi` and stored as any other finding.
**＋** A parent that lacks `problem` still gets its finding of a missing section.
**－** A Case with no sub-cases keeps its `problem` with no such finding.

## Result

2026-09-30, uv run pytest tests/test_casecheck.py -k problem: 4 passed — a sub-case with problem sent back, a parent without problem still missing it, a Case with no sub-cases keeping its problem

## History

- 2026-09-30 created · [[decision-case-544.4]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L22
