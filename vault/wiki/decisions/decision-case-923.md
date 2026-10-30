---
type: decision
case: "923"
status: current
create: ["[[estimate-orchestration-states-a-subagent-fact-from-its-transcript]]"]
update: ["[[rule-orchestration]]", "[[insight-orchestration-writes-from-its-own-reading]]"]
origin: raw/2026-10-30/0304/ledger.md#case-923
sprint: plugin
created: 2026-10-30
tags: [session, workflow, orchestration, harness]
---

## Problem

No text says that a fact about what a subagent did comes from its transcript. The main agent stated such a fact from the subagents' summaries, which do not show their tool errors.

## Recommend

- **What the Case does with the Insight**
  - Recommended: (b) add one sentence to `orchestration.md`: a fact about what a subagent did is stated only after the main agent reads it in that subagent's transcript, and mark the Insight as dealt with.
  - Answer: agreed, (b).
- **Which Estimate checks the new sentence**
  - Recommended: (a) a new Estimate, `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, read by hand at the Retro of this session and after the first reply under the new Render that states such a fact.
  - Answer: agreed, (a).
- **Change**
  - Asked: after a finding of `/pre-spec`, the person chose that the sentence tells two cases apart: a fact the main agent states as its own of what a subagent did needs that subagent's transcript, and what a subagent reports of its own calls the main agent may pass on with no transcript, marked as that subagent's report; the report of `/pre-spec` stays as it is.
  - Taken: the new sentence, the `then` and the `purpose` of the new Estimate now tell the two cases apart.

## History

- 2026-10-30 created · raw/2026-10-30/0304/ledger.md#case-923
