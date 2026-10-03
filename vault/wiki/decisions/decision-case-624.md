---
type: decision
case: "624"
status: current
update: ["[[rule-handoff]]", "[[estimate-handoff-holds-each-fact-once]]"]
origin: raw/2026-10-04/0112/ledger.md#case-624
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness, render]
---

## Problem

The `/handoff` skill forbids naming any Case, reading or lesson in two sections. A note on a decision must name it, and nothing says where the readings that wait belong. So every handoff the check has read repeats things, and `estimate-handoff-holds-each-fact-once` stays failed.

## Recommend

- **What "each fact once" means**
  - Recommended: (b) one statement once: a section may name a Case, check or lesson that another section names, when it says something new about it; saying the same thing about it twice is the failure; the skill text and the check's pass condition are both rewritten to say this.
  - Answer: agreed with the recommendation, (b).
- **Where the checks that wait for a later session are listed**
  - Recommended: (a) Debt only: the Debt line is widened to every check that cannot be measured yet, each with the moment it waits for; the instructions to the librarian list no checks.
  - Answer: agreed with the recommendation, (a).
- **Which report the new check is measured on**
  - Recommended: (b) the first report written from the new text: a report of a later session, written after the new skill text takes effect.
  - Answer: agreed with the recommendation, (b).

## History

- 2026-10-04 created · raw/2026-10-04/0112/ledger.md#case-624
