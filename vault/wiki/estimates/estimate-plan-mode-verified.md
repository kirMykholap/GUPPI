---
type: estimate
kind: QA
status: passed
target: rule-plan-mode
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Context

The children check one mechanism each. This is the cross-cutting one: that the two
verification points hold end to end, and that the second one recommends without
preventing the plan from being written.

## Criterion

A `create` for a page whose purpose the index already carries is flagged in the Case's `given` before ratification; the pre-task hook fires before the plan is written and the
plan is still written.

## Method

`make test-plan-mode`, the pipeline over `tests/test_spec.py` and `tests/test_pretask.py`;
the flagging is one live reading by hand, written into the estimate line.

## Result

at the approval of 11:40:48: ExitPlanMode passed after the pretask line of 11:26:29 in the window of the hi 10:29:12, and the plan was written; the pretask line is unstamped (`--------`) and counted by position — the lesson below

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
- 2026-09-10 updated: criterion names the Case's given, not now · raw/2026-09-10/ledger.md#case-40
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L38
