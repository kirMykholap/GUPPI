---
type: lesson
kind: error
root_cause: the guard runs from the working tree on each Edit and Write, so a change of the contract between two of its functions made in two steps leaves the hook broken between them; changing the caller first, whose error the hook catches and lets the call run, keeps the edits possible.
status: new
origin: raw/2026-10-28/1907/ledger.md#L21
sprint: plugin
created: 2026-10-28
tags: [hooks, harness]
---

## Trigger

in Work Mode an Edit changed held_number of .guppi/guppi/ratified.py to return a pair before its caller guard was changed, and the live PreToolUse guard refused every Edit and Write until git checkout restored the file and the edits were made again with the caller first.

## Root cause

the guard runs from the working tree on each Edit and Write, so a change of the contract between two of its functions made in two steps leaves the hook broken between them; changing the caller first, whose error the hook catches and lets the call run, keeps the edits possible.

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#L21
