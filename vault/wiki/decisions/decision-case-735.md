---
type: decision
case: "735"
status: current
update: ["[[rule-case-example]]"]
origin: raw/2026-10-08/1547/ledger.md#case-735
sprint: migration
created: 2026-10-08
tags: [session, workflow, harness]
---

## Problem

The example Case that `case-guppi` copies gives a MOC's Estimate a `method` that names only a `pytest` command, which the stricter check of Case 733 reports, so that check cannot land while the example stands.

## Recommend

- **When is the patch applied?**
  - Recommended: (a) the example now, the patch in the next session, after the librarian's run renders the example; the pre-spec Estimate stays `failed` until then.
  - Answer: agreed, (a).
- **What method does the cart Estimate of the example name?**
  - Recommended: (a) a make target: `make test-cart`, which runs the `pytest` command; the cart stays a MOC.
  - Answer: agreed, (a).
- **Is the cart Estimate in the Spec-block example fixed too?**
  - Recommended: (a) the same entry as the Case: its `kind`, `purpose` and `method` as in the example Case.
  - Answer: agreed, (a).
- **Which Estimate checks the change to the example?**
  - Recommended: (a) the Criterion of `estimate-case-example-passes-the-check` stands.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/1547/ledger.md#case-735
