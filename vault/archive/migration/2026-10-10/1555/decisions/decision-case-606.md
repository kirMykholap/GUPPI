---
type: decision
case: "606"
status: archived
children: ["[[decision-case-606.1]]", "[[decision-case-606.2]]"]
origin: raw/2026-10-02/2300/ledger.md#case-606
sprint: migration
created: 2026-10-02
tags: [session, workflow, ledger]
---

## Problem

A Case can write a `by hand` box whose check only runs after Work Mode and Retro of its own session have ended. Nobody ticks such a box, and the brief carries it from session to session. The question was whether to tick it later or stop writing it. The person chose to fix the cause and to close the box open today by a Work Mode task.

## Recommend

- **Which boxes does the closer tick?**
  - Recommended: (a) every box Work Mode ticks — code, a test, a migration or a `by hand` check — in an earlier session's Spec, ticked by whoever closes its Work line.
  - Answer: not answered; replaced by **Fix the cause, or tick the box later?**
- **Where is the rule written?**
  - Recommended: (a) one sentence in the ticking paragraph of `orchestration.md`, which applies at `/hi`, in Work Mode and at Retro.
  - Answer: not answered; replaced by **Fix the cause, or tick the box later?**
- **The box open today**
  - Recommended: (a) a Work Mode task of this Case: run `make lint`, tick the box in `raw/2026-10-02/1202/spec.md` when no `fence` line on `decision-case-13` appears, and close its Work line. Whatever the answer on the cause, the tick then rests on a ratified decision.
  - Answer: (a).
- **How is the new rule checked?**
  - Recommended: (a) rewrite the Criterion of `estimate-case-protocol-case-form` whole, adding a line that `tasks` holds no `by hand` box whose moment comes after Work Mode of its session, read by hand at the close of a later session. A hook that matches words would miss other phrasings.
  - Answer: (a). The first round asked this question about the ticking rule, and it went unanswered there.
- **Fix the cause, or tick the box later?**
  - Recommended: (a) fix the cause. A Case writes no `by hand` box whose moment comes after Work Mode of its session. Such a check is the reading of an Estimate or the `make lint` of the librarian's run, and the box open today is closed once.
  - Answer: (a). The person asked why such a box stays unticked at all and said the earlier direction was wrong.
- **Where is the new rule written?**
  - Recommended: (a) one sentence in the `tasks` part of `case-schema.md`, the Render of `rule-case-protocol`, which `case-guppi` reads whole.
  - Answer: (a).
- **What does the second sub-case record in the ledger?**
  - Recommended: (a) an `update` of `decision-case-13` with `change` alone, which writes one History line on that page saying that the check of its fence has been run and the box ticked; nothing else on the page changes.
  - Answer: not answered in a round; the person ratified Case 603, which was built on (a), with its sub-cases.

## History

- 2026-10-03 created · raw/2026-10-02/2300/ledger.md#case-606
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
