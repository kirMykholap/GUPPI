---
type: lesson
kind: error
root_cause: on Windows Python prints to the console in cp1252 and the Bash tool decodes the bytes as UTF-8; a character inside cp1252, such as the dash, prints without an error and shows as U+FFFD, so a mark of the reading tool was taken for a fault of the thing read, with no check of the bytes of the source file
status: new
origin: raw/2026-09-30/0248/ledger.md#L11
sprint: migration
created: 2026-09-30
tags: [harness, session]
---

## Trigger

session 0138 read the transcript of session 876c4080 with a scratchpad Python script run through the Bash tool with no encoding set; the dash of the UserPromptSubmit hook output showed as U+FFFD, the reading and the handoff called it a defect of guppi context --prompt, while the transcript held the dash and a second run with PYTHONIOENCODING=utf-8 printed it

## Root cause

on Windows Python prints to the console in cp1252 and the Bash tool decodes the bytes as UTF-8; a character inside cp1252, such as the dash, prints without an error and shows as U+FFFD, so a mark of the reading tool was taken for a fault of the thing read, with no check of the bytes of the source file

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#L11
