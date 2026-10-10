---
type: lesson
kind: error
root_cause: the agent wrote a text of its own in the turn before the dispatch, and the check judges every text of the turn, so the step its refusal names, the round shown again with nothing before it, cannot clear it
status: archived
origin: raw/2026-10-06/1448/ledger.md#L2
sprint: migration
created: 2026-10-06
tags: [hooks, harness]
---

## Trigger

the main agent wrote "Creating the plan file, then dispatching case-guppi for Case 691." before the dispatch, and the round it showed after was refused three times by the Stop check of rule-case-check before the fourth showing passed by LIMIT

## Root cause

the agent wrote a text of its own in the turn before the dispatch, and the check judges every text of the turn, so the step its refusal names, the round shown again with nothing before it, cannot clear it

## History

- 2026-10-07 created · raw/2026-10-06/1448/ledger.md#L2
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
