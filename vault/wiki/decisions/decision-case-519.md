---
type: decision
case: "519"
status: current
defer: ["[[rule-estimates-schema]]"]
origin: raw/2026-09-29/1432/ledger.md#case-519
sprint: migration
created: 2026-09-29
tags: [harness, render, schema]
---

## Context

Case 513 of session 1432 moved the frame of a Case, its `given`, off the Decision page into the Case file. The Render of `rule-estimates-schema` still says, in the description of `## Criterion` in `vault/wiki/estimates/schema.yaml`: "no `Given:`: the frame of the Case stays on its Decision page (case 378.2)". /pre-spec did not find it; Work Mode did, while it read the schema for a reading. Retro ratifies no update.

## Problem

The sentence says the frame of a Case stays on its Decision page, which is false for every Case after case 513.

## Deferred

### [[rule-estimates-schema]]

Correct the description of

## History

- 2026-09-29 created · raw/2026-09-29/1432/ledger.md#case-519
