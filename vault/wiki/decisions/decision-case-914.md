---
type: decision
case: "914"
status: current
update: ["[[estimate-close-commits]]"]
origin: raw/2026-10-29/2341/ledger.md#case-914
sprint: plugin
created: 2026-10-29
tags: [harness, workflow, git, librarian]
---

## Problem

On Windows the list that the close command passes to `git add` carries a carriage return on each path, so the command as written fails, and the librarian ran a changed command. The Estimate of the commit passed on the end state, and its tests cannot see a line ending.

## Recommend

- **Where the line ending is fixed**
  - Recommended: (a) `--paths` alone prints bare line feeds, set on its own output before it prints.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) replace the Criterion of `estimate-close-commits` with the line ending and the close command as written; a new test runs `--paths` as a real process and asserts no carriage return; the page goes back to `pending`.
  - Answer: agreed, (a).
- **What happens to the reading of passed**
  - Recommended: (a) the main agent writes a new reading `failed` from the saved chat, before this Case's decision lines.
  - Answer: agreed, (a).
- **Whether a failed close command goes into the report**
  - Recommended: (a) left out of this Case.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#case-914
