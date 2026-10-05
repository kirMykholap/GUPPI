---
type: decision
case: "660"
status: current
children: ["[[decision-case-660.1]]", "[[decision-case-660.2]]", "[[decision-case-660.3]]", "[[decision-case-660.4]]"]
origin: raw/2026-10-05/1616/ledger.md#case-660
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness, ledger, librarian, render, schema]
---

## Problem

One tag `{supersedes:case N}` on a parent Case means two different things in three scripts. As a result, a short defer of a parent fails at `/pre-spec`, and the librarian would apply the work the person put off.

## Recommend

- **What a tag on a parent retires**
  - Recommended: (a) the parent and all its sub-cases, in all three scripts; a tag on N.M retires N.M and its own sub-cases only.
  - Answer: agreed, (a).
- **Which code shares the one test of "N or one of its sub-cases"**
  - Recommended: (a) only the readers of the retire tag call one function of `guppi/materialize.py`: the Spec hook, the pre-spec check, `materialize` and the clash check of `casecheck`; the other copies stay.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) a sub-case for each script that changes, each replacing the Criterion of its Estimate and naming the shared function; the Estimate of the Spec hook stands.
  - Answer: agreed, (a).
- **Whether the Decision pages of the sub-cases become `superseded` too**
  - Recommended: (a) yes: `generate` sets each page of the `children` of a superseded page, at any depth, `superseded`, with its own sub-case and a new Criterion of `estimate-generate-writes-the-decision-page`.
  - Answer: agreed, (a).
- **How many tags the check asks for when a Case is rebuilt in another shape**
  - Recommended: (a) keep one tag per number; the check, its Estimate and the paragraph of `case-schema.md` stay.
  - Answer: agreed, (a).
- **Whether the Retro and handoff texts read the tag the same way**
  - Recommended: (a) yes: both texts say the tag covers the sub-cases, in a fourth sub-case with a new Estimate read by hand at a later Retro.
  - Answer: agreed, (a).
- **What happens to a sub-case's Decision page that is already archived**
  - Recommended: (a) only sub-case pages that stand `current` change; an archived or superseded one stays as it is, and the question `decision-case-469` put off stays open.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#case-660
