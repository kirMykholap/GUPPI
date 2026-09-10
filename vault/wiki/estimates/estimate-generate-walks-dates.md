---
type: estimate
kind: QA
status: passed
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
criterion: Without --date, generate walks every vault/raw/<date>/ with a materialize.yaml in date order and applies the unapplied entries of each; a date with nothing unapplied changes no page; --date keeps one date; a failure on one date is reported, the walk goes on, and the exit code is 1 at the end.
method: tests/test_generate.py with two dated folders; live, the librarian's first run
---

## Result

tests/test_generate.py 14 green with the three walk tests; live 2026-09-10: `uv run guppi generate` walked 2026-09-09 (old-harness failed, reported, the walk went on) and 2026-09-10, exit 1 at the end; the second run wrote 0 pages for the applied entries; the first live run also exposed three defects recorded as lessons below, none of them in the walk itself

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L95
