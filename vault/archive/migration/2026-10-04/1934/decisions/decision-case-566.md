---
type: decision
case: "566"
status: archived
defer: ["[[rule-case-rebuild-cost]]"]
superseded_by: ["[[decision-case-629.2]]"]
origin: raw/2026-09-30/2356/ledger.md#case-566
sprint: migration
created: 2026-09-30
tags: []
---

## Context

In session 2356 `case-guppi` wrote Case 561, with fourteen sub-cases, whole three times: once to build it, and twice to change a few lines of 561.9. Each time the whole text came back into the context of the main agent. The main agent spent about 40 000 tokens to join two Cases. The `case-guppi` of Case 561 reached about 500 000 tokens by its usage line. Its last rebuild ran 7.7 minutes with no tool call. The `context` of a Case lists every search of the frame, those that changed nothing included. The person asked to take this up in the next session.

## Problem

A Case is rewritten whole, and returned whole to the main agent, when only a part of it changed. Its `context` also holds searches that change nothing.

## Deferred

### [[rule-case-rebuild-cost]]

Prevents a Case from being rewritten whole and returned whole into the main agent's context when only a sub-case changed, and its context from listing searches that change nothing; options from session 2356 - the SubagentStop hook merges a changed sub-case into the stored answer, case-guppi writes the Case file itself and returns a short answer, the context keeps only what changes the decision, a large item split into several Cases

## History

- 2026-10-01 created · raw/2026-09-30/2356/ledger.md#case-566
- 2026-10-04 superseded by decision-case-629.2 · [[decision-case-629.2]]
- 2026-10-04 archived · superseded
- 2026-10-04 archived · cleanup
