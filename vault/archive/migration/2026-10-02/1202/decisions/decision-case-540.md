---
type: decision
case: "540"
status: archived
defer: ["[[rule-work-mode]]"]
superseded_by: ["[[decision-case-591.7]]"]
origin: raw/2026-09-30/0248/ledger.md#case-540
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, render]
---

## Context

`/work` runs Work Mode on the approved Spec of the session, `raw/<date>/<hi HHMM>/spec.md`, and names no other Spec. In session 0138 the conserved Spec of session 2024 was run from its own folder: its boxes were ticked there, and its `carry.md` was deleted in Work Mode. `rule-work-mode` says nothing of that path (handoff of 0138, What is not done).

## Problem

A session that takes up a conserved Spec runs Work Mode by the agent's own reading, since `rule-work-mode` does not say which `spec.md` to run, where to tick its boxes, or when to delete `carry.md`.

## Deferred

### [[rule-work-mode]]

Prevents implementation starting before the plan, branch and baseline exist

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-540
- 2026-10-02 superseded by decision-case-591.7 · [[decision-case-591.7]]
- 2026-10-02 archived · superseded
- 2026-10-02 archived · cleanup
