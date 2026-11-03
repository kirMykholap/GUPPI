---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case that has decision lines in the session and comes back from case-guppi in another shape under its old number goes back to case-guppi with a new number to build it under
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k shape
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

Then:
For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
**＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
**＋** The finding names each such number and a new id of the sprint of Case N: one above the highest number of that sprint that the Decision pages under `vault/wiki/decisions/` and `vault/archive/`, the decision lines of the session's ledger, the keys of `<plan>.checked.json` and the names of the files under `raw/<date>/<hi HHMM>/cases/` hold.
**＋** The judgment comes from one function of `.guppi/guppi/casecheck.py`, and the new id from `next_id` of `.guppi/guppi/caseid.py`, which the command for the next id runs too.
**＋** The finding tells `case-guppi` to build the Case under the new id. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
**＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new id.
**－** A file that holds sub-cases of Case N without Case N gets no finding of this check.
**－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

## Result

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
