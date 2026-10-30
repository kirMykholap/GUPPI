---
type: lesson
kind: error
root_cause: the steps the agent gave wrote out the command with UV_OFFLINE=1 and UV_CACHE_DIR only for p2, and step 6 for p4 said "the same two variables as in step 4" in a new window, which leaves the person to retype them by memory
status: new
origin: raw/2026-10-30/2005/ledger.md#L56
sprint: plugin
created: 2026-10-30
tags: [plugin, workflow]
---

## Trigger

at the stop of Work Mode of session 2005 the project p4-own-files-offline was installed online: uv sync passed with "Installed 9 packages" at 23:10:33, and the empty uv-cache folder holds nothing written after 23:01, so the rollback of a project with files set aside was not seen

## Root cause

the steps the agent gave wrote out the command with UV_OFFLINE=1 and UV_CACHE_DIR only for p2, and step 6 for p4 said "the same two variables as in step 4" in a new window, which leaves the person to retype them by memory

## History

- 2026-10-30 created · raw/2026-10-30/2005/ledger.md#L56
