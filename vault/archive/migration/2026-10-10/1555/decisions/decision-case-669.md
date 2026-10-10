---
type: decision
case: "669"
status: archived
children: ["[[decision-case-669.1]]", "[[decision-case-669.2]]", "[[decision-case-669.3]]", "[[decision-case-669.4]]", "[[decision-case-669.5]]", "[[decision-case-669.6]]", "[[decision-case-669.7]]", "[[decision-case-669.8]]", "[[decision-case-669.9]]", "[[decision-case-669.10]]", "[[decision-case-669.11]]", "[[decision-case-669.12]]", "[[decision-case-669.13]]", "[[decision-case-669.14]]", "[[decision-case-669.15]]", "[[decision-case-669.16]]"]
origin: raw/2026-10-05/1831/ledger.md#case-669
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session, librarian, hooks, ledger, render, schema]
---

## Problem

Fifteen Estimates come back at every session as readings due. Some wait for an event that does not come, some cost a long reading by hand, and four failed and were put off again and again. The person decided to close them all as `passed`, and to treat a problem seen later as a lesson.

## Recommend

- **How the Case sets the 15 checks to passed**
  - Recommended: (a) one change per check in this Case: the state set to `passed` and the date to today, a result text written, and the promise written back word for word; complete on its own and dependent on no Case not yet written.
  - Answer: agreed, (a).
- **What the result text of each check says**
  - Recommended: (a) the person's decision first, then the last reading kept unchanged, so the known faults stay on the page.
  - Answer: agreed, (a).
- **Whether the known faults of the four failed checks become lessons now**
  - Recommended: (a) no lesson now; a lesson is written only when a fault is seen again in later work.
  - Answer: agreed, (a).
- **What happens to the put-off decisions on three of the checks**
  - Recommended: (a) this Case retires them: the change on each of the three pages marks each put-off decision on it as replaced by this Case.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec the main agent put to the person that the text of `case-schema.md` and of the Estimate schema forbids a Case to set the status of an Estimate, while the code allows it; the person agreed to option (a), a new sub-case that updates `rule-case-protocol` and `rule-estimates-schema` so that a Case may, by the person's decision, set an Estimate `passed` or `failed` with its Criterion written back unchanged, its Result opening with the date and the place of the decision, and `checked` the date of the decision.
  - Taken: Case 669.16 makes these changes, and holds the task that this session's `handoff.md` names none of the fifteen as a reading that waits; 669.6, 669.7 and 669.10 also retire the decisions that put their Estimates off, by the answer to the question on put-off decisions.

## History

- 2026-10-05 created · raw/2026-10-05/1831/ledger.md#case-669
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
