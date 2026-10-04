---
type: decision
case: "633"
status: current
children: ["[[decision-case-633.1]]", "[[decision-case-633.2]]"]
origin: raw/2026-10-04/2041/ledger.md#case-633
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Problem

The frame of `ask-guppi` sets the three lists of `/pre-spec` and nothing around them. `estimate-ask-finds` refuses every word beyond the lists and the paths, and it reads the order of searches as a limit. Each run adds what `CLAUDE.md` and the third question need: what was read, what was not checked, and searches that check a count. The check fails each time on text and searches that are useful. The question is what may stand around the lists, how freely the agent searches at `/pre-spec`, and how each is checked.

## Recommend

- **What may stand around the three lists**
  - Recommended: (b) a fixed frame: one line before the first list that names what was read, and after the findings one list of what was not checked, then the paths; no summary and no list of what holds.
  - Answer: agreed with the recommendation, (b).
- **How freely the agent searches at /pre-spec**
  - Recommended: (a) the fixed start stays, the Grep of the rules and one Grep per category; after them, more Greps and Reads are allowed to check a finding, and the frame gains one sentence that says so.
  - Answer: agreed with the recommendation, (a).
- **A count check that reaches the Decision pages**
  - Recommended: (a) a search that runs again a count stated in a Case may cover `vault/wiki/decisions/`, file names and counts only, no Decision page opened.
  - Answer: not as recommended. Other Decision pages are not counted again: that is extra context and needs no fixing. Each Decision page states its own at its moment, and reading them again would mean editing history all the time.
- **One promise or two**
  - Recommended: (a) two sub-cases: `estimate-ask-finds` keeps the form of the answer alone, and a new Estimate checks the searches at `/pre-spec`; both are read from the same transcript.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-04 created · raw/2026-10-04/2041/ledger.md#case-633
