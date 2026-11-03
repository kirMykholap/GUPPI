---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop check refuses a showing of a Case whose file under cases/ differs from the text the store holds for it
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k changed_file
checked: 2026-10-06
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, and `uv run --project .guppi guppi casecheck` reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

Then:
The hook reads the Cases of that file by `split_cases` of `.guppi/guppi/materialize.py` and compares each with the entry of the store under its id alone, line ends and trailing spaces aside.
**＋** A Case of the file whose text differs from its entry, or that the store does not hold, exits 2 with a reason that names the Case and the file, joined with the other reasons of the hook.
**＋** The comparison is one function of `.guppi/guppi/casecheck.py`, which the Spec hook `.guppi/guppi/ratified.py` imports.
**－** A heading with no section, a fence tagged `DIFF` and a deferred decision in the short form are not compared, and no file is read for them.
**－** With `stop_hook_active` set the file is compared the same, as by the other checks of the same run, and its reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.

## Result

2026-10-06, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
