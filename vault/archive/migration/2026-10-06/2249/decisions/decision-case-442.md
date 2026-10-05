---
type: decision
case: "442"
status: archived
defer: ["[[rule-ledger-write]]"]
superseded_by: ["[[decision-case-682.1]]"]
origin: raw/2026-09-26/1745/ledger.md#case-442
sprint: migration
created: 2026-09-26
tags: [session, hooks, harness, ledger]
---

## Context

A lesson line in the ledger must carry the mark `{addressed_by:case N}` when it is written after the Case of this session that closed its cause. When the lesson is written before the Case, the decision line of that Case carries the mark `{addresses:…}` (case 379). Today nothing makes the agent set the mark: the ledger hook writes the line without it. In session 1337 the line `lesson-hooks-subagentstop-fires-before-and-after-the-handback` stayed with no mark, although Case 434 closed its cause. The librarian then does not link the lesson to the decision, and the lesson stays `new`.

## Problem

No check finds a lesson line with no mark when a Case of the same session closed its cause. How to catch such a missing mark? The decision is deferred.

## Deferred

### [[rule-ledger-write]]

A lesson line whose cause a Case of the same session closed carries addressed_by or the decision line carries addresses; nothing catches a missing mark

## History

- 2026-09-26 created · raw/2026-09-26/1745/ledger.md#case-442
- 2026-10-06 superseded by decision-case-682.1 · [[decision-case-682.1]]
- 2026-10-06 archived · superseded
- 2026-10-06 archived · cleanup
