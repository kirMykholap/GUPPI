---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: "--show prints the yaml and writes nothing under raw/"
method: pytest in .guppi/tests/test_materialize.py, the tests of the --show path
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger, tests]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize --show [--date YYYY-MM-DD]` runs.

Then:
Stdout holds the yaml each date would be written with — entries, `unparsed`,
`incomplete` marks, decision groups — one document per date, and no file under
`raw/` changes; exit 0, or 1 on an error of the walk as without `--show`.
**＋** Without `--show` the command writes as before.

## Result

2026-09-16, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
