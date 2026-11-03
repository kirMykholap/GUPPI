---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook turns a tag line of a Case file into an entry of new_tags in the then block, leaves it out of the tasks block, and refuses a tag line off the form, and whether the check of the Case file reads the line alike
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py .guppi/tests/test_casecheck.py -k tag
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` of `.guppi/guppi/ratified.py` writes into the plan file a ratified Case whose `tasks` in `raw/<date>/<hi HHMM>/cases/case-<N>.md` hold a line `` - [ ] tag `<tag>` ``.
**＋** Or the `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks that file.

Then:
A task line that opens with `tag` and the tag in its first code span, with the sub-points `meaning` and `aliases`, each one code span, becomes one entry of the key `new_tags` in the block tagged `then`: its `tag`, `meaning` and `aliases`.
**＋** Each tag line of a Case becomes an entry of its own, in the order of the file.
**＋** The tag line is no task: the block tagged `tasks` does not hold it.
**＋** `.guppi/guppi/casecheck.py` reads the tag line by the same function of `.guppi/guppi/ratified.py`, and a refusal of the hook is a finding of the check.
**－** A tag line with `meaning` or `aliases` missing, with another sub-point, or with a value that is not one code span is refused: exit 2 with the reason on stderr, and nothing of the Case is written.
**－** A sub-point under a line that is neither a tag line nor an item of `create`, `update`, `delete` or `defer` is refused as before.

## Result

2026-10-07, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
