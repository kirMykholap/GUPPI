---
type: decision
case: "959"
status: current
create: ["[[estimate-sprint-keeps-one-live-page]]"]
update: ["[[entity-sprint]]"]
origin: raw/2026-10-31/0431/ledger.md#case-959
sprint: plugin
created: 2026-10-31
tags: [sprint, workflow]
---

## Problem

`entity-sprint` has `core: true` and no Estimate, so the cascade never sets it `built`, and `guppi ship` refuses for as long as it stands `draft`.

## Recommend

- **How does `entity-sprint` become `built`?**
  - Recommended: (a) an Estimate over all sprints, on something that holds across all sprints and that no single sprint page owns.
  - Answer: agreed, (a).
- **What does the Estimate of `entity-sprint` measure?**
  - Recommended: (a) at most one live sprint page, and each other sprint page in the archive, read on the real vault at the Retro of this session.
  - Answer: agreed, (a).

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-959
