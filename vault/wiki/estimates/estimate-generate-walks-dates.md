---
type: estimate
kind: QA
status: pending
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

Without --date, generate walks every vault/raw/<date>/ with a materialize.yaml in date order and applies the unapplied entries of each; a date with nothing unapplied changes no page; --date keeps one date; a failure on one date is reported, the walk goes on, and the exit code is 1 at the end.

### case 103.3

When:
`uv run guppi generate` runs, with `--date` or without.

Then:
Every `materialize.yaml` under `raw/` is applied: the date-level one of a date first, then the sessions of the date in folder order, dates ascending.
**＋** `estimate-generate-walks-dates` gets a `### case 103.3` block, `pending`.

## Method

tests/test_generate.py with two dated folders; live, the librarian's first run

## Result

tests/test_generate.py 14 green with the three walk tests; live 2026-09-10: `uv run guppi generate` walked 2026-09-09 (old-harness failed, reported, the walk went on) and 2026-09-10, exit 1 at the end; the second run wrote 0 pages for the applied entries; the first live run also exposed three defects recorded as lessons below, none of them in the walk itself

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L95
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.3 added · [[decision-case-103.3]]
