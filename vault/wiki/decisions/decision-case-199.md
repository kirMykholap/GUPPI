---
type: decision
case: "199"
status: current
update: [estimates-schema]
origin: raw/2026-09-16/1651/ledger.md#case-199
sprint: migration
created: 2026-09-16
tags: []
---

## Context

`estimates/schema.md` describes `## Result`: omitted while `pending`, one line for QA, the substance of the page for Research; overwritten, never appended. Case 193 rewrote the table and the Criterion but said of the content of Result only "overwritten". Point 11 of the model: a reading is the line `estimate[slug][passed|failed] text`, the date and the command are the first line of Result; Result is about one run of one check. Today the date of a reading shows only in History, the command nowhere but in `method`, which need not repeat it. This Case touches no Estimate: a Rule-class file.

## Problem

A reader of Result does not know when and by what it was checked: "tests green (379)" without a date and a command is an opinion, not a result. Point 11 did not enter 193.

## Given

The `estimate[...]` line is written by the agent at the moment of the reading; `generate` puts its text into `## Result` whole.
**－** `schema.yaml` does not change: the same section, the same requiredness.

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#case-199
