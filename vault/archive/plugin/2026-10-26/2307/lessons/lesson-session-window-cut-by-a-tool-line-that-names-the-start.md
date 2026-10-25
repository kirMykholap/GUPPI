---
type: lesson
kind: error
root_cause: "`session_event_logs` of .guppi/guppi/ledger.py tests the marker as a substring of the whole text of a day's log, so any logged tool line whose text holds the stamp followed by the start word ends the walk on a day with no `hi`, and the window loses the session"
status: archived
insight: "[[insight-ledger-window-ends-at-any-start-text-of-the-stamp]]"
origin: raw/2026-10-17/2307/ledger.md#L40
sprint: plugin
created: 2026-10-17
tags: [session, hooks, ledger]
---

## Trigger

on 2026-10-25 in session 2307 the ledger hook refused a reply with "no /hi recorded for session 392fc00e" twice: a Grep of a case-guppi and then a Bash check of the main agent held the stamp, a space and the word session-start in their pattern or command, the event hook logged each under this session's stamp in vault/raw/2026-10-25/event_log.md, and the person removed those lines by hand each time

## Root cause

`session_event_logs` of .guppi/guppi/ledger.py tests the marker as a substring of the whole text of a day's log, so any logged tool line whose text holds the stamp followed by the start word ends the walk on a day with no `hi`, and the window loses the session

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#L40
- 2026-10-26 updated: clustered under insight-ledger-window-ends-at-any-start-text-of-the-stamp (synthesis) · raw/2026-10-17/2307/ledger.md#L40
- 2026-10-26 archived · insight actioned
- 2026-10-26 archived · cleanup
