---
type: decision
case: "880"
status: current
children: ["[[decision-case-880.1]]", "[[decision-case-880.2]]", "[[decision-case-880.3]]", "[[decision-case-880.4]]", "[[decision-case-880.5]]", "[[decision-case-880.6]]", "[[decision-case-880.7]]", "[[decision-case-880.8]]", "[[decision-case-880.9]]", "[[decision-case-880.10]]", "[[decision-case-880.11]]", "[[decision-case-880.12]]", "[[decision-case-880.13]]", "[[decision-case-880.14]]", "[[decision-case-880.15]]", "[[decision-case-880.16]]", "[[decision-case-880.17]]", "[[decision-case-880.18]]", "[[decision-case-880.19]]", "[[decision-case-880.20]]", "[[decision-case-880.21]]"]
origin: raw/2026-10-17/1805/ledger.md#case-880
sprint: plugin
created: 2026-10-17
tags: [git, github, harness, plugin, session, workflow, render, tests, hooks, ci, ledger, librarian, sprint]
---

## Problem

The clean version of GUPPI ships Criteria of `passed` Estimates with sentences that hold only in the repository of GUPPI, so a new project reads promises that are false there or point to pages it does not hold; each fix replaces a Criterion whole and sets its Estimate `pending`.

## Recommend

- **How does a Criterion sentence that holds only in GUPPI change?**
  - Recommended: (a) replace each Criterion whole.
  - Answer: agreed, (a).
- **How much does this Case take?**
  - Recommended: (b) only the Estimates whose reading this session can take.
  - Answer: agreed, (b).
- **What happens to a check that is meant to hold only in GUPPI?**
  - Recommended: (b) move the GUPPI part into a new Estimate on `entity-guppi-repository`.
  - Answer: agreed, (b).
- **How is a sentence reworded?**
  - Recommended: (a) the same way as the last session.
  - Answer: agreed, (a).
- **Is a pointer to an Estimate that is still `pending` reworded?**
  - Recommended: (b) keep these pointers, and leave the six out of this Case.
  - Answer: agreed, (b).
- **What happens to the promise that git ignores the event log?**
  - Recommended: (b) leave both Estimates out of this Case, and name the gap for `rule-clean-branch`.
  - Answer: agreed, (b).
- **What happens to the temporary old path in the Case check?**
  - Recommended: (b) leave this Estimate out of this Case.
  - Answer: agreed, (b).
- **What happens to the other facts that hold only in GUPPI?**
  - Recommended: (b) say the first by role, drop the second, move the third.
  - Answer: agreed, (b).
- **What happens to the put-off on `rule-clean-branch`?**
  - Recommended: (b) take it up and put it off again, naming only what is left.
  - Answer: agreed, (b).

## History

- 2026-10-17 created · raw/2026-10-17/1805/ledger.md#case-880
