---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: lint counts the Estimates still in the shape before case 193 in one line, and prints none at zero
method: uv run pytest tests/test_lint.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-401.5
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` reads the live Estimates under `vault/wiki/estimates/`.

Then:
One line `estimates: unmigrated: <N> pages in the shape before case 193` — `page` when N is 1 — N the Estimates without a `method` field, or with `## Context`, `## Method` or a `### case N` block under `## Criterion`.
**＋** At zero there is no line.

## Result

2026-09-24, `uv run pytest tests/test_lint.py`: 69 passed

## History

- 2026-09-25 created · [[decision-case-401.5]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L46
