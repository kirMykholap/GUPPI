---
type: decision
case: "629"
status: current
children: ["[[decision-case-629.1]]", "[[decision-case-629.2]]", "[[decision-case-629.3]]", "[[decision-case-629.4]]", "[[decision-case-629.5]]"]
origin: raw/2026-10-04/1439/ledger.md#case-629
sprint: migration
created: 2026-10-04
tags: [hooks, harness, workflow, session]
---

## Problem

A clash between two Cases of one session is found only after the person ratified both, so they are built and ratified twice. And a Case changed in one sub-case is written and returned whole, its `context` full of searches that changed nothing. The question is how the early check sees the session's other Cases, how a Case comes back by its changed parts, and what `context` keeps.

## Recommend

- **Which other Cases does the early check compare an answer with?**
  - Recommended: (b) the ratified Cases of the plan file and the Cases built but not yet ratified in the store, leaving out a stored Case with findings, one a supersedes mark replaced, and the answer's own earlier version.
  - Answer: agreed.
- **What does the early check do when an answer clashes with another Case?**
  - Recommended: (a) a finding: `case-guppi` changes its own Case, and where the other Case should change the main agent asks the person.
  - Answer: agreed.
- **Does the late check, after ratification, stay?**
  - Recommended: (a) keep it as a backstop.
  - Answer: agreed.
- **What will check that the early check compares an answer with the other Cases?**
  - Recommended: (a) a new Estimate on `rule-case-check`, the Criterion of `estimate-case-check-sends-back-a-faulty-case` standing.
  - Answer: agreed.
- **How does a Case come back when only a sub-case changed?**
  - Recommended: (b) the changed sub-cases alone, plus the parent when its own parts changed, the hook checking them with the parent's stored parts and merging them into the store and the file.
  - Answer: agreed; its part on the parent was replaced by the question on the parent's own text.
- **What does a Case's `context` say about the searches it ran?**
  - Recommended: (b) only the searches the Case rests on, each with its pattern and paths.
  - Answer: agreed.
- **Is a large item split into several Cases?**
  - Recommended: (a) no rule for this now; the context names it as not done.
  - Answer: agreed.
- **When the parent's own text changes, what comes back?**
  - Recommended: (a) the whole Case; the changed sub-cases alone only while the parent's `context`, `problem` and `recommend` stand as they were.
  - Answer: agreed.
- **Where does the decision on the cost of rebuilding a Case live?**
  - Recommended: (a) on `rule-case-build` and `rule-case-check`, the placeholder retired by a `delete` with both supersedes marks.
  - Answer: agreed.
- **How are the two items cut, and what checks each part?**
  - Recommended: (a) one Case with five sub-cases: the clash with other Cases, a new Estimate; the answer by changed sub-cases with the placeholder retired, the Criterion of `estimate-case-build-writes-the-case` replaced; a lone sub-case judged with its stored parent, a new Estimate; the titles of the rounds read in the stored `recommend` too, the Criterion of `estimate-case-check-requires-each-question-of-the-rounds` replaced; `context` keeping only the searches the Case rests on, the Criterion of `estimate-case-build-checks-the-finished-case` replaced.
  - Answer: agreed.

## History

- 2026-10-04 created · raw/2026-10-04/1439/ledger.md#case-629
