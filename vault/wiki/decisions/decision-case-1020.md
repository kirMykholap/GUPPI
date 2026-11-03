---
type: decision
case: "1020"
status: current
create: ["[[estimate-clean-branch-leaves-out-the-source-pictures]]"]
update: ["[[rule-clean-branch]]"]
origin: raw/2026-11-03/1825/ledger.md#case-1020
sprint: plugin
created: 2026-11-03
tags: [ci, plugin, git]
---

## Problem

The two source pictures of the plugin icon sit in a folder at the root of the repository that no rule names, put there only until a place was chosen.

## Recommend

- **Where the two source pictures live for good**
  - Recommended: (b) they move to `plugin/assets/`, beside the manifest that names the icon made from them.
  - Answer: agreed, (b).
- **Which page says where the pictures live**
  - Recommended: (a) `rule-clean-branch`, a sentence in its Purpose and `plugin/assets/` in its `implementation_ref`.
  - Answer: agreed, (a).
- **How the new place is checked**
  - Recommended: (a) a new Estimate on `rule-clean-branch`, `estimate-clean-branch-leaves-out-the-source-pictures`, checked by a new test of `.guppi/tests/test_ship.py`.
  - Answer: agreed, (a).

## History

- 2026-11-03 created · raw/2026-11-03/1825/ledger.md#case-1020
