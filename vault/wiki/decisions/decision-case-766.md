---
type: decision
case: "766"
status: current
update: ["[[estimate-sprint-plugin-pull-requests-reviewed-on-github]]"]
origin: raw/2026-10-10/1913/ledger.md#case-766
sprint: plugin
created: 2026-10-10
tags: [sprint, github, git]
---

## Problem

The pull-request Estimate of the sprint `plugin` cannot be read now, since no pull request from a second account exists. Its wording leaves open whether a second account of the owner counts as another account, and it asks for a pull request against `main`, which does not move before the sprint closes.

## Recommend

- **What happens to the pull-request check?**
  - Recommended: (a) keep the check; a second account of the owner counts, and the page gets a History line saying that it waits under the rule of Case 764.
  - Answer: agreed, (a).
- **Change**
  - Asked: pre-spec found that a History line alone cannot make a second account of the owner count, since the kept Criterion still says an account other than the owner's, and that the Criterion asks for a pull request against `main`, which does not move before the close; the person chose (a), a pull request from the second account against `plugin`, CI on it, reviewed and merged into `plugin`, read before the close.
  - Taken: the Criterion is replaced whole with the branch `plugin` and the second account of the owner, the `purpose` is set anew, and the Estimate is set `pending`.

## History

- 2026-10-10 created · raw/2026-10-10/1913/ledger.md#case-766
