---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A replace pair inside an Estimate's Criterion is refused before the Spec is approved, so a promise changes only whole
method: pytest .guppi/tests/test_prespec.py and .guppi/tests/test_materialize.py on a temp plan and vault
origin: raw/2026-09-23/1355/ledger.md#case-378.4
sprint: migration
created: 2026-09-23
tags: [harness, workflow]
---

## Criterion

When:
`guppi prespec --check` reads a plan where an `update` of an Estimate carries a `replace` pair whose `old` stands inside the `## Criterion` of that page.

Then:
`guppi prespec --check` prints a finding with the Case, the slug and the opening of the `old`, and exits 1.
**＋** `guppi materialize` marks such an entry `incomplete: [criterion]` and sets no `pending`.
**－** A pair outside `## Criterion` still changes its part alone, with no `pending`.

## Result

2026-09-23, uv run pytest tests/test_prespec.py tests/test_materialize.py -k "replace_pair or pair_inside or pair_outside": 4 passed — a pair inside the Criterion is a prespec finding and exit 1, incomplete: [criterion] with no status in materialize; a pair outside is clean

## History

- 2026-09-23 created · [[decision-case-378.4]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L41
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
