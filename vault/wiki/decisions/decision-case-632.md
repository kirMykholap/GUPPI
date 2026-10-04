---
type: decision
case: "632"
status: current
children: ["[[decision-case-632.1]]", "[[decision-case-632.2]]", "[[decision-case-632.3]]", "[[decision-case-632.4]]", "[[decision-case-632.5]]", "[[decision-case-632.6]]", "[[decision-case-632.7]]", "[[decision-case-632.8]]", "[[decision-case-632.9]]", "[[decision-case-632.10]]"]
origin: raw/2026-10-04/2041/ledger.md#case-632
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, harness, session, librarian, render, tests, ledger, hooks, schema]
---

## Problem

The Cases that built the close of a sprint left texts that contradict the schema of rule pages, the close itself, the code and each other. They also left four Estimates that speak of what those Cases changed. The question is how each contradiction is fixed before the close of migration, and which checks follow.

## Recommend

- **Do the fixes mark the earlier decisions as replaced?**
  - Recommended: (a) no mark: new sub-cases change the pages, each `context` names the earlier sub-case it corrects, and the earlier decision pages stay current.
  - Answer: agreed.
- **How is the Case cut?**
  - Recommended: (a) one Case, one sub-case per promise, the count set by the other answers.
  - Answer: agreed.
- **Where does the description of the close go?**
  - Recommended: (a) both sections leave: the Purpose of `rule-sprint-close` keeps only the failure it prevents, the two parts with no other home go into `rule-orchestration`, and the section of `rule-cleanup` goes into the docstring of `guppi/cleanup.py`.
  - Answer: agreed.
- **What does "Definition of done" mean when the close does not wait for it?**
  - Recommended: (a) reword the three texts: the Estimates are the Definition of done, read before the close; one not passed goes to the archive with the sprint page, its status kept in the record of the close.
  - Answer: agreed.
- **What bar does the lint check of migration keep?**
  - Recommended: (a) widen the exception to an `unread` of an Estimate whose method names a moment at or after the closing librarian's run and which the close line carries by `--carry`; the Criterion replaced, its purpose and method following.
  - Answer: agreed.
- **Which pages of the opening run carry the new sprint id?**
  - Recommended: (a) the texts follow the code: the pages written from the session that creates the sprint page carry its id.
  - Answer: agreed.
- **Can the session that opens the next sprint take a conserved Spec?**
  - Recommended: (a) no: while the opening line stands, `/hi` lists no conserved Spec, the sentence is reworded so that only the opening line comes first, and the Criterion of `estimate-hi-takes-a-conserved-spec` is replaced.
  - Answer: agreed.
- **How does the older clash check stop running the newer tests?**
  - Recommended: (a) narrow the older method to `-k subagent_clash`.
  - Answer: agreed.
- **What does the schema check of Insights claim about its text?**
  - Recommended: (a) replace the Criterion with no word-for-word claim; pending, read by its test and `make lint`.
  - Answer: agreed.
- **Does the check of the main agent's own questions cover the new question?**
  - Recommended: (a) replace the Criterion, its When naming the question after a clash.
  - Answer: agreed.
- **Does the check of the Work readings change for the closing session?**
  - Recommended: (a) its Criterion stands, and `context` says why.
  - Answer: agreed.

## History

- 2026-10-04 created · raw/2026-10-04/2041/ledger.md#case-632
