---
type: decision
case: "728"
status: current
update: ["[[estimate-orchestration-defers-in-one-reply]]"]
origin: raw/2026-10-08/0050/ledger.md#case-728
sprint: migration
created: 2026-10-08
tags: [session, workflow, ledger]
---

## Problem

`estimate-orchestration-defers-in-one-reply` can be read only on a live reply that puts off a decision of another source than the sprint or the backlog. A session with no such reply leaves it `failed` with no fault seen, and keeps `rule-orchestration` in `draft`.

## Recommend

- **What the method reads**
  - Recommended: (b) read the new Render of `rule-orchestration` in the Spec at Retro of the session that changes the Estimate, as sibling Estimates do.
  - Answer: agreed, (b).
- **How the check leaves `failed`**
  - Recommended: (a) set it `passed` now by the person's decision, its Criterion written back unchanged, after the Render as it stands was read against the Criterion.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0050/ledger.md#case-728
