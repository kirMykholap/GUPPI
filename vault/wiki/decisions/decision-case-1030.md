---
type: decision
case: "1030"
status: current
children: ["[[decision-case-1030.1]]", "[[decision-case-1030.2]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1030
sprint: plugin
created: 2026-11-04
tags: [plugin, ci, tests, git]
---

## Problem

The clean copy fails its own style commands and two of its own tests, so a project that installs GUPPI starts red, and nothing runs those commands over the copy, so the defect shows only at a trial install.

## Recommend

- **How the copy gets clean style**
  - Recommended: (a) remove the leftovers, then format the copy with `ruff format` at the end of the build.
  - Answer: agreed, (a).
- **Where the new test runs**
  - Recommended: (c) style in `guppi test`, the tests over the copy under the `live` mark.
  - Answer: agreed, (c).
- **A guard before the `prod` branch**
  - Recommended: (a) leave the workflow as it is.
  - Answer: agreed, (a).
- **What checks this Case**
  - Recommended: (a) a new check, and the old line moves into it.
  - Answer: agreed, (a).
- **One Case or two**
  - Recommended: (a) one Case.
  - Answer: agreed, (a).
- **How the old check gives up its promise**
  - Recommended: (a) two sub-cases.
  - Answer: (a).

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1030
