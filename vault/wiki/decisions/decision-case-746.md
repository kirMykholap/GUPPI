---
type: decision
case: "746"
status: current
children: ["[[decision-case-746.1]]", "[[decision-case-746.2]]", "[[decision-case-746.3]]"]
origin: raw/2026-10-09/0200/ledger.md#case-746
sprint: migration
created: 2026-10-09
tags: [sprint, workflow, harness, session, hooks]
---

## Problem

The two sprint skill pages hang under `rule-session` and not under the phases that Case 743 named. `rule-session` therefore lists more than its five phases while the Estimate of that list stands `passed`. The two Estimates of the skills are `failed` without a reading, and the moment their method names has passed.

## Recommend

- **What this Case does with the earlier Case**
  - Recommended: (a) fix the live pages only; Case 743 and its ledger lines stay as they are, and the stale-line mechanism and the missing check of the type field stay separate Frontier items.
  - Answer: agreed, (a).
- **Where the two skill pages sit**
  - Recommended: (a) move them under their phases as signed: `rule-skill-sprint-open` under `rule-session-start` and `rule-skill-sprint-close` under `rule-plan-mode`, and `rule-session` lists the five phases alone.
  - Answer: agreed, (a).
- **How the two failed Estimates get read**
  - Recommended: (a) send both back for a reading at the Retro of this session, their Criteria unchanged and their method moved to that reading of the live pages and skill files.
  - Answer: agreed, (a).
- **How the move of the two skill pages is checked**
  - Recommended: (b) send `estimate-session-phases-in-order` back for a reading, its Criterion and method unchanged, read at the close of this session.
  - Answer: agreed, (b).
- **When the phases Estimate is read**
  - Recommended: (a) a method that runs at the Retro of this session: the session test run, the marks of the last finished session in time order, and the children of `rule-session` as the Spec of this Case sets them; the Criterion unchanged.
  - Answer: agreed, (a).

## History

- 2026-10-09 created · raw/2026-10-09/0200/ledger.md#case-746
