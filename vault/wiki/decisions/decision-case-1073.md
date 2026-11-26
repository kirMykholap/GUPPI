---
type: decision
case: "1073"
status: current
update: ["[[estimate-synthesis-keeps-actioned-by-the-mark]]"]
supersedes: ["[[decision-case-1009]]"]
origin: raw/2026-11-26/2333/ledger.md#case-1073
sprint: plugin
created: 2026-11-26
tags: [harness, workflow, librarian]
---

## Problem

The check of the mark at synthesis has waited since its Criterion was last replaced for a librarian's run that may never come in this sprint, and three of its branches were never read. It needs a verdict that does not wait for that run.

## Recommend

- **How the check gets its verdict**
  - Recommended: (b) set `passed` by the person's decision, its Criterion written back unchanged, its result saying that the earlier run read one branch and that three branches were never exercised.
  - Answer: agreed, (b).

## History

- 2026-11-27 created · raw/2026-11-26/2333/ledger.md#case-1073
