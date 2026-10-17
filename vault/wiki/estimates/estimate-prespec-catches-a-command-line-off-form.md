---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A tasks line that names render or sprint outside the first code span is a finding of prespec --check; the ticker's form passes
method: "pytest .guppi/tests/test_prespec.py on a temp plan; by hand, after a /pre-spec: its findings on its own plan read against the Criterion"
checked: 2026-10-17
origin: raw/2026-09-20/1749/ledger.md#case-279.2
sprint: migration
created: 2026-09-20
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the `tasks` block of every Case of a plan, as `/pre-spec` runs it on the plan of this Plan Mode.

Then:
A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run --project .guppi guppi render` or `uv run --project .guppi guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`.
**＋** The form the tickers of `render` and `sprint` match is `` - [ ] `uv run --project .guppi guppi render`: … `` and `` - [ ] `uv run --project .guppi guppi sprint` ``, the command in the first code span.
**－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (as set in case 235).

## Result

2026-10-17, Retro of session 1805: uv run --project .guppi pytest .guppi/tests/test_prespec.py 267 passed; by hand, the /pre-spec of this session: the plan of Cases 879 and 880 holds no render or sprint task line, and guppi prespec --check printed no render line finding

## History

- 2026-09-20 created · [[decision-case-279.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L19
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.1) · [[decision-case-484.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L73
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the method waits for a /pre-spec, with no past moment · [[decision-case-875]]
- 2026-10-17 updated: the Criterion replaced whole — the bare case number written in a bracket with the word case · [[decision-case-880.13]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L70
