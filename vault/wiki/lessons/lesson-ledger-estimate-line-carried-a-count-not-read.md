---
type: lesson
kind: error
root_cause: the reading's line was composed after one combined pytest run of three files; the per-file number was never printed, and the agent filled it in instead of running the file alone or naming the combined count only
status: clustered
insight: "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"
origin: raw/2026-09-20/0740/ledger.md#L15
sprint: migration
created: 2026-09-20
tags: [session, workflow, tests]
---

## Trigger

the estimate line of estimate-prespec-checks-the-plan at 09:10:20 said "72 green in the file"; pytest tests/test_prespec.py alone gives 52 — the 119 of the three files was split from memory, not read

## Root cause

the reading's line was composed after one combined pytest run of three files; the per-file number was never printed, and the agent filled it in instead of running the file alone or naming the combined count only

## History

- 2026-09-20 created · raw/2026-09-20/0740/ledger.md#L15
- 2026-09-23 updated: clustered by librarian: a fact signed on a check that does not cover it, with lesson-fact-asserted-from-a-partial-check · raw/2026-09-22/2046/ledger.md#L21
