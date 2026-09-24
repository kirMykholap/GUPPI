---
type: decision
case: "389"
status: current
defer: ["[[rule-case-protocol]]"]
origin: raw/2026-09-23/1859/ledger.md#case-389
sprint: migration
created: 2026-09-23
tags: [session, workflow, ledger]
---

## Context

By Case 387.2 the `Stop` hook of `rule-spec-write` writes a Case into the Spec only after a reply whose `LEDGER` block holds that Case's decision lines. At the re-ratification of Cases 384–388 in session 1859 the agent wrote no `LEDGER` block: the lines were the same, and the ledger hook skips a line it already holds. With the hook live, that re-ratification would not have reached the Spec. The Case schema does not say that the acknowledging reply of a re-ratification carries the `LEDGER` block again.

## Problem

A re-ratified Case can stay out of the Spec, because the schema lets the acknowledging reply of a re-ratification go without its `LEDGER` block.

## Deferred

### [[rule-case-protocol]]

The acknowledging reply of a re-ratification carries the LEDGER block with the Case's lines again, so the hook of rule-spec-write writes it

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-389
