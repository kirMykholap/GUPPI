---
type: decision
case: "942"
status: current
children: ["[[decision-case-942.1]]", "[[decision-case-942.2]]"]
origin: raw/2026-10-30/2005/ledger.md#case-942
sprint: plugin
created: 2026-10-30
tags: [harness, schema, tests, hooks, workflow, session, git, librarian, ledger, render]
---

## Problem

Eleven Leaf rules describe their mechanism in a section that the schema keeps for a MOC, beside the code that decides it, so the two texts can part.

## Recommend

- **Which Leaf rules lose the section, and where its facts go**
  - Recommended: (a) all eleven now, each fact the docstring of the page's code lacks moved into it first, a rendered Leaf with no code taking it into its Purpose or its Render, then a `drop`.
  - Answer: (a).
- **How the removal is checked**
  - Recommended: (a) a new Estimate on `rule-rules-schema`, read by hand at Retro against the Spec and after the librarian's run by a search, and the schema sentence reworded.
  - Answer: agreed, (a).
- **Where the facts of `rule-internal-context` go**
  - Recommended: (a) into its `## Purpose`.
  - Answer: agreed, (a).
- **Whether remarks on what stood before a Case move too**
  - Recommended: (b) they are left out; the History of each page and its Decision pages keep them.
  - Answer: agreed, (b).
- **One Case for all eleven pages, or one part per page**
  - Recommended: (a) one Case, one Estimate.
  - Answer: (a).
- **Change**
  - Asked: `/pre-spec` found that the change of the schema can fail alone while every docstring holds its facts, and the person agreed to two sub-cases: one for the eleven pages, checked by the new Estimate, and one for the schema, checked by `estimate-rules-schema-checked` with its Criterion replaced.
  - Taken: the Case is built again as Case 942 in two sub-cases, under a new number, since Case 940 has decision lines.
- **Change**
  - Asked: `/pre-spec` found that the new Purpose of `rule-internal-context` describes what the page does, not the failure the rule prevents.
  - Taken: the same facts stand in the Purpose, each written as the failure that a line of the list prevents.
- **Change**
  - Asked: `/pre-spec` found that the line of `then` on pointers in brackets repeats the promise of two Estimates of `rule-clean-branch`.
  - Taken: the line is left out, and `context` names those two Estimates.

## History

- 2026-10-30 created · raw/2026-10-30/2005/ledger.md#case-942
