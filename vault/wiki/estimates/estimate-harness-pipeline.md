---
type: estimate
kind: QA
status: pending
target: "[[rule-harness]]"
method: make test-harness over tests/test_render.py and tests/test_lint.py; the live reading of make lint by hand
checked: 2026-09-23
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Criterion

When:
`make lint` and `make test-harness` run, and someone reads the Purpose of `rule-harness`.

Then:
The Purpose says: three rules belong to no phase of the session — the renderer, the page `settings.json` is assembled from, lint — and with them the check of `rule-sprint` runs in `make lint`, in this order: the harness files against their pages, the sprint file against its page, the glossary file against its page, then the pages.
**＋** The Purpose names eight more rules that belong to it and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History.
**＋** `make test-harness` is green; the first three steps of `make lint` — `render`, `sprint` and `glossary --check` — exit 0 with no output on the committed tree; the fourth, `guppi lint`, is read by its own Estimates.

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
- 2026-09-24 updated: the Criterion replaced whole — seven rules outside the pipeline, no Given (case 392.3) · [[decision-case-392.3]]
- 2026-09-25 updated: the Criterion replaced whole — eight rules outside the pipeline, the hooks of rule-page-read among them (case 420.2) · [[decision-case-420.2]]
