---
type: decision
case: "626"
status: archived
children: ["[[decision-case-626.1]]", "[[decision-case-626.2]]"]
origin: raw/2026-10-04/0112/ledger.md#case-626
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Problem

The frame of `ask-guppi` requires five lines for every answer, while `/pre-spec`, the one moment the main agent dispatches it, asks for three kinds of findings. The answers swing between the two forms, and `estimate-ask-finds` fails on them. Its lines about a page asked in either language, a crossed rule and an archived slug wait for a dispatch that no normal run makes. The question is which form the answer takes at `/pre-spec`, and where the rest of the check is read.

## Recommend

- **Which form the answer of ask-guppi takes at /pre-spec**
  - Recommended: (a) a second form for `/pre-spec`: the frame keeps five lines for a question whether a thing exists and sets, for `/pre-spec`, numbered findings under the three questions, each naming its Case and page, "none" for a question with no finding, a file list allowed after; `rule-ask` and the Criterion of `estimate-ask-finds` change.
  - Answer: agreed with the recommendation, (a).
- **How the "does it exist" parts of the check get read**
  - Recommended: (b) read them in the transcript of `case-guppi` when it runs the search itself before a `create`; `estimate-ask-finds` keeps only the dispatch at `/pre-spec`.
  - Answer: agreed with the recommendation, (b).
- **The question put off on rule-ask: may ask-guppi open Decision pages**
  - Recommended: (a) close it as already settled: both agents now read Decision pages by the rule of `ask-guppi.md`; the change of `rule-ask` retires the defer, and nothing about Decision pages changes.
  - Answer: agreed with the recommendation, (a).
- **Where the "does it exist" lines of the check go**
  - Recommended: (a) a new Estimate on `rule-ask`, `estimate-ask-query-before-a-create`, read by hand in a session where `case-guppi` builds a Case with a `create` without a `ref`.
  - Answer: agreed with the recommendation, (a).
- **Does the /pre-spec skill also state the form**
  - Recommended: (a) the form lives in the frame of `ask-guppi` alone; `rule-prespec` and its Estimate stay.
  - Answer: agreed with the recommendation, (a).
- **Where the put-off question of a page goes in the /pre-spec answer**
  - Recommended: (a) in the finding that names the page, by a second replace pair in `rule-ask`; the five-line answer keeps it on the `exists` or `near` line; one more line of the Criterion of `estimate-ask-finds` checks it.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-04 created · raw/2026-10-04/0112/ledger.md#case-626
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
