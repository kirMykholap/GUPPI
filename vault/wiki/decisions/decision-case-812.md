---
type: decision
case: "812"
status: current
children: ["[[decision-case-812.1]]", "[[decision-case-812.2]]"]
origin: raw/2026-10-14/0232/ledger.md#case-812
sprint: plugin
created: 2026-10-14
tags: [session, workflow, harness, ledger]
---

## Problem

The command that numbers a new Case is written without the option that tells it the session, and without it, or without the plan file of that session, the command prints an id that it does not hold and that may already be taken.

## Recommend

- **Where should the command get the session id when you start a new Case?**
  - Recommended: (c) the pages name `--session <id>`, and the command refuses to run without it.
  - Answer: agreed, (c).
- **Which check should prove the fix?**
  - Recommended: (a) rewrite the text of `estimate-ratification-case-id-carries-the-sprint` whole.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec` — the placeholder `<id>` of the stamp clashes with the sprint `<id>` of the same sentence of `ratification.md`.
  - Taken: the stamp is written `<stamp>` in every new text.
- **Change**
  - Asked: a finding of `/pre-spec` — `estimate-orchestration-shows-the-built-case` promises the dispatch under the id of a run that now prints no id.
  - Taken: Case 812.2 replaces its Criterion, and the Case is built again with sub-cases under a new number.
- **Change**
  - Asked: a finding of `/pre-spec`, put to the person — with a stamp that finds no plan file the command still prints an id it does not hold; the person agreed that it refuses: prints no id and exits 1, and the main agent creates the plan file before it takes a number.
  - Taken: the refusal stands in the `then` and the Criterion of Case 812.1, with a task for the code and its test, and the Render has the plan file created before the first run of the command.

## History

- 2026-10-14 created · raw/2026-10-14/0232/ledger.md#case-812
