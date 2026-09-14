---
type: lesson
kind: error
root_cause: the test helpers wrote the event log under a pinned TODAY of 2026-09-09 while cli.main reads the real clock, so the tests passed only on the day they were written; the three CLI tests now pass the local clock's date to the helpers
status: archived
insight: "[[insight-tests-clock-not-pinned]]"
origin: raw/2026-09-10/ledger.md#L7
sprint: migration
created: 2026-09-10
tags: [tests]
---

## Trigger

`make test` on 2026-09-10 morning, the three CLI dispatch tests of test_event.py, test_ledger.py and test_pretask.py red with a missing raw/2026-09-09/event_log.md

## Root cause

the test helpers wrote the event log under a pinned TODAY of 2026-09-09 while cli.main reads the real clock, so the tests passed only on the day they were written; the three CLI tests now pass the local clock's date to the helpers

## Insight

- [[insight-tests-clock-not-pinned]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L7
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-11 updated: clustered by librarian: a test reads the real clock, with lesson-tests-generate-history-date-unpinned · raw/2026-09-11/ledger.md#L71
- 2026-09-14 insight section derived
- 2026-09-14 updated: tags filled (case 113) · [[decision-case-113]]
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
