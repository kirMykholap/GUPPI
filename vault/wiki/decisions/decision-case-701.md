---
type: decision
case: "701"
status: current
children: ["[[decision-case-701.1]]", "[[decision-case-701.2]]", "[[decision-case-701.3]]", "[[decision-case-701.4]]", "[[decision-case-701.5]]", "[[decision-case-701.6]]", "[[decision-case-701.7]]"]
origin: raw/2026-10-07/0425/ledger.md#case-701
sprint: migration
created: 2026-10-07
tags: [session, workflow, hooks, harness, orchestration, ledger]
---

## Problem

After `/pre-spec`, a Case that was built and then dropped keeps the hook of `rule-prespec-onward` silent for the rest of Plan Mode, because its file has no decision line, and the person has to push the agent on by hand.

## Recommend

- **How the hook learns that a Case was dropped**
  - Recommended: (a) an empty file is no Case. `case-guppi` empties the file of a Case it drops, and the hook skips an empty file, both when it judges a Case out and when it judges a Case built again after `/pre-spec`.
  - Answer: agreed, (a).
- **Whether the Insight closes with this Case**
  - Recommended: (a) this Case sets `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` `actioned`, since an earlier Case closed its other cause.
  - Answer: agreed, (a).
- **Who empties the file when the person puts off or drops a Case after it was shown**
  - Recommended: (a) the main agent sends the drop to the same `case-guppi`, which empties the file and answers with a line `**Dropped:**` and the path.
  - Answer: agreed, (a).
- **How the emptying by `case-guppi` is checked**
  - Recommended: (a) one more line in the Criterion of `estimate-case-build-writes-the-case`, and a dropped Case added to the live dispatches its method reads after the render.
  - Answer: agreed, (a).
- **Change**
  - Asked: by the report of `/pre-spec`, fix the findings on Case 701: the dropped Case kept in the store of the check, the closer of a dropped item, the file left under an earlier number, the citation and the two unqualified sentences of `rule-prespec-onward`, the `description` of `case-guppi`, and `estimate-case-check-sends-back-a-faulty-case` named in `context`.
  - Taken: Case 701.7 leaves an empty Case file out of the other Cases of the check; 701.4 adds no closer and names the existing ones; 701.3 allows the file left under an earlier number and names the drop in the `description`; 701.1 and 701.2 each cite their own part and 701.2 qualifies both sentences; `context` names the faulty-case Estimate and says why it stands.
- **Change**
  - Asked: at `/pre-spec`, option (a): the turn of the person's words ends with one `**Waiting:**` line, and the short Case, its `LEDGER` block and the Frontier come in the turn that the answer `**Dropped:**` opens; the Criteria of `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-shows-the-frontier-after-a-closed-line` are replaced.
  - Taken: 701.4 sets the `**Waiting:**` line; Case 701.5 replaces the Criterion of `estimate-orchestration-defers-in-one-reply` and Case 701.6 that of `estimate-orchestration-shows-the-frontier-after-a-closed-line`, each with a pair on the Render of `rule-orchestration`.

## History

- 2026-10-07 created · raw/2026-10-07/0425/ledger.md#case-701
