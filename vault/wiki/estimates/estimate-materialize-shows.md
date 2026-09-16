---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
ref: rule-materialize
purpose: "--show prints the yaml and writes nothing under raw/"
method: pytest in tests/test_materialize.py, the tests of the --show path
---

## Criterion

When:
`uv run guppi materialize --show [--date YYYY-MM-DD]` runs.

Then:
Stdout holds the yaml each date would be written with — entries, `unparsed`,
`incomplete` marks, decision groups — one document per date, and no file under
`raw/` changes; exit 0, or 1 on an error of the walk as without `--show`.
**＋** Without `--show` the command writes as before.

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green, the three --show tests among them — the yaml of each unit on stdout, one document per unit with `---` between, nothing written under raw/, exit 1 on a unit error as without --show; a carried-over unit is passed by in --show too, with no separator for it

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L29
