---
type: decision
case: "725"
status: archived
children: ["[[decision-case-725.1]]", "[[decision-case-725.2]]"]
origin: raw/2026-10-07/2114/ledger.md#case-725
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, session]
---

## Problem

A fix that adds a second behaviour to a ratified Case with no sub-cases has no step in the rule of `case-guppi`. A Case built again under a new number is refused by the check while the build it replaces stands in the plan. The rule also tells `case-guppi` to empty the file of a ratified Case that it leaves behind under the old number.

## Recommend

- **Where the second behaviour of a ratified Case with no sub-cases goes**
  - Recommended: (a) a Case of its own under a new number beside the ratified one, with no retiring mark; a build under a new number stays only for a fix that changes what the ratified Case already set.
  - Answer: agreed, (a).
- **Whether this Case also fixes the check's refusal of a build under a new number**
  - Recommended: (a) fix it here, in a sub-case: the check also leaves out each Case that a retiring mark on a ledger line of the answer's own file names, checked by a new Estimate.
  - Answer: agreed, (a).
- **What happens to the file left behind under the old number**
  - Recommended: (a) empty only the file of a Case with no ledger line; the file of a ratified Case stays, and the Criterion of `estimate-case-build-writes-the-case` is replaced.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/2114/ledger.md#case-725
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
