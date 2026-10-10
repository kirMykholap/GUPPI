---
type: decision
case: "685"
status: archived
children: ["[[decision-case-685.1]]", "[[decision-case-685.2]]"]
origin: raw/2026-10-06/0104/ledger.md#case-685
sprint: migration
created: 2026-10-06
tags: [session, hooks, harness, ledger, workflow]
---

## Problem

A Case that fixes the cause of a lesson written earlier in the same session can be ratified with no `{addresses:...}` on its decision lines, and nothing tells the agent, so the librarian never links the lesson to its fix.

## Recommend

- **Where the missing mark on a decision line is caught**
  - Recommended: (a) the ledger hook holds the decision lines once and asks.
  - Answer: no hold by the hook. The hook should look at the reply and tell the agent after the lines are written. The person does not want the agent to stop to work out whether to mark the lesson again, and asked whether the agent stops or goes on.
- **When the agent hears about a possible missing mark**
  - Recommended: (a) at the end of the same reply, after the lines are written.
  - Answer: agreed, (a).
- **Which ratifications bring the reminder**
  - Recommended: (a) every ratification after the lesson, until a mark links it.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec` the main agent sent back findings, with no word of the person needed: the sentence of `rule-orchestration` left out the reply of Case 688.7; a `－` line of Case 685.1 read as excluding a lesson already in the ledger; the link was judged on two sides with a test instead of by one function; and the context said `rule-prespec-onward` stands.
  - Taken: the sentence names the acknowledging reply and the reply that answers the reminder; the `－` line names a fresh lesson the same `Stop` holds back or refuses; one function of `guppi/materialize.py` judges the link and the hook imports it; the context leaves `rule-prespec-onward` to Case 686, and `given` names the case files of Cases 686 and 688.
- **Change**
  - Asked: the confirming check of `/pre-spec` found the reply that answers the hold of Case 688.7 named twice in the sentence of `rule-orchestration`, by both Cases; the person chose that Case 685.1 drops its mention and Case 688.7 keeps its own clause.
  - Taken: the new text of Case 685.1 names the acknowledging reply and the reply that answers the reminder alone, and the context says the hold reply is named by Case 688.7.

## History

- 2026-10-06 created · raw/2026-10-06/0104/ledger.md#case-685
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
