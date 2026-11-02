---
type: decision
case: "998"
status: current
update: ["[[estimate-case-build-reads-the-readers-of-a-changed-step]]"]
origin: raw/2026-11-02/0039/ledger.md#case-998
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness, case-build]
---

## Problem

The Estimate has failed four times on readers that `/pre-spec` caught before the Spec was approved. Each failure added one more sentence to `rule-case-build`. The check does not measure whether a missed reader actually gets through: it fails on any miss by `case-guppi` alone, however the next check handles it.

## Recommend

- **Where and when a miss is looked for**
  - Recommended: (a) at the Retro of the same session.
  - Answer: (b) at Retro, and again after the next session.
- **What the Criterion promises**
  - Recommended: (a) replace the Criterion whole with the outcome.
  - Answer: (a).
- **Which Estimates change**
  - Recommended: (a) this Estimate only.
  - Answer: (a), after the main agent explained the question in plain words.
- **One reading or two**
  - Recommended: (a) one reading, after the next session, covering both sessions.
  - Answer: (a).

## History

- 2026-11-02 created · raw/2026-11-02/0039/ledger.md#case-998
