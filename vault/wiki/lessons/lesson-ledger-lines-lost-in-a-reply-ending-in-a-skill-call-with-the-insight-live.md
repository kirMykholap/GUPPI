---
type: lesson
kind: error
root_cause: the transcript holds only the final text of a turn (insight-ledger-hook-reads-only-the-final-text, severity 3, lesson-transcript-omits-text-emitted-before-tool-calls of session L); the agent ended a reply with ledger lines in a tool call anyway, with the lesson and the Insight live in the vault and the Insight's Proposal unactioned. A reply that carries ledger lines must end in text, never in a tool call.
status: clustered
insight: insight-ledger-hook-reads-only-the-final-text
origin: raw/2026-09-14/0747/ledger.md#L33
sprint: migration
created: 2026-09-14
tags: [ledger, hooks, workflow]
---

## Trigger

the reply of session M that carried the decision lines of Cases 115 and 116 ended with the Skill call /pre-task; the Stop hook of the next reply wrote the lines of that reply only, and guppi pretask --check kept naming 115 and 116 as items without a line.

## Root cause

the transcript holds only the final text of a turn (insight-ledger-hook-reads-only-the-final-text, severity 3, lesson-transcript-omits-text-emitted-before-tool-calls of session L); the agent ended a reply with ledger lines in a tool call anyway, with the lesson and the Insight live in the vault and the Insight's Proposal unactioned. A reply that carries ledger lines must end in text, never in a tool call.

## Insight

- [[insight-ledger-hook-reads-only-the-final-text]]

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#L33
- 2026-09-14 updated: clustered under insight-ledger-hook-reads-only-the-final-text · raw/2026-09-14/0747/ledger.md#L33
