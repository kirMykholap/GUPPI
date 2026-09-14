---
type: lesson
kind: knowledge
root_cause: the client enumerates .claude/agents/ at session start and does not re-read the folder on an Agent call; session E's counter-example most likely saw a file that already existed at its start; the librarian's render is the last step before its commit and every agent it renders is planned for from the next session
status: new
origin: raw/2026-09-14/1229/ledger.md#L29
sprint: migration
created: 2026-09-14
tags: [harness, hooks]
---

## Trigger

the probe of case 139.1 — a new agent file under .claude/agents/ written mid-session and dispatched at once was not found, and not found again after its body was replaced, Claude Code 2.1.228, no compaction

## Root cause

the client enumerates .claude/agents/ at session start and does not re-read the folder on an Agent call; session E's counter-example most likely saw a file that already existed at its start; the librarian's render is the last step before its commit and every agent it renders is planned for from the next session

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#L29
