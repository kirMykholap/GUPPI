---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of an answer of case-guppi leaves out of the other Cases of the session a Case that a supersedes mark on a decision line of the answer's own file names, so that a Case built again under a new number passes while the build it replaces stands in the plan
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k superseded_by_the_file
origin: raw/2026-10-07/2114/ledger.md#case-725.2
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case whose file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds a decision line that carries `{supersedes:case M}`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`, while the plan file or the store holds Case M.
**＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, plan file, store and ledger.

Then:
The hook leaves Case M and its sub-cases out of the other Cases of the session, by `other_blocks` of `.guppi/guppi/casecheck.py`, as it leaves out a Case that a mark of the session's ledger names; a mark on a sub-case leaves out that sub-case alone.
**＋** Case M is not judged with the Cases of the answer by `check_same_target` of `.guppi/guppi/prespec.py`, and its pairs are not applied before theirs by `check_pairs`, so a Case built again under a new number gets no clash and no pair finding from the build it replaces while that build stands in the plan file or the store.
**＋** The marks are read from the decision lines of the `ratification` fences of the answer by `ratification_records` of `.guppi/guppi/casecheck.py`, the one reading of those lines in the hook.
**＋** A clash or a pair finding with any other Case of the session stays a finding.
**－** The mark removes nothing from the plan file or the store: the `Stop` hook of `rule-spec-write` removes Case M only when the Case that carries the mark is ratified.
**－** The findings on a Case ratified in the session and built again under its old number, in another shape or without a target, still read the decision lines of the session's ledger.

## Result

2026-10-07, Retro of session 2114: uv run pytest tests/test_casecheck.py -k superseded_by_the_file 4 passed — a Case of the plan that a {supersedes} mark of the answer's file names gives no clash and no pair finding, a mark on a sub-case leaves its parent compared, the same answer without the mark gives the clash; on the code of HEAD before the change the first two failed

## History

- 2026-10-07 created · [[decision-case-725.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/2114/ledger.md#L24
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
