---
type: decision
case: "841"
status: current
update: ["[[estimate-sprint-plugin-ci-writes-a-clean-branch]]"]
origin: raw/2026-10-16/0104/ledger.md#case-841
sprint: plugin
created: 2026-10-16
tags: [sprint, ci, git]
---

## Problem

No tag `prod-x.y.z` stands in the history of `plugin`, so no clean version is built, locally or by CI. The question is which tag is placed, when and where, and where its push stands while the draft pages with `core: true` still stop the build of `prod`.

## Recommend

- **Which name does the tag take?**
  - Recommended: (a) `prod-0.2.0`, the name the open task and `rule-clean-branch` already use.
  - Answer: agreed, (a).
- **When and on which commit is the tag placed?**
  - Recommended: (a) the first task of Work Mode, on the last commit of `plugin` at that moment, local only.
  - Answer: agreed, (a).
- **What does the push of the tag do in this session?**
  - Recommended: (a) a `stop:` task in this Work Mode: the tag is pushed on the person's word; the run fails on the draft pages and writes nothing to `prod`, and the Estimate stays `pending`.
  - Answer: agreed, (a).
- **Which Estimate checks this Case?**
  - Recommended: (a) `estimate-sprint-plugin-ci-writes-a-clean-branch` stands as it is.
  - Answer: agreed, (a).
- **Are the seven draft pages with `core: true` part of this Case?**
  - Recommended: (a) left out: this Case sets only the tag and its push.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, move the `stop:` task of the push out of this Case into Case 847, since Work Mode runs the tasks in the order of the Spec and Case 843 reads before the push; and name `estimate-clean-branch-ships-neutral-texts`, whose reading the tag opens.
  - Taken: the push left this Case and stands in Case 850, a new Case after the install readings; this Case keeps the local tag as the first task of Work Mode, and `context` names the Estimate that the Retro of this session reads by its `method`.

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-841
