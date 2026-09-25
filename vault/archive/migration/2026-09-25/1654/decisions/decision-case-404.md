---
type: decision
case: "404"
status: archived
defer: ["[[rule-context-size]]"]
superseded_by: ["[[decision-case-430]]"]
origin: raw/2026-09-24/1916/ledger.md#case-404
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Context

Case 392.2 set a limit of 400 000 tokens, a constant in `guppi/context.py`: past it the `Stop` hook adds a warning to the size line, and the `UserPromptSubmit` hook orders the session closed with `/retro` and `/handoff`. The person proposed the figure as one to discuss. In session 1916 the limit was never reached; there is no data yet to move it up or down.

## Problem

Which limit is right: decided once a session reaches it and the behaviour of the context near it is seen.

## Deferred

### [[rule-context-size]]

The limit of 400 000 tokens in guppi/context.py, proposed as a figure to discuss; judged once a session reaches it

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-404
- 2026-09-25 superseded by decision-case-430 · [[decision-case-430]]
- 2026-09-25 archived · superseded
- 2026-09-25 archived · cleanup
