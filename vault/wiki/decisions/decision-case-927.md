---
type: decision
case: "927"
status: current
update: ["[[estimate-harness-make-runs-in-both-shells]]", "[[rule-lint]]"]
supersedes: ["[[decision-case-838]]"]
origin: raw/2026-10-30/1713/ledger.md#case-927
sprint: plugin
created: 2026-10-30
tags: [harness, workflow]
---

## Problem

`guppi check` stays red on one line because the method of `estimate-harness-make-runs-in-both-shells` says "make with", and the check reads `with` as a target of the `Makefile`.

## Recommend

- **Fix the page or the check**
  - Recommended: (a) reword this one method so that it names the targets as `make help`, `make style`, `make test` and `make lint`.
  - Answer: agreed, (a).
- **The put-off decision on rule-lint**
  - Recommended: (a) take it up and close it in this Case, by an update of `rule-lint` with a History line only.
  - Answer: agreed, (a).

## History

- 2026-10-30 created · raw/2026-10-30/1713/ledger.md#case-927
