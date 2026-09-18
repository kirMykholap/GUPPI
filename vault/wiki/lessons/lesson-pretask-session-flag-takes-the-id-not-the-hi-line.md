---
type: lesson
kind: knowledge
root_cause: "--session takes the eight-character session id alone, the second token of the hi: line, and reads the event log by it; the skill text says \"the stamp from the hi: line\", which reads as the whole line; the exit 0 with nothing checked is easy to take for a clean run — read the first line of the output, not the exit code"
status: clustered
source: guppi/pretask.py and the run of guppi pretask --check in session 1252
insight: "[[insight-pretask-session-flag-takes-the-id-not-the-hi-line]]"
origin: raw/2026-09-18/1252/ledger.md#L38
sprint: migration
created: 2026-09-18
tags: [harness, session]
---

## Trigger

guppi pretask --check <plan> --session "12:52:48 122e02e9", the stamp as the hi: line prints it, answered "no hi recorded for session 12:52:48; nothing checked", exit 0; the same call with --session 122e02e9 ran the check

## Root cause

--session takes the eight-character session id alone, the second token of the hi: line, and reads the event log by it; the skill text says "the stamp from the hi: line", which reads as the whole line; the exit 0 with nothing checked is easy to take for a clean run — read the first line of the output, not the exit code

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#L38
- 2026-09-18 updated: clustered by librarian under insight-pretask-session-flag-takes-the-id-not-the-hi-line · raw/2026-09-18/2253/ledger.md#L3
