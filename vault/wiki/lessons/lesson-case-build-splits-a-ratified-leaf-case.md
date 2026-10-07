---
type: lesson
kind: error
root_cause: rule-case-build sets no step for a fix that adds a second behaviour to a ratified Case with no sub-cases, which keeps its decision lines and cannot become a parent
status: clustered
insight: "[[insight-ledger-ratified-line-never-withdrawn]]"
origin: raw/2026-10-07/1804/ledger.md#L28
sprint: migration
created: 2026-10-07
tags: [workflow, orchestration]
---

## Trigger

sent pre-spec finding F6, which asked ratified Case 713, a Case with no sub-cases, to replace one more Criterion, its case-guppi split 713 into 713.1 and 713.2, then undid that and built a new Case 719 to supersede 713

## Root cause

rule-case-build sets no step for a fix that adds a second behaviour to a ratified Case with no sub-cases, which keeps its decision lines and cannot become a parent

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#L28
- 2026-10-07 updated: clustered under insight-ledger-ratified-line-never-withdrawn (synthesis) · raw/2026-10-07/1804/ledger.md#L28
