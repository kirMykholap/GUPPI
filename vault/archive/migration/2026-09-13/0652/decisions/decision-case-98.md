---
type: decision
case: "98"
status: archived
defer: [rule-skill-hi]
superseded_by: [decision-case-106]
origin: raw/2026-09-12/ledger.md#case-98
sprint: migration
created: 2026-09-12
tags: [session, harness]
---

## Context

`git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the
pull brings is rendered only at the following session start. Case 89 puts the render in
the librarian's phase and leaves this half open.

## Problem

The render has to run once more after the pull, inside `/hi`. It waits for the pull
itself, which has no upstream to pull from yet (sprint, Slice 5).

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-98
- 2026-09-13 superseded by decision-case-106 · [[decision-case-106]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
