---
type: lesson
kind: error
root_cause: case-guppi took the Work Mode rule of orchestration.md — a new top-level Case that supersedes a ratified one — for a change asked in Plan Mode, where a ratified Case changes under its own number, and it took a new id itself, though only the main agent gets one from guppi caseid
status: clustered
insight: "[[insight-case-build-opens-a-new-case-where-one-was-named]]"
origin: raw/2026-10-16/0342/ledger.md#L20
sprint: plugin
created: 2026-10-16
tags: [case-build, prespec]
---

## Trigger

at /pre-spec of session 0342 the findings on Case 851, ratified in Plan Mode, went to its case-guppi, which wrote case-856.md with `{supersedes:case 851}` marks under an id that no `guppi caseid --next` printed, and the main agent sent it back to rebuild under 851

## Root cause

case-guppi took the Work Mode rule of orchestration.md — a new top-level Case that supersedes a ratified one — for a change asked in Plan Mode, where a ratified Case changes under its own number, and it took a new id itself, though only the main agent gets one from guppi caseid

## History

- 2026-10-16 created · raw/2026-10-16/0342/ledger.md#L20
- 2026-10-16 updated: clustered under insight-case-build-opens-a-new-case-where-one-was-named (synthesis) · raw/2026-10-16/0342/ledger.md#L20
