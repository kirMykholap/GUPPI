---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A tasks line that names render or sprint outside the first code span is a finding of prespec --check; the ticker's form passes
method: pytest .guppi/tests/test_prespec.py on a temp plan; the live reading /pre-spec of this session on its own plan
checked: 2026-09-29
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
**－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (235).

## Result

2026-09-29, uv run pytest tests/test_prespec.py -k "off_form or render_line or command": 4 passed; live, /pre-spec of session 1134 on its plan: every render and sprint line opens with the command in a code span, no off-form finding

## History

- 2026-09-20 created · [[decision-case-279.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L19
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.1) · [[decision-case-484.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L73
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
