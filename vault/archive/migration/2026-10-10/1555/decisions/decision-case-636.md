---
type: decision
case: "636"
status: archived
update: ["[[rule-case-build]]", "[[estimate-case-build-checks-the-finished-case]]", "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"]
origin: raw/2026-10-04/2245/ledger.md#case-636
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness, ledger, tests]
---

## Problem

A Case's `context` states files and counts of searches that the searches did not print, because `case-guppi` writes them from its own reading during the build. The instruction to claim nothing a search did not print has failed in three sessions since it was set, and only the pre-spec check catches the fault.

## Recommend

- **How should the fix work?**
  - Recommended: (a) just before answering with a Case, `case-guppi` runs each search it cites again, exactly as the context writes it, and copies the files or the count from that output; the Criterion of `estimate-case-build-checks-the-finished-case` replaced to match.
  - Answer: agreed with the recommendation, (a).
- **Which texts does the fix cover?**
  - Recommended: (a) Case contexts only; reading and ledger lines stay under the writing rule of `CLAUDE.md`.
  - Answer: agreed with the recommendation, (a).
- **Change**
  - Asked: at pre-spec, on the archive of the Insight's children by the cascade and on the lesson of Case 620 with another cause: (a) name the cascade in `context` and keep the rest as it is, with `context` saying that the four lessons are archived, that the lesson of Case 620 has another cause which this Case does not close, and that the Criterion line of `estimate-case-build-checks-the-finished-case` on searching the rules of the same moment already covers that cause; or (b) take that lesson out of the Insight's `children`. Recommended (a); the person agreed, (a).
  - Taken: `context` names `estimate-generate-cascades` and the archive of the four children, and says which three children share the cause this Case closes; `given`, `then`, the pairs and the ledger lines are unchanged.
- **Change**
  - Asked: at the second pre-spec run, on the lesson of Case 620, whose `root_cause` gives two causes: (a) fix the wording so that `context` says the moment-search line of the Criterion covers the first cause, that no line covers the second (the cascade of a `set` not searched), that this Case does not close it, and that the lesson is archived with the Insight all the same and a recurrence raises it again; or (b) leave it as it is. Recommended (a); the person agreed, (a).
  - Taken: `context` says so; `given`, `then`, the pairs and the ledger lines are unchanged.

## History

- 2026-10-05 created · raw/2026-10-04/2245/ledger.md#case-636
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
