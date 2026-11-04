---
type: decision
case: "1025"
status: current
children: ["[[decision-case-1025.1]]", "[[decision-case-1025.2]]"]
origin: raw/2026-11-04/0358/ledger.md#case-1025
sprint: plugin
created: 2026-11-04
tags: [sprint, case-build, session, workflow, harness]
---

## Problem

The rule does not say whether the root folder counts among the folders that hold a new file. A one-time check passed on the agent's own judgment that it does not, and the person judges that it does.

## Recommend

- **Does the root `.gitignore` count as an ignore file of a folder that holds the new files**
  - Recommended: (a) yes, the root counts; the check did not hold, and the Estimate is set `failed` by the person's decision.
  - Answer: agreed, (a).
- **Does the rule say that the root counts**
  - Recommended: (a) yes; the rule names every folder from the folder of the new file up to the root, and the Criterion of the lasting check is replaced with the same words.
  - Answer: agreed, (a).
- **Change**
  - Asked: at the finding 1.4 of `/pre-spec`, the person chose that the path search and the readers clause go up to the root as well, the root included, and not the ignore files alone.
  - Taken: Case 1025.2 replaces all three folder clauses of `rule-case-build` and the lines of its Criterion on them.
- **What the path search does at the root**
  - Recommended: (a) the path search stops below the root, since the root has no path; the ignore files and the readers take the root in.
  - Answer: agreed, (a).

## History

- 2026-11-04 created · raw/2026-11-04/0358/ledger.md#case-1025
