---
type: decision
case: "856"
status: current
children: ["[[decision-case-856.1]]", "[[decision-case-856.2]]", "[[decision-case-856.3]]"]
origin: raw/2026-10-16/1712/ledger.md#case-856
sprint: plugin
created: 2026-10-16
tags: [harness, render, schema, session, workflow, ledger, plugin, ci, sprint, git]
---

## Problem

The clean version of GUPPI carries three sentences of rules and four shipped Estimates that hold only in the repository of GUPPI, and the Render of `rule-rules-schema` still says that a page with `core: true` ships without its Estimates.

## Recommend

- **How should the `core` field read?**
  - Recommended: (a) one wording true in both places: the page is part of GUPPI, `guppi ship` writes it in the repository of GUPPI into the clean version that a project installs, and a page without it is a page of the project that holds it.
  - Answer: agreed, (a).
- **How should the sentence on old Case ids in `rule-ratification` read?**
  - Recommended: (a) name the list `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py`, and put the two sprint names in a bracket with the pointer, which `guppi ship` removes.
  - Answer: agreed, (a).
- **What happens to the Estimate on the merge of `migration` into `main`?**
  - Recommended: (a) delete it and remove it from the `estimates` of `rule-skill-sprint-close`.
  - Answer: agreed, (a).
- **What should the three methods that preview `--sprint migration` say?**
  - Recommended: (a) preview the open sprint, `--sprint <id>` with `<id>` the sprint that `vault/wiki/sprint.md` names.
  - Answer: agreed, (a).
- **Does the fifth Estimate, which the reading missed, come in?**
  - Recommended: (a) leave it for the next reading to list.
  - Answer: agreed, (a).
- **Should this Case also take up the put-off fix of `rule-rules-schema`?**
  - Recommended: (a) take it up here as a sub-case.
  - Answer: agreed, (a).
- **How is the fix checked?**
  - Recommended: (a) the same Estimate, read again, with every sentence read.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, the check of Case 856.2 can never close while the line of `estimate-ratification-case-id-carries-the-sprint` stays on the list; the person agreed to narrow it.
  - Taken: Case 856.2 is checked when the list of the reading holds no sentence of the four Estimates it changes; the line of the fifth Estimate may stay on the list for a later Case.

## History

- 2026-10-16 created · raw/2026-10-16/1712/ledger.md#case-856
