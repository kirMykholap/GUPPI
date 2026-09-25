---
type: decision
case: "418"
status: current
defer: ["[[rule-context-size]]"]
origin: raw/2026-09-25/0051/ledger.md#case-418
sprint: migration
created: 2026-09-25
tags: [hooks, harness, session]
---

## Context

Cases 404 and 409 deferred the limit of 400 000 tokens in `guppi/context.py` and the text of the `UserPromptSubmit` hook past it: take no more work, not close the session. The session that would judge them has not come yet; this session did not take the item up.

## Problem

Which limit is right, and what the hook says past it: decided once a session reaches it.

## Deferred

### [[rule-context-size]]

The limit of 400 000 tokens in guppi/context.py, and the text of the UserPromptSubmit hook past it — take no more work, not close the session; judged once a session reaches it

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#case-418
