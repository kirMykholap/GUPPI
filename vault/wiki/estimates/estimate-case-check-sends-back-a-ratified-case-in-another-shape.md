---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case that has decision lines in the session and comes back from case-guppi in another shape under its old number goes back to case-guppi with a new number to build it under
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k shape
checked: 2026-10-13
origin: raw/2026-10-03/0115/ledger.md#case-610.1
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
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
**－** An answer on the old path that holds sub-cases of Case N without Case N gets no finding of this check.
**－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

## Result

2026-10-13, uv run pytest tests/test_casecheck.py -k shape: 13 passed — the new id stands above an id held only by the store, only by a Case file and only by a Decision page, and new_number and guppi caseid --next give the same id

## History

- 2026-10-03 created · [[decision-case-610.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-05 updated: the method is pytest alone; the live send-back is no longer waited for (case 637.1) · [[decision-case-637.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L6
- 2026-10-05 updated: the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.15) · [[decision-case-645.15]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L7
- 2026-10-13 updated: the Criterion replaced whole — the new id is counted by next_id of guppi/caseid.py over the Decision pages, the ledger, the store and the Case files of the session (case 788.4) · [[decision-case-788.4]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L50
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
