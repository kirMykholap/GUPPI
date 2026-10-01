---
type: lesson
kind: error
root_cause: the Spec hook of rule-spec-write writes a re-ratified Case by its sub-case headings and does not remove the body the parent held when it stood alone, so a Case that gains sub-cases on re-ratification signs its content twice and must be built again under a new id that supersedes it
status: clustered
insight: "[[insight-spec-write-parent-body-kept-on-re-ratification]]"
origin: raw/2026-10-01/1441/ledger.md#L32
sprint: migration
created: 2026-10-01
tags: [harness, workflow]
---

## Trigger

session 1441, Case 580 was ratified with no sub-cases, then built again on the findings of /pre-spec as 580.1 and 580.2 and ratified again; the plan file kept the old given, when, then, then block and tasks of 580 under its heading beside the two sub-cases, and guppi prespec --check and guppi ratified found the replace of rule-prespec and the Criterion of estimate-prespec-gathers-the-answers-after-findings signed twice

## Root cause

the Spec hook of rule-spec-write writes a re-ratified Case by its sub-case headings and does not remove the body the parent held when it stood alone, so a Case that gains sub-cases on re-ratification signs its content twice and must be built again under a new id that supersedes it

## History

- 2026-10-01 created · raw/2026-10-01/1441/ledger.md#L32
- 2026-10-01 updated: clustered under insight-spec-write-parent-body-kept-on-re-ratification (synthesis) · raw/2026-10-01/1441/ledger.md#L32
