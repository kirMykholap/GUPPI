---
type: decision
case: "409"
status: archived
defer: ["[[rule-context-size]]"]
superseded_by: ["[[decision-case-430]]"]
origin: raw/2026-09-24/2214/ledger.md#case-409
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Context

Case 404 deferred the limit of 400 000 tokens in `guppi/context.py`. The brief of session 1916 adds a second point on the same page: past the limit the `UserPromptSubmit` hook orders the session closed with `/retro` and `/handoff`, and the person reads the mark as "take no more work", not as a reason to leave Plan Mode for Retro. Both wait for a session that reaches the limit.

## Problem

Which limit is right, and what the hook says past it: decided once a session reaches it.

## Deferred

### [[rule-context-size]]

The limit of 400 000 tokens in guppi/context.py, and the text of the UserPromptSubmit hook past it — take no more work, not close the session; judged once a session reaches it

## History

- 2026-09-25 created · raw/2026-09-24/2214/ledger.md#case-409
- 2026-09-25 superseded by decision-case-430 · [[decision-case-430]]
- 2026-09-25 archived · superseded
- 2026-09-25 archived · cleanup
