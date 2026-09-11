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

## Criterion

Without --date, materialize walks every vault/raw/<date>/ with a ledger.md in date order, extends or writes each yaml, prints one line per date, and a ledger line written after its date's librarian commit is materialized by the next run on a later date; --date keeps one date; an error on one date stops the walk with exit 1.

## Method

tests/test_materialize.py with two dated folders; live, the librarian's first run over 2026-09-09 and 2026-09-10

## Result

tests/test_materialize.py 15 green with the three walk tests (order, --date, an error stops the walk); live 2026-09-10: the librarian's `uv run guppi materialize` at 11:48:27 walked 2026-09-09 (+0 entries) and 2026-09-10 (+8), one stdout line per date, exit 0; the pickup of a line after a later date's run is covered by the test only, both sessions of today share the date

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L94
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
