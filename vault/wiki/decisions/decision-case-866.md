---
type: decision
case: "866"
status: current
update: ["[[rule-close]]"]
origin: raw/2026-10-16/2104/ledger.md#case-866
sprint: plugin
created: 2026-10-16
tags: [harness, workflow, git, librarian]
---

## Problem

The close command of the librarian is written for a POSIX shell, and its Render does not say so, so a reader may take it for a command that runs in Windows PowerShell 5.1, which does not parse its `&&`.

## Recommend

- **What should this Case do with the close command?**
  - Recommended: (a) name the Bash tool in the Render and keep the command as it is.
  - Answer: agreed, (a).
- **How is this change checked?**
  - Recommended: (a) use `estimate-close-commits` as it stands; no Estimate is created or changed.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-866
