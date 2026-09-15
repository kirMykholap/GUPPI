---
type: lesson
kind: error
root_cause: in this harness (VS Code extension, focus view) an assistant text emitted before a tool call in the same turn is not persisted to the transcript and is not last_assistant_message, so the hook has nothing to read; lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn, withdrawn by case 70 as the hook dropping nothing, described the same loss — the hook reads faithfully what the transcript never received
status: archived
insight: "[[insight-ledger-hook-reads-only-the-final-text]]"
origin: raw/2026-09-13/ledger.md#L42
sprint: migration
created: 2026-09-13
tags: [hooks, ledger, harness]
---

## Trigger

the reply that ratified Case 109 carried its LEDGER block in a text written before four Edit calls and a closing text of the same turn; the Stop hook wrote nothing, and the session transcript holds that turn as thinking, tool_use and the closing text only — the first text is absent, so ledger.session_lines over the transcript returns 38 lines and none of 109; every earlier block of the session stood in the last text of its turn and reached the ledger

## Root cause

in this harness (VS Code extension, focus view) an assistant text emitted before a tool call in the same turn is not persisted to the transcript and is not last_assistant_message, so the hook has nothing to read; lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn, withdrawn by case 70 as the hook dropping nothing, described the same loss — the hook reads faithfully what the transcript never received

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#L42
- 2026-09-13 updated: clustered under insight-ledger-hook-reads-only-the-final-text · raw/2026-09-13/ledger.md#L42
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
