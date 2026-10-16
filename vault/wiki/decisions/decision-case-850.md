---
type: decision
case: "850"
status: current
update: ["[[estimate-sprint-plugin-ci-writes-a-clean-branch]]"]
origin: raw/2026-10-16/0104/ledger.md#case-850
sprint: plugin
created: 2026-10-16
tags: [sprint, ci, git]
---

## Problem

The push of the tag would run before the install readings that the person wants first, because Work Mode runs the tasks in the order of the Spec.

## Recommend

- **How should the line name the tag?**
  - Recommended: (a) only the form `prod-x.y.z`, with no number, in the milestone line that Case 847 sets.
  - Answer: agreed, (a).
- **What should the line list as the work left?**
  - Recommended: (a) the tag, the CI run read by its Estimate, and the draft core pages that stop the run.
  - Answer: agreed, (a).
- **Which check confirms this change?**
  - Recommended: (a) the existing `estimate-sprint-plugin-ci-writes-a-clean-branch`, its Criterion unchanged.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the person agreed that the `stop:` task that pushes `prod-0.2.0` moves out of Case 841 and runs after the one `stop:` task of Case 846 for every install by hand, on the person's word.
  - Taken: the push stands in this Case, beside Case 847 and after it, since Case 847 already has a decision line; Case 847 stays as it is.

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-850
