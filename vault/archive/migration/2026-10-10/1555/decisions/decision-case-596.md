---
type: decision
case: "596"
status: archived
children: ["[[decision-case-596.1]]", "[[decision-case-596.2]]", "[[decision-case-596.3]]"]
origin: raw/2026-10-02/2049/ledger.md#case-596
sprint: migration
created: 2026-10-02
tags: [session, workflow, hooks, harness, render]
---

## Problem

After the reply that ends Retro, the hook of `rule-retro-onward` speaks once per stretch. When the ledger hook refuses a line of that reply, the agent must answer with a second reply that writes the line again and ends. Nothing then sends the agent on, so the run stops before the commit and `/handoff` where no person is needed. The Retro text also forbids that second reply.

## Recommend

- **Which refusals let the hook send the agent on again**
  - Recommended: (a) after a refusal of the ledger hook. The hook stays silent only when its own refusal stands and no refusal of the ledger hook stands at the same ending or after it. It stays bounded because the ledger hook refuses each faulty line once a stretch. The change lives in `rule-retro-onward` and `guppi/onward.py`.
  - Answer: agreed with the recommendation, (a).
- **Retro's text on the reply that writes a refused line again**
  - Recommended: (a) add one exception to `rule-retro`: the sentence allows the reply that writes again the lines the ledger hook refused, with nothing else in it. After it, the hook sends the agent on to the commit and `/handoff`.
  - Answer: agreed with the recommendation, (a).
- **How the change is checked**
  - Recommended: (a) replace the promise of `estimate-retro-onward-sends-the-agent-to-the-handoff` whole, with its `purpose` and `method` updated to match. The hand check is read at the first end of Retro where the ledger hook refuses a line. `estimate-retro-onward-exits-2-on-an-error` stands.
  - Answer: agreed with the recommendation, (a).
- **The Plan Mode version of the hook**
  - Recommended: (a) Retro only. The Plan Mode version is left as it is and named as not done.
  - Answer: agreed with the recommendation, (a).
- **Change**
  - Asked: Case 597 of this session drops `stop_hook_active` as the guard of `uv run guppi onward --plan`, and the person agreed. So the line of 596.1 saying that the Plan Mode run keeps that flag as its guard becomes false. It should instead say that the Plan Mode run keeps its own judgment, set by `rule-prespec-onward`, and Case 596 is ratified again.
  - Taken: the last `－` line of the `then` of 596.1 now says that `uv run guppi onward --plan` keeps its own judgment, set by `rule-prespec-onward`. `given` names the case file of Case 597. `context` says that Case 597 changes the Plan Mode run and leaves the Estimate of 596.1 untouched.

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#case-596
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
