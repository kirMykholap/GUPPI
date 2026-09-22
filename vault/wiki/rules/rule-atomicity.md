---
type: rule
kind: Leaf
purpose: Prevents a unit from being split or kept whole by taste — one closing judgment, one unit; two conditions that fail apart are two children
status: draft
enforcement: render
governs: vault/wiki/case-schema.md
render_mode: partial
parent: "[[rule-case-protocol]]"
estimates: ["[[estimate-atomicity-rendered]]"]
origin: raw/2026-09-22/1121/ledger.md#case-317
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Purpose

Prevents a unit from being split or kept whole by taste. The rule cannot be checked in substance, so its guard is the one `rule-language` and `rule-agent-writing` have: the text stands in the file the agent reads — `case-schema.md`, loaded by `/hi` in every working session — and `render --check` keeps it identical to this page, while the governed-files hook refuses a hand edit. The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case with no written Criterion, signed for `rule-prespec`.

## Render

## Atomicity — when a unit splits

A unit stays whole as long as its closing act — ratification, a reading, `built` — is one indivisible judgment. The moment it breaks into two or more conditions that can fail independently and need different fixes, it splits into children.

The test is mechanical. List the conditions of "done". For each pair, ask: could one fail while the other passes, and would the fix be a different one? Yes for any pair — split.

It holds for a Case, an Entity, a Rule and an Estimate alike. Not for a Lesson: a recorded fact does not split. Not for an Insight: it is born by clustering, which is this rule running in reverse. Depth is not fixed in advance — it follows the rule and nothing else. Two conditions that are different behaviours are two children; the same behaviour checked from two angles is one page and two Estimates.

## History

- 2026-09-22 created · [[decision-case-317]]
