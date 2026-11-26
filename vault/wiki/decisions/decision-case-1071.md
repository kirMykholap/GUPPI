---
type: decision
case: "1071"
status: current
children: ["[[decision-case-1071.1]]", "[[decision-case-1071.2]]"]
origin: raw/2026-11-26/1515/ledger.md#case-1071
sprint: plugin
created: 2026-11-26
tags: [harness, workflow, session, ledger, render, schema, sprint]
---

## Problem

A lasting check on a rule page that reads the transcript of a session can wait long and fail often. While it stands failed, it stops the clean build of a page that ships. No rule says where such a reading belongs, and nothing reports a Case that puts one on a rule page.

## Recommend

- **Whether the split becomes a rule**
  - Recommended: (b) a rule for each new Estimate, and for each Estimate whose Criterion a Case replaces; the Estimates that stand today change only when a Case replaces their Criterion.
  - Answer: agreed, (b).
- **What reports a Case that misses the split**
  - Recommended: (b) the text, and a finding of `guppi prespec --check`, by one new function of `.guppi/guppi/lint.py` that the lint run does not call.
  - Answer: agreed, (b).
- **Whether a Criterion set again word for word counts as replaced**
  - Recommended: (b) not a replacement: a Criterion written back unchanged gives no finding, so `/merge-main` keeps its steps.
  - Answer: agreed, (b).
- **Change**
  - Asked: `/pre-spec` asked that the new text of `rule-case-protocol`, a page with `core: true`, name `/merge-main` only where the project holds `.claude/skills/merge-main/SKILL.md`, and that a lasting `method` may read the text of any page that ships, in the Spec at Retro or in the file rendered from it, not only the Render of its own rule.
  - Taken: the new sentence of `rule-case-protocol` names `/merge-main` with that condition, and the new text of both pages and the then of Case 1071.1 say that a lasting `method` reads a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it.

## History

- 2026-11-26 created · raw/2026-11-26/1515/ledger.md#case-1071
