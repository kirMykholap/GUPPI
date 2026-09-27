---
type: lesson
kind: error
root_cause: the tests of case 464 asserted that generate prints "applied by hand" for no entry by writing the phrase into tests/, and the new test text was not checked against the grep of an Estimate that forbids the phrase in the tree; the asserts were removed and the grep is empty again
status: new
origin: raw/2026-09-27/2050/ledger.md#L33
sprint: migration
created: 2026-09-27
tags: [harness]
---

## Trigger

the reading of estimate-sprint-migration-rule-class-files-dissolved in session 2050 failed: its method greps guppi/ and tests/ for "applied by hand" and found three asserts of the new tests of case 464 in tests/test_generate.py

## Root cause

the tests of case 464 asserted that generate prints "applied by hand" for no entry by writing the phrase into tests/, and the new test text was not checked against the grep of an Estimate that forbids the phrase in the tree; the asserts were removed and the grep is empty again

## History

- 2026-09-27 created · raw/2026-09-27/2050/ledger.md#L33
