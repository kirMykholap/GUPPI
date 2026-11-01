---
type: decision
case: "995"
status: current
children: ["[[decision-case-995.1]]", "[[decision-case-995.2]]", "[[decision-case-995.3]]"]
origin: raw/2026-11-01/2227/ledger.md#case-995
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, case-build]
---

## Problem

`case-guppi` did few of the searches and readings that its rule sets for a new file outside the vault pages, and missed a test that reads every file of that file's folder. Nothing in the Case shows which of them it made, and `ask-guppi` at `/pre-spec` did not look for the reader it missed.

## Recommend

- **What changes after the failed reading**
  - Recommended: (a) the Case lists each search and reading it made for the new file.
  - Answer: (a).
- **Whether the second agent's check is part of this Case**
  - Recommended: (a) no, this Case covers only the agent that builds Cases.
  - Answer: (b) yes, a second part of this Case changes the plan checker too.
- **Where the plan checker's new step goes**
  - Recommended: (a) a new question in the `/pre-spec` list.
  - Answer: agreed, (a).
- **How far the plan checker looks on its own**
  - Recommended: (b) it checks the list and also runs its own search for folder walks.
  - Answer: agreed, (b).
- **How the builder's part is checked**
  - Recommended: (a) replace the Criterion of `estimate-case-build-reads-the-readers-of-a-new-files-folder` and set it back to waiting.
  - Answer: agreed, (a).
- **How the plan checker's part is checked**
  - Recommended: (a) a new check on `rule-prespec`, and `estimate-prespec-reconciles` gets the new question in its list.
  - Answer: agreed, (a).

## History

- 2026-11-02 created · raw/2026-11-01/2227/ledger.md#case-995
