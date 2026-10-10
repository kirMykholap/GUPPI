---
type: decision
case: "697"
status: archived
children: ["[[decision-case-697.1]]", "[[decision-case-697.2]]", "[[decision-case-697.3]]", "[[decision-case-697.4]]"]
origin: raw/2026-10-07/0211/ledger.md#case-697
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness, ledger]
---

## Problem

On an empty Frontier, the hook sends the agent on to `/pre-spec` in the same turn as the reply that closed the last line. So the person has no turn to ask a question before `/pre-spec` runs.

## Recommend

- **How the agent stops to ask before `/pre-spec`**
  - Recommended: (a) the reply asks whether to go on, in the plain form of the question which item is next, and the hook no longer sends the agent to `/pre-spec`; a yes makes the agent call `/pre-spec`, and a question of the person gets an answer and the question again.
  - Answer: agreed, (a).
- **Which replies ask the question**
  - Recommended: (a) all three ask: the acknowledging reply, the defer reply and the reply that closes a line with no ratification; no reply calls `/pre-spec` on its own.
  - Answer: agreed, (a).
- **The steps after `/pre-spec`**
  - Recommended: (a) the steps after `/pre-spec` stay automatic.
  - Answer: agreed, (a).
- **How this Case and Case 696 share the hook's text**
  - Recommended: (a) this Case builds on top of Case 696 and rewrites the hook's promise and rule text again, Case 696 untouched.
  - Answer: agreed, (a); the check of the Case then showed that this cannot hold, and the question was asked again as "How this Case and Case 696 share the hook's text (asked again)".
- **When you take a saved plan from an earlier session at `/hi`**
  - Recommended: (a) the reply that takes a conserved Spec goes on to `/pre-spec` with no question, as `/hi` sets it.
  - Answer: agreed, (a).
- **How this Case and Case 696 share the hook's text (asked again)**
  - Recommended: (a) Case 696 is built again with the change, and this Case changes only the replies.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec`, agreed to by the person: after `/pre-spec`, a reply with no `LEDGER` block that leaves no line under `## Cases` open goes on by itself, to the check and the exit or with the loop after the findings.
  - Taken: Case 697.2 says so in its new text of `rule-orchestration` and in its `then`.
- **Change**
  - Asked: a finding of `/pre-spec`, agreed to by the person: the Criterion of `estimate-orchestration-asks-in-the-grill-me-shape` gains the question whether to go on to `/pre-spec` in its list of questions that keep their own form.
  - Taken: Case 697.4 replaces that Criterion and carries the pair of `rule-orchestration` that adds the question to the list, moved from Case 697.1, since one sub-case replaces one Criterion.

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#case-697
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
