---
type: decision
case: "198"
status: current
update: ["[[rule-prespec]]"]
origin: raw/2026-09-16/1651/ledger.md#case-198
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Context

`rule-prespec` is a Leaf, `enforcement: render`, `governs: .claude/skills/pre-task/SKILL.md`; its Estimate `estimate-prespec-reconciles`, six blocks, is deferred for its recut by case 191. The second paragraph of the Render builds the list of decisions for `ask-guppi`. Case 186.2 replaced its second sentence: a deferred decision enters the list by its slug and the word `defer`, without its `purpose`, and its body is not read. But the first sentence of the paragraph stands as it was: "slug — decision type — purpose" for every decision — and demands a `purpose` of a `defer`, contradicting the next one. This Case touches `estimate-prespec-reconciles` as the Estimate of the live reading of the Render but does not replace its Criterion: the recut is deferred by 191, and the promise of 186.2 and of this change goes into it. It touches no other Estimate.

## Problem

Two neighbouring sentences of one paragraph demand the opposite; an agent reading the skill picks either. Defect 7 of the brief.

## Given

`/pre-task` builds the list from the decisions of this Plan Mode and hands it to `ask-guppi` in one dispatch.
**－** The body of a deferred Case is not read — 186.2; this Case repeats the condition, it does not change it.

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#case-198
