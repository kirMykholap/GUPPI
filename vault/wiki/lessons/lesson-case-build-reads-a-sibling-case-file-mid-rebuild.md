---
type: lesson
kind: error
root_cause: Cases sent back in one message are built again in parallel, and a case-guppi that reads the file of a sibling Case reads what stands at that moment, before the sibling's rebuild ends
status: clustered
insight: "[[insight-subagents-read-a-sibling-mid-flight]]"
origin: raw/2026-10-16/0104/ledger.md#L21
sprint: plugin
created: 2026-10-16
tags: [case-build, prespec]
---

## Trigger

Case 843 kept an Other Case line asking that Case 846 read its two projects before the push, though the finished case-846.md held that reading

## Root cause

Cases sent back in one message are built again in parallel, and a case-guppi that reads the file of a sibling Case reads what stands at that moment, before the sibling's rebuild ends

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#L21
- 2026-10-16 updated: clustered under insight-subagents-read-a-sibling-mid-flight (synthesis) · raw/2026-10-16/0104/ledger.md#L21
