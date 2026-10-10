---
type: decision
case: "714"
status: archived
create: ["[[estimate-prespec-hook-reports-a-schema-condition-not-met]]"]
origin: raw/2026-10-07/1804/ledger.md#case-714
sprint: migration
created: 2026-10-07
tags: [harness, workflow, schema]
---

## Problem

A Case can break a condition of a schema, such as an `actioned` Insight with no `addressed_by`, and no check before ratification sends it back; `make lint` reports it only after the librarian's run.

## Recommend

- **What should a check before ratification cover?**
  - Recommended: (b) every such condition of every schema, on the page as the Case leaves it, through the code of `make lint`.
  - Answer: agreed, (b).
- **Where should the check run?**
  - Recommended: (a) inside the shared function of `guppi/prespec.py`, so `/pre-spec`, the check of the Case file and the check after ratification all run it.
  - Answer: agreed, (a).
- **Which Case does the check send back?**
  - Recommended: (a) only the Case that causes the break: a `create` that breaks a condition, or a `set` of the value that starts one with no required field or section on the page or in the Case.
  - Answer: agreed, (a).
- **Do the fields set by another Case of the same session count?**
  - Recommended: (a) only the page and the Cases checked together.
  - Answer: agreed, (a).
- **What happens when the same session changes the schema itself?**
  - Recommended: (a) skip that page type, as the key check does.
  - Answer: agreed, (a).
- **How is the check proven to work?**
  - Recommended: (a) a new Estimate on `rule-prespec-hook`, checked by tests.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-714
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
