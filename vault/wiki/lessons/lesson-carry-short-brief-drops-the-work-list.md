---
type: lesson
kind: error
root_cause: step 1 of rule-carry-over (case 451.9) leaves Readings due and Next session out of the short brief on the claim that make lint lists the pending Estimates again, while /hi takes its Work list only from the Next session of the brief and reads neither make lint nor the Frontier of the previous session.
status: clustered
insight: "[[insight-session-vault-knowledge-not-loaded]]"
origin: raw/2026-09-30/0138/ledger.md#L1
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Trigger

the /carry of session 2024 (commit 8e4c918) wrote brief.md in the short shape; the /hi of session 2026-09-30/0138 assembled no Work list — the 38 open W lines of the 2024 Frontier and the Readings due of the brief of 1c196e8 (5 failed, 36 pending) stood on no list the Frontier reads, and the person found it.

## Root cause

step 1 of rule-carry-over (case 451.9) leaves Readings due and Next session out of the short brief on the claim that make lint lists the pending Estimates again, while /hi takes its Work list only from the Next session of the brief and reads neither make lint nor the Frontier of the previous session.

## History

- 2026-09-30 created · raw/2026-09-30/0138/ledger.md#L1
- 2026-09-30 updated: clustered under insight-session-vault-knowledge-not-loaded (synthesis) · raw/2026-09-30/0138/ledger.md#L1
