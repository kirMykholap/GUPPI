---
type: lesson
kind: knowledge
root_cause: a SendMessage to a case-guppi that has finished resumes it in the background and returns only "Resuming agent"; its answer comes back after the turn has ended as a user record with origin.kind task-notification, which opens a turn of its own, so each answer forces one reply of the main agent and the quiet wait of case 561.2 cannot be wholly silent, while an Agent call's answer stands in its tool_result inside the turn
status: new
source: the transcript of session 2356, records 145 and 337, read by a script for case 562
origin: raw/2026-09-30/2356/ledger.md#L46
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Trigger

measuring where an answer of case-guppi stands in the transcript before the round check of case 562 was written

## Root cause

a SendMessage to a case-guppi that has finished resumes it in the background and returns only "Resuming agent"; its answer comes back after the turn has ended as a user record with origin.kind task-notification, which opens a turn of its own, so each answer forces one reply of the main agent and the quiet wait of case 561.2 cannot be wholly silent, while an Agent call's answer stands in its tool_result inside the turn

## History

- 2026-10-01 created · raw/2026-09-30/2356/ledger.md#L46
