---
type: lesson
kind: error
root_cause: the run helper of test_generate.py called generate.run without now, so History and log lines took the real clock (case 47 dates them by the run) while the assertions used the pinned DATE; a test that passes only on the day it was written; fixed by pinning now in the helper
status: archived
insight: "[[insight-tests-clock-not-pinned]]"
origin: raw/2026-09-11/ledger.md#L71
sprint: migration
created: 2026-09-11
tags: [harness, tests]
---

## Trigger

on 2026-09-11 five tests of tests/test_generate.py failed on the committed tree before any change of session H, asserting a History line dated 2026-09-10 that the page carried as 2026-09-11

## Root cause

the run helper of test_generate.py called generate.run without now, so History and log lines took the real clock (case 47 dates them by the run) while the assertions used the pinned DATE; a test that passes only on the day it was written; fixed by pinning now in the helper

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#L71
- 2026-09-11 updated: clustered by librarian: a test reads the real clock, with lesson-tests-cli-date-pinned · raw/2026-09-11/ledger.md#L71
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
