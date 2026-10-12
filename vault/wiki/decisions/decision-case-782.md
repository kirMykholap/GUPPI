---
type: decision
case: "782"
status: current
children: ["[[decision-case-782.1]]", "[[decision-case-782.2]]"]
origin: raw/2026-10-12/2252/ledger.md#case-782
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
---

## Problem

A Criterion whose `When` or `Then` needs a reading that only a later session can take passes `/pre-spec` unless the `ask-guppi` run happens to see it as a contradiction, since nothing asks about it by name.

## Recommend

- **What form, if any, should a check on the `When` and `Then` take?**
  - Recommended: (c) a fourth question for the `ask-guppi` run, a judgment of meaning, since a word list cannot tell describing a later session from needing to observe one.
  - Answer: (c).
- **How does the `ask-guppi` side learn about the fourth question?**
  - Recommended: (b) name the questions only in the skill; `rule-ask` and `estimate-ask-finds` say the agent answers each question the skill sets, in its order.
  - Answer: agreed, (b).
- **How is the rewritten `estimate-ask-finds` read?**
  - Recommended: (a) wait for a named event: a `/pre-spec` run after the render, its answer read in the agent transcript.
  - Answer: agreed, (a).
- **Does the builder of a Case also judge this, for Cases built again after the first `/pre-spec`?**
  - Recommended: (a) no, the Case covers `/pre-spec` only.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/2252/ledger.md#case-782
