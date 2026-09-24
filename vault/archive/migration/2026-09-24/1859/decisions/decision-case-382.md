---
type: decision
case: "382"
status: archived
defer: ["[[rule-bash-guard]]"]
superseded_by: ["[[decision-case-384]]"]
origin: raw/2026-09-23/1355/ledger.md#case-382
sprint: migration
created: 2026-09-23
tags: [hooks, harness]
---

## Context

`rule-bash-guard` refuses a heredoc with a backslash and sends the agent to Write. The agent follows it, and at every Retro reports the refusal as a finding. The refusal is the behaviour the hook was made for, so these reports are noise.

## Problem

The message of the hook does not say that the refusal is legal and needs no report, so the agent takes it for an event of the session each time.

## Deferred

### [[rule-bash-guard]]

The refusal message says the refusal is by design — use Write, and do not report it at Retro

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-382
- 2026-09-24 superseded by decision-case-384 · [[decision-case-384]]
- 2026-09-24 archived · superseded
- 2026-09-24 archived · cleanup
