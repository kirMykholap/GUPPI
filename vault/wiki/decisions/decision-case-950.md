---
type: decision
case: "950"
status: current
children: ["[[decision-case-950.1]]", "[[decision-case-950.2]]"]
origin: raw/2026-10-31/0128/ledger.md#case-950
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Problem

The `method` of two pending Estimates asks for a reading at a Retro that has passed. `rule-retro` does not take that reading while the other part of the method waits for its event, and an `estimate` line cannot hold half a reading. So `estimate-case-build-reads-each-list-of-a-new-member` holds no record of its Retro part, and `estimate-orchestration-shows-the-built-case` would hold none either.

## Recommend

- **What happens to the Retro part of the method?**
  - Recommended: (a) read the live instruction together with the `/pre-spec` part, both in one estimate line.
  - Answer: agreed, (a).
- **How is the update of the Estimate written?**
  - Recommended: (a) write the Criterion back unchanged, with `pending` and the new method.
  - Answer: agreed, (a).
- **Which `/pre-spec` does the reading wait for?**
  - Recommended: (b) the first `/pre-spec` on the new instruction whose plan holds a Case that adds a member to a list.
  - Answer: agreed, (b).
- **Does the Case also fix the other open Estimate with the same two-part shape?**
  - Recommended: (a) this Estimate only.
  - Answer: (b), both Estimates.
- **Change**
  - Asked: Case 954 asks, by its line Other Case, for one `－` line in the Criterion of `estimate-orchestration-shows-the-built-case` after the line on `ask-guppi` at pre-spec: a start of `ask-guppi` in Work Mode for a test by hand of a hook that judges its calls is outside this promise, and `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads it.
  - Taken: Case 950.2 adds that line as the first `－` line of its `then`, names the new Estimate in its `given`, and replaces the Criterion whole instead of writing it back unchanged.
- **Change**
  - Asked: the findings of `ask-guppi` at `/pre-spec`. The `＋` line that says the main agent dispatches `ask-guppi` only at pre-spec contradicts the new `－` line. `context` says the session folder holds no `ledger.md`, though it now holds one. The new `method` of Case 950.2 does not say which Render its first summary falls under.
  - Taken: the `＋` line takes the exception of the start that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads, so "only" holds. The `－` line points to that Estimate in general words. `context` reports what the searches of the ledger printed. The `method` waits for a summary in a session that opens on the Render of `rule-orchestration` rendered by the librarian's run after session 0128.
- **Change**
  - Asked: the check of the plan found that the new `method` and the `change` of Case 950.2 name a session outside a bracket of their own.
  - Taken: both now name the event by the Render alone, the Render of `rule-orchestration` that lets the main agent start `ask-guppi` in Work Mode for a test of a hook that judges its calls.

## History

- 2026-10-31 created · raw/2026-10-31/0128/ledger.md#case-950
