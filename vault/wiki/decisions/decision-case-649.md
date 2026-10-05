---
type: decision
case: "649"
status: current
defer: ["[[estimate-ask-searches-at-prespec]]"]
origin: raw/2026-10-05/0311/ledger.md#case-649
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Context

`estimate-ask-searches-at-prespec` failed at the `/hi` of session 0109 (L9): call 16 of an ask-guppi of session 2245 ran a Grep over `vault/wiki` with the glob `!decisions/**` and printed 29 lines of Decision pages. Case 640 put `.claude/rules/search-leaves-out-decisions.md` in place and set the method of the Estimate anew; its next reading waits for a `/pre-spec` after that render.

## Problem

The Estimate stands `failed`, and no Case of session 0311 takes it up before its reading again.

## Deferred

### [[estimate-ask-searches-at-prespec]]

Whether ask-guppi at /pre-spec greps the rules first and leaves vault/wiki/decisions/ out of every search but the two reasons its frame names; failed at L9 of session 0109, read again at a /pre-spec after the render by case 640; put off by session 0311

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#case-649
