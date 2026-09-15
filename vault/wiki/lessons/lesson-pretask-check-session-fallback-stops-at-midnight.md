---
type: lesson
kind: error
root_cause: "`pretask.resolve_session` falls back to the last `session-start` of today's event log, and after midnight today's log holds no line of a session opened yesterday, so the stamp resolves to `--------`; the ledger hook keeps the `hi` window across midnight, the pre-task check does not walk back to the `hi` date"
status: clustered
insight: "[[insight-ledger-hi-tied-to-its-session-by-position]]"
origin: raw/2026-09-15/2225/ledger.md#L16
sprint: migration
created: 2026-09-15
tags: [harness, session]
---

## Trigger

at 01:2x on 2026-09-16 `uv run guppi pretask --check <plan>` for the session opened by `hi` at 22:25 on 2026-09-15 printed "no hi recorded for session --------; nothing checked", `CLAUDE_SESSION_ID` empty in the agent's Bash; it ran only with `--session 8836b091`

## Root cause

`pretask.resolve_session` falls back to the last `session-start` of today's event log, and after midnight today's log holds no line of a session opened yesterday, so the stamp resolves to `--------`; the ledger hook keeps the `hi` window across midnight, the pre-task check does not walk back to the `hi` date

## History

- 2026-09-16 created · raw/2026-09-15/2225/ledger.md#L16
- 2026-09-16 updated: clustered under insight-ledger-hi-tied-to-its-session-by-position · raw/2026-09-15/2225/ledger.md#L16
