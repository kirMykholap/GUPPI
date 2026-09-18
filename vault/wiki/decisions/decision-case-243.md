---
type: decision
case: "243"
status: current
defer: ["[[rule-git-context]]", "[[rule-github-issues]]"]
origin: raw/2026-09-18/1252/ledger.md#case-243
sprint: migration
created: 2026-09-18
tags: [session, harness, git, github]
---

## Context

`git pull` at `/hi` fails without an upstream of `migration` (decision 11.1), and `gh` is not logged in with no GitHub remote (11.2); both are printed lines of `/hi`, items of every Frontier, deferred by case 220 to the close of the sprint and read by `estimate-sprint-migration-leftovers-gone`. Nothing changed in session 1252: the same two lines, the same decision.

## Problem

The decision stands at the close of the sprint, Slice 5, and the Frontier lists the two lines every session until then.

## Deferred

### [[rule-git-context]]

the pull without an upstream at /hi — set the upstream of migration, or keep the printed failure as decision 11.1 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone

### [[rule-github-issues]]

gh not logged in, no GitHub remote — log in and add the remote, or keep the printed line as decision 11.2 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-243
