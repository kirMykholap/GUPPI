---
type: decision
case: "1085"
status: current
children: ["[[decision-case-1085.1]]", "[[decision-case-1085.2]]", "[[decision-case-1085.3]]", "[[decision-case-1085.4]]", "[[decision-case-1085.5]]", "[[decision-case-1085.6]]", "[[decision-case-1085.7]]", "[[decision-case-1085.8]]", "[[decision-case-1085.9]]"]
origin: raw/2026-11-27/1402/ledger.md#case-1085
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow, session, render, ledger, sprint, librarian]
---

## Problem

The map of the plan shows each task with a sign and no box, and no tick of Work Mode or of the librarian's run reaches the map of the plan file or the copy in `spec.md`, so the person cannot follow the progress of the Spec on the map.

## Recommend

- **Where the map with live boxes stands after the approval**
  - Recommended: (b) `spec.md` only, its maps rebuilt from its Cases, the map of the plan file kept as approved.
  - Answer: (c) both; the main idea is to see the boxes in the plan file.
- **When a box of the map follows a tick**
  - Recommended: (b) at once after each edit of `spec.md`, by a new hook that runs after the edit.
  - Answer: agreed, (b).
- **How a line of the map shows its box**
  - Recommended: (a) the box takes the place of ✅, with ⛔ and 🔍 after an open box.
  - Answer: agreed, (a).
- **Whether the librarian's ticks reach the maps**
  - Recommended: (a) the scripts rebuild the map of each `spec.md` they tick; the plan file keeps the boxes as Work Mode left them.
  - Answer: agreed, (a).
- **How the boxes in the plan file are checked as you see them**
  - Recommended: (b) keep the open check of the plan view, and add a new check for the boxes, read by the person's answer in the next session.
  - Answer: agreed, (b).

## History

- 2026-11-27 created · raw/2026-11-27/1402/ledger.md#case-1085
