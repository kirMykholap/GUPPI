---
type: decision
case: "74"
status: current
update: ["[[rule-pretask]]"]
supersedes: ["[[decision-case-68]]"]
origin: raw/2026-09-12/ledger.md#case-74
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness]
---

## Context

Case 59.3 says `guppi pretask --check` reports "a Case that has decision lines and no
`tasks` block". At the first live run the three deferred decisions of session I (Cases
63–65) were reported: a defer has lines and no work, so no `tasks` block. The code
exempts a Case whose lines are all `defer` (commit `2b7dd42`); the ratified wording does
not. Deferred as Case 68.

## Problem

The Render of `rule-pretask` and the criterion of `estimate-pretask-reconciles` say "a
Case with decision lines". The code says "a Case with a line other than `defer`". One
of them yields.

## Given

`rule-pretask` Render: "for every ratified Case without a `tasks` block"; `deferred_by:
[decision-case-68]`. `guppi/pretask.py` `check_tasks`: `with_work` is the Cases with a
line whose kind is not `defer`; the finding "decision lines and no tasks block" fires
for those only, with the comment "a defer-only Case has no work (case 59.5)".
**＋** `estimate-pretask-reconciles` Criterion: "a Case with decision lines and no
`tasks` block ... are each one finding"; `pending` since 72.5; its Criterion gains this
Case's block by 72.3 and the `### case 68` removal finds nothing to remove.
**＋** Case 59.5: a short-form defer has `context`, `problem` and a `defer` block only.
**＋** 72.5 and 73.4 update the same Render this session; the three `replace` items
touch different sentences.
**－** A Case that mixes a `defer` with another kind still needs its `tasks` block.

## Criterion

- [[estimate-pretask-reconciles]] § case 74

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-74
