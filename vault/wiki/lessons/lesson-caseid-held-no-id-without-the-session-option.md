---
type: lesson
kind: error
root_cause: guppi/caseid.py takes the session stamp only from `--session` or a hook payload, and a Bash call has no payload, while orchestration.md names the command without `--session`
status: new
origin: raw/2026-10-14/0101/ledger.md#L58
sprint: plugin
created: 2026-10-14
tags: [harness, session]
---

## Trigger

`uv run guppi caseid --next`, run in Bash as orchestration.md writes it, printed "caseid: no plan file of the session — the id is not held" and 808 twice, though the plan file stood; it held the id only when run with `--session 28e2bf37`

## Root cause

guppi/caseid.py takes the session stamp only from `--session` or a hook payload, and a Bash call has no payload, while orchestration.md names the command without `--session`

## History

- 2026-10-14 created · raw/2026-10-14/0101/ledger.md#L58
