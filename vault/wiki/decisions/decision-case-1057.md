---
type: decision
case: "1057"
status: current
children: ["[[decision-case-1057.1]]", "[[decision-case-1057.2]]", "[[decision-case-1057.3]]", "[[decision-case-1057.4]]", "[[decision-case-1057.5]]"]
origin: raw/2026-11-25/0816/ledger.md#case-1057
sprint: plugin
created: 2026-11-25
tags: [sprint, workflow, session, harness, librarian, case-build]
---

## Problem

A failed one-off Estimate counts as done on the sprint page, in `sprint.md` and at the close, but stays red in lint. The person decided that a failed reading is not done.

## Recommend

- **Does lint still flag a failed one-off Estimate of a sprint page?**
  - Recommended: (a) no flag for a failed one-off reading of a sprint page.
  - Answer: none of the options; a failed reading is not done, and the earlier decision is reversed; a one-off Estimate is worked on until it passes once, and `once` means one passed reading is enough, so it is not read again when pages change.
- **How does this one Estimate reach a passed reading?**
  - Recommended: (a) a new Criterion on a fresh build.
  - Answer: (a).
- **What does the close of the sprint do with a failed one-off Estimate?**
  - Recommended: (a) the close refuses it unless it is named.
  - Answer: (a).
- **Change**
  - Asked: findings of `/pre-spec` — step 4 of `rule-skill-sprint-close` and `estimate-sprint-close-takes-the-readings-in-groups` would be false after 1057.3; the `－` line of 1057.4 and its purpose went past the bound of `context`; the person agreed that the line holds for that Estimate alone and that the general rule goes into the Backlog of `entity-sprint-plugin`.
  - Taken: Case 1057.5 added; the `－` line of 1057.4 names this Estimate alone; 1057.1 adds the Backlog line.

## History

- 2026-11-25 created · raw/2026-11-25/0816/ledger.md#case-1057
