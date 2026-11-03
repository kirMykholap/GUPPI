---
type: decision
case: "1018"
status: current
children: ["[[decision-case-1018.1]]", "[[decision-case-1018.2]]"]
origin: raw/2026-11-03/0316/ledger.md#case-1018
sprint: plugin
created: 2026-11-03
tags: [sprint, workflow, harness]
---

## Problem

A sprint opens from its id and from options the agent builds, and nothing asks the person first, in their own words, what the sprint is to build.

## Recommend

- **Who asks the open question, and when**
  - Recommended: (a) the main agent, in its own message after the id, before it sends `case-guppi`.
  - Answer: outside the options: ask first what the sprint is about, before the id, since that matters most; the id is proposed after it; Case 1017 is built again to match.
- **How the change is checked**
  - Recommended: (a) this Case replaces the Criterion of `estimate-skill-sprint-open-asks-the-opening-questions` whole, the setup exception included, and the Criterion of `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`; Case 1017 no longer replaces the first.
  - Answer: agreed, (a).
- **Where the options of the goal question come from**
  - Recommended: (c) no goal question: the opening Case words the goal from the person's answer alone, and the person corrects it at the showing.
  - Answer: agreed, (c), after asking what options a goal question could hold once the person has described the work.
- **Who proposes the sprint id**
  - Recommended: (b) the main agent, right after the person's answer, before it sends `case-guppi` with `<id>-1`.
  - Answer: agreed, (b).

## History

- 2026-11-03 created · raw/2026-11-03/0316/ledger.md#case-1018
