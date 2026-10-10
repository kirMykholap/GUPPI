---
type: decision
case: "686"
status: archived
children: ["[[decision-case-686.1]]", "[[decision-case-686.2]]"]
origin: raw/2026-10-06/0104/ledger.md#case-686
sprint: migration
created: 2026-10-06
tags: [session, workflow, hooks, harness]
---

## Problem

After `/pre-spec`, the hook of `rule-prespec-onward` tells the agent that the Cases built again on the findings are ratified at any reply with a `LEDGER` block, before any Case has gone back to be built again, and sends it to the exit of Plan Mode.

## Recommend

- **How the hook tells the start of the loop after the findings from its end**
  - Recommended: (a) look for files of rebuilt Cases: the check and the exit only when a Case file was written after the `/pre-spec` run and every such Case is ratified; otherwise on with the loop.
  - Answer: agreed, (a).
- **Where this Case stops beside the item on the loop after the findings**
  - Recommended: (a) only the hook, its rule page and its checks; the text of the `/pre-spec` skill left to the other item.
  - Answer: (b) the hook and one sentence of the `/pre-spec` skill on what the hook says inside the loop.
- **What checks the new judgment of the hook**
  - Recommended: (b) a new check for the new judgment, and the line of `estimate-prespec-onward-sends-the-agent-on` on the message after `/pre-spec` rewritten to point to it; two sub-cases.
  - Answer: agreed, (b).
- **Change**
  - Asked: bring the `context` in line with Case 688 on `estimate-prespec-onward-reads-the-decisions-of-the-session`: the Estimate stands, for the reason Case 688 gives; no Estimate and no `then` line changes.
  - Taken: the `context` says that the Estimate stands and gives that reason; nothing else changed.

## History

- 2026-10-06 created · raw/2026-10-06/0104/ledger.md#case-686
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
