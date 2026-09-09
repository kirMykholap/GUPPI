---
type: estimate
kind: QA
status: pending
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

A `create` for a page whose purpose the index already carries is flagged in the Case's
`now` before ratification; the pre-task hook fires before the plan is written and the
plan is still written.

## Method

`make test-plan-mode`, the pipeline over `tests/test_spec.py` and `tests/test_pretask.py`;
the flagging is one live reading by hand, written into the estimate line.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
