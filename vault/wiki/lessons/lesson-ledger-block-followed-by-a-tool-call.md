---
type: lesson
kind: error
root_cause: the Case protocol says a reply with a LEDGER block ends in that text and no tool call follows, and the agent loaded a deferred tool in the same reply instead of the next one
status: clustered
insight: "[[insight-ledger-hook-reads-only-the-final-text]]"
origin: raw/2026-09-16/2238/ledger.md#L48
sprint: migration
created: 2026-09-16
tags: [ledger, harness]
---

## Trigger

the reply that acknowledged case 222 carried its LEDGER block and then called ToolSearch to load ExitPlanMode; the Stop hook read nothing and the two decision lines were not written

## Root cause

the Case protocol says a reply with a LEDGER block ends in that text and no tool call follows, and the agent loaded a deferred tool in the same reply instead of the next one

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#L48
- 2026-09-17 updated: clustered by librarian under insight-ledger-hook-reads-only-the-final-text
