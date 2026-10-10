---
type: decision
case: "579"
status: archived
children: ["[[decision-case-579.1]]", "[[decision-case-579.2]]"]
origin: raw/2026-10-01/1441/ledger.md#case-579
sprint: migration
created: 2026-10-01
tags: [session, workflow, ledger, harness]
---

## Problem

The check `case-guppi` runs on its finished Case missed a clash with a Case ratified earlier in the same session, because such a Case is not yet in the rule pages it searches. It also missed an Estimate whose `purpose` still stated the promise its replaced Criterion had dropped. The question was how the related Cases of the session reach `case-guppi`, which Cases count as related, whether the `purpose` and `method` of a replaced Estimate are checked, and how each change is measured.

## Recommend

- **Change the rule, or read the Estimate again?**
  - Recommended: (b) a Case that adds both checks: `case-guppi` reads the case files of the session for a Case at the same moment or on the same pages, and checks the `purpose` and `method` of an Estimate whose Criterion it replaces.
  - Answer: none of the options. `case-guppi` must not read the Cases of this session. The main agent knows all the Cases, so it is the main agent's task to tell `case-guppi` that a related Case already exists.
- **What the main agent writes about a related Case**
  - Recommended: (a) the id, one sentence on what it sets and which pages it changes, and the path of its case file; `case-guppi` reads that file and no other Case of the session.
  - Answer: (a).
- **Which Cases count as related**
  - Recommended: (a) each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment.
  - Answer: (a).
- **The `purpose` and `method` lines of a replaced Estimate**
  - Recommended: (a) keep this check: when `case-guppi` replaces a Criterion, it rewrites in the same Case each of those lines that states the old promise.
  - Answer: (a).
- **How the change is checked**
  - Recommended: (a) two sub-cases: a new Estimate on `rule-case-protocol` for the dispatch, and the Criterion of `estimate-case-build-checks-the-finished-case` replaced; both read in a later session after the render.
  - Answer: (a).

## History

- 2026-10-01 created · raw/2026-10-01/1441/ledger.md#case-579
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
