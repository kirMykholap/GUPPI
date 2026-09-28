---
type: decision
case: "495"
status: current
defer: ["[[rule-case-build]]"]
origin: raw/2026-09-28/2229/ledger.md#case-495
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Context

`estimate-case-build-writes-a-plain-round` was read `failed` in session 2000 (L25 of `raw/2026-09-28/2000/ledger.md`): Case 482 Q2 and Q4 gave no before, and Case 483 Q3 and Q4 gave only "After:". The rounds of this session showed the same gap in part: some options stated a before and an after, others did not.

## Problem

How `case-guppi` is made to state the before and the after of each option of a round, so that the Estimate passes.

## Deferred

### [[rule-case-build]]

Each option of a round of case-guppi states what is before and what is after, as estimate-case-build-writes-a-plain-round promises; read failed in session 2000 (L25), put off in session 2229

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-495
