---
type: decision
case: "919"
status: current
children: ["[[decision-case-919.1]]", "[[decision-case-919.2]]"]
origin: raw/2026-10-30/0304/ledger.md#case-919
sprint: plugin
created: 2026-10-30
tags: [plugin, tests, ci, git]
---

## Problem

A test docstring holds a pointer to a case outside a bracket, so `guppi check` is red and the clean version would carry it; and no step before the librarian's run judges the code and the tests for such a pointer, so the next one is found as late as this one.

## Recommend

- **How should the docstring be fixed?**
  - Recommended: (a) move the pointer into a bracket at the end of the sentence.
  - Answer: agreed, (a).
- **How should the fix be checked?**
  - Recommended: (a) set `estimate-clean-branch-code-holds-pointers-only-in-brackets` back to `pending`, its Criterion unchanged, and read it at Retro.
  - Answer: agreed, (a).
- **Should the Case also add a guard against a repeat?**
  - Recommended: (a) fix this one docstring only.
  - Answer: (b), also add a test that runs the pointer check over the live `.guppi/` folder.
- **What should the guard test judge, and how does it run?**
  - Recommended: (a) an unmarked test over the files of `.guppi/` alone, by `judged` of `.guppi/guppi/ship.py`, with no read of the vault.
  - Answer: agreed, (a).
- **How should the guard be checked?**
  - Recommended: (a) a new Estimate on `rule-clean-branch`.
  - Answer: agreed, (a).
- **Should `rule-clean-branch` say that the guard exists?**
  - Recommended: (a) add one sentence after the passage on `guppi ship --check`.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-30/0304/ledger.md#case-919
