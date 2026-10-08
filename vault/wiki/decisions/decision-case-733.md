---
type: decision
case: "733"
status: current
update: ["[[estimate-prespec-catches-a-method-without-a-form]]"]
origin: raw/2026-10-08/0213/ledger.md#case-733
sprint: migration
created: 2026-10-08
tags: [harness, workflow]
---

## Problem

Pre-spec and the check of the Case file pass a MOC's Estimate whose `method` names a test file or `pytest` alone, which `make lint` reports only at the librarian's run.

## Recommend

- **How much of the MOC test does pre-spec take over?**
  - Recommended: (a) the form only: on a MOC, a `method` that names neither a `make` target nor `by hand` is a finding; the Makefile and the children stay with lint; one shared function in `guppi/lint.py`.
  - Answer: agreed, (a).
- **Which pages count as a MOC when pre-spec judges?**
  - Recommended: (a) as the plan leaves the page: the live page, a `create` or an `update` of the plan that writes `kind: MOC`.
  - Answer: agreed, (a).
- **How is the promise recorded?**
  - Recommended: (a) replace the Criterion of `estimate-prespec-catches-a-method-without-a-form`, its `purpose` and `method` set anew.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0213/ledger.md#case-733
