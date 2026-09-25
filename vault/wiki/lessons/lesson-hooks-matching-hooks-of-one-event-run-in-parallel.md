---
type: lesson
kind: knowledge
root_cause: Claude Code runs all matching hooks of one event in parallel ("All matching hooks run in parallel"); the order of a hooks array is no order of execution, so a hook that needs what another hook of the same event writes reads it from the payload itself, never from that hook's file
status: new
source: https://code.claude.com/docs/en/hooks.md
origin: raw/2026-09-25/0051/ledger.md#L15
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
---

## Trigger

frame-guppi read the Stop hooks of .claude/settings.json as running in the listed order — guppi ledger before guppi ratified — from the History of rule-hook-registry, and no page of the vault says otherwise

## Root cause

Claude Code runs all matching hooks of one event in parallel ("All matching hooks run in parallel"); the order of a hooks array is no order of execution, so a hook that needs what another hook of the same event writes reads it from the payload itself, never from that hook's file

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#L15
