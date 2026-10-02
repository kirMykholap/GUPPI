---
type: rule
kind: Leaf
purpose: Prevents a unit from being split or kept whole by taste — one closing judgment, one unit; two conditions that fail apart are two children
status: built
enforcement: render
governs: vault/wiki/ratification.md
render_mode: partial
parent: "[[rule-ratification]]"
estimates: ["[[estimate-atomicity-rendered]]"]
origin: raw/2026-09-22/1121/ledger.md#case-317
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Purpose

Prevents a unit from being split or kept whole by taste. The rule cannot be checked in substance, so its guard is the one `rule-language` and `rule-agent-writing` have: the text stands in the file both agents read — `ratification.md`, loaded by `/hi` in every working session and read by `case-guppi` — and `render --check` keeps it identical to this page, while the governed-files hook refuses a hand edit. The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case that each set a new Criterion, written or lifted, signed for `rule-prespec` (case 472.3).

## Render

<!-- rule-atomicity -->
## Atomicity — when a unit splits

A unit stays whole as long as its closing act — ratification, a reading, `built` — is one indivisible judgment. The moment it breaks into two or more conditions that can fail independently and need different fixes, it splits into children.

The test is mechanical. List the conditions of "done". For each pair, ask: could one fail while the other passes, and would the fix be a different one? Yes for any pair — split.

It holds for a Case, an Entity, a Rule and an Estimate alike. Not for a Lesson: a recorded fact does not split. Not for an Insight: it is born by clustering, which is this rule running in reverse. Depth is not fixed in advance — it follows the rule and nothing else. Two conditions that are different behaviours are two children; the same behaviour checked from two angles is one page and two Estimates.
<!-- /rule-atomicity -->

## History

- 2026-09-22 created · [[decision-case-317]]
- 2026-09-23 updated: the Render carries its own markers, so the page renders into case-schema.md — the hand fix of commit 94277ea signed after the fact (case 324) · [[decision-case-324]]
- 2026-09-23 status: draft → built · cascade
- 2026-09-28 updated: the refusal of pre-spec counts a written Criterion too (case 472.3) · [[decision-case-472.3]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-02 updated: rendered into ratification.md under rule-ratification (case 595.5) · [[decision-case-595.5]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-02 status: draft → built · cascade
