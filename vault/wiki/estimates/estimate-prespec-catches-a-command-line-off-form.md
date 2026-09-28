---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: A tasks line that names render or sprint outside the first code span is a finding of prespec --check; the ticker's form passes
method: pytest tests/test_prespec.py on a temp plan; the live reading /pre-spec of this session on its own plan
origin: raw/2026-09-20/1749/ledger.md#case-279.2
sprint: migration
created: 2026-09-20
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi prespec --check <plan> --session <id>` reads the `tasks` block of every Case of a plan, as `/pre-spec` runs it on the plan of this Plan Mode.

Then:
A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run guppi render` or `uv run guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`.
**＋** The form the tickers of `render` and `sprint` match is `` - [ ] `uv run guppi render`: … `` and `` - [ ] `uv run guppi sprint` ``, the command in the first code span.
**－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (235).

## Result

2026-09-20, pytest tests/test_prespec.py 64 passed, four of them the form of a render or sprint line; live, guppi prespec --check on the plan of session 1749 exit 0 — its render lines in the ticker's form — and on raw/2026-09-20/1308/spec.md as a plan: nine findings "render line off form", one per unticked `- [ ] render `<file>`` line of 1308

## History

- 2026-09-20 created · [[decision-case-279.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L19
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.1) · [[decision-case-484.1]]
