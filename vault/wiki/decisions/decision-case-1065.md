---
type: decision
case: "1065"
status: current
update: ["[[estimate-case-build-settles-form-by-itself]]"]
origin: raw/2026-11-26/1336/ledger.md#case-1065
sprint: plugin
created: 2026-11-26
tags: [session, workflow, harness]
---

## Problem

The Criterion of `estimate-case-build-settles-form-by-itself` says that a change is always built under the number of its Case. `case-schema.md` sets a new number for a ratified Case that comes back in another shape. So a correct build reads as `failed`.

## Recommend

- Recommended: drop the line on the number from the Criterion of `estimate-case-build-settles-form-by-itself`, because `estimate-case-build-writes-the-case` already checks that rule with its exception; set its `purpose` and `method` anew.
- Answer: ratified as built

## History

- 2026-11-26 created · raw/2026-11-26/1336/ledger.md#case-1065
