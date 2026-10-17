---
type: decision
case: "879"
status: current
children: ["[[decision-case-879.1]]", "[[decision-case-879.2]]", "[[decision-case-879.3]]", "[[decision-case-879.4]]"]
origin: raw/2026-10-17/1805/ledger.md#case-879
sprint: plugin
created: 2026-10-17
tags: [hooks, harness, workflow, session]
---

## Problem

The Spec hook reads every Case whose lines are all put-offs as the short form, so a Case that `case-guppi` built in full with only put-offs is refused, or reaches the Spec only in the main agent's words.

## Recommend

- **Which side changes so that a full Case made only of put-offs reaches the Spec?**
  - Recommended: (a) the Spec hook changes.
  - Answer: agreed, (a).
- **How does the hook tell a full Case made only of put-offs from a short put-off?**
  - Recommended: (a) by what the reply shows.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) a new Estimate for the full Case made only of put-offs, and the Criterion of `estimate-spec-write-writes-a-defer` replaced.
  - Answer: agreed, (a).
- **What happens to the two other checks that say a Case made only of put-offs has no file?**
  - Recommended: (a) replace both Criteria too.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-17/1805/ledger.md#case-879
