---
type: decision
case: "825"
status: current
update: ["[[rule-morph]]", "[[estimate-morph-sets-up-the-project-at-the-first-hi]]", "[[rule-claude-md]]", "[[rule-guppi-config]]", "[[rule-clean-branch]]", "[[entity-sprint-plugin]]", "[[rule-permissions]]"]
origin: raw/2026-10-15/1959/ledger.md#case-825
sprint: plugin
created: 2026-10-15
tags: [session, harness, plugin, render, ci, git, sprint, workflow]
---

## Problem

Two pages each put a different Case first at the first `/hi` of a new project, with no order between them, and the pages call the setup "the install Case", as if `/guppi:install` were a Case.

## Recommend

- **In what order do setup and the first sprint come?**
  - Recommended: (a) setup first, then the sprint, in one session.
  - Answer: agreed, (a).
- **Should the "install Case" be renamed "setup Case"?**
  - Recommended: (a) rename to "setup" everywhere.
  - Answer: agreed, (a).
- **Where does the start-to-finish description live?**
  - Recommended: (a) in the Purpose of `rule-morph`.
  - Answer: agreed, (a).
- **How is the order checked?**
  - Recommended: (a) rewrite that check's promise.
  - Answer: agreed, (a).
- **Change**
  - Asked: a `/pre-spec` finding: `rule-permissions` still says that the folder name is set "at install".
  - Taken: a pair on `rule-permissions` names the setup Case of `rule-morph` there.

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#case-825
