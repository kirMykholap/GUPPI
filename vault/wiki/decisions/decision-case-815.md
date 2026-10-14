---
type: decision
case: "815"
status: current
update: ["[[rule-clean-branch]]", "[[estimate-clean-branch-writes-a-clean-copy]]", "[[entity-sprint-plugin]]"]
origin: raw/2026-10-14/1536/ledger.md#case-815
sprint: plugin
created: 2026-10-14
tags: [ci, git, plugin, sprint, workflow]
---

## Problem

`guppi ship` never judges or cleans the prose around the example Case, so the pointers there reach the branch `prod`.

## Recommend

- **How the prose around the example Case gets cleaned**
  - Recommended: (a) drop both exceptions; the example Case and the example `then` block stay aside as fenced blocks, and the brackets in the prose are removed from the copy.
  - Answer: agreed, (a).
- **When the CI run is read again**
  - Recommended: (a) in this session, after Work Mode commits the fix: the owner pushes `plugin` and a tag `prod-2`, and the main agent reads the run against the unchanged Criterion.
  - Answer: agreed, (a).

## History

- 2026-10-14 created · raw/2026-10-14/1536/ledger.md#case-815
