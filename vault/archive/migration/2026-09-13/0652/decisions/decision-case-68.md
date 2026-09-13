---
type: decision
case: "68"
status: archived
defer: [rule-pretask]
superseded_by: [decision-case-74]
origin: raw/2026-09-12/ledger.md#case-68
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness]
---

## Context

Case 59.3 says `guppi pretask --check` reports "a Case that has decision lines and no
`tasks` block". At the first live run the three deferred decisions of the session (Cases
63–65) were reported: a defer has lines and no work, so no `tasks` block. The code exempts
a Case whose lines are all `defer` (commit 2b7dd42); the ratified wording does not.

## Problem

The Render of `rule-pretask` and the criterion of `estimate-pretask-reconciles` will be
generated from the wording of 59.3 and say "a Case with decision lines". One word: "a Case
with a line other than `defer`". An `update` of both; the next Plan Mode.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-68
- 2026-09-12 superseded by decision-case-74 · [[decision-case-74]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
