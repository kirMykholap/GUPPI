---
type: decision
case: "1042"
status: current
children: ["[[decision-case-1042.1]]", "[[decision-case-1042.2]]"]
origin: raw/2026-11-20/1353/ledger.md#case-1042
sprint: plugin
created: 2026-11-20
tags: [ci, plugin, tests, git]
---

## Problem

A clean version whose style check or tests fail can reach `prod`, and nobody has run the suite on Linux, the system of the job that writes `prod`.

## Recommend

- **What the run checks before it commits**
  - Recommended: (b) the two copy tests of `test_ship.py`, `-k own_style` and `-m live -k own_tests`.
  - Answer: agreed, (b).
- **On which system the check runs**
  - Recommended: (a) a step in the same Linux job, before the commit.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) a new Estimate for the workflow, and the old Criterion replaced without its line on `prod.yml`.
  - Answer: agreed, (a).

## History

- 2026-11-23 created · raw/2026-11-20/1353/ledger.md#case-1042
