---
type: decision
case: "985"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-reads-the-readers-of-a-changed-step]]"]
origin: raw/2026-11-01/1721/ledger.md#case-985
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, case-build]
---

## Problem

The search that finds the readers of a changed step does not reach the harness code, so a step done by a function there is changed on one input and missed on another.

## Recommend

- **What changes after the third failed reading**
  - Recommended: (a) the rule follows a step into the harness code.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#case-985
