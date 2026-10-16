---
type: decision
case: "844"
status: current
update: ["[[estimate-clean-branch-ships-the-tests]]"]
origin: raw/2026-10-16/0104/ledger.md#case-844
sprint: plugin
created: 2026-10-16
tags: [plugin, tests]
---

## Problem

The part by hand of the reading of `estimate-clean-branch-ships-the-tests` needs a tag `prod-x.y.z` in the history of HEAD, and none stands. Its `method` waits only for an event that has already come, so the page looks ready to read when it is not, and a Retro would set it `failed` again for the same reason.

## Recommend

- **What does this Case change on the Estimate?**
  - Recommended: (a) the `method` waits until a tag `prod-x.y.z` stands in the history of HEAD; the Criterion stays and is written back unchanged; the page stays `pending`, and Retro reads it in this session after the tag is set.
  - Answer: agreed, (a).
- **Does this reading share its build folder with the plugin-install reading of item C4?**
  - Recommended: (a) each reading builds its own folder; this one builds into its own empty temporary folder, as its `method` says.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-844
