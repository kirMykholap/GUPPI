---
type: estimate
kind: QA
status: passed
target: rule-materialize
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

`materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only. (The Problem of case 43, in English.)

## Criterion

Without --date, materialize walks every vault/raw/<date>/ with a ledger.md in date order, extends or writes each yaml, prints one line per date, and a ledger line written after its date's librarian commit is materialized by the next run on a later date; --date keeps one date; an error on one date stops the walk with exit 1.

### case 103.2

When:
`uv run guppi materialize` runs, with `--date` or without.

Then:
The unit of the walk is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`: its yaml `raw/<date>/<HHMM>/materialize.yaml`, its Spec `raw/<date>/<HHMM>/spec.md` alone, the `origin` of its entries `raw/<date>/<HHMM>/ledger.md#case-N` and `#L<n>`.
**＋** A date-level `raw/<date>/ledger.md` (the shape before this Case) is walked as today: the Specs of the date, `raw/<date>/materialize.yaml`, the date form of `origin`; on a date with both shapes the date-level one goes first, then the sessions in folder order.
**＋** `--date` walks the date-level ledger and every session of the date; stdout carries one line per yaml.
**＋** `estimate-materialize-walks-dates` gets a `### case 103.2` block, `pending`.

## Method

tests/test_materialize.py with two dated folders; live, the librarian's first run over 2026-09-09 and 2026-09-10

## Result

block 103.2: the librarian of session L walked the date-level unit raw/2026-09-13 (79 entries) and the session unit raw/2026-09-13/0652 (4 entries) in that order, the session's yaml and origin in its own folder; unit tests green

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L94
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.2 added · [[decision-case-103.2]]
- 2026-09-14 updated: Context added from the Problem of case 43 (case 112.4) · [[decision-case-112.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L42
