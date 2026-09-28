---
type: decision
case: "475"
status: current
defer: ["[[rule-spec-write]]"]
origin: raw/2026-09-28/0000/ledger.md#case-475
sprint: migration
created: 2026-09-28
tags: [hooks, harness, workflow, session]
---

## Context

Case 471 was ratified whole, then built again after pre-spec as a parent with sub-cases 471.1 and 471.2 and ratified again. The hook of `rule-spec-write` replaced the parent's prose in the plan file from the new answer, but kept the old body of 471 — its `given`, `when`, `then`, `then` block and `tasks` — under the parent heading. The old `replace` pairs used up the anchors, `guppi ratified` refused 471.1, and the Case had to be superseded by Case 474 (lesson `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`).

## Problem

A ratified Case that is built again as a parent with sub-cases cannot be written into the Spec: the hook keeps the sections the new answer leaves to its sub-cases, and the only way out is a new Case id.

## Deferred

### [[rule-spec-write]]

The Spec hook, writing a Case built again as a parent with sub-cases, drops the body the new answer leaves to its sub-cases, so the Case keeps its id

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#case-475
