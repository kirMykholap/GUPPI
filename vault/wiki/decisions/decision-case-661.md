---
type: decision
case: "661"
status: current
children: ["[[decision-case-661.1]]", "[[decision-case-661.2]]"]
origin: raw/2026-10-05/1616/ledger.md#case-661
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

`tests/test_orchestration.py` still skips when `vault/wiki/orchestration.md` holds no `showing` or `defer` example, though both examples now stand there and both readings passed. A lost example would go unchecked while the tests stay green. The question was what the tests do when the page holds no example.

## Recommend

- **What the test does when the page has no example**
  - Recommended: (a) fail with a message that names the file.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#case-661
