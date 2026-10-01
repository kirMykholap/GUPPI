---
type: decision
case: "575"
status: current
defer: ["[[rule-prespec-onward]]"]
origin: raw/2026-10-01/1237/ledger.md#case-575
sprint: migration
created: 2026-10-01
tags: [session, workflow, hooks, harness]
---

## Context

`guppi onward --plan`, the hook of `rule-prespec-onward`, finds a Case still out by the time of its file against its last decision line in `ledger.md`. A Case built again and ratified with lines the ledger already holds adds no line, so the hook stays silent after it (handoff of session 2356, Observations). The person put the remaining items off to go to work.

## Problem

The decision on what else the hook should judge a Case still out by is put off.

## Deferred

### [[rule-prespec-onward]]

Whether guppi onward --plan judges a Case still out by something other than the ledger's last decision line, since a re-ratification with unchanged lines adds none and the hook then stays silent

## History

- 2026-10-01 created · raw/2026-10-01/1237/ledger.md#case-575
