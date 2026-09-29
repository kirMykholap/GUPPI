---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A supersedes of the session's window whose Case still stands in the plan is a finding of prespec --check; a line of the superseded Case needs no item
method: pytest tests/test_prespec.py on a temp plan; the live reading the first /pre-spec of a later session whose window holds a supersedes of a Case of that session — this session's /pre-spec runs on the old check
checked: 2026-09-29
origin: raw/2026-09-21/1853/ledger.md#case-299.2
sprint: migration
created: 2026-09-21
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi prespec --check <plan> --session <id>` reads a plan and the record lines of the session's window, and a decision line of the window carries `{supersedes:case N}`.

Then:
A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
**＋** A decision line of Case N, N superseded by a line of the window, is no finding "no Case N heading" and needs no item in the plan.
**＋** A superseded sub-case: the one heading `### Case N.M` leaves; the parent with its other sub-cases stays.
**－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.

## Result

2026-09-29, uv run pytest tests/test_prespec.py -k supersed: 8 passed; live, the /pre-spec of session 1432, whose window holds {supersedes:case 511.2} on the lines of Case 512: both runs print no finding on 511.2, the plan holds no ### Case 511.2 heading, its decision lines ask for no item, and Case 511 stands with 511.1; the finding of a superseded Case still in the plan was not met live

## History

- 2026-09-22 created · [[decision-case-299.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L25
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds lines out (case 484.2) · [[decision-case-484.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L29
