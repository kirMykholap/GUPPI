---
type: decision
case: "762"
status: current
create: ["[[estimate-skill-sprint-close-migration-merged-into-main]]"]
supersedes: ["[[decision-case-757]]"]
origin: raw/2026-10-10/1713/ledger.md#case-762
sprint: plugin
created: 2026-10-10
tags: [sprint, git, workflow]
---

## Problem

The work of `migration` is not on `main`, and the session must merge it without leaving Work Mode on `main`. No check says when this merge is done.

## Recommend

- **How should `main` take the work of `migration`?**
  - Recommended: (a) fast-forward only, a refusal a stop for the person's word.
  - Answer: agreed, (a).
- **Which branch does the work go on after the merge?**
  - Recommended: (a) a new branch `plugin` made from `main`, and `migration` deleted by `git branch -d`.
  - Answer: agreed, (a).
- **What checks that the merge is done?**
  - Recommended: (a) a new Estimate under `rule-skill-sprint-close`, read by hand in this session and at each later opening after a sprint with a branch of its own.
  - Answer: agreed, (a).
- **What happens to the unticked merge line in the old Spec?**
  - Recommended: (a) a task of this Case ticks it by hand after the merge.
  - Answer: agreed, (a).
- **Does this Case also make the merge a step of opening a sprint?**
  - Recommended: (a) this merge only; a merge step of the sprint turn stays for the milestone that fixes the opening and the close.
  - Answer: agreed, (a).
- **Change**
  - Asked: the findings of `/pre-spec`: the stop on a refusal named as the first condition of `vault/wiki/where-to-stop.md`; the Estimate narrowed to the merge of `migration` in this session, the person's choice (a), since no Render sets the steps for later openings; and `estimate-where-to-stop-stops-only-on-its-conditions` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` named with why they stand.
  - Taken: built again as Case 762 in place of Case 757, the Estimate under the new slug `estimate-skill-sprint-close-migration-merged-into-main` with `when` and `then` on this merge alone, the `－` line on the first condition, and the two Estimates named in `context`.

## History

- 2026-10-10 created · raw/2026-10-10/1713/ledger.md#case-762
