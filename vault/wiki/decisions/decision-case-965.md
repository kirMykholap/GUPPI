---
type: decision
case: "965"
status: current
create: ["[[rule-librarian-report-copy]]", "[[estimate-librarian-report-copy-writes-the-file]]"]
update: ["[[rule-librarian-report-copy]]", "[[rule-hook-registry]]"]
supersedes: ["[[decision-case-956.1]]"]
origin: raw/2026-10-31/0431/ledger.md#case-965
sprint: plugin
created: 2026-10-31
tags: [hooks, harness, librarian, render]
---

## Problem

The `then` block of 956.1 creates `rule-librarian-report-copy` with `core` as the string `true`, so the page would be born without `core: true`.

## Recommend

- Recommended: the Rule, the Estimate and the registration of 956.1 as they stood, with `core: true` set by an `update` of the new Rule right after its `create`, so that the `then` block holds a boolean.
- Answer: ratified as built

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-965
