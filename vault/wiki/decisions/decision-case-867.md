---
type: decision
case: "867"
status: current
update: ["[[estimate-page-schemas-one-file-per-rule]]"]
supersedes: ["[[decision-case-829]]"]
origin: raw/2026-10-16/2104/ledger.md#case-867
sprint: plugin
created: 2026-10-16
tags: [harness, render, schema]
---

## Problem

The `method` of `estimate-page-schemas-one-file-per-rule` has no form that lint accepts on the Estimate of a MOC. Its defer points at an archived Decision page, so the item stays in the backlog.

## Recommend

- **What should the `method` of `estimate-page-schemas-one-file-per-rule` say?**
  - Recommended: (a) `pytest` over the four test files that cover the promise, then `guppi check`.
  - Answer: agreed, (a).
- **How is the fix checked?**
  - Recommended: (a) the existing check covers it: `estimate-lint-checks-the-method`, whose Criterion stands.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-867
