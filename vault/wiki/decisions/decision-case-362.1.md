---
type: decision
case: "362.1"
status: current
update: ["[[rule-lint]]", "[[estimate-lint-catches]]", "[[estimate-decisions-schema-checked]]", "[[estimate-entities-schema-checked]]", "[[estimate-estimates-schema-checked]]", "[[estimate-insights-schema-checked]]", "[[estimate-lessons-schema-checked]]", "[[estimate-rules-schema-checked]]", "[[estimate-page-schemas-one-file-per-rule]]"]
origin: raw/2026-09-23/0034/ledger.md#case-362.1
sprint: migration
created: 2026-09-23
tags: [harness, workflow, render, schema]
---

## Context

Lint takes the shape of a page from the `schema.yaml` of its category: `required`, `optional`, `values`, `conditional`. None of these keys says a field holds one link and not a list. A list under `addressed_by` passes lint without a word: the field stands in `LINK_FIELDS`, and lint checks only that each slug exists. Since 361 a list is not a shape of that field, and nothing refuses it mechanically.
`rule-lint` stands `draft`, its classes described in the docstring of `guppi/lint.py`; its Estimate `estimate-lint-catches` stands `pending` and is touched. `rule-insights-schema` stands `built`; the live reading of its Render is `estimate-insights-schema-checked`, touched, which 361 changes too.

## Problem

The shape "one link" is written in the schema in words, while lint reads keys only, so a list passes with no finding.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-362.1
