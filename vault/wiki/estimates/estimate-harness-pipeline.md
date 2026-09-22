---
type: estimate
kind: QA
status: passed
target: "[[rule-harness]]"
method: make test-harness over tests/test_render.py and tests/test_lint.py; the live reading of make lint by hand
checked: 2026-09-23
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Criterion

Given:
`make lint` is `render --check`, `sprint --check`, `glossary --check`, `guppi lint` (cases 227, 306.5); `rule-sprint` and `rule-glossary` are children of `rule-documentation`, not of `rule-harness`.
**＋** `estimate-harness-pipeline` is the old shape — a recut with `set.method`.

When:
`make lint` and `make test-harness` run; someone reads `rule-harness`.

Then:
The Purpose says: three rules belong to no phase of the session, and five more stand outside the pipeline — the renderer, the page `settings.json` is assembled from, lint — and with them the check of `rule-sprint` runs in `make lint`, in this order: the harness files against their pages, the sprint file against its page, the glossary file against its page, then the pages.
**＋** `make test-harness` is green; `make lint` exits 0 on the committed tree by its first three steps — the file checks, `render`, `sprint` and `glossary --check` silent; the fourth, `guppi lint`, is read by its own Estimates (case 311).

## Result

2026-09-23, make test-harness: 95 passed; uv run guppi render --check, guppi sprint --check, guppi glossary --check each exit 0 with no output; the Purpose of rule-harness read by hand: three rules in make lint in the order harness files, sprint file, glossary file, then the pages, five more outside the pipeline

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L74
- 2026-09-14 criterion: case 153 added · [[decision-case-153]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L3
- 2026-09-18 updated: the Criterion replaced whole — make lint with three steps (case 233.1) · [[decision-case-233.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L15
- 2026-09-22 updated: two lines of the Criterion — glossary --check the third step of make lint (case 306.5; pre-spec) · [[decision-case-306.5]]
- 2026-09-22 updated: the then line counts three file checks, glossary --check the third (case 311) · [[decision-case-311]]
- 2026-09-22 updated: the Purpose it reads names five rules outside the pipeline (case 323) · [[decision-case-323]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L60
