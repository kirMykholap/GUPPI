---
type: lesson
kind: error
root_cause: the hook reads raw/<today>/event_log.md only and needs a session-start of its own session before the hi; both lay in raw/2026-09-10/event_log.md, and the day's new log held tool lines and a hi with no start; a session that crosses midnight, or any hi whose start is in another day's file, cannot write the ledger until the session is resumed
status: archived
insight: "[[insight-ledger-hi-tied-to-its-session-by-position]]"
origin: raw/2026-09-11/ledger.md#L45
sprint: migration
created: 2026-09-11
tags: [harness, hooks, ledger]
---

## Trigger

session H crossed midnight; the Stop hook refused the 44 lines of Case 53 with "no /hi recorded", and a fresh /hi on 2026-09-11 did not help

## Root cause

the hook reads raw/<today>/event_log.md only and needs a session-start of its own session before the hi; both lay in raw/2026-09-10/event_log.md, and the day's new log held tool lines and a hi with no start; a session that crosses midnight, or any hi whose start is in another day's file, cannot write the ledger until the session is resumed

## Insight

- [[insight-ledger-hi-tied-to-its-session-by-position]]

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#L45
- 2026-09-14 updated: clustered under insight-ledger-hi-tied-to-its-session-by-position · raw/2026-09-14/0747/ledger.md#L2
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
