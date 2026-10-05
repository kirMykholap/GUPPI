---
type: decision
case: "648"
status: current
defer: ["[[rule-prespec-onward]]"]
origin: raw/2026-10-05/0311/ledger.md#case-648
sprint: migration
created: 2026-10-05
tags: [session, workflow, hooks, harness]
---

## Context

At the `/pre-spec` of session 0109 the hook `guppi onward --plan` said that the Cases built again on the findings were ratified, after the reply of the defer 643 and before any Case had been sent back to its `case-guppi`: it judged the loop after the findings ended while it had not started (handoff of 0109, For the next session).

## Problem

No Case of session 0311 decides whether this is a bug of the hook of `rule-prespec-onward`.

## Deferred

### [[rule-prespec-onward]]

Prevents Plan Mode from stopping where no person is needed; its hook guppi onward --plan judged the loop after the findings of /pre-spec ended before it started in session 0109, put off by session 0311

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#case-648
