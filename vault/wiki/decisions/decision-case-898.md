---
type: decision
case: "898"
status: current
children: ["[[decision-case-898.1]]", "[[decision-case-898.2]]", "[[decision-case-898.3]]"]
origin: raw/2026-10-29/0327/ledger.md#case-898
sprint: plugin
created: 2026-10-29
tags: [plugin, ci, session, workflow, harness, case-build, librarian, render, ledger, hooks, tests]
---

## Problem

The reading of `estimate-clean-branch-ships-neutral-texts` has no single yardstick for a sentence that holds only in the repository of GUPPI. It failed sentences that hold as they read in an installed project. Some methods of shipped Estimates also wait for one moment in the past of GUPPI, which an installed project never meets.

## Recommend

- **Which sentences count as true only in the repository of GUPPI**
  - Recommended: (a) a sentence that holds as it reads in an installed project passes, because it states its condition or says how the shipped files came about; only sentences that are false or empty there are reworded, and the Criterion gets a line that says this.
  - Answer: agreed, (a).
- **Which method moments hold in any project**
  - Recommended: (a) "the session that changes it", "the new Render" and "the Spec that changes it" stand; methods that point to one moment of the past ("the next session", "the first … under the new Render", the VS Code chat) are reworded to a kind of moment.
  - Answer: agreed, (a).
- **What the Case does with the doubtful sentences**
  - Recommended: (a) judge them by the same yardstick in this Case, reword the ones that fail, and say why the others stand.
  - Answer: agreed, (a).
- **The sprint names in the shipped code**
  - Recommended: (a) the text stands, and the value in the shipped code is left to a Case of its own.
  - Answer: agreed, (a).

## History

- 2026-10-29 created · raw/2026-10-29/0327/ledger.md#case-898
