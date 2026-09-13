---
type: decision
case: "106"
status: current
defer: [rule-skill-hi]
supersedes: [decision-case-98]
origin: raw/2026-09-13/ledger.md#case-106
sprint: migration
created: 2026-09-13
tags: [session, harness]
---

## Context

`git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the pull brings is rendered only at the following session start. Case 89 puts the render in the librarian's phase and leaves this half open. Deferred as 98 in session K.

## Problem

The render has to run once more after the pull, inside `/hi`. It waits for the pull itself, which has no upstream to pull from yet (sprint, Slice 5).

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-106
