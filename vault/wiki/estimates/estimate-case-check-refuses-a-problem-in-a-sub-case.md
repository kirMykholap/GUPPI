---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of each answer of case-guppi sends back a sub-case that carries its own problem
method: "pytest .guppi/tests/test_casecheck.py -k problem: a sub-case with problem, a parent without problem, a Case with no sub-cases"
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case that has sub-cases, and `uv run --project .guppi guppi casecheck --subagent` checks the chat form of each Case of the answer.

Then:
A sub-case of the answer that carries a `problem` section is a finding of that sub-case from `form_findings` of `.guppi/guppi/casecheck.py`, sent back to `case-guppi` and stored as any other finding.
**＋** A parent that lacks `problem` still gets its finding of a missing section.
**－** A Case with no sub-cases keeps its `problem` with no such finding.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
