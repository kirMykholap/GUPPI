---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a Case whose tasks hold a stop line and a render line of a file that its when or then names, by one function of .guppi/guppi/prespec.py, and leaves alone a Case without one of them or whose when and then name no file of its render lines
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k stop_before_render
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py`, or the check of the file of `case-guppi` in `.guppi/guppi/casecheck.py`, reads a Case whose `tasks` block holds a line that opens with `stop:` after its box and a render line that `command_line` of `.guppi/guppi/render.py` matches.

Then:
For each file of its render lines that the `when` or `then` of that Case names in a code span, the check gives one finding `case N: stop before the render of <file> — the file changes only at the librarian's run, so a reading at a stop of Work Mode tests its old text`.
**＋** The judgment is one function of `.guppi/guppi/prespec.py` that `judge` calls, so `--check`, the `ExitPlanMode` hook of `rule-prespec-hook` and the check of the file of `case-guppi` give the same finding.
**＋** The file of a render line is a code span after the command that `command_line` matches.
**－** A Case with a `stop:` line and no render line, or whose `when` and `then` name no file of its render lines, gives no such finding.
**－** A render line and a `stop:` line under two different Case headings give no such finding.

## Result

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
