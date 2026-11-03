---
type: decision
case: "1017"
status: current
children: ["[[decision-case-1017.1]]", "[[decision-case-1017.2]]", "[[decision-case-1017.3]]", "[[decision-case-1017.4]]", "[[decision-case-1017.5]]", "[[decision-case-1017.6]]", "[[decision-case-1017.7]]", "[[decision-case-1017.8]]", "[[decision-case-1017.9]]"]
origin: raw/2026-11-03/0316/ledger.md#case-1017
sprint: plugin
created: 2026-11-03
tags: [ci, plugin, ledger, session, harness, hooks, render, git, sprint, workflow]
---

## Problem

A project that installs GUPPI opens its first sprint on the settings of the repository of GUPPI, since no step sets them and the ledger hook refuses a Case before the opening of a sprint.

## Recommend

- **How much of the setup this Case builds**
  - Recommended: (a) all of it, in one Case with sub-cases.
  - Answer: agreed, (a).
- **How guppi.toml marks the setup as done**
  - Recommended: (a) a key `setup_done`, `false` in the clean version and `true` here.
  - Answer: agreed, (a).
- **Which id the setup Case takes**
  - Recommended: (a) the id `guppi caseid --next` prints, `guppi-1`.
  - Answer: agreed, (a).
- **Which decision lines the ledger hook lets through before a sprint opens**
  - Recommended: (a) every decision line while the key says the setup is not done.
  - Answer: agreed, (a).
- **The name of the setup skill**
  - Recommended: (a) `/setup`, from a new page `rule-skill-setup`.
  - Answer: agreed, (a), after a step-by-step account of the flow.
- **What the setup does with the main branch and the git remote**
  - Recommended: (b) neither is taken; a line of the backlog keeps a main branch of another name.
  - Answer: agreed, (b).
- **How /hi starts the setup**
  - Recommended: (a) the hook `guppi sprint --hi` prints a setup line first.
  - Answer: agreed, (a).
- **When rule-morph and the setup skill page get core: true**
  - Recommended: (a) in this Case, so that the local copy holds them; `prod` waits until the readings pass.
  - Answer: agreed, (a).
- **How each part is checked**
  - Recommended: (a) the two Estimates by hand stay, and a test Estimate checks each code part.
  - Answer: agreed, (a).
- **Where the change to how every sprint opens goes**
  - Recommended: (b) a Case of its own in this session.
  - Answer: agreed, (b); the person asked that every sprint open with an open question on what to build, and the item became C8.
- **How the setup Case hands over to the opening of the first sprint**
  - Recommended: (a) the reply that acknowledges the setup Case shows no Frontier and asks the id of the sprint.
  - Answer: agreed, (a).
- **Change**
  - Asked: after the ratification, the person asked that the reply that acknowledges the setup Case end with the open question on what the sprint is to build, since what the sprint is about matters more than its id, and that the id be proposed afterwards.
  - Taken: the setup reply ends with that open question in Cases 1017.3, 1017.4, 1017.6 and 1017.7, and the Criterion of `estimate-skill-sprint-open-asks-the-opening-questions` takes the answer first and the proposed id after it.
- **How the opening Case gets its own id once the sprint id is no longer the first question**
  - Recommended: (a) the main agent proposes the id in one plain question right after the person's answer, then dispatches the opening Case under `<id>-1`.
  - Answer: (a), asked again after the person had agreed in one message with this and with the opposite answer of Case 1018.

## History

- 2026-11-03 created · raw/2026-11-03/0316/ledger.md#case-1017
