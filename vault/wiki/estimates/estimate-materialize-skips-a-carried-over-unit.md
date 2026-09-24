---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A unit holding carry.md is skipped, with one line on stdout
method: pytest in tests/test_materialize.py, the tests of the skip
checked: 2026-09-24
origin: raw/2026-09-16/1034/ledger.md#case-190.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi materialize` reaches a unit whose folder holds `carry.md`.

Then:
The unit is skipped and one line naming it is printed on stdout; no `materialize.yaml` is written or extended for it.
**－** The unit is marked neither `applied` nor `failed`.

## Result

2026-09-24, `uv run pytest tests/test_materialize.py`: 75 passed

## History

- 2026-09-16 created · [[decision-case-190.3]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L34
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-25 updated: the Criterion replaced whole — the Given of case 190.3 out by the model of case 378 (case 401.7) · [[decision-case-401.7]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L32
