---
type: decision
case: "747"
status: archived
update: ["[[estimate-case-check-sends-back-a-faulty-round]]"]
origin: raw/2026-10-09/0200/ledger.md#case-747
sprint: migration
created: 2026-10-09
tags: [hooks, harness, workflow]
---

## Problem

`estimate-case-check-sends-back-a-faulty-round` stands `failed` because its method waits for a faulty round that only chance produces. One line of its Criterion promises an act of the agent that no run of this check can show.

## Recommend

- **How should the failed reading of the round check be closed?**
  - Recommended: (b) read it again at the end of this session, with a staged run of the hook command on a copy of a real agent transcript ending in a faulty round, in place of the live part.
  - Answer: agreed, (b).
- **Does the promise keep the line that the agent answers again?**
  - Recommended: (a) drop that line from the promise; it ends at what the hook does, and the other lines stay word for word.
  - Answer: (a).

## History

- 2026-10-09 created · raw/2026-10-09/0200/ledger.md#case-747
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
