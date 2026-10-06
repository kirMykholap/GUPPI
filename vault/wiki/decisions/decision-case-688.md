---
type: decision
case: "688"
status: current
children: ["[[decision-case-688.1]]", "[[decision-case-688.2]]", "[[decision-case-688.3]]", "[[decision-case-688.4]]", "[[decision-case-688.5]]", "[[decision-case-688.6]]", "[[decision-case-688.7]]", "[[decision-case-688.8]]", "[[decision-case-688.9]]"]
origin: raw/2026-10-06/0104/ledger.md#case-688
sprint: migration
created: 2026-10-06
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A showing copied wrong a second time, after the check of a showing refused the first, reaches the person unchecked, and a decision line copied wrong into the acknowledging reply lands in the ledger, where pages are made from it.

## Recommend

- **What this Case changes about the copied showing**
  - Recommended: (b) the showing check stops trusting the flag: it runs on every reply and guards its loop by its own refusals in the transcript, as the Spec hook does.
  - Answer: (b). The person added that the person seeing a wrong version first cannot be avoided, and asked whether the agent could show the ledger lines first, in a reply of their own; after the answer that a check runs only at the end of a turn, the person said no separate question on it is needed.
- **Whether the ledger lines written when you ratify come into this Case**
  - Recommended: (a) leave them out.
  - Answer: (b) bring them in.
- **How often the showing check refuses the same wrong showing**
  - Recommended: (b) up to three times for the same Case since the person's last message, then let it through with a line that says it is unchecked.
  - Answer: agreed, (b).
- **Which parts of the end-of-reply check stop trusting the flag**
  - Recommended: (a) all four: the comparison, the sending of the file, the layout of a showing and the opening of a round.
  - Answer: agreed, (a).
- **How often the ledger hook holds back a wrong decision line**
  - Recommended: (b) every time it is still wrong.
  - Answer: agreed, (b).
- **What the ledger comparison sets aside**
  - Recommended: (a) an added lesson mark and the lines that put a decision off; a line of a Case with no stored text is held.
  - Answer: agreed, (a).
- **How the work is split and checked**
  - Recommended: (a) sub-cases, a new check for each hook.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec` the sentence of `rule-orchestration` on where decision lines are written named the reply that answers a hold twice, in Case 685.1 and in Case 688.7; the person chose that Case 685.1 drops its mention and Case 688.7 keeps its clause.
  - Taken: the clause of Case 688.7 stays as written, its anchor apart from the text of Case 685.1, and the context says it is the one place that names that reply.

## History

- 2026-10-06 created · raw/2026-10-06/0104/ledger.md#case-688
