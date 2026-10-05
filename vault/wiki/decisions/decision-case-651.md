---
type: decision
case: "651"
status: current
children: ["[[decision-case-651.1]]", "[[decision-case-651.2]]", "[[decision-case-651.3]]"]
origin: raw/2026-10-05/1343/ledger.md#case-651
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

`orchestration.md` calls the reply of `case-guppi` "the answer" while that reply is now a summary, and it states the `ratification` of a showing and the `then` block of a short-form defer in words that the main agent has twice read into a form the checks refuse. The question was which words replace "the answer", how far the change reaches, how the two forms are shown and checked, and what happens to the Insight.

## Recommend

- **Which word replaces "the answer"**
  - Recommended: (a) a word for each meaning: the summary where the main agent reads the reply of `case-guppi`, the file where the Case is sent, and the text the check stored where the Spec hook reads; a round and a Fact reply keep their names.
  - Answer: agreed, (a).
- **How far the change reaches**
  - Recommended: (a) only `orchestration.md`; the other pages and the code keep their words.
  - Answer: agreed, (a).
- **How the page states the two forms**
  - Recommended: (b) an example checked by a test that runs the checks over it and fails on any refusal.
  - Answer: agreed, (b).
- **Which forms the page covers**
  - Recommended: (a) the `ratification` of a showing and the `then` block of a short-form defer, the two the lessons name.
  - Answer: agreed, (a).
- **One check or one per form**
  - Recommended: (a) three sub-cases: the rewording, checked by `estimate-orchestration-shows-the-built-case` as it stands; the example of a showing with a new Estimate; the example of a short-form defer with a new Estimate.
  - Answer: agreed, (a).
- **What the test does before the page holds the example**
  - Recommended: (a) skip until the render, with a reason that names `orchestration.md`; a Case of a later session removes the skip after the readings pass.
  - Answer: agreed, (a).
- **What the example of a showing shows**
  - Recommended: (a) a parent with two sub-cases: the heading, a list of two items, one `ratification` quote block with the lines of both, the horizontal rule and the agent's own text.
  - Answer: agreed, (a), with the heading of the example in English, since the example is part of the documentation.
- **What happens to the open Insight**
  - Recommended: (a) mark it `actioned`, addressed by this Case.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#case-651
