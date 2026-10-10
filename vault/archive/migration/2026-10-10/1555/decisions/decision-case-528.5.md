---
type: decision
case: "528.5"
status: archived
update: ["[[estimate-sprint-migration-leftovers-gone]]", "[[entity-sprint-migration]]"]
origin: raw/2026-09-29/2024/ledger.md#case-528.5
sprint: migration
created: 2026-09-29
tags: [sprint, git, workflow]
---

## Problem

`/hi` runs two commands against a remote that is not this project, and both fail at every session start. The note that keeps them off the Frontier goes away with the sprint. After the merge, `main` would pull from the product repository. The promise on the raw date folders asks that folders git does not track be gone, but `rule-raw-archive` keeps their logs on purpose.

## History

- 2026-09-30 created · raw/2026-09-29/2024/ledger.md#case-528.5
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
