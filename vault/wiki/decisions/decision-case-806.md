---
type: decision
case: "806"
status: current
children: ["[[decision-case-806.1]]", "[[decision-case-806.2]]", "[[decision-case-806.3]]", "[[decision-case-806.4]]"]
origin: raw/2026-10-13/2118/ledger.md#case-806
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness, render]
---

## Problem

In Work Mode a ratified Case of the approved Spec is built again under its own number when the work meets a choice it did not make, so the Spec the person approved and `/pre-spec` checked is rewritten after the fact, and no check of the plan runs on the changed Case before its work.

## Recommend

- **What does Work Mode do when the work meets a choice that a ratified Case did not make?**
  - Recommended: (b) the ratified Case stands, and the choice goes to the next session.
  - Answer: not (b); the person does not move the Case to the next session, and wants a new Case that replaces the old one, most likely only the sub-case, since replacing a whole Case for one point is too much.
- **Does this Case also fix why the fork happened?**
  - Recommended: (a) no, only what Work Mode does at the fork.
  - Answer: agreed, (a).
- **What does the new Case replace?**
  - Recommended: (a) only the sub-case the choice touches.
  - Answer: (a).
- **Does the approved Spec change when a new Case replaces a sub-case?**
  - Recommended: (b) the Spec stays as signed, and the new Case is added after it.
  - Answer: (a), after a discussion of both ways: the Spec changes, the replaced sub-case leaves it, the hook writes the new Case into the Spec so that `materialize` takes it, and only what is confirmed reaches the wiki.
- **Is the new Case checked before its tasks run?**
  - Recommended: (a) the script of `/pre-spec` runs on the plan before the new tasks run.
  - Answer: agreed, (a).
- **Does this hold for every change to a ratified Case in Work Mode, or only for a fork the work runs into?**
  - Recommended: (a) every route.
  - Answer: agreed, (a).
- **How is a finding of the check on the new Case fixed?**
  - Recommended: (a) a Case ratified in Work Mode is fixed in place until its tasks start.
  - Answer: agreed, (a).
- **How is this Case checked?**
  - Recommended: (a) each sub-case replaces the Criterion of the existing Estimate of its page.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, the first condition of `where-to-stop.md` is widened: the work needs a choice no ratified Case makes, or a ratified Case turns out wrong, by a finding of the check or by a text the agent finds wrong, and a new Case is needed.
  - Taken: 806.4 updates `rule-where-to-stop` and replaces the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions`.
- **Change**
  - Asked: at pre-spec, the route of this Case does not hold in a `/work` that `/box` calls: there a fork is a stop with no new Case, and the choice goes to the handoff as a line; no code of `/box` changes.
  - Taken: 806.1 and 806.3 say so in their `then` and in the text they render.

## History

- 2026-10-14 created · raw/2026-10-13/2118/ledger.md#case-806
