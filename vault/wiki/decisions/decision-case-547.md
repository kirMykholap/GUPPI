---
type: decision
case: "547"
status: current
create: ["[[estimate-orchestration-shows-the-frontier-after-a-closed-line]]"]
update: ["[[rule-case-protocol]]"]
origin: raw/2026-09-30/1736/ledger.md#case-547
sprint: migration
created: 2026-09-30
tags: [session, workflow, ledger]
---

## Problem

A reply that closes a Frontier line with no ratification and no defer does not show the Frontier. The person does not see what is still open before choosing the next item. The rule names the Frontier only for the reply after a ratification and the reply after a defer.

## Recommend

- **When must the agent show the Frontier after it closes a line?**
  Recommended: every closed line from `/hi` to the end of Plan Mode; Work Mode and Retro unchanged.
  Answer: agreed, as recommended; the first reply of `/hi` is excluded by the change below.
- **What does the Frontier look like in these replies?**
  Recommended: the same form as after a ratification, with the last question as after a defer: which item is next, or whether to run `/pre-spec` when no Cases line is open.
  Answer: agreed, as recommended.
- **How is the new behaviour checked?**
  Recommended: a new Estimate on `rule-case-protocol`; `estimate-orchestration-acknowledging-reply` stays as it is.
  Answer: agreed, as recommended.
- **Should the larger item `rule-orchestration` that was put off come into this Case?**
  Recommended: leave it in the backlog; this Case adds one sentence to `case-schema.md` through `rule-case-protocol`.
  Answer: agreed, as recommended.
- **Change**
  Asked: at pre-spec, the rule holds after the first reply of `/hi`, and that reply keeps its own form set by `rule-skill-hi`; `rule-skill-hi` enters `given`.
  Taken: `when`, `then` and the new sentence start after the first reply of `/hi`; a `－` line of `then` keeps the form of that reply; `rule-skill-hi` is in `given`.
- **Change**
  Asked: at pre-spec, `context` says that `estimate-hi-writes-frontier` stays true with this bound.
  Taken: `context` says so.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-547
