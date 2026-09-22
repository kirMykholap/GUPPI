---
type: decision
case: "336"
status: archived
update: ["[[rule-estimates-schema]]", "[[estimate-estimates-schema-checked]]"]
supersedes: ["[[decision-case-330.2]]"]
superseded_by: ["[[decision-case-343]]"]
origin: raw/2026-09-22/1724/ledger.md#case-336
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Context

The description of the field `method` in the Render of `rule-estimates-schema` gives an example, not a list, and does not say that one of the forms must stand; the agent writing a `create` guesses. Case 330.2 set out to repair that, but its text carried two errors: it counted the forms as three where lint and case 331 of the same Spec count four, and it promised a finding of the class `method` to a page that names none — while a page with no `method` field at all is counted `unmigrated`, not `method`. Both came from `/pre-spec`.
`rule-estimates-schema` renders `vault/wiki/estimates/schema.yaml`. Its live reading is `estimate-estimates-schema-checked`, `passed`, whose Criterion opens "The file equals the Render": a change to the Render asks for it to be read again (case 187), and 330.2 named it nowhere — the third finding.

## Problem

The set of forms is written as a set nowhere, and the attempt to write it parted company with the code on the count and overpromised in its consequence. The Estimate of the live reading of that same Render is not named.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-336
- 2026-09-23 superseded by decision-case-343 · [[decision-case-343]]
- 2026-09-23 archived · superseded
- 2026-09-23 archived · cleanup
