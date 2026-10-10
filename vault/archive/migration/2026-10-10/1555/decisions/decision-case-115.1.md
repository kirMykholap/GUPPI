---
type: decision
case: "115.1"
status: archived
update: ["[[rule-render-harness]]"]
origin: raw/2026-09-14/0747/ledger.md#case-115.1
sprint: migration
created: 2026-09-14
tags: [harness, render]
---

## Context

`git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the pull brings is rendered only at the following session start. Case 89 puts the render in the librarian's phase and leaves this half open. Deferred as 98 in session K. (Case 106 as it stands.)

## Problem

The render has to run once more after the pull, inside `/hi`. It waits for the pull itself, which has no upstream to pull from yet (sprint, Slice 5). (Case 106 as it stands.)

## Given

`rule-render-harness` How it works, line 27: "`--sync`, the `SessionStart` hook, prints a unified diff for each differing file … so the agent's first turn shows what the render changed". With 115 the same command runs a second time inside `/hi`, after the pull. `contract: same`: the two Estimates of the page check the render and the report, not where `--sync` is called from.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-115.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
