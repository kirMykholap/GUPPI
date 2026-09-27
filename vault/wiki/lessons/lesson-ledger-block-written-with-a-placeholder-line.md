---
type: lesson
kind: error
root_cause: the main agent began the block before its lines were composed and left a stub to fill instead of finishing the block before sending it
status: new
origin: raw/2026-09-27/1819/ledger.md#L36
sprint: migration
created: 2026-09-27
tags: [session, ledger]
---

## Trigger

session 1819, the reply that recorded thirteen readings sent a LEDGER block whose second line was "- estimate-backlog-renders[passed] placeholder", then a corrected block in the same reply; the hook skipped the stub, which is no record line, and wrote the repeated first line once

## Root cause

the main agent began the block before its lines were composed and left a stub to fill instead of finishing the block before sending it

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#L36
