---
type: decision
case: "565"
status: current
defer: ["[[rule-spec-box]]"]
origin: raw/2026-09-30/2356/ledger.md#case-565
sprint: migration
created: 2026-09-30
tags: [session, workflow, git, harness]
---

## Context

`make lint` reports three findings on `rule-spec-box`: missing field `kind`, missing field `estimates`, and no other live page names it. It also reports one finding on `decision-case-13`: a code fence is still open at the end of `## When`. The fix of the fence has no page of its own to defer. It goes with this item. The person put the remaining items off to go to work.

## Problem

The fix of the four lint findings is put off to a later session.

## Deferred

### [[rule-spec-box]]

The lint findings that stand, missing kind, missing estimates and orphan on rule-spec-box, and the fence open at the end of the When section of decision-case-13, are fixed in a later session

## History

- 2026-10-01 created · raw/2026-09-30/2356/ledger.md#case-565
