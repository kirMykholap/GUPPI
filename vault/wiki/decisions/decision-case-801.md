---
type: decision
case: "801"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-reads-the-last-output-of-a-check]]"]
origin: raw/2026-10-13/1753/ledger.md#case-801
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Problem

The instruction of `case-guppi` and the Estimate that checks it disagree. The instruction lets `context` only name the last output of a check, while the Criterion asks that `context` quotes it with its source. The reading failed, and `make lint` flags the Estimate.

## Recommend

- **Which text changes: the instruction or the check?**
  - Recommended: (a) the instruction says that `context` quotes the output with its source; the Criterion stands.
  - Answer: agreed, (a).
- **How is the fix checked?**
  - Recommended: (a) set the same Estimate back to `pending`, and read it again at the Retro of this session against the new instruction text.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-13/1753/ledger.md#case-801
