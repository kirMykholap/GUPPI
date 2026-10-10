---
type: decision
case: "562"
status: archived
create: ["[[estimate-case-check-refuses-text-before-a-round]]"]
update: ["[[rule-case-check]]"]
origin: raw/2026-09-30/2356/ledger.md#case-562
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow, session]
---

## Problem

The rule that the main agent writes nothing of its own before a round of `case-guppi` is text alone, and it failed at every round of a session. No script reads the reply that shows a round. The question is how the rule is enforced, and how the defer of case 560 on the failed Estimate is retired.

## Recommend

- **How is the rule "nothing before a round" enforced?**
  Recommended: (a) a check at the end of the reply: `guppi casecheck` on `Stop`, when the turn holds a round of `case-guppi`, refuses a reply that does not open with the Context paragraph or the first question line, and the agent shows the round again; the main agent's own questions are not checked.
  Answer: (a).
- **How is the earlier put-off closed?**
  Recommended: (a) Case 561.9, sent back to its own `case-guppi`, carries `{supersedes:case 560}` on its line for `estimate-orchestration-shows-the-built-case` and is ratified again; this Case holds only the check.
  Answer: (a).
- **Who fixes the schema's sentence on a refused reply?**
  Recommended: (a) Case 561.9, while it is sent back, narrows the sentence of the schema and its line in the check to a reply that shows a Case, and adds that a refused round is shown again with nothing before it; this Case stays the check alone.
  Answer: (a).
- **Change**
  Asked: the pre-spec finding that the check would refuse the gathered list of the loop after the findings of `/pre-spec`, which runs in one turn. The person agreed with the recommendation: once the session's event log holds a `prespec` line of this session after its `hi`, the check does not judge text before the last tool call of the turn and judges only the first line of the reply. Before `/pre-spec` the check stays whole. The context also says that `## How it works` of `rule-case-check` is kept, as 561.10 keeps it.
  Taken: a `then` line and a `－` line bound the text check to the time before `/pre-spec`. The window is judged by the function of the hook of `rule-prespec-hook`, and the page text and the tasks say so. The context records the finding and the kept section.

## History

- 2026-10-01 created · raw/2026-09-30/2356/ledger.md#case-562
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
