---
type: decision
case: "784"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-checks-the-finished-case]]"]
origin: raw/2026-10-12/2252/ledger.md#case-784
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
---

## Problem

`case-guppi` writes a Case whose sub-cases contradict each other on one behaviour when they change different pages, and it misses a glossary row or an Estimate that speaks of a changed field without naming a changed page; `/pre-spec` finds these late, and the Case is shown again.

## Recommend

- **Where are the parts of a Case compared with each other?**
  - Recommended: (a) the building agent compares the parts by meaning: in every Case with parts, before it writes the file, it lists each behaviour, field and term any part sets and reads every sentence of every part on it side by side, whatever page the part changes.
  - Answer: agreed, (a).
- **Which texts outside the Case does the agent search for a changed field?**
  - Recommended: (a) search the live pages outside the Decision pages, and `.claude/`, for the name of each field, term or command whose behaviour the Case changes, glossary rows and the Criterion of each check page included.
  - Answer: agreed, (a).
- **Which check page proves the fix?**
  - Recommended: (a) rewrite the promise of `estimate-case-build-checks-the-finished-case`: its line on parts of one page widened, one line for the field search, its purpose and method set anew, read at this session's Retro.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/2252/ledger.md#case-784
