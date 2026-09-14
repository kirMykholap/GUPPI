---
type: lesson
kind: knowledge
root_cause: the event log is a debugging record cut to one line, and the gate reads it as a source of truth for the plan path; recorded as knowledge on the owner's choice, a Case when a path of 80 or more characters is met
status: new
source: guppi/event.py, DETAIL_LIMIT = 80, read by guppi/gate.py
origin: raw/2026-09-14/1229/ledger.md#L20
sprint: migration
created: 2026-09-14
tags: [hooks, harness]
---

## Trigger

guppi gate (case 122) finds the session's plan file by the `tool Write:`/`tool Edit:` lines of the event log, and event.py cuts a line's detail at DETAIL_LIMIT 80 characters, so a plan path longer than that is not found and the gate passes silently; session N's paths were 54 characters, this session's 51

## Root cause

the event log is a debugging record cut to one line, and the gate reads it as a source of truth for the plan path; recorded as knowledge on the owner's choice, a Case when a path of 80 or more characters is met

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#L20
- 2026-09-14 updated: source added (case 144.2) · [[decision-case-144.2]]
