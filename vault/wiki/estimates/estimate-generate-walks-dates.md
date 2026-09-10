---
type: estimate
kind: QA
status: pending
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
criterion: Without --date, generate walks every vault/raw/<date>/ with a materialize.yaml in date order and applies the unapplied entries of each; a date with nothing unapplied changes no page; --date keeps one date; a failure on one date is reported, the walk goes on, and the exit code is 1 at the end.
method: tests/test_generate.py with two dated folders; live, the librarian's first run
---

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
