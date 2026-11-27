---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook turns a tag line of a Case file into an entry of new_tags in the then block, leaves it out of the tasks block, and refuses a tag line off the form, and whether the check of the Case file reads the line alike
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py .guppi/tests/test_casecheck.py -k tag
checked: 2026-11-28
origin: raw/2026-10-07/0425/ledger.md#case-702
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` of `.guppi/guppi/ratified.py` writes into the Cases file `<plan stem>.cases.md` beside the plan file a ratified Case whose `tasks` in `raw/<date>/<hi HHMM>/cases/case-<N>.md` hold a line `` - [ ] tag `<tag>` ``.
**＋** Or the `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks that file.

Then:
A task line that opens with `tag` and the tag in its first code span, with the sub-points `meaning` and `aliases`, each one code span, becomes one entry of the key `new_tags` in the block tagged `then`: its `tag`, `meaning` and `aliases`.
**＋** Each tag line of a Case becomes an entry of its own, in the order of the file.
**＋** The tag line is no task: the block tagged `tasks` does not hold it.
**＋** `.guppi/guppi/casecheck.py` reads the tag line by the same function of `.guppi/guppi/ratified.py`, and a refusal of the hook is a finding of the check.
**－** A tag line with `meaning` or `aliases` missing, with another sub-point, or with a value that is not one code span is refused: exit 2 with the reason on stderr, and nothing of the Case is written.
**－** A sub-point under a line that is neither a tag line nor an item of `create`, `update`, `delete` or `defer` is refused as before.

## Result

2026-11-28, Retro of session 2214, uv run --project .guppi pytest .guppi/tests/test_ratified.py .guppi/tests/test_casecheck.py -k tag: 27 passed; against Case 1087.7: two tag lines become two entries of new_tags in the then block of the Case written into the Cases file, and its tasks block holds no tag line

## History

- 2026-10-07 created · [[decision-case-702]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0425/ledger.md#L22
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-28 updated: the Criterion replaced whole — the Case with a tag line is written into the Cases file of the plan · [[decision-case-1087.7]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L36
