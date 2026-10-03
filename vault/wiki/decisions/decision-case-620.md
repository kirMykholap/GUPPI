---
type: decision
case: "620"
status: current
children: ["[[decision-case-620.1]]", "[[decision-case-620.2]]"]
origin: raw/2026-10-04/0004/ledger.md#case-620
sprint: migration
created: 2026-10-04
tags: [session, harness, workflow, sprint]
---

## Problem

A session that runs a conserved Spec has no valid mark for a Frontier line whose target that Spec already puts off. `rule-skill-hi` gives `defer case N`, but `guppi prespec` looks for Case N only in the session's own plan, which holds no Case. So the agent closed the line `work` by its own judgment, and `estimate-hi-takes-a-conserved-spec` failed.

## Recommend

- **Fix the failed check together with its cause, or on its own?**
  - Recommended: (a) one Case for both items. The check failed only because the rule has no mark for this line, so it cannot pass until the rule changes.
  - Answer: (a) one Case for both items.
- **Which mark closes a line whose put-off is already in the saved plan?**
  - Recommended: (a) keep `defer case N` and let N point into the conserved Spec that the plan's title line names. `guppi prespec` looks there through the function `/box` already uses.
  - Answer: Agreed with the recommendation.
- **Does this Case also close the pattern that groups the two lessons?**
  - Recommended: (a) mark the insight `actioned` and addressed by this Case, since both of its cases then have a mark.
  - Answer: Agreed with the recommendation.
- **Should the agent also stop when a line fits no mark?**
  - Recommended: (b) leave the stop out of this Case. Every known case has a mark, and a recurrence reopens the insight.
  - Answer: Agreed with the recommendation.

## History

- 2026-10-04 created · raw/2026-10-04/0004/ledger.md#case-620
