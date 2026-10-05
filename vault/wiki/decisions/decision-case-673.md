---
type: decision
case: "673"
status: current
update: ["[[rule-orchestration]]"]
origin: raw/2026-10-05/2103/ledger.md#case-673
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

A Case ratified again with a mark added to a decision line leaves two lines for one decision in the ledger. The rule of `generate` says that this is expected and harmless, but the main agent does not read that rule. So the handoff reports the pair as a gap, and the pair comes back as a Frontier item.

## Recommend

- **Whether anything changes for a ledger line written again with a mark added**
  - Recommended: (a) one sentence in the orchestration file the main agent loads: the marked line stands beside the first, the page changes once, and the mark still retires the older decision; no new check.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/2103/ledger.md#case-673
