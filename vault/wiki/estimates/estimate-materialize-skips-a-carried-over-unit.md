---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A unit holding carry.md is skipped, with one line on stdout
method: pytest in .guppi/tests/test_materialize.py, the tests of the skip
checked: 2026-09-24
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` reaches a unit whose folder holds `carry.md`.

Then:
The unit is skipped and one line naming it is printed on stdout; no `materialize.yaml` is written or extended for it.
**－** The unit is marked neither `applied` nor `failed`.

## Result

2026-09-24, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
