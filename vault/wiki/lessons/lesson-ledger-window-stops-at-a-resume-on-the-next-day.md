---
type: lesson
kind: error
root_cause: session_event_logs in guppi/ledger.py walks the event logs back from today and stops at the newest date that holds a session-start of the stamp, which is the resume of 2026-10-15, so the startup and the hi of 2026-10-14 are never read and hi_moment finds no hi
status: new
origin: raw/2026-10-15/0553/ledger.md#L61
sprint: plugin
created: 2026-10-15
tags: [ledger, session]
---

## Trigger

session 44ee5004 opened with /hi on 2026-10-14 at 19:07 and was resumed on 2026-10-15 at 05:35; the ledger hook then refused the 23 decision lines of Case 821 with "no /hi recorded for session 44ee5004", and a second /hi opened a new session folder raw/2026-10-15/0553/ beside raw/2026-10-14/1907/, whose hooks then looked for the case files of the session in the new folder

## Root cause

session_event_logs in guppi/ledger.py walks the event logs back from today and stops at the newest date that holds a session-start of the stamp, which is the resume of 2026-10-15, so the startup and the hi of 2026-10-14 are never read and hi_moment finds no hi

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#L61
- 2026-10-15 deferred · [[decision-case-836]]
