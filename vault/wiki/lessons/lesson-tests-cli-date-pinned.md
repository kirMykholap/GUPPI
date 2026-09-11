---
type: lesson
kind: error
root_cause: the test helpers wrote the event log under a pinned TODAY of 2026-09-09 while cli.main reads the real clock, so the tests passed only on the day they were written; the three CLI tests now pass the local clock's date to the helpers
status: new
origin: raw/2026-09-10/ledger.md#L7
sprint: migration
created: 2026-09-10
---

## Trigger

`make test` on 2026-09-10 morning, the three CLI dispatch tests of test_event.py, test_ledger.py and test_pretask.py red with a missing raw/2026-09-09/event_log.md

## Root cause

the test helpers wrote the event log under a pinned TODAY of 2026-09-09 while cli.main reads the real clock, so the tests passed only on the day they were written; the three CLI tests now pass the local clock's date to the helpers

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L7
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
