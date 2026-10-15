---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi]]"
purpose: uv run --project .guppi guppi test is green on the branch — the whole suite of the harness
method: uv run --project .guppi guppi test, 0 failed; read after each Work Mode
checked: 2026-09-29
origin: raw/2026-09-22/0014/ledger.md#case-306.2
sprint: migration
created: 2026-09-22
tags: [harness, tests]
---

## Criterion

When:
`uv run --project .guppi guppi test` runs `uv run --project .guppi pytest -q` over `.guppi/tests/` on the working branch, after a Work Mode.

Then:
pytest reports no failed test and no error, and `uv run --project .guppi guppi test` exits 0.
**－** A skipped test is not a failure.

## Result

2026-09-29, session 1134, make test on migration at 8d5798c+ff62585: 900 passed, 2 skipped, 0 failed, exit 0

## History

- 2026-09-22 created · [[decision-case-306.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L64
- 2026-09-29 updated: the Criterion replaced whole — the one-time build of entity-guppi out, the purpose kept as When and Then (case 488.5) · [[decision-case-488.5]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L23
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
