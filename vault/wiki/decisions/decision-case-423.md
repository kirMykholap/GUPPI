---
type: decision
case: "423"
status: current
defer: ["[[rule-spec-reconcile]]"]
origin: raw/2026-09-25/1228/ledger.md#case-423
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow, session]
---

## Context

Case 416 deferred a guard on the plan and the time of the translation; Case 419 superseded 416 and took only the core of its scheme, so the defer falls. After Cases 419 and 421 the hooks write every Case into the plan, a defer included, and the agent edits the plan only to translate the name, `context` and `problem` before the approval, which `rule-spec-reconcile` watches. This session puts every item that needs a decision after the new scheme of Cases.

## Problem

Whether a guard refuses every edit of the plan by the agent while a line under `## Cases` of the Frontier is open, and when and how the prose of a Case is translated (the question of case 410).

## Deferred

### [[rule-spec-reconcile]]

A guard that refuses the agent's edits of the plan while a line under Cases of the Frontier is open; when and how the prose of a Case is translated (the question of case 410)

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#case-423
