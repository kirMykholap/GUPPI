---
type: decision
case: "799"
status: current
update: ["[[rule-lint]]", "[[estimate-lint-checks-the-statuses]]"]
origin: raw/2026-10-13/1426/ledger.md#case-799
sprint: plugin
created: 2026-10-13
tags: [harness, workflow]
---

## Problem

`make lint` marks red every Estimate that is not yet read, also one whose reading cannot be taken before a later event or session. The same red lines are carried from session to session, and lint stays red on GitHub, though most of them cannot be cleared before their moment.

## Recommend

- **What should lint do with a pending check that waits for a later event?**
  - Recommended: (a) lint leaves out a check whose reading waits for a later moment; the brief still lists it under Readings due and moves it to Work when its event comes, and the sprint close still puts each one left to the person.
  - Answer: agreed, (a), after the person asked how such an event is found later and what shows that an Estimate has not passed.
- **Should the check of the git context be read in this session?**
  - Recommended: (a) read it in this session's Work Mode.
  - Answer: agreed, (a).
- **What happens to `rule-morph`, the decision that keeps being put off?**
  - Recommended: (a) take it up as its own item in this session; this Case leaves it out.
  - Answer: (a), added as a separate item.
- **Must every part of a check's method wait before lint leaves it out, or is one waiting part enough?**
  - Recommended: (b) one waiting part is enough, since a check is read once as a whole; the brief's Work list, not lint, puts up a reading whose moment has come.
  - Answer: agreed, (b).
- **Change**
  - Asked: rewrite the two places of `context` that still spoke of a reading that is due, to the rule as it works.
  - Taken: `context` now says that lint marks a `pending` Estimate red only when no part of its `method` waits, and that the `Work` list of the brief puts up a reading whose moment has come.

## History

- 2026-10-13 created · raw/2026-10-13/1426/ledger.md#case-799
