---
type: decision
case: "794"
status: current
create: ["[[rule-github-repository]]"]
update: ["[[estimate-sprint-plugin-pull-requests-reviewed-on-github]]", "[[entity-sprint-plugin]]"]
supersedes: ["[[decision-case-787.1]]"]
origin: raw/2026-10-12/2349/ledger.md#case-794
sprint: plugin
created: 2026-10-12
tags: [github, ci, git, sprint, workflow]
---

## Problem

Case 787.1 would push the whole history, the former product's commits included. It would also make `lint` block every merge into `main`, though lint is red at the Baseline and is only a signal.

## Recommend

- **Change**
  - Asked: the person, in Work Mode, chose to cut the history at `8b34941a` before the first push, so that the commits after it keep their content with new ids, and to make only `style` and `test` required on `main`, with `lint` shown but not blocking.
  - Taken: Case 787.1 is built again as Case 794 with `{supersedes:case 787.1}`. The Purpose of `rule-github-repository`, the Criterion of `estimate-sprint-plugin-pull-requests-reviewed-on-github` and the tasks change as `context` says.
- **Where should the old history stay on this computer?**
  - Recommended: (b) a local backup branch only while the cut is made and checked; after the push and its check, the backup branch and the tag `vault-v1` are removed, and git clears the old commits.
  - Answer: agreed, (b).
- **What happens to the commit ids that pages already quote?**
  - Recommended: (a) they stay as records; the texts do not change.
  - Answer: agreed, (a).
- **Does this Case change the README sentence about the history?**
  - Recommended: (a) this Case changes the sentence before the push: the public history starts at the commit that removed the product, and the earlier history stays only in the owner's local copy.
  - Answer: agreed, (a).
- **How is the cut checked?**
  - Recommended: (a) a check by hand in Work Mode just before the push: the first commit has no parent and holds the files of the commit that removed the product, the last commit of `plugin` holds the same files as before the cut, and a search of the new history for the key and the token finds nothing; the check page of the sprint keeps only the pull request.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-794
