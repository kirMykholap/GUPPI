---
type: decision
case: "729"
status: current
update: ["[[rule-skill-hi]]", "[[estimate-hi-writes-frontier]]"]
origin: raw/2026-10-08/0050/ledger.md#case-729
sprint: migration
created: 2026-10-08
tags: [session, harness, workflow]
---

## Problem

A brief line that names the same item as a line of the sprint's current milestone becomes a second Frontier line, and the person has to close it by hand.

## Recommend

- **Where is the repeat stopped?**
  - Recommended: (a) `/hi` merges the lines (`rule-skill-hi`): it has both texts in its context, so one check there catches a repeat from any route.
  - Answer: agreed, (a).
- **Which repeats count?**
  - Recommended: (a) only an item of the current milestone, the repeat that happened.
  - Answer: agreed, (a).
- **What is left of the brief's line?**
  - Recommended: (a) nothing: the sprint line stands as it is, with its one source, so the closers do not change.
  - Answer: agreed, (a).
- **Which Estimate checks the merge?**
  - Recommended: (a) replace the Criterion of `estimate-hi-writes-frontier` with one line added, and keep its `method`.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0050/ledger.md#case-729
