---
type: decision
case: "1034"
status: current
children: ["[[decision-case-1034.1]]", "[[decision-case-1034.2]]", "[[decision-case-1034.3]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1034
sprint: plugin
created: 2026-11-04
tags: [sprint, workflow, harness, git, session, render]
---

## Problem

On `main` the opening Case writes no branch task and Work Mode refuses to start, so the first sprint of every project stops until the person makes the branch by hand.

## Recommend

- **How the branch task runs, since Work Mode refuses to start on main**
  - Recommended: (a) Work Mode runs the branch task first, then goes on.
  - Answer: agreed, (a).

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1034
