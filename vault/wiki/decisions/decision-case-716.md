---
type: decision
case: "716"
status: current
children: ["[[decision-case-716.1]]", "[[decision-case-716.2]]"]
origin: raw/2026-10-07/1804/ledger.md#case-716
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Problem

The two Estimates of `case-guppi` stand `failed` after every Case that changes them. Their `method` waits for dispatches or a `/pre-spec` after the render, which come only in a later session, and partly for kinds of dispatch that seldom happen.

## Recommend

- **How wide should the fix be?**
  - Recommended: (a) fix this check's method only: Retro reads the new text of the agent's instructions against the promise, in the session that changes it.
  - Answer: agreed, (a).
- **Does the fix also cover the second hanging check of `case-guppi`?**
  - Recommended: (a) yes, one Case fixes both checks.
  - Answer: agreed, (a).
- **How does the check leave `failed` now?**
  - Recommended: (a) set it back to `pending` with its promise unchanged, and this session's Retro reads it.
  - Answer: agreed, (a).
- **Does the check still record the tokens and seconds of each call?**
  - Recommended: (a) keep it: the reading line also gives the tokens and seconds of this session's calls, when there were any.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-716
