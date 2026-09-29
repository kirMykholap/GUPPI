---
type: decision
case: "533"
status: current
defer: ["[[rule-carry-over]]"]
origin: raw/2026-09-30/0138/ledger.md#case-533
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, render]
---

## Context

`/carry` rewrites `vault/wiki/brief.md` in the short shape. Step 1 of `rule-carry-over` (case 451.9) leaves out Readings due and Next session, on the claim that `make lint` of the finishing session lists the pending Estimates again. `/hi` takes its Work list only from the Next session of the brief. After the `/carry` of session 2024, the `/hi` of session 0138 had no Work list: the 38 open W lines of the 2024 Frontier and the Readings due of the brief of 1c196e8 stood on no list, and they were restored by hand into the Frontier of 0138. Case 531.10 of the conserved Spec of 2024 keeps the short shape without Next session. The person put the item off at the close of Plan Mode in session 0138.

## Problem

A session after `/carry` starts with no Work list, and the open readings drop out of sight.

## Deferred

### [[rule-carry-over]]

The short brief of /carry keeps the Work list, so the /hi after a conserved Spec finds the open readings and W lines; put off in session 0138

## History

- 2026-09-30 created · raw/2026-09-30/0138/ledger.md#case-533
