---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the Stop check refuses a showing of a Case whose file under cases/ differs from the text the store holds for it
method: uv run pytest tests/test_casecheck.py -k changed_file
origin: raw/2026-10-05/0311/ledger.md#case-645.4
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
`Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, and `uv run guppi casecheck` reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

Then:
The hook reads the Cases of that file by `split_cases` of `guppi/materialize.py` and compares each with the entry of the store under its id alone, line ends and trailing spaces aside.
**＋** A Case of the file whose text differs from its entry, or that the store does not hold, exits 2 with a reason that names the Case and the file, joined with the other reasons of the hook.
**＋** The comparison is one function of `guppi/casecheck.py`, which the Spec hook `guppi/ratified.py` imports.
**－** A heading with no section, a fence tagged `DIFF` and a deferred decision in the short form are not compared, and no file is read for them.
**－** On the re-fire (`stop_hook_active`) it exits 0, as the other checks of the same run do.

## History

- 2026-10-05 created · [[decision-case-645.4]]
