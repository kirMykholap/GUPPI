---
type: lesson
kind: error
root_cause: the agent chose a shell script for a multi-part edit of a source file instead of the Edit tool that the hooks require
status: new
origin: raw/2026-10-12/2349/ledger.md#L59
sprint: plugin
created: 2026-10-12
tags: [workflow, hooks]
---

## Trigger

in Work Mode the agent changed guppi/materialize.py by a python heredoc in Bash; the shellwrite hook turned its CRLF endings into LF, and a later heredoc for a JSON file was refused by bashguard

## Root cause

the agent chose a shell script for a multi-part edit of a source file instead of the Edit tool that the hooks require

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#L59
