---
type: decision
case: "71.1"
status: current
create: [estimate-governed-files-hook-refuses, estimate-claude-md-rendered]
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Context

Cases 59.6 and 59.8 (session I) created `rule-governed-files-hook` and `rule-claude-md`,
each with a nested `estimate` in its `then` block: `estimate-governed-files-hook-refuses`
and `estimate-claude-md-rendered`, criterion and method ratified there. Neither got a
paired `create` line, so neither has a yaml entry or a page; both Rule pages carry
`estimates: []` and cannot become `built`. The brief names this under "What the next
session does first", item 3. Recorded as
`lesson-pretask-nested-estimate-exempt-from-the-line-check`.

## Problem

Two decisions: how the two pages come to exist now, and how a Leaf's nested Estimate
reaches the yaml without a step the agent can forget.

## Given

`index.md` §5: a Leaf `create` also logs a paired `create` for its Estimate; §3 "Paired
Estimate on create" shows the two lines. `materialize.find_item` reads the nested block
only for a decision line with the Estimate's slug (test
`test_the_nested_estimate_is_its_own_create_entry`, seeded with that line).
**＋** `pretask.items_of` marks a nested `estimate` as `nested: True`, "covered by its
parent's line since case 53.1"; Case 53.1 says "a lesson entry writes the lesson only;
no paired Estimate" and nothing about Leaf creates.
**＋** `rule-pretask` Render: "It prints one line for every decision line of this session
that has no item under its own Case in the plan, for every item that has no line, …".
`estimate-pretask-reconciles` Criterion: "a line without an item, an item without a
line, and an item under another sub-case's heading are each one finding, exit 1".
**＋** `generate` on a `create` of category `estimates` with `ref` appends the slug to
the target's `estimates` and its `## Estimates` section (`generate.py` lines 278–281,
335–341). Both slugs are free in `wiki/` and `archived/`.
**＋** Tags: `rule-governed-files-hook` [hooks, harness, render], `rule-claude-md`
[harness, render]; the Estimates take their Rule's tags, as a nested one would.
**－** Case 68 (deferred) is the other wording of `rule-pretask`, the `defer`-only
exemption; this Case does not touch it.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-71.1
