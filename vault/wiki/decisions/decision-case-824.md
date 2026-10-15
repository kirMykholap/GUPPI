---
type: decision
case: "824"
status: current
update: ["[[rule-language]]", "[[rule-spec-write]]", "[[rule-case-build]]", "[[rule-case-protocol]]", "[[rule-morph]]", "[[rule-permissions]]", "[[estimate-clean-branch-ships-neutral-texts]]"]
origin: raw/2026-10-15/1959/ledger.md#case-824
sprint: plugin
created: 2026-10-15
tags: [harness, render, workflow, hooks, session, ledger, plugin, ci]
---

## Problem

Shipped rule pages call the documentation language English and say "this repository" where they mean the repository of GUPPI, so they read false in an installed project, and the check that should catch this is due but cannot run without a version tag.

## Recommend

- **Which pages does this Case rewrite?**
  - Recommended: (b) the five pages and `rule-permissions`.
  - Answer: agreed, (b).
- **How does a sentence name the language?**
  - Recommended: (a) the placeholder in rendered text, plain words elsewhere.
  - Answer: agreed, (a).
- **How is a sentence about GUPPI's own repository reworded?**
  - Recommended: (a) name GUPPI's repository.
  - Answer: agreed, (a).
- **How is the fix checked?**
  - Recommended: (b) that check stands, and its method waits for a tag.
  - Answer: agreed, (b).
- **Change**
  - Asked: a `/pre-spec` finding: Case 825 renames the install Case to the setup Case, so this Case should use that name in the sentences it writes.
  - Taken: the `then` lines on `rule-morph` and `rule-permissions` and the `context` say "setup Case", and `given` names the file of Case 825.

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#case-824
