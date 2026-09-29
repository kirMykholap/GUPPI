---
type: decision
case: "522"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-29/1753/ledger.md#case-522
sprint: migration
created: 2026-09-29
tags: [harness, workflow, ledger]
---

## Problem

A repeat applies nothing, but it ticks a line of the Spec, and no promise names that tick. When a Case's section holds a second line of the same kind and slug, the repeat marks it as done although nobody did its work. A repeated `delete` can also tick a `read` line of a Case ratified after the first `delete`.

## History

- 2026-09-29 created · raw/2026-09-29/1753/ledger.md#case-522
