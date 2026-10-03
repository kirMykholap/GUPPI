---
type: decision
case: "625"
status: current
update: ["[[estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]]", "[[estimate-prespec-onward-sends-the-agent-on]]", "[[estimate-retro-onward-sends-the-agent-to-the-handoff]]", "[[estimate-retro-runs-on-to-the-handoff]]"]
origin: raw/2026-10-04/0112/ledger.md#case-625
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness, hooks]
---

## Problem

Four Estimates name in their `method` a moment that a normal run never brings: a `/work` the person types, or a refusal of the ledger hook. Each passed only on the person's word, and when a later Case sets one `pending`, its reading waits for that moment for good. The question is whether the `method` keeps the moment or drops it.

## Recommend

- **Drop or keep the moment that never comes**
  - Recommended: (a) drop the moment from the `method` of all four; the tests of `tests/test_onward.py` keep covering the refusal path of the two hooks, and a fault at a typed `/work` or in the answer to a refusal shows as a lesson when it comes.
  - Answer: agreed with the recommendation, (a).
- **Only these four pages, or a general rule**
  - Recommended: (a) only the four pages; no sentence is added to `rule-estimates-schema`.
  - Answer: agreed with the recommendation, (a).
- **What the pages promise about the moment that was dropped**
  - Recommended: (a) keep the promises and change only `method`; the four stay `passed`, as `estimate-retro-runs-on-to-the-handoff` already treats a typed `/retro`.
  - Answer: agreed with the recommendation, (a).
- **How we know this change is done**
  - Recommended: (a) no new check; the Case names `estimate-lint-reports-a-method-tied-to-a-one-off-moment` for the form and `estimate-hi-takes-its-readings` for the next reading.
  - Answer: agreed with the recommendation, (a).
- **One Case or one sub-case per page**
  - Recommended: (a) one Case with four page updates, ratified together.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-04 created · raw/2026-10-04/0112/ledger.md#case-625
