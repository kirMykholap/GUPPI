---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case that has decision lines in the session and comes back from case-guppi in another shape under its old number goes back to case-guppi with a new number to build it under
method: uv run pytest tests/test_casecheck.py -k shape
checked: 2026-10-05
origin: raw/2026-10-03/0115/ledger.md#case-610.1
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

Then:
For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
**＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
**＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
**＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
**＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new number.
**＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
**－** An answer on the old path that holds sub-cases of Case N without Case N gets no finding of this check.
**－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

## Result

2026-10-05, at the /hi of session 0109: uv run pytest -q tests/test_casecheck.py -k shape 8 passed, 122 deselected

## History

- 2026-10-03 created · [[decision-case-610.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-05 updated: the method is pytest alone; the live send-back is no longer waited for (case 637.1) · [[decision-case-637.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L6
- 2026-10-05 updated: the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.15) · [[decision-case-645.15]]
