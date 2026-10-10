---
type: decision
case: "769"
status: current
children: ["[[decision-case-769.1]]", "[[decision-case-769.2]]", "[[decision-case-769.3]]", "[[decision-case-769.4]]", "[[decision-case-769.5]]"]
origin: raw/2026-10-10/1913/ledger.md#case-769
sprint: plugin
created: 2026-10-10
tags: [session, workflow, sprint, harness, hooks, ledger]
---

## Problem

The opening of a sprint is one Frontier line among others, so the session that opens a sprint cannot take up the first milestone of that sprint, and the opening is not a step of its own.

## Recommend

- **Is the opening a Frontier line, a step before the Frontier, or a session of its own?**
  - Recommended: (b) a step before the Frontier: `/sprint-open` runs first, and once the opening Case is ratified the Frontier is built with the items of the new first milestone.
  - Answer: agreed, (b).
- **Does the close change now, or wait for the close of `plugin`?**
  - Recommended: (a) the close waits; it is judged at the close of `plugin`, and a flaw seen then becomes a Case.
  - Answer: agreed, (a).
- **Do the questions of the opening Case stay as they are?**
  - Recommended: (a) keep the questions.
  - Answer: agreed, (a).
- **Where do the readings and the Ask questions of `/hi` go in the session that opens a sprint?**
  - Recommended: (a) all of it after the opening: the reply that confirms the opening Case writes the whole Frontier, takes the readings and puts the Ask questions before the question which item is next.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the fixes of the findings of `/pre-spec`: one wording across the sub-cases for when `frontier.md` is written; the sentences of `rule-session-start` that become false replaced; the method of `estimate-hi-writes-frontier` set to the new moment; and the Criterion of `estimate-sprint-close-next-session-opens-the-sprint` replaced, its method left as it is.
  - Taken: every sub-case says the Frontier is assembled and written before the reply that acknowledges the opening Case, which shows it; Case 769.2 replaces the sentences of `rule-session-start` on the sources and the first turn and sets the method; Case 769.5 replaces the Criterion of `estimate-sprint-close-next-session-opens-the-sprint`.
- **How is the check of the session after a close read, now that it cannot wait for that session?**
  - Recommended: (a) the tests of the ledger refusal and of the sprint id on the pages, and a reading by hand at the Retro of this session of the new texts of `/hi` and `/sprint-open` in its Spec.
  - Answer: agreed, (a).
- **Change**
  - Asked: the confirmation of `/pre-spec` found that the `purpose` of the new Estimate of Case 769.4 and the `change` line of its `rule-orchestration` update still said that the acknowledging reply writes the Frontier; the person chose to fix them.
  - Taken: both say that the Frontier is written and the readings taken before that reply, which shows the Frontier.

## History

- 2026-10-10 created · raw/2026-10-10/1913/ledger.md#case-769
