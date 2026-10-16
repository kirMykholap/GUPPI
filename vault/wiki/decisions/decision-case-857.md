---
type: decision
case: "857"
status: current
update: ["[[rule-close]]", "[[estimate-close-commits]]"]
origin: raw/2026-10-16/1712/ledger.md#case-857
sprint: plugin
created: 2026-10-16
tags: [harness, workflow, git, librarian]
---

## Problem

The close commit of the librarian names four fixed paths, and the render writes a file outside them, so that file stays uncommitted after the run.

## Recommend

- **How should the close commit find the files the render wrote?**
  - Recommended: (b) a command prints the files the render writes, and the commit adds `vault` and those files.
  - Answer: agreed, (b).
- **How is the fix checked?**
  - Recommended: (a) replace the Criterion of `estimate-close-commits` whole.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/1712/ledger.md#case-857
