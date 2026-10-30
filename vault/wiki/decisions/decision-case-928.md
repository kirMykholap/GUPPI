---
type: decision
case: "928"
status: current
update: ["[[estimate-clean-branch-code-holds-pointers-only-in-brackets]]"]
origin: raw/2026-10-30/1713/ledger.md#case-928
sprint: plugin
created: 2026-10-30
tags: [ci, plugin]
---

## Problem

The reading of the clean code, as its `method` and its Criterion write it, exits 1 and writes nothing while any page with `core: true` stands `draft`.

## Recommend

- **How the reading of the clean code runs while a core page stands draft**
  - Recommended: (c) read by `guppi ship --check --review` in the `method` and in the `When`.
  - Answer: agreed, (c).
- **Whether the Estimate of the pages gets the same fix**
  - Recommended: (a) this Case changes only the Estimate of the code.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-30/1713/ledger.md#case-928
