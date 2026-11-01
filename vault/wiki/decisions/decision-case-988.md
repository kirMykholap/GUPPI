---
type: decision
case: "988"
status: current
update: ["[[estimate-ratification-ledger-line-form]]"]
origin: raw/2026-11-01/1721/ledger.md#case-988
sprint: plugin
created: 2026-11-01
tags: [session, workflow, ledger]
---

## Problem

`rule-ratification` stays `draft`, and blocks the clean version, because its check of the ledger-line form waits for a lesson line with a new tag that no session has written, while the rest of that check can be read now and the new-tag form is already checked from the side of the hook.

## Recommend

- **What happens to the put-off removal of the sprint list**
  - Recommended: (a) leave it waiting: the put-off stays, and the removal waits for the first session after `plugin` closes.
  - Answer: agreed, (a).
- **How the check of the ledger-line form gets its reading**
  - Recommended: (a) drop the new-tag line from this check and read the rest at Retro, from the archived ledgers and their transcripts; the new-tag form stays checked by the hook's Estimate.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#case-988
