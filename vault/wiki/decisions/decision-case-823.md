---
type: decision
case: "823"
status: current
children: ["[[decision-case-823.1]]", "[[decision-case-823.2]]", "[[decision-case-823.3]]", "[[decision-case-823.4]]", "[[decision-case-823.5]]", "[[decision-case-823.6]]"]
origin: raw/2026-10-15/1959/ledger.md#case-823
sprint: plugin
created: 2026-10-15
tags: [ci, plugin, session, workflow, harness, hooks, sprint, git, ledger]
---

## Problem

Sixteen shipped Estimates hold pointers outside a bracket, so every build of `prod` exits 1, and `/pre-spec` cannot catch a new one in an Estimate.

## Recommend

- **How does the build stop failing on these Estimates?**
  - Recommended: (a) leave such an Estimate out of the copy.
  - Answer: the pages must be rewritten, (b).
- **Does `/pre-spec` catch such a reference in the new text of an Estimate?**
  - Recommended: (b) add it as a sub-case.
  - Answer: (b).
- **How is a reference in a `method` reworded?**
  - Recommended: (a) move the reference into a bracket at the end, and fix the wait where `/pre-spec` would report it.
  - Answer: agreed, (a).
- **How are the four Estimates whose Criterion changes read again?**
  - Recommended: (a) give those two a `method` that runs in this session.
  - Answer: agreed, (a).
- **What checks that no shipped Estimate holds such a reference?**
  - Recommended: (a) a new Estimate with a test over the live repository.
  - Answer: agreed, (a).
- **What checks that `/pre-spec` judges the new text of an Estimate?**
  - Recommended: (a) replace that Estimate's Criterion.
  - Answer: agreed, (a).
- **What does the line on the insight say in the new Criterion of the defer-example Estimate?**
  - Recommended: (a) say what holds now, the reference in a closing bracket.
  - Answer: agreed, (a).
- **Change**
  - Asked: a `/pre-spec` finding — seven new methods said "the session that set this method", which would point at this session.
  - Taken: each names the session by what happened in it, its pointer in the bracket at its end.
- **Change**
  - Asked: a `/pre-spec` finding — `form_finding` is a nested function of `.guppi/guppi/prespec.py`, not of `lint.py`.
  - Taken: `context` says so.
- **Change**
  - Asked: a `/pre-spec` finding — the live test is red until the librarian's run; the person chose a pytest marker that the default run leaves out.
  - Taken: the test carries the marker `live`, `.guppi/pyproject.toml` registers it and leaves it out by default, and the new Estimate runs it with `-m live`.
- **Change**
  - Asked: a `/pre-spec` finding — the Criterion of Case 823.2 asked what only a later `case-guppi` shows; the person chose to drop that sentence.
  - Taken: the sentence is dropped; the Estimate promises the note of the hook alone.

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#case-823
