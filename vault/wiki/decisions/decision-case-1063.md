---
type: decision
case: "1063"
status: current
children: ["[[decision-case-1063.1]]", "[[decision-case-1063.2]]", "[[decision-case-1063.3]]"]
origin: raw/2026-11-25/2003/ledger.md#case-1063
sprint: plugin
created: 2026-11-25
tags: [sprint, workflow, session, ledger, harness, render, schema, git]
---

## Problem

A one-off Estimate checks one state once, but a later Case must set it `pending` and read it again whenever it changes what that Estimate checked. The person decided that a passed one-off Estimate is not read again.

## Recommend

- **Is a passed one-off Estimate left alone by later Cases?**
  - Recommended: (a) left alone once passed: no `update`, no `pending`, and no missed Estimate at `/pre-spec`; a `pending` or `failed` one is updated as before.
  - Answer: (a).
- **How the new rule is checked**
  - Recommended: (b) a one-off reading of the four texts on the sprint page.
  - Answer: agreed, (b); the reading waits for the librarian's run of this session, since the four files change at its render.
- **Change**
  - Asked: the findings of `/pre-spec`, which the person accepted. The step of `/merge-main` and `estimate-skill-merge-main-joins-a-conflicted-page` set every Estimate of a joined text `pending`. The `－` line asked `estimates/schema.yaml` for a sentence it does not hold. `estimate-case-protocol-case-form` holds the sentence that the Case qualifies.
  - Taken: Case 1060 built again as Case 1063. Case 1063.1 holds its texts, with the `－` line narrowed to the other three texts. Case 1063.2 replaces the Criterion of `estimate-case-protocol-case-form`. Case 1063.3 qualifies the step of `/merge-main` and replaces the Criterion of its Estimate.

## History

- 2026-11-26 created · raw/2026-11-25/2003/ledger.md#case-1063
