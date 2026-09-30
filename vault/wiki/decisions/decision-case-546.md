---
type: decision
case: "546"
status: current
defer: ["[[rule-orchestration]]"]
supersedes: ["[[decision-case-545]]"]
origin: raw/2026-09-30/1306/ledger.md#case-546
sprint: migration
created: 2026-09-30
tags: []
---

## Context

The question shape of the skill `grill-me` governs a round of `case-guppi`. No rule names that shape for a question the main agent asks the person itself. In session 0248 the main agent asked the person the questions of a pre-spec report in its own shape (`lesson-prespec-report-decisions-off-the-question-shape`). Case 545 deferred this to `rule-skill-grill-me`, which Case 543.2 of the same plan updates; the defer moves to `rule-orchestration`, the rule put off for the orchestration of the main agent.

## Problem

A question the main agent puts to the person outside a round of `case-guppi` — in a pre-spec report, at `/hi` or in Work Mode — follows no shape, so its options and its recommendation read differently from a round.

## Deferred

### [[rule-orchestration]]

The orchestration of the main agent — the triage of a Frontier item, the dispatch of case-guppi, the acknowledging reply, LEDGER, defers and the one rule — as a rule of its own loaded by /hi, and case-schema.md read by case-guppi alone

## History

- 2026-09-30 created · raw/2026-09-30/1306/ledger.md#case-546
