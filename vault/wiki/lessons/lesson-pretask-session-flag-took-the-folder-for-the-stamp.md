---
type: lesson
kind: error
root_cause: the `/pre-task` skill still says "the stamp from the `hi:` line" and the line carries three tokens — time, session id, folder; `--session` takes the eight-character id alone, and the message cuts the value to eight characters so the wrong token is not obvious; the same cause as `lesson-pretask-session-flag-takes-the-id-not-the-hi-line` of session 1252, which changed no text of the skill
status: clustered
insight: "[[insight-pretask-session-flag-takes-the-id-not-the-hi-line]]"
origin: raw/2026-09-18/2253/ledger.md#L3
sprint: migration
created: 2026-09-18
tags: [harness, session]
---

## Trigger

`guppi pretask --check <plan> --session 2026-09-18/2253`, the session folder passed as the stamp, answered "no hi recorded for session 2026-09-; nothing checked", exit 0; the same call with `--session 757fff5b` ran the check

## Root cause

the `/pre-task` skill still says "the stamp from the `hi:` line" and the line carries three tokens — time, session id, folder; `--session` takes the eight-character id alone, and the message cuts the value to eight characters so the wrong token is not obvious; the same cause as `lesson-pretask-session-flag-takes-the-id-not-the-hi-line` of session 1252, which changed no text of the skill

## History

- 2026-09-18 created · raw/2026-09-18/2253/ledger.md#L3
- 2026-09-18 updated: clustered by librarian under insight-pretask-session-flag-takes-the-id-not-the-hi-line · raw/2026-09-18/2253/ledger.md#L3
