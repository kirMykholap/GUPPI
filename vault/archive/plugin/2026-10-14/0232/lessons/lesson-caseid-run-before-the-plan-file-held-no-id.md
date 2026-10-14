---
type: lesson
kind: error
root_cause: orchestration.md set the plan file before the first dispatch, not before the first run of the command, and the command exited 0 and printed an id with no plan file
status: archived
insight: "[[insight-caseid-printed-an-id-it-did-not-hold]]"
origin: raw/2026-10-14/0232/ledger.md#L15
sprint: plugin
created: 2026-10-14
tags: [orchestration, session]
---

## Trigger

at the first Case of session 0232 the main agent ran `uv run guppi caseid --next --session cfcb07e8` before the plan file stood; it printed 810 and exit 0, and only a line on stderr said the id was not held

## Root cause

orchestration.md set the plan file before the first dispatch, not before the first run of the command, and the command exited 0 and printed an id with no plan file

## History

- 2026-10-14 created · raw/2026-10-14/0232/ledger.md#L15
- 2026-10-14 updated: clustered under insight-caseid-printed-an-id-it-did-not-hold (synthesis) · raw/2026-10-14/0232/ledger.md#L15
- 2026-10-14 archived · insight actioned
- 2026-10-14 archived · cleanup
