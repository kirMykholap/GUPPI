---
type: lesson
kind: error
root_cause: "`guppi caseid --next` has one mode, print and hold, and the main agent took a run of it for a read of the store"
status: new
origin: raw/2026-10-14/0232/ledger.md#L16
sprint: plugin
created: 2026-10-14
tags: [orchestration, session]
---

## Trigger

after case-guppi built Case 812 under a number of its own, the main agent ran `uv run guppi caseid --next --session cfcb07e8` to check that 812 was held; the command printed and held 813, which no Case uses

## Root cause

`guppi caseid --next` has one mode, print and hold, and the main agent took a run of it for a read of the store

## History

- 2026-10-14 created · raw/2026-10-14/0232/ledger.md#L16
