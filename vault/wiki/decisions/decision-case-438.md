---
type: decision
case: "438"
status: current
defer: ["[[rule-prespec]]"]
origin: raw/2026-09-26/1337/ledger.md#case-438
sprint: migration
created: 2026-09-26
tags: [session, workflow, harness]
---

## Context

After Case 437 the write hook writes the plan and the ratified copy from the answer of `case-guppi` stored in `.checked.json`, not from the showing of the agent. The skill `/pre-spec` (the Render of `rule-prespec`) says: "Fix the plan, the frontier or the line for each finding". If the agent corrects the body of a Case in the plan by hand, the next ratification overwrites the correction from the store, and before that the comparison with the copy marks the Case as changed. Also, the store holds the Case in Russian, as `case-guppi` wrote it. If a rebuilt Case is shown with its `context` and `problem` (or with the Russian heading of a sub-case), the write hook puts the Russian text back into the plan over the English translation, and the translation must be done again.

## Problem

The Render of `rule-prespec` does not say that a finding in `given`, `when`, `then`, the `then` block or `tasks` is fixed by the `case-guppi` of that Case with a new ratification, while the agent fixes prose (the name, `context`, `problem`) in the plan and shows a `DIFF`. It also does not say that the translation is the last step, after every ratification again.

## Deferred

### [[rule-prespec]]

After case 437, a pre-spec finding in the body of a Case goes to its case-guppi and a new ratification, prose is fixed in the plan as a DIFF, and the translation of name, context and problem is the last step

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#case-438
