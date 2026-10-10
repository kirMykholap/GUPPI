---
type: decision
case: "774"
status: current
update: ["[[entity-sprint-plugin]]"]
origin: raw/2026-10-10/2350/ledger.md#case-774
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow]
---

## Problem

The current milestone of `entity-sprint-plugin` holds a note that can end only at the close of the sprint, which is already the last line of the last milestone, so the current milestone cannot close before the sprint does.

## Recommend

- **Where does the opening-and-close note go?**
  - Recommended: (a) remove the note; the close line of the last milestone and its Done-when check hold the close, and the other Case of this batch holds the known flaw of the opening.
  - Answer: agreed, (a).
- **Does the sprint Purpose still name the opening?**
  - Recommended: (b) change the Purpose and its `purpose` field to name only the close, since nothing in this sprint checks the opening.
  - Answer: agreed, (b).

## History

- 2026-10-11 created · raw/2026-10-10/2350/ledger.md#case-774
