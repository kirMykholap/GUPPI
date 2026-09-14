---
type: lesson
kind: knowledge
root_cause: the pretask mark has no session id, as the hi had before case 111; two sessions open at once could lend each other a pretask, the same binding by position that insight-ledger-hi-tied-to-its-session-by-position names; a stamped pretask written by a hook on the Skill call, or by guppi gate, is the fix
status: archived
source: raw/2026-09-14/event_log.md, lines 348 and 268
insight: insight-ledger-hi-tied-to-its-session-by-position
origin: raw/2026-09-14/1029/ledger.md#L40
sprint: migration
created: 2026-09-14
tags: [hooks, session, harness]
---

## Trigger

the pretask line of session N reads `- 11:26:29 -------- pretask` — the /pre-task skill writes it through a `!` substitution where CLAUDE_SESSION_ID is empty — and pretask.window counts any pretask after our hi, whatever its stamp, so ExitPlanMode passed

## Root cause

the pretask mark has no session id, as the hi had before case 111; two sessions open at once could lend each other a pretask, the same binding by position that insight-ledger-hi-tied-to-its-session-by-position names; a stamped pretask written by a hook on the Skill call, or by guppi gate, is the fix

## Insight

- [[insight-ledger-hi-tied-to-its-session-by-position]]

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#L40
- 2026-09-14 updated: clustered under insight-ledger-hi-tied-to-its-session-by-position · raw/2026-09-14/1029/ledger.md#L40
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
