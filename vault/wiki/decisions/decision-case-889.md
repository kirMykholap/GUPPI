---
type: decision
case: "889"
status: current
children: ["[[decision-case-889.1]]", "[[decision-case-889.2]]"]
origin: raw/2026-10-26/0118/ledger.md#case-889
sprint: plugin
created: 2026-10-26
tags: [session, workflow, hooks, harness]
---

## Problem

After `/pre-spec`, a batch ratified in part leaves the Cases still out with no turn: the hook that sends the agent on stays silent while any Case is out, so the run stops where no person is needed.

## Recommend

- **How the run goes on after a partial ratification**
  - Recommended: (a) the hook sends the agent on with a third message.
  - Answer: agreed, (a).
- **Which replies get the new message**
  - Recommended: (a) the same replies as today.
  - Answer: agreed, (a).
- **What the new message names**
  - Recommended: (a) the message names each Case left without a ratification.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) rewrite the two existing checks, in two sub-cases.
  - Answer: agreed, (a).
- **Change**
  - Asked: the findings of `/pre-spec`: the text that each reason adds asks for `STOP:` for a Case still with its `case-guppi` while the third reason asks for the `**Waiting:**` line; the `context` claimed that the item of Case 887 stays in `backlog.md`; the tests of `estimate-prespec-onward-reads-the-decisions-of-the-session` tell a Case not out by exit 2 alone.
  - Taken: `ONLY_THE_PERSON` and the line of Case 889.1 keep `STOP:` for a question or a Case that waits only for the person's word and send a `case-guppi` that has not answered to the end of the turn that `orchestration.md` sets for a Case out, which Case 890.3 sets for a Case sent back after a refusal; the `context` says that Case 890 retires the item of Case 887; the tests of a Case not out assert the reason of the exit or of the loop, and that Estimate's Criterion stands, as the `context` says.

## History

- 2026-10-26 created · raw/2026-10-26/0118/ledger.md#case-889
