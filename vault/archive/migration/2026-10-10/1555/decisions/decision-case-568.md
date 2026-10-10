---
type: decision
case: "568"
status: archived
update: ["[[rule-case-build]]", "[[rule-case-protocol]]", "[[estimate-case-build-records-the-rounds-in-recommend]]"]
origin: raw/2026-10-01/1237/ledger.md#case-568
sprint: migration
created: 2026-10-01
tags: [session, workflow, harness, ledger]
---

## Problem

The rule that an item whose answer changed only one sub-case must stand under that sub-case asks `case-guppi` for a judgment it keeps missing, and the person sees no harm in the item standing on the parent. The question is where an item of `recommend` may stand in a Case with sub-cases.

## Recommend

- **How do we stop answers being filed in the wrong place?**
  - Recommended: (b) every question item goes on the parent, a sub-case carries only the Change items asked on it, and a script can refuse a question title under a sub-case.
  - Answer: outside the options: simply allow `recommend` to be written on the parent, since the person sees no problem in it.
- **What happens to the two Cases already ratified with misplaced entries?**
  - Recommended: (a) leave them as they are; under the new rule nothing in them is misplaced.
  - Answer: (a). Not answered in the first round, asked again.
- **Must question entries stand on the parent, or may they stand there?**
  - Recommended: (a) must, with no script check: every question item on the parent, a sub-case only with the Change items asked on it.
  - Answer: (c) may: an item stands on the parent or under the one sub-case its answer changed, as `case-guppi` judges, and no script checks the place.

## History

- 2026-10-01 created · raw/2026-10-01/1237/ledger.md#case-568
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
