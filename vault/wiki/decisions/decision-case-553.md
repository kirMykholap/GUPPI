---
type: decision
case: "553"
status: current
defer: ["[[rule-ask]]"]
origin: raw/2026-09-30/1736/ledger.md#case-553
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Context

At the pre-spec of session 1736, `ask-guppi` could not check a claim of Case 550 about `decision-case-538` and `decision-case-539`: its frame `.claude/agents/ask-guppi.md`, the Render of `rule-ask`, forbids opening `vault/wiki/decisions/` except for the `## Problem` of a page's `deferred_by` or a Decision reached through `origin`. `case-guppi` read the same pages while it built the Case. The check of a Case at pre-spec reads less of the vault than the builder of the Case, so a fact about a Decision page in a `context` goes unchecked. The person asked to put the fix off.

## Problem

The two agents that read the vault for a Case follow different rules on Decision pages, so a claim the builder reads from a Decision page cannot be checked at pre-spec.

## Deferred

### [[rule-ask]]

ask-guppi and case-guppi read Decision pages by one rule, so that a claim a Case makes about a Decision page can be checked at pre-spec; today case-guppi opens them and the frame of ask-guppi forbids it but for deferred_by and origin

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-553
