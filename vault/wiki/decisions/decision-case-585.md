---
type: decision
case: "585"
status: current
defer: ["[[insight-spec-write-parent-body-kept-on-re-ratification]]"]
origin: raw/2026-10-01/1725/ledger.md#case-585
sprint: migration
created: 2026-10-01
tags: [harness, workflow, hooks, session]
---

## Context

`insight-spec-write-parent-body-kept-on-re-ratification` clusters two lessons. A Case ratified whole and then ratified again as a parent with sub-cases keeps its old body in the Spec, because the Spec hook of `rule-spec-write` writes the new answer by its sub-case headings and does not remove the body the parent held alone. Session 1441 worked around it with a new id (581). The person put the remaining items off to go to work.

## Problem

The decision whether the Spec hook replaces the whole Case on re-ratification is put off.

## Deferred

### [[insight-spec-write-parent-body-kept-on-re-ratification]]

A Case ratified whole and then ratified again as a parent with sub-cases keeps its old body in the Spec, since the Spec hook of rule-spec-write writes the new answer by its sub-case headings and does not remove the given, when, then, then block and tasks the parent held when it stood alone; whether the hook replaces the whole Case on re-ratification

## History

- 2026-10-01 created · raw/2026-10-01/1725/ledger.md#case-585
