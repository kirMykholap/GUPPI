---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi]]"
purpose: uv run --project .guppi guppi test is green on the branch — the whole suite of the harness
method: "by hand, after each Work Mode: uv run --project .guppi guppi test, read against the Criterion, 0 failed"
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
- 2026-10-15 deferred · [[decision-case-829]]
- 2026-10-16 defer by decision-case-829 superseded · [[decision-case-861]]
- 2026-10-16 updated: the method a reading by hand of guppi test, a form that fits a MOC; the defer of case 829 retired · [[decision-case-861]]
