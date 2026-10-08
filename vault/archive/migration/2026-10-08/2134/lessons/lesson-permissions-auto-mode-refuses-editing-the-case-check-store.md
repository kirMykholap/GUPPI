---
type: lesson
kind: knowledge
root_cause: the auto mode classifier reads a change of a check's own state file as tampering with an audit record, so the agent cannot clear a stale store entry even on the person's word; only the person, or a permission rule, can
status: archived
source: Claude Code 2.1.292 auto mode classifier, session 1804
insight: "[[insight-permissions-classifier-weighs-the-rules-not-the-persons-word]]"
origin: raw/2026-10-07/1804/ledger.md#L30
sprint: migration
created: 2026-10-07
tags: [harness]
---

## Trigger

the person chose to remove the stale entries 713.1 and 713.2 from adaptive-gathering-dewdrop.checked.json; the script that does it was denied as Logging/Audit Tampering and did not run

## Root cause

the auto mode classifier reads a change of a check's own state file as tampering with an audit record, so the agent cannot clear a stale store entry even on the person's word; only the person, or a permission rule, can

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#L30
- 2026-10-07 updated: clustered under insight-permissions-classifier-weighs-the-rules-not-the-persons-word (synthesis) · raw/2026-10-07/1804/ledger.md#L30
- 2026-10-08 archived · insight actioned
- 2026-10-08 archived · cleanup
