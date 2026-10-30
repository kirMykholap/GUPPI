---
type: lesson
kind: error
root_cause: the method read only the end state of the close commit, so a run that reached it by a command other than the one the instructions write passed the check
status: new
origin: raw/2026-10-29/2341/ledger.md#L40
sprint: plugin
created: 2026-10-29
tags: [session, librarian]
---

## Trigger

at the /hi of session 2341 the main agent read estimate-close-commits passed from git log and git status after the librarian's commit of session 1930, while the librarian's report said the close command as written failed with git add exit 128 on a CRLF path and passed only with tr -d '\r' added

## Root cause

the method read only the end state of the close commit, so a run that reached it by a command other than the one the instructions write passed the check

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#L40
