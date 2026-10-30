---
type: decision
case: "931"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-writes]]", "[[rule-case-protocol]]"]
supersedes: ["[[decision-case-897.3]]"]
origin: raw/2026-10-30/1713/ledger.md#case-931
sprint: plugin
created: 2026-10-30
tags: [harness, workflow, ledger, session]
---

## Problem

No form of a page `update` removes a section, so a Leaf rule cannot lose `## How it works` at its next touch without an edit by hand, and `rule-page-generation` carries the put-off of that form.

## Recommend

- **What does this Case do with the put-off?**
  - Recommended: (a) a new update key that names the sections to remove.
  - Answer: (a).
- **Which sections may the new key remove?**
  - Recommended: (a) any section except the ones the page's schema requires.
  - Answer: agreed, (a).
- **What happens when a named section is not on the page?**
  - Recommended: (a) the entry fails.
  - Answer: agreed, (a).
- **How is the new key checked?**
  - Recommended: (b) the Criterion of `estimate-generate-writes` replaced as a whole.
  - Answer: agreed, (b).
- **What is the key called?**
  - Recommended: (a) `drop`.
  - Answer: agreed, (a).
- **Where does the promise that the lift carries `drop` stand?**
  - Recommended: (b) a new Case beside Case 931 carries the lift.
  - Answer: agreed, (b).

## History

- 2026-10-30 created · raw/2026-10-30/1713/ledger.md#case-931
