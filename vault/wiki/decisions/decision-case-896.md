---
type: decision
case: "896"
status: current
children: ["[[decision-case-896.1]]", "[[decision-case-896.2]]", "[[decision-case-896.3]]", "[[decision-case-896.4]]"]
origin: raw/2026-10-28/2312/ledger.md#case-896
sprint: plugin
created: 2026-10-28
tags: [harness, case-build, hooks, session, workflow]
---

## Problem

The helper that builds a Case keeps everything in its context and grows towards about 967 000 tokens. The test of the remedy showed that the compaction comes below the set size, so the check of the test stands failed.

## Recommend

- **Do we build the remedy for the helper's memory now?**
  - Recommended: (a) build it now.
  - Answer: agreed, (a).
- **How is the failed check set right?**
  - Recommended: (a) rewrite its first line and read it again from the saved files.
  - Answer: agreed, (a).
- **At what size does the helper compact?**
  - Recommended: no single answer, since how far below the set size the compaction comes was not checked; (a), a size of 400 000, is the one that keeps the limit of 400 000 whatever that share is.
  - Answer: agreed; read as (a), the option the main agent named after the round as the one that keeps the limit.
- **When does the helper write its working note?**
  - Recommended: (a) always, after each round, each answer it gets and each change.
  - Answer: agreed, (a).
- **Where does the working note live?**
  - Recommended: (a) beside the Case file, as `cases/note-<N>.md`.
  - Answer: agreed, (a).
- **How do we check that the real helper goes on after a compaction?**
  - Recommended: (a) a new check, read at the first real compaction of `case-guppi`.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the fixes of the findings of `/pre-spec` as proposed.
  - Taken: the new `method` of `estimate-case-build-goes-on-after-a-compaction` describes the test by its procedure, and the one past run stands in a bracket of its own. Case 896.2 adds to `rule-spec-reconcile` the sentence that the hook writes any other file of `case-guppi` under `cases/`, and rewords the refusal of the guard; `context` names `estimate-spec-reconcile-refuses-an-edit-of-the-plan`, which stands. Case 896.4 reuses `case_number` in place of a new judgment of the note, and its `then` and the new Criterion no longer claim that a call that wrote only the note counts as no file. The claim in `context` on the other Estimates of `rule-case-check` is narrowed.

## History

- 2026-10-29 created · raw/2026-10-28/2312/ledger.md#case-896
