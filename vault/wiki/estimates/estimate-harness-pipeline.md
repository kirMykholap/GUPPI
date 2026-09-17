---
type: estimate
kind: QA
status: pending
target: "[[rule-harness]]"
method: make test-harness over tests/test_render.py and tests/test_lint.py; the live reading of make lint by hand
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Criterion

Given:
`make lint` is `render --check`, `sprint --check`, `guppi lint` (case 227); `rule-sprint` is a child of `rule-documentation`, not of `rule-harness`.
**＋** `estimate-harness-pipeline` is the old shape — a recut with `set.method`.

When:
`make lint` and `make test-harness` run; someone reads `rule-harness`.

Then:
The Purpose says: three rules belong to no phase of the session — the renderer, the page `settings.json` is assembled from, lint — and with them the check of `rule-sprint` runs in `make lint`, in this order: the harness files against their pages, the sprint file against its page, then the pages.
**＋** `make test-harness` is green; `make lint` exits 0 on the committed tree by its first two steps.

## Result

block 153: rule-harness Purpose carries the ratified text; make test-harness runs pytest over tests/test_render.py and tests/test_lint.py, 67 passed; make lint by hand 2026-09-15: render --check exit 0, then guppi lint 84 findings exit 1, in that order

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L74
- 2026-09-14 criterion: case 153 added · [[decision-case-153]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L3
- 2026-09-18 updated: the Criterion replaced whole — make lint with three steps (case 233.1) · [[decision-case-233.1]]
