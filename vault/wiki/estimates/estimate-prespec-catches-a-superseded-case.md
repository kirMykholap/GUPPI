---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A supersedes of the session's window whose Case still stands in the plan is a finding of prespec --check; a line of the superseded Case needs no item
method: "pytest .guppi/tests/test_prespec.py on a temp plan; by hand, after a /pre-spec whose window holds a supersedes of a Case of its session: its findings read against the Criterion"
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads a plan and the record lines of the session's window, and a decision line of the window carries `{supersedes:case N}`.

Then:
A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
**＋** A heading of a sub-case of Case N, at any depth, that still stands in the plan is the same finding under the number of that sub-case.
**＋** A decision line of Case N or of a sub-case of Case N, N superseded by a line of the window, is no finding "no Case N heading", needs no item in the plan and asks for no `tasks` block.
**＋** A `{supersedes:case N.M}` covers Case N.M and its own sub-cases; the parent with its other sub-cases stays.
**＋** Whether a tag covers a Case is judged by `in_family` of `.guppi/guppi/materialize.py`, the function that the Spec hook and `guppi materialize` read the tag by.
**－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
