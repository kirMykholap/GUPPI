---
type: decision
case: "1069"
status: current
children: ["[[decision-case-1069.1]]", "[[decision-case-1069.2]]"]
origin: raw/2026-11-26/1515/ledger.md#case-1069
sprint: plugin
created: 2026-11-26
tags: [hooks, harness, session, render, orchestration, workflow]
---

## Problem

The hook that keeps the box and the closer of a Frontier line together reads only edits, so a shell command can tick a box alone, and an edit can do the same, and the line stands half closed.

## Recommend

- **Which shell calls on frontier.md the guard refuses**
  - Recommended: (a) refuse every Bash or PowerShell command that names `frontier.md`, reads too, before it runs.
  - Answer: agreed, (a).
- **Whether an edit that ticks the box alone is refused too**
  - Recommended: (a) refuse a closed box with no closer as well, by one function that the check of `/pre-spec` and the hook share.
  - Answer: agreed, (a).

## History

- 2026-11-26 created · raw/2026-11-26/1515/ledger.md#case-1069
