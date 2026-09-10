---
type: estimate
kind: QA
status: pending
target: rule-materialize
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
criterion: Without --date, materialize walks every vault/raw/<date>/ with a ledger.md in date order, extends or writes each yaml, prints one line per date, and a ledger line written after its date's librarian commit is materialized by the next run on a later date; --date keeps one date; an error on one date stops the walk with exit 1.
method: tests/test_materialize.py with two dated folders; live, the librarian's first run over 2026-09-09 and 2026-09-10
---

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
