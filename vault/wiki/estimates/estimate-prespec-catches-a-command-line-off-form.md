---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A tasks line that names render or sprint outside the first code span is a finding of prespec --check; the ticker's form passes
method: pytest tests/test_prespec.py on a temp plan; the live reading /pre-spec of this session on its own plan
origin: raw/2026-09-20/1749/ledger.md#case-279.2
sprint: migration
created: 2026-09-20
tags: [harness, workflow]
---

## Criterion

Given:
`guppi prespec --check <plan>` reads the `tasks` block of every Case of the plan and prints one finding per line, exit 1 on any (cases 59.3, 264.2).
**＋** The tickers of `render` and `sprint` match a line that opens with a code span holding the command (case 235).
**＋** `tests/test_prespec.py` fixes the behaviour on a temp plan.

When:
`/pre-spec` — `guppi prespec --check` on the plan of this Plan Mode.

Then:
A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run guppi render` or `uv run guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`; the form the ticker knows is `- [ ] `uv run guppi render`: …` and `- [ ] `uv run guppi sprint``.
**－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (235).
**－** Nothing else in pre-spec changes.

## Result

2026-09-20, pytest tests/test_prespec.py 64 passed, four of them the form of a render or sprint line; live, guppi prespec --check on the plan of session 1749 exit 0 — its render lines in the ticker's form — and on raw/2026-09-20/1308/spec.md as a plan: nine findings "render line off form", one per unticked `- [ ] render `<file>`` line of 1308

## History

- 2026-09-20 created · [[decision-case-279.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L19
