---
type: decision
case: "751"
status: archived
children: ["[[decision-case-751.1]]", "[[decision-case-751.2]]", "[[decision-case-751.3]]", "[[decision-case-751.4]]", "[[decision-case-751.5]]", "[[decision-case-751.6]]"]
origin: raw/2026-10-09/2049/ledger.md#case-751
sprint: migration
created: 2026-10-09
tags: [session, workflow, harness, hooks]
---

## Problem

In a batch the questions of one Case run into those of the next, and a reply of `case-guppi`, a Fact answer included, does not stand apart from the rest of the chat. The check of the layout would note the rules that would fix this.

## Recommend

- **Where does the rule stand around a single reply of `case-guppi`?**
  - Recommended: (a) a rule before and after each round, Fact answer and built Case.
  - Answer: agreed, (a).
- **What separates the Cases of a batch?**
  - Recommended: (a) a rule between the rounds of two Cases and between the showings of two Cases.
  - Answer: agreed, (a).
- **Does the loop of fixes after `/pre-spec` take the same rules?**
  - Recommended: (a) yes, `rule-prespec` changes too.
  - Answer: agreed, (a).
- **How does the layout check change?**
  - Recommended: (a) the check accepts the rules and reads past a rule to the next Case heading.
  - Answer: agreed, (a).
- **Does the example of a showing gain the new rules?**
  - Recommended: (a) yes, a rule above the heading too.
  - Answer: agreed, (a).
- **How is the Case split, and how is each part checked?**
  - Recommended: (a) one part per promise.
  - Answer: agreed, (a).

## History

- 2026-10-09 created · raw/2026-10-09/2049/ledger.md#case-751
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
