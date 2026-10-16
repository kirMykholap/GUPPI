---
type: decision
case: "861"
status: current
update: ["[[estimate-guppi-tests-green]]"]
supersedes: ["[[decision-case-829]]"]
origin: raw/2026-10-16/1712/ledger.md#case-861
sprint: plugin
created: 2026-10-16
tags: [harness, tests]
---

## Problem

`estimate-guppi-tests-green` passed, but its `method` names `guppi test` alone, a form that lint refuses on the Estimate of a MOC, and the defer of case 829 that waits for a fitting `method` keeps it in `backlog.md`.

## Recommend

- **What should the `method` of `estimate-guppi-tests-green` say?**
  - Recommended: (a) a reading by hand of `guppi test` after each Work Mode, read against the Criterion, 0 failed.
  - Answer: agreed, (a). Before the answer, the person asked why a MOC may not name `guppi test`; the reply was that the rule wants a MOC's Estimate to run the tests of its own part, which on the top MOC is the whole suite, and that a rule change would be a Case of its own.
- **How is the fix checked?**
  - Recommended: (a) the existing check covers it: `estimate-lint-checks-the-method`, whose Criterion stands.
  - Answer: agreed, (a).
- **Does the other check put off by the same defer join this Case?**
  - Recommended: (a) leave `estimate-page-schemas-one-file-per-rule` out; it stays in the backlog.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/1712/ledger.md#case-861
