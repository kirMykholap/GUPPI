---
type: decision
case: "115.2"
status: current
update: ["[[rule-skill-hi]]"]
origin: raw/2026-09-14/0747/ledger.md#case-115.2
sprint: migration
created: 2026-09-14
tags: [session, harness]
---

## Context

`git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the pull brings is rendered only at the following session start. Case 89 puts the render in the librarian's phase and leaves this half open. Deferred as 98 in session K. (Case 106 as it stands.)

## Problem

The render has to run once more after the pull, inside `/hi`. It waits for the pull itself, which has no upstream to pull from yet (sprint, Slice 5). (Case 106 as it stands.)

## Given

`rule-skill-hi` body, line 45 (rendered as `.claude/skills/hi/SKILL.md:30`): "what `guppi render --sync` printed at session start is an item when it shows a hand edit". The `Render:` line of 115 is a second output of the same command inside the skill. `contract: same`: the two Estimates of the page are about read calls and the Frontier file. 111.4 updates the same page; two entries in ledger order.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-115.2
