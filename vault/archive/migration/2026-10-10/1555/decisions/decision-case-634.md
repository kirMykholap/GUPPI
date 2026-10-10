---
type: decision
case: "634"
status: archived
children: ["[[decision-case-634.1]]", "[[decision-case-634.2]]", "[[decision-case-634.3]]"]
origin: raw/2026-10-04/2041/ledger.md#case-634
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Problem

`/pre-spec` sends one `ask-guppi` over the whole plan and takes its answer as the check of the whole Spec, though one run returns only a sample of the findings. A Case rebuilt on a finding reaches the approved Spec read only by the agent that rebuilt it. The question is how the first check covers each Case, how a rebuilt Case is confirmed without a loop of checks that never ends, and what the report says about how much was checked.

## Recommend

- **How the first check covers the whole plan**
  - Recommended: (a) one `ask-guppi` run per top-level Case, all at once; each judges its own Case and its sub-cases and reads the others only to find a clash; no run is repeated.
  - Answer: agreed with the recommendation, (a).
- **How a rebuilt Case is read against the vault**
  - Recommended: (b) one more `ask-guppi` run over the rebuilt Cases only, announced to the person before it starts.
  - Answer: not answered. The person asked whether this meant the same `ask-guppi` or a new one, and said a new one is bad: an agent always finds an error, so the checks would never end, and the real question is how many checks are enough, a small point missed being acceptable. Replaced by **How many checks a rebuilt Case gets**.
- **What the report says about how much was checked**
  - Recommended: (a) the report names which Cases each run read and repeats each run's list of what it did not check, and never says the Spec is checked as a whole.
  - Answer: agreed with the recommendation, (a).
- **How many checks a rebuilt Case gets**
  - Recommended: (b) the same `ask-guppi` confirms its own findings once: no new search and no new question; a finding not closed goes to the person as one question, fix or leave; the loop ends there.
  - Answer: agreed with the recommendation, (b).
- **When the found errors are confirmed as fixed**
  - Recommended: (a) before the rebuilt Cases are shown, so that each is ratified once, already confirmed, and no hook changes.
  - Answer: agreed with the recommendation, (a).
- **How the Case is cut and checked**
  - Recommended: (a) three sub-cases: the runs per Case with the coverage of the report, replacing the Criterion of `estimate-prespec-reconciles`; the confirmation, with a new Estimate; the sentence of `rule-orchestration`, replacing the Criterion of `estimate-orchestration-shows-the-built-case`.
  - Answer: agreed with the recommendation, (a).
- **Change**
  - Asked: the `/pre-spec` of session 2041 found six points in this Case, and no question was put to the person on them.
  - Taken: the runs follow the conserved Spec that the plan's title line names; the result of the confirmation stands after the horizontal rule; the question to fix or leave is a question after the confirmation; the confirmation runs no Grep, and the opening sentence of the frame of `rule-ask` leaves it out; the `method` of `estimate-case-build-checks-the-finished-case` reads the answers of the runs; the count of the lesson is stated with one finding unplaced.

## History

- 2026-10-04 created · raw/2026-10-04/2041/ledger.md#case-634
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
