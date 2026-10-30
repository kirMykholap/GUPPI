---
type: decision
case: "939"
status: current
update: ["[[estimate-clean-branch-pages-hold-pointers-only-in-brackets]]", "[[rule-clean-branch]]"]
origin: raw/2026-10-30/2005/ledger.md#case-939
sprint: plugin
created: 2026-10-30
tags: [ci, plugin, git]
---

## Problem

The reading of the pages that ship, as its `method` and its Criterion write it, exits 1 and writes nothing while any page with `core: true` stands `draft`.

## Recommend

- **How the reading of the pages runs while a core page stands draft**
  - Recommended: (a) add `--allow-draft` and replace the Criterion whole.
  - Answer: agreed, (a).
- **When the new reading is taken**
  - Recommended: (a) at Retro of this session.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec`, which the person agreed to: the sentence of `rule-clean-branch` that gives `--allow-draft` the install by hand as its one use should name both uses, the install by hand and the reading of the pages by `--review`.
  - Taken: an `update` of `rule-clean-branch` replaces that sentence, and `estimate-clean-branch-refuses-a-draft-core-page` is named as the check of the flag.

## History

- 2026-10-30 created · raw/2026-10-30/2005/ledger.md#case-939
