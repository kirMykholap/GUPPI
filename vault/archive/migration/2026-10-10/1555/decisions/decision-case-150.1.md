---
type: decision
case: "150.1"
status: archived
update: ["[[rule-claude-md]]"]
origin: raw/2026-09-14/1633/ledger.md#case-150.1
sprint: migration
created: 2026-09-14
tags: [harness, render]
---

## Context

The lesson of O: `retro/SKILL.md` carries `disable-model-invocation: true`; a typed `/retro` is expanded as a prompt, the Skill tool is not called, `guppi gate` does not see it — neither the check of 122 nor the `retro` mark; `rule-event-log` and `gate.MARKS` promise three marks, the second never appears.

## Problem

The owner allows the agent to start the Retro itself after Work Mode: the Retro stops at the lessons and the readings anyway, and `/handoff` stands behind the gate. Decide: remove the flag — one mechanism for the three skills, no code change.

## Given

The Render, line 62: "`/retro` (the person), `/handoff` (the agent, …)". After 150 the agent may call `/retro` itself (pre-task).

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-150.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
