---
type: decision
case: "943"
status: current
children: ["[[decision-case-943.1]]", "[[decision-case-943.2]]", "[[decision-case-943.3]]"]
origin: raw/2026-10-30/2005/ledger.md#case-943
sprint: plugin
created: 2026-10-30
tags: [harness, plugin, render]
---

## Problem

Four install readings are due, and each needs the person to install by hand. No task of the Spec makes Work Mode stop for that, so without one the run goes on to Retro and the readings go to the handoff unread. Two of their Criteria also say that the person writes the clean copy, while the agent writes it.

## Recommend

- **Which pages does the Case name?**
  - Recommended: (a) the two rules the checks belong to, by an `update` with only `change`.
  - Answer: agreed, (a).
- **Who makes the five test projects?**
  - Recommended: (a) the agent, before the stop.
  - Answer: agreed, (a).
- **Which check closes the Case?**
  - Recommended: (a) the four install checks, their wording kept.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec` — two Criteria say that the person writes the clean copy; the person agreed that the Case replaces both whole, with the agent as the one who writes it, and that Retro reads both against the Spec.
  - Taken: Cases 943.2 and 943.3 replace those Criteria whole and set each `method` anew for Retro.
- **Where do the two rewritten checks go?**
  - Recommended: (a) Case 941 built again under a new number, with sub-cases.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-30/2005/ledger.md#case-943
