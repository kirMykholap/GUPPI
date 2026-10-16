---
type: decision
case: "842"
status: current
update: ["[[estimate-clean-branch-installs-as-a-plugin]]"]
supersedes: ["[[decision-case-831]]"]
origin: raw/2026-10-16/0104/ledger.md#case-842
sprint: plugin
created: 2026-10-16
tags: [ci, plugin]
---

## Problem

The plugin install check is `failed` and put off. It was never read, because no tag `prod-x.y.z` stood. Its `method` does not say that it waits for that tag, and it does not say who installs the plugin.

## Recommend

- **How does the plugin-install check come back to a reading?**
  - Recommended: (a) set it `pending`, keep its promise word for word, and make the by-hand part of its `method` wait for a tag `prod-x.y.z` in the history of HEAD; the defer is taken up.
  - Answer: agreed, (a).
- **Who installs the plugin into an empty project?**
  - Recommended: (a) the person installs by `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace` in an empty project in Claude Code; the agent runs the test, the build, `claude plugin validate` and the reading of the files.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-842
