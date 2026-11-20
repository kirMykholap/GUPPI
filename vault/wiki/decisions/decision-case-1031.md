---
type: decision
case: "1031"
status: current
children: ["[[decision-case-1031.1]]", "[[decision-case-1031.2]]", "[[decision-case-1031.3]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1031
sprint: plugin
created: 2026-11-04
tags: [session, workflow, harness, plugin, render]
---

## Problem

`case-guppi` puts bookkeeping to the person as if it were a decision, and the setup Case of a new project asks for commands that the person cannot place, so the check of the setup fails and each Case costs questions that change nothing.

## Recommend

- **The two standing questions of form**
  - Recommended: (a) both follow the general rule.
  - Answer: agreed, (a).
- **The questions on `test` and `style` at setup**
  - Recommended: (b) it asks only where the project holds code of its own.
  - Answer: (b), after a plain explanation; the person first leaned to no question at all, and asks that the question say how the project's own tests and style check run together with GUPPI's, not which commands to set.

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1031
