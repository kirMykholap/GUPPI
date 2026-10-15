---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A chain of more than seven ＋ lines is named without blocking the Spec
method: pytest .guppi/tests/test_prespec.py on a temp plan
origin: raw/2026-09-23/1355/ledger.md#case-378.8
sprint: migration
created: 2026-09-23
tags: [harness, workflow]
---

## Criterion

When:
`guppi prespec --check` reads a plan where the `given` or the `then` of a Case holds more than seven `**＋**` lines.

Then:
`guppi prespec --check` prints a line opening with `note:`, with the Case number and the section.
**－** A `note:` line is not a finding and does not change the exit code.
**＋** The agent answers a `note:` line in one line in the chat; the run is repeated while findings remain.

## Result

2026-09-23, uv run pytest tests/test_prespec.py -k "and_lines": 2 passed — eight ＋ lines in then give one note: line and exit 0; seven give nothing

## History

- 2026-09-23 created · [[decision-case-378.8]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L43
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
