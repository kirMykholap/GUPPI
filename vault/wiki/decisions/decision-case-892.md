---
type: decision
case: "892"
status: current
update: ["[[estimate-clean-branch-code-holds-pointers-only-in-brackets]]"]
origin: raw/2026-10-28/1907/ledger.md#case-892
sprint: plugin
created: 2026-10-28
tags: [ci, plugin]
---

## Problem

A docstring and a comment of `.guppi/tests/test_casecheck.py` name test data as `Case 5`, outside a bracket. `guppi ship --check` flags them, and `guppi check` reports them. No Estimate promises that the test files pass this check.

## Recommend

- **How are the two lines reworded?**
  - Recommended: (a) name the Case without its number, as the sibling Case.
  - Answer: agreed, (a).
- **Which Estimate checks the fix?**
  - Recommended: (a) widen the Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets` to cover `.guppi/tests/`.
  - Answer: agreed, (a).
- **Does this Case also stop a new test from bringing the defect back?**
  - Recommended: (a) fix the two lines only.
  - Answer: agreed, (a).

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#case-892
