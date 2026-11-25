---
type: decision
case: "1045"
status: current
create: ["[[estimate-event-log-keeps-the-whole-path]]"]
origin: raw/2026-11-25/0605/ledger.md#case-1045
sprint: plugin
created: 2026-11-25
tags: [session, hooks, harness]
---

## Problem

The event log cuts a file path at 80 characters, and the plan file of a session now has a longer path, so `plan_path` finds no plan file and each hook that needs it, `guppi caseid` first, fails or passes with nothing to check.

## Recommend

- **How the event log keeps a path**
  - Recommended: (a) a file path stays whole; shell commands, patterns and the other details are still cut at 80 characters.
  - Answer: agreed, (a).
- **A plan file that a subagent writes**
  - Recommended: (a) left out of this Case, since the guard lets through only a title line of a new plan file and no such line was ever logged, and the naming of those files is not in the Claude Code documentation.
  - Answer: agreed, (a).

## History

- 2026-11-25 created · raw/2026-11-25/0605/ledger.md#case-1045
