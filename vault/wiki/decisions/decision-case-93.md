---
type: decision
case: "93"
status: current
defer: [rule-work-mode, rule-subagent-guppi]
supersedes: [decision-case-78]
origin: raw/2026-09-12/ledger.md#case-93
sprint: migration
created: 2026-09-12
tags: []
---

## Context

`rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, now
78, without `kind`, `estimates` or `tags`; two of lint's three orphans. The draft in
`docs/migration/` still has to be reconciled with case 59.3 — no separate `plan.md`, the
`tasks` blocks of the Spec — and with the fork clause.

## Problem

The phase the harness spends most of its time in is the one phase with no ratified rule.
It needs a Plan Mode of its own, not a corner of this one.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-93
