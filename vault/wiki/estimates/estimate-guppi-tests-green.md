---
type: estimate
kind: QA
status: pending
target: "[[entity-guppi]]"
purpose: make test is green on the branch — the whole suite of the harness
method: make test, 0 failed; read after each Work Mode
origin: raw/2026-09-22/0014/ledger.md#case-306.2
sprint: migration
created: 2026-09-22
tags: [harness, tests]
---

## Criterion

When:
`make test` runs `uv run pytest -q` over `tests/` on the working branch, after a Work Mode.

Then:
pytest reports no failed test and no error, and `make test` exits 0.
**－** A skipped test is not a failure.

## Result

2026-09-22, make test after Work Mode: 529 passed, 2 skipped (the conditional cases of insights and decisions in tests/test_schemas.py), 0 failed

## History

- 2026-09-22 created · [[decision-case-306.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L64
- 2026-09-29 updated: the Criterion replaced whole — the one-time build of entity-guppi out, the purpose kept as When and Then (case 488.5) · [[decision-case-488.5]]
