---
type: decision
case: "797"
status: current
children: ["[[decision-case-797.1]]", "[[decision-case-797.2]]"]
origin: raw/2026-10-13/1426/ledger.md#case-797
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Problem

`case-guppi` can build a Case by the state at the end of the session: it can use a form that only the session's own Work Mode makes valid, or time a reading before the text it reads changes. A passed Estimate of `rule-case-build` also states that an open insight is closed.

## Recommend

- **How wide should the new instruction to `case-guppi` be?**
  - Recommended: (b) every judgment about a moment: the form a check reads, the moment of a reading and what it will find, judged by the state at that moment.
  - Answer: agreed, (b).
- **What should `case-guppi` do when a Case needs a form that another Case of the same session adds?**
  - Recommended: (b) ask the person in a round, with the form the code accepts now as a possible recommended answer.
  - Answer: agreed, (b).
- **What should happen to the group page and to the out-of-date line about it?**
  - Recommended: (a) remove the line from the Criterion of the Estimate and read it again; the insight stays open.
  - Answer: agreed, (a).
- **How should the new instruction be checked?**
  - Recommended: (a) a new Estimate, read by hand when such a Case comes up.
  - Answer: agreed, (a).
- **Change**
  - Asked: by the findings of `/pre-spec`, the new sentence names a one-off task by hand in Work Mode, such as the removal of a section in Case 796.1, as a way a page changes before the librarian's run; and the `method` of `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` names its event in the form of case 781.
  - Taken: the sentence of Case 797.1 and `context` name such a task; Case 797.2 sets the `method` anew as `by hand, after` the first such Case, with the same reading.

## History

- 2026-10-13 created · raw/2026-10-13/1426/ledger.md#case-797
