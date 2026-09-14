---
type: lesson
kind: knowledge
root_cause: the payload carries `last_assistant_message` with the whole reply text, `stop_hook_active` (false on an ordinary stop), `session_id`, `transcript_path`, `cwd`, `permission_mode`; a `Stop` registration added to `settings.json` fired at the end of the same turn, no restart needed
status: new
source: the Slice 1 probe on Stop, session B 2026-09-09, probe-Stop-6.json — removed with raw/notes/ by case 100.6
origin: raw/2026-09-09/ledger.md#L29
sprint: migration
created: 2026-09-09
tags: [hooks, ledger]
---

## Trigger

the Slice 1 probe on `Stop`, 2026-09-09, session B (`probe-Stop-6.json`)

## Root cause

the payload carries `last_assistant_message` with the whole reply text, `stop_hook_active` (false on an ordinary stop), `session_id`, `transcript_path`, `cwd`, `permission_mode`; a `Stop` registration added to `settings.json` fired at the end of the same turn, no restart needed

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L29
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 updated: tags and source filled (case 113) · [[decision-case-113]]
