---
type: lesson
kind: error
root_cause: a slash command typed by the person is expanded by the client into the prompt and is never a tool call, so removing disable-model-invocation (case 150) enabled only the agent's call; the then of 150 assumed both paths go through the Skill tool and was read failed
status: archived
insight: "[[insight-retro-typed-command-is-never-a-tool-call]]"
origin: raw/2026-09-15/1110/ledger.md#L27
sprint: migration
created: 2026-09-15
tags: [harness, session]
---

## Trigger

at the /retro of session Q typed by the person the event log shows no Skill call, no gate and no retro mark, while the agent's own Skill call minutes later shows all three

## Root cause

a slash command typed by the person is expanded by the client into the prompt and is never a tool call, so removing disable-model-invocation (case 150) enabled only the agent's call; the then of 150 assumed both paths go through the Skill tool and was read failed

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#L27
- 2026-09-15 updated: clustered under insight-retro-typed-command-is-never-a-tool-call · raw/2026-09-15/1110/ledger.md#L27
- 2026-09-15 archived · insight actioned
- 2026-09-15 archived · cleanup
