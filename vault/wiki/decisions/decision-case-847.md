---
type: decision
case: "847"
status: current
update: ["[[entity-sprint-plugin]]"]
supersedes: ["[[decision-case-830]]"]
origin: raw/2026-10-16/0104/ledger.md#case-847
sprint: plugin
created: 2026-10-16
tags: [sprint, workflow]
---

## Problem

The milestone line of `entity-sprint-plugin` waits for a fix that is already done, and for a tag `prod-2` that `guppi ship` does not read. It does not say that the draft core pages still stop the run.

## Recommend

- **How should the line name the tag?**
  - Recommended: (a) only the form `prod-x.y.z`, with no number.
  - Answer: agreed, (a).
- **What should the line list as the work left?**
  - Recommended: (a) the tag, the CI run read by its Estimate, and the draft core pages that stop the run.
  - Answer: agreed, (a).
- **Which check confirms this change?**
  - Recommended: (a) the existing `estimate-sprint-plugin-ci-writes-a-clean-branch`, its Criterion unchanged.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-847
