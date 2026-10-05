---
type: lesson
kind: knowledge
root_cause: in plan mode Claude Code checks a call that is not read-only, Agent and SendMessage among them, by the server-side auto mode classifier; when that server gives no verdict the call is refused as a transient failure, after ten such responses in a row the turn stops, and the same call passes unchanged once the server answers again
status: archived
source: the Agent and SendMessage tool results of session 1318 on 2026-09-28, Claude Code in plan mode with defaultMode plan
insight: "[[insight-hi-skill-substitution-checked-by-a-model-call]]"
origin: raw/2026-09-28/1318/ledger.md#L41
sprint: migration
created: 2026-09-28
tags: [harness, session]
---

## Trigger

in plan mode six calls in a row, four SendMessage to a live case-guppi and two Agent, failed with "The server-side auto mode classifier gave no verdict (error)", and two rounds of a Case waited while the person thought the subagent was dead

## Root cause

in plan mode Claude Code checks a call that is not read-only, Agent and SendMessage among them, by the server-side auto mode classifier; when that server gives no verdict the call is refused as a transient failure, after ten such responses in a row the turn stops, and the same call passes unchanged once the server answers again

## History

- 2026-09-28 created · raw/2026-09-28/1318/ledger.md#L41
- 2026-09-28 updated: clustered under insight-hi-skill-substitution-checked-by-a-model-call (synthesis) · raw/2026-09-28/1318/ledger.md#L41
- 2026-10-06 archived · insight actioned
- 2026-10-06 archived · cleanup
