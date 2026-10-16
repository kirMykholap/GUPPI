---
type: decision
case: "877"
status: current
children: ["[[decision-case-877.1]]", "[[decision-case-877.2]]"]
origin: raw/2026-10-17/0027/ledger.md#case-877
sprint: plugin
created: 2026-10-17
tags: [harness, render, schema, workflow]
---

## Problem

Lint and pre-spec refuse `guppi test` alone on the Estimate of a MOC with no parent, whose own check is the whole suite, and the question of Case 873 stays open in the backlog.

## Recommend

- **May the Estimate of a MOC name `guppi test` alone?**
  - Recommended: (a) only a MOC with no parent.
  - Answer: agreed, (a).
- **Which project commands may a top MOC name alone?**
  - Recommended: (a) `guppi test` only.
  - Answer: agreed, (a).
- **Does `estimate-guppi-tests-green` go back to `guppi test` alone?**
  - Recommended: (a) keep it as it is.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) replace the Criterion of both Estimates, one sub-case each.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-17/0027/ledger.md#case-877
