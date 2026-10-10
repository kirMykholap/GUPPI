---
type: decision
case: "361"
status: archived
update: ["[[rule-insights-schema]]", "[[estimate-insights-schema-checked]]"]
origin: raw/2026-09-23/0034/ledger.md#case-361
sprint: migration
created: 2026-09-23
tags: [harness, render, schema]
---

## Context

By the schema `addressed_by` is one link to the decision that fixed or rejected the pattern. A new lesson that reopens the Insight keeps the field; by case 284.4 the librarian's `update` moves the field to the decision of its own unit when that decision closed the cause. Case 332.2, later superseded, promised two decisions in `addressed_by`, and the brief warned that the move of 284.4 would cut a list of two to one link without a word. All 15 `actioned` Insights of the vault carry one link today.
`rule-insights-schema` stands `built`, its Render `vault/wiki/insights/schema.yaml`; the live reading of that Render is `estimate-insights-schema-checked`, `passed`, and it is touched.

## Problem

The schema names one link but does not say which decision it names when the pattern was closed twice, or where the earlier one goes; a Case once wrote a list there, and the move of 284.4 would drop it without a trace.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-361
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
