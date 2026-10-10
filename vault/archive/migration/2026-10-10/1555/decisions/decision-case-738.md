---
type: decision
case: "738"
status: archived
update: ["[[rule-prespec]]"]
origin: raw/2026-10-08/2134/ledger.md#case-738
sprint: migration
created: 2026-10-08
tags: [session, workflow, harness]
---

## Problem

The stricter check that Case 733 ratified is not in the code, so pre-spec still passes a MOC's Estimate whose `method` names a test file or `pytest` alone, and its Estimate stands `failed`.

## Recommend

- **How does this session carry the code that is already ratified?**
  - Recommended: (a) a Case that lands the code by the patch, `make style` and the full `make test`, with one `update` of `rule-prespec` that adds a History line, its `context` naming `estimate-prespec-catches-a-method-without-a-form` as the check, the Criterion unchanged, read at Retro.
  - Answer: agreed, (a).
- **What happens to the four unticked boxes in the earlier Spec?**
  - Recommended: (a) they stay unticked; this session's boxes and its handoff record that the code landed here.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/2134/ledger.md#case-738
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
