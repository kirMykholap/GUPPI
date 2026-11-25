---
type: lesson
kind: error
root_cause: plan_path of .guppi/guppi/ledger.py takes the path of the plan file from the event log, whose detail guppi event cuts at DETAIL_LIMIT = 80 characters, and Claude Code now names a plan file with the id of the session after "-of-", so its path runs past that limit and the cut path names no file
status: archived
insight: "[[insight-event-log-cuts-the-plan-path]]"
origin: raw/2026-11-25/0605/ledger.md#L4
sprint: plugin
created: 2026-11-25
tags: [hooks, harness]
---

## Trigger

at the first Case of session 2026-11-25/0605, uv run --project .guppi guppi caseid --next --session 16ad52b9 printed "caseid: no plan file of session 16ad52b9 — no id printed"; line 20 of vault/raw/2026-11-25/event_log.md holds the path of the plan file cut to "C:\Users\kir\.claude\plans\frolicking-crafting-backus-of-16ad52b9-2613-43c4-8115", while the file is frolicking-crafting-backus-of-16ad52b9-2613-43c4-8115-f092d2d530c2.md, 106 characters; the session went on after the person appended the whole path as a tool Write line by Add-Content

## Root cause

plan_path of .guppi/guppi/ledger.py takes the path of the plan file from the event log, whose detail guppi event cuts at DETAIL_LIMIT = 80 characters, and Claude Code now names a plan file with the id of the session after "-of-", so its path runs past that limit and the cut path names no file

## History

- 2026-11-25 created · raw/2026-11-25/0605/ledger.md#L4
- 2026-11-25 updated: clustered under insight-event-log-cuts-the-plan-path (synthesis) · raw/2026-11-25/0605/ledger.md#L4
- 2026-11-25 archived · insight actioned
- 2026-11-25 archived · cleanup
