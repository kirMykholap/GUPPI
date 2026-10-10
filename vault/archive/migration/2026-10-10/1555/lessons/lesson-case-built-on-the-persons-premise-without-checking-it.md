---
type: lesson
kind: error
root_cause: a remark from the person was taken as a finding instead of as a report to verify, so the agent searched for a defect that would make the remark true rather than reading the record of what happened; the event log holds every tool call of the day and was one read away.
status: archived
origin: raw/2026-09-22/2046/ledger.md#L16
sprint: migration
created: 2026-09-22
tags: [workflow, harness]
---

## Trigger

the person said that `/carry` does not name the brief's path and that the agent greps for it; the agent built Case 347 on that premise without opening the event log of the day, where the call at 20:43:03 shows the grep ran over `.claude/agents/librarian-guppi.md`, while step 1 of the skill names `vault/wiki/brief.md` in full.

## Root cause

a remark from the person was taken as a finding instead of as a report to verify, so the agent searched for a defect that would make the remark true rather than reading the record of what happened; the event log holds every tool call of the day and was one read away.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L16
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
