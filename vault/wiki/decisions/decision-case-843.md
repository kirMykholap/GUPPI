---
type: decision
case: "843"
status: current
update: ["[[estimate-plugin-install-writes-guppi-into-an-empty-project]]"]
supersedes: ["[[decision-case-831]]"]
origin: raw/2026-10-16/0104/ledger.md#case-843
sprint: plugin
created: 2026-10-16
tags: [plugin, harness]
---

## Problem

The promise of the plugin install was never read, since no local copy could be built with no tag `prod-x.y.z`; once Case 841 sets the tag, the page must come back to `pending` and be read by its `method`.

## Recommend

- **How does the Estimate come back for a new reading?**
  - Recommended: (a) set it to pending, with the same Criterion; one `update` also takes back the defer.
  - Answer: agreed, (a).
- **Does this reading share one install by hand with Cases 845 and 846?**
  - Recommended: (a) one copy and one first project for all three; this Case adds only the second project with its own `CLAUDE.md`.
  - Answer: agreed, (a).
- **Does the reading run before the tag is pushed to GitHub?**
  - Recommended: (a) before the push, so that a failed install can still stop the push.
  - Answer: agreed, (a).
- **Change**
  - Asked: Work Mode runs the tasks in Spec order, so a push in Case 841 would run before this reading; the person agreed that one `stop:` task of Case 846 holds every install by hand, this Case's second project included, and that the push moves to Case 850.
  - Taken: the `stop:` task of this Case is gone; the reading of the two projects against this Criterion moves into the `stop:` task of Case 846, which stands before the push of Case 850.

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-843
