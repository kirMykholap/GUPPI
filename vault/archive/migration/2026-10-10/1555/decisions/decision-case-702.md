---
type: decision
case: "702"
status: archived
create: ["[[estimate-spec-write-reads-a-new-tag]]"]
update: ["[[rule-spec-write]]", "[[rule-case-protocol]]"]
origin: raw/2026-10-07/0425/ledger.md#case-702
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A Case file cannot declare a new tag, so a tag that a ratified page carries, such as `orchestration`, can never enter `tags.md`, and `generate` warns about it.

## Recommend

- **Register the tag or take it off the pages**
  - Recommended: (a) take the tag off the live lesson and the Insight, and use `workflow` and `session` like the other pages about `rule-orchestration`, with no code change.
  - Answer: (b) register it: give the Case file a way to declare a tag, then declare `orchestration`.
- **Whether anything stops an unlisted tag from getting in again**
  - Recommended: (a) leave it not done; the Case says that no check stops an unlisted tag.
  - Answer: agreed, (a).
- **How a Case file declares a new tag**
  - Recommended: (a) a task line `tag` with the tag in a code span and two sub-points, `meaning` and `aliases`, each one code span, which the Spec hook turns into one entry of `new_tags`; a tag line with a missing or a foreign sub-point is refused.
  - Answer: agreed, (a).
- **When `orchestration` itself is declared**
  - Recommended: (a) a Case of a later session declares it, after the render puts the form into `case-schema.md`; the handoff names it.
  - Answer: agreed, (a).
- **What checks that the hook reads the new line**
  - Recommended: (a) a new Estimate of `rule-spec-write`, `estimate-spec-write-reads-a-new-tag`, checked by tests in `tests/test_ratified.py`; the Criterion of `estimate-spec-write-copies-the-ratified-case` stands.
  - Answer: agreed, (a).
- **Whether the tag line leaves a box in the Spec**
  - Recommended: (b) no box: the hook puts the declaration into `new_tags` of the `then` block and leaves the line out of the `tasks` block; `generate` and Retro do not change.
  - Answer: agreed, (b).

## History

- 2026-10-07 created · raw/2026-10-07/0425/ledger.md#case-702
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
