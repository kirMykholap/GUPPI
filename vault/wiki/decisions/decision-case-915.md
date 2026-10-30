---
type: decision
case: "915"
status: current
children: ["[[decision-case-915.1]]", "[[decision-case-915.2]]", "[[decision-case-915.3]]"]
origin: raw/2026-10-29/2341/ledger.md#case-915
sprint: plugin
created: 2026-10-29
tags: [session, workflow, harness, hooks, ledger]
---

## Problem

The ledger hook asks the same question about a lesson with no mark after every ratification, and each time it costs one more reply in the chat. It asks about `knowledge` lessons too, though no Case fixes the cause of a fact.

## Recommend

- **How often should the hook ask about a lesson with no mark?**
  - Recommended: (a) once a lesson, at the first ratification after it, judged from the session's ledger.
  - Answer: none of the options; a later Case may still fix the lesson, only an error lesson needs the judgment and a knowledge lesson none, and the question should be quiet or answered inside the reply that holds the Frontier; replaced by **Where should the question about an error lesson with no mark reach the agent?**
- **Where should the question about an error lesson with no mark reach the agent?**
  - Recommended: (b) the Case answers it when it is built: `case-guppi` weighs each open error lesson and writes the mark on its own ledger lines, which the person ratifies.
  - Answer: agreed, (b).
- **Which lessons does the question cover?**
  - Recommended: (a) error lessons only, for the new question and for the hold of a lesson written after a Case.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed with the fixes that `/pre-spec` proposed: the new text of `rule-case-build` names only a lesson that stands before the decision lines of a reply, and reads the ledger by a Grep for `lesson\[error\]` and a Grep for `\{addresses:`; the pair of `rule-prespec-onward` keeps the pointer to case 688.7; the `then` of 915.1 names the new Render of `rule-orchestration` in the Spec.
  - Taken: each fix as proposed; the `method` of `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line` adds the reading of that Render at Retro.

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#case-915
