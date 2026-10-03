---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case that has decision lines in the session and comes back from case-guppi in another shape under its old number goes back to case-guppi with a new number to build it under
method: uv run pytest tests/test_casecheck.py -k shape, then by hand the first answer of case-guppi the hook sends back for this reason
origin: raw/2026-10-03/0115/ledger.md#case-610.1
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

Then:
For an answer that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
**＋** Case N gets a finding when a number of its family that has such a line has no section in the answer, or when a number that has such a line has a sub-case in the answer.
**＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
**＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
**＋** The hook exits 2 with the finding on stderr, and `case-guppi` answers again.
**＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
**－** An answer that holds sub-cases of Case N without Case N gets no finding of this check.
**－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

## History

- 2026-10-03 created · [[decision-case-610.1]]
