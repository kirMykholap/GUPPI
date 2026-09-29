---
type: decision
case: "521.1"
status: current
update: ["[[rule-spec-write]]", "[[estimate-spec-write-writes-a-defer]]"]
origin: raw/2026-09-29/1753/ledger.md#case-521.1
sprint: migration
created: 2026-09-29
tags: [hooks, harness, workflow, session]
---

## Problem

YAML cuts a value without quotes at ` #`, and no check sees the cut. So a short-form Case can reach the Spec, the Decision page and the backlog with a value the person never wrote, as the purpose of case 519 did. The backlog item of `rule-estimates-schema` also carries that cut text, and the sentence it was meant to correct is still wrong.

## History

- 2026-09-29 created · raw/2026-09-29/1753/ledger.md#case-521.1
