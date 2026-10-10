---
type: decision
case: "753"
status: current
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-10-10/1508/ledger.md#case-753
sprint: migration
created: 2026-10-10
tags: [sprint, workflow]
---

## Problem

The milestone item `rule-sprint-close` cannot be ticked before the sprint closes, because its last three Estimates can only be read at the close or after it. So it comes back at every `/hi`, and the closing session must put it off again.

## Recommend

- **What closing C1 does to the sprint page**
  - Recommended: (a) take the item out of Slice 5; the rule's content is finished, and the closing Case handles its waiting checks like any other unread check.
  - Answer: agreed with the recommendation, (a).
- **Who decides what happens to the three waiting checks**
  - Recommended: (a) leave it to the closing Case, which sorts the checks into groups and picks carry or archive-unread for each one.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-10 created · raw/2026-10-10/1508/ledger.md#case-753
