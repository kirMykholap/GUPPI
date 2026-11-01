---
type: decision
case: "991"
status: current
children: ["[[decision-case-991.1]]", "[[decision-case-991.2]]", "[[decision-case-991.3]]", "[[decision-case-991.4]]"]
origin: raw/2026-11-01/2038/ledger.md#case-991
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, orchestration, prespec, sprint, ledger]
---

## Problem

The texts the main agent reads say that a Frontier line closes `· case N` when its Case is ratified, while the check of `/pre-spec` asks that a decision line of that Case end the item. So the agent closes a line that the check then refuses, and the line is closed again.

## Recommend

- **How the agent learns that a line does not close by its Case**
  - Recommended: (a) say it in the text the agent reads; no code changes.
  - Answer: (a).
- **Which texts carry the rule of the closer**
  - Recommended: (a) change both `orchestration.md` and the skill `/hi` the same way.
  - Answer: (a).
- **How a sprint line closes when its Case updates no sprint page**
  - Recommended: (a) it closes `[-] … · sprint · defer`, and the decision lines of the Case stand.
  - Answer: (a).
- **Which Estimate checks the new text**
  - Recommended: (a) a new Estimate, `estimate-orchestration-closes-a-line-by-what-its-case-does`, read by hand at the Retro of this session.
  - Answer: (a).
- **What happens to the closing line of `estimate-hi-writes-frontier`**
  - Recommended: (a) a sub-case replaces its Criterion whole, with the one false line changed and pointing to `orchestration.md`.
  - Answer: (a).
- **Change**
  - Asked: the findings of `/pre-spec` on the Case as first ratified: the short form and the take-back sentence of `rule-orchestration`, the Criteria of `estimate-orchestration-takes-back-a-ratified-case` and `estimate-orchestration-defers-in-one-reply`, the backlog items the check does not judge, the reading of `estimate-hi-writes-frontier`, and `estimate-prespec-binds-a-sprint-line`.
  - Taken: 991.1 gains the pairs on the short form and the take-back, and its text and `then` name what the check judges and how an open Insight ends. Cases 991.3 and 991.4 replace the two Criteria. 991.2 keeps its `read` line, which the check of the case file asks for, and the Retro of this session leaves the Estimate `pending`, since its `method` waits for the close of a sprint. The `context` says why `estimate-prespec-binds-a-sprint-line` stands.
- **Change**
  - Asked: the person agreed, at the confirmation of the findings of `/pre-spec`, that 991.2 also rewrites the `method` of `estimate-hi-writes-frontier` into the form `by hand, after the reply that acknowledges the opening Case of /sprint-open in the session after the close of a sprint: …`, with the same meaning and the event named before the colon, the Criterion and the task line unchanged.
  - Taken: the `update` of 991.2 sets that `method` beside `status: pending`, and its `read` line stays.

## History

- 2026-11-01 created · raw/2026-11-01/2038/ledger.md#case-991
