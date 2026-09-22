---
type: decision
case: "338.2"
status: current
update: ["[[estimate-prespec-checks-the-plan]]"]
origin: raw/2026-09-22/1724/ledger.md#case-338.2
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, tests]
---

## Context

Two Cases of this session change behaviour promised by pages they do not name. Case 335 narrows the `sprint` test to the source segment, while `estimate-prespec-binds-a-sprint-line` (`passed`) promises it "by the segments" twice — in its `When` and in a `－` line. Case 331 makes a `create` of an Estimate with no `method` a finding, while `estimate-prespec-checks-the-plan` carries a `－` line saying in so many words that no such finding exists. Both came from `/pre-spec`.
`estimate-prespec-checks-the-plan` is already changed in this Spec by 327 and 335, in lines 33 and 34 of its Criterion; the line changed here is 39, and the places do not meet. A pair inside `## Criterion` sends the page to `pending` by itself (case 296); the Criterion is not replaced whole.

## Problem

The promise stays written in the old shape while the code moves to the new. lint is silent on it; the cost falls on the next session, which reads the Criterion and measures by the wrong thing.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-338.2
