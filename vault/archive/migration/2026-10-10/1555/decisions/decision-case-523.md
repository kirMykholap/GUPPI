---
type: decision
case: "523"
status: archived
update: ["[[rule-case-protocol]]", "[[estimate-orchestration-defers-in-one-reply]]"]
supersedes: ["[[decision-case-518]]"]
origin: raw/2026-09-29/1753/ledger.md#case-523
sprint: migration
created: 2026-09-29
tags: [session, workflow, ledger]
---

## Problem

The rule on the question after a defer is under a defer, and its Estimate reads as failed. The rule text was right, and the one wrong question came from a gap that is now closed. The `method` of the Estimate also lets a defer that leaves Cases lines open count as a reading, and such a defer never tests the question that failed.

## History

- 2026-09-29 created · raw/2026-09-29/1753/ledger.md#case-523
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
