---
type: lesson
kind: knowledge
root_cause: the ledger only grows and the hook appends no line it holds; only a supersedes block retires an entry, so a ratified sub-case that drops an item takes a new id whose line carries supersedes of the old one, as 445.7 did
status: clustered
source: vault/wiki/case-schema.md
insight: "[[insight-ledger-ratified-line-never-withdrawn]]"
origin: raw/2026-09-26/2300/ledger.md#L34
sprint: migration
created: 2026-09-26
tags: [workflow, session]
---

## Trigger

the rebuilt 445.5 dropped the create of estimate-skill-hi-opens-only-in-plan-mode, whose decision line already stood in the ledger

## Root cause

the ledger only grows and the hook appends no line it holds; only a supersedes block retires an entry, so a ratified sub-case that drops an item takes a new id whose line carries supersedes of the old one, as 445.7 did

## History

- 2026-09-27 created · raw/2026-09-26/2300/ledger.md#L34
- 2026-10-05 updated: clustered under insight-ledger-ratified-line-never-withdrawn (synthesis) · raw/2026-10-05/1616/ledger.md#L41
