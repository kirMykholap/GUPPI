---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

`materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only. (The Problem of case 43, in English.)

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

block 103.3: the librarian of session L applied raw/2026-09-13/materialize.yaml (107 pages) then raw/2026-09-13/0652/materialize.yaml (8 pages), exit 0, stderr empty; unit tests green

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L95
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.3 added · [[decision-case-103.3]]
- 2026-09-14 updated: Context added from the Problem of case 43 (case 112.4) · [[decision-case-112.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L43
