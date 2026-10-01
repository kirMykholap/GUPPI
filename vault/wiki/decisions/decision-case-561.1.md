---
type: decision
case: "561.1"
status: current
parent: "[[decision-case-561]]"
update: ["[[rule-prespec]]", "[[rule-prespec-hook]]", "[[estimate-prespec-reconciles]]", "[[rule-prespec]]"]
supersedes: ["[[decision-case-503]]"]
origin: raw/2026-09-30/2356/ledger.md#case-561.1
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, hooks]
---

## Recommend

- **How often does `ask-guppi` check the plan?**
  Recommended: (a) once per session, at the first `/pre-spec`; later checks are mechanical, and a rebuilt Case is checked by its own `case-guppi`.
  Answer: (a). The person accepts the risk left and asked for another option to be named. That option became Case 561.4.
- **What stays in the `/pre-spec` skill?**
  Recommended: (a) a short skill that gives the order, with the list of what the check prints moved to `rule-prespec-hook`.
  Answer: (a).
- **Change**
  Asked: the pre-spec check found that the new Render decides the question that case 503 put off on `rule-prespec`, the numbering of the report and its split into two parts. The person agreed with the recommended fix.
  Taken: the decision line of this sub-case on `rule-prespec` carries `{supersedes:case 503}`.
- **Change**
  Asked: the pre-spec check found that a catalog of what the check compares in the Purpose of the Leaf `rule-prespec-hook` goes against `rule-rules-schema`, which keeps the mechanism of a Leaf in the docstring of its code. The person agreed with the recommended fix. The choice to take the catalog out of the skill and put it beside the code stands.
  Taken: the catalog goes into the module docstring of `guppi/prespec.py` as a Work Mode task. The Purpose of `rule-prespec-hook` gains one sentence that points there, and the Render of the skill names the docstring.

## History

- 2026-10-01 created · raw/2026-09-30/2356/ledger.md#case-561.1
