---
type: lesson
kind: knowledge
root_cause: "`tool_input` is `{}`; the plan text is in `tool_response.plan`, whole, with `session_id`, `transcript_path`, `cwd` and `permission_mode` beside it, so C9 (copying the approved plan into `raw/<date>/spec.md`) can be a hook"
status: new
origin: raw/2026-09-09/ledger.md#L30
sprint: migration
created: 2026-09-09
---

## Trigger

the Slice 1 probe on `PostToolUse ExitPlanMode`, 2026-09-09, session B (`probe-PostToolUse-1.json`)

## Root cause

`tool_input` is `{}`; the plan text is in `tool_response.plan`, whole, with `session_id`, `transcript_path`, `cwd` and `permission_mode` beside it, so C9 (copying the approved plan into `raw/<date>/spec.md`) can be a hook

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L30
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
