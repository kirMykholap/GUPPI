---
type: decision
case: "570"
status: archived
defer: ["[[rule-case-rebuild-cost]]"]
superseded_by: ["[[decision-case-629.2]]"]
origin: raw/2026-10-01/1237/ledger.md#case-570
sprint: migration
created: 2026-10-01
tags: []
---

## Context

`rule-case-rebuild-cost` holds the defer of case 566: a Case is rewritten whole and returned whole to the main agent when only a sub-case changed. In session 1237 Cases 567, 568 and 569 were each built and returned whole again after the round. The person put the remaining items off to go to work.

## Problem

The decision on how a Case is rebuilt and returned is put off again.

## Deferred

### [[rule-case-rebuild-cost]]

Prevents a Case from being rewritten whole and returned whole into the main agent's context when only a sub-case changed, and its context from listing searches that change nothing; options from session 2356 - the SubagentStop hook merges a changed sub-case into the stored answer, case-guppi writes the Case file itself and returns a short answer, the context keeps only what changes the decision, a large item split into several Cases

## History

- 2026-10-01 created · raw/2026-10-01/1237/ledger.md#case-570
- 2026-10-04 superseded by decision-case-629.2 · [[decision-case-629.2]]
- 2026-10-04 archived · superseded
- 2026-10-04 archived · cleanup
