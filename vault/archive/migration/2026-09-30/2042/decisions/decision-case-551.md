---
type: decision
case: "551"
status: archived
defer: ["[[rule-case-build]]"]
superseded_by: ["[[decision-case-557.3]]"]
origin: raw/2026-09-30/1736/ledger.md#case-551
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Context

The reading of `estimate-case-build-writes-a-plain-round` in session 1736 read the first rounds of `case-guppi` on Cases 547 to 550. Each Context gives the mechanism with an example, its quotations stand as blockquotes, and no number stands alone. But the sentence on what the round decides runs its parts inside one sentence: on 548 and 550 it names three parallel clauses, and on 547 the Context names five examples in one sentence. `.claude/skills/grill-me/SKILL.md` sets a series of two or more parallel clauses one per line. The person put the fix off to take the readings first.

## Problem

The Context of a first round of `case-guppi` carries a list inside a sentence, against the list rule of `grill-me`, so `estimate-case-build-writes-a-plain-round` stays failed.

## Deferred

### [[rule-case-build]]

The Context of a first round of case-guppi writes what the round decides, and a series of examples, one item per line as grill-me sets a list, never inside one sentence; estimate-case-build-writes-a-plain-round failed on this in session 1736

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-551
- 2026-09-30 superseded by decision-case-557.3 · [[decision-case-557.3]]
- 2026-09-30 archived · superseded
- 2026-09-30 archived · cleanup
