---
type: lesson
kind: error
root_cause: "the agent took the style step of /work as due once per stop: task, not before each reply that stops there, so a stop repeated at the same task after the person's answer got no style run; Case 1084 of this session makes the Render say every time"
status: new
origin: raw/2026-11-27/1402/ledger.md#L26
sprint: plugin
created: 2026-11-27
tags: [workflow, harness]
---

## Trigger

/work of session 1402 stood three times before the stop: task of Case 1082 — first before the person's file, then after two exports that missed the bound — and ran uv run --project .guppi guppi style only before the first of those stops

## Root cause

the agent took the style step of /work as due once per stop: task, not before each reply that stops there, so a stop repeated at the same task after the person's answer got no style run; Case 1084 of this session makes the Render say every time

## History

- 2026-11-27 created · raw/2026-11-27/1402/ledger.md#L26
