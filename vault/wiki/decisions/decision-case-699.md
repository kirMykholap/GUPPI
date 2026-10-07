---
type: decision
case: "699"
status: current
children: ["[[decision-case-699.1]]", "[[decision-case-699.2]]", "[[decision-case-699.3]]", "[[decision-case-699.4]]", "[[decision-case-699.5]]", "[[decision-case-699.6]]", "[[decision-case-699.7]]"]
origin: raw/2026-10-07/0211/ledger.md#case-699
sprint: migration
created: 2026-10-07
tags: [session, workflow, hooks, harness, render]
---

## Problem

A layout fault of a shown round or Case makes the `Stop` check send the reply back after the person has read it, and the agent shows the whole round or Case a second time. In a batch, the agent marks where each Case's round begins with a heading of its own, because the rules set no mark, and the check reads that heading as such a fault.

## Recommend

- **What the check does when only the layout of a round is wrong**
  - Recommended: (b) let it through, and tell the agent at the next message: the check lets the reply through, and a hook at the person's next message tells the agent what was wrong.
  - Answer: agreed, (b).
- **How a joint showing marks where each Case's round begins**
  - Recommended: (a) the Context label names the Case, such as `**Context — Case 697 (C4):**`, translated; a later round is marked by its question numbers alone.
  - Answer: agreed, (a).
- **Whether a layout fault in a shown Case is handled the same way**
  - Recommended: (a) layout faults of a Case get the note too; a file not sent or ledger lines that differ from the checked ones are still sent back.
  - Answer: agreed, (a).
- **Whether the person sees anything when a layout fault is let through**
  - Recommended: (a) the agent alone is told, at the person's next message.
  - Answer: agreed, (a).
- **Change**
  - Asked: by a finding of `/pre-spec` the person agreed to, let the batch label stand in the showing of a round in `rule-orchestration` and in the Criterion of `estimate-orchestration-shows-the-built-case`.
  - Taken: Case 699.4 adds a pair on the Render and two lines of its Criterion.
- **Change**
  - Asked: by a finding of `/pre-spec` the person agreed to, replace the sentence that a refusal of the check names the limit a showing broke.
  - Taken: Case 699.6 adds a pair that names the note at the next message too, and a line of its Criterion.
- **Change**
  - Asked: by a finding of `/pre-spec` the person agreed to, the label holds in the list of the rounds after the findings too, through `rule-prespec` and `estimate-prespec-gathers-the-answers-after-findings`.
  - Taken: the new Case 699.7 does it, since it replaces the Criterion of another Estimate.
- **Change**
  - Asked: by the person's answer (a) to the question of `/pre-spec`, name the old lesson `lesson-orchestration-batch-rounds-headed-by-own-text` and its Insight, and set `insight-orchestration-items-taken-together-unruled` `actioned`.
  - Taken: `context` names both, and Case 699.5 sets the Insight `actioned`.

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#case-699
