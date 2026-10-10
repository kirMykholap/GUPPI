---
type: decision
case: "767"
status: current
update: ["[[estimate-sprint-plugin-ci-writes-a-clean-branch]]"]
origin: raw/2026-10-10/1913/ledger.md#case-767
sprint: plugin
created: 2026-10-10
tags: [sprint, ci, git]
---

## Problem

The check starts on a commit to `main`, which does not happen before the sprint closes, so the check cannot be read in time.

## Recommend

- **Who sets when this check is read**
  - Recommended: (a) the general rule of Case 764 decides it; the method stays, and this Case covers only the trigger.
  - Answer: agreed, (a).
- **What starts the check: a commit on `main`, or on the sprint branch**
  - Recommended: (a) the trigger names the branch `plugin`; the rest of the promise stays.
  - Answer: agreed, (a).
- **Change**
  - Asked: pre-spec found that `context` gave the Criterion of `estimate-skill-sprint-close-leads-the-closing-session` as wider than it is, with an "only" it does not hold; the person agreed to fix the wording.
  - Taken: `context` gives that Criterion as it stands: the merge task line is left unticked for the session that opens the next sprint, and it does not forbid `main` to move before the close.

## History

- 2026-10-10 created · raw/2026-10-10/1913/ledger.md#case-767
