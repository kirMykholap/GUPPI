---
type: decision
case: "652"
status: current
update: ["[[estimate-case-protocol-example-passes-the-check]]"]
origin: raw/2026-10-05/1343/ledger.md#case-652
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

`tests/test_case_schema.py` still skips when `vault/wiki/case-schema.md` holds no example, though the example now stands there and its reading passed. A lost example would go unchecked while the tests stay green. The question was what the test does when the page holds no example.

## Recommend

- **What the test does when the page holds no example**
  - Recommended: (a) fail, with a message that names the file.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#case-652
