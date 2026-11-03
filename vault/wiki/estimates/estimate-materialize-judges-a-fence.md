---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: "Every reader of a fence judges it by the functions of .guppi/guppi/materialize.py, as CommonMark does: a fence closes only on a run of its own character at least as long"
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py -k fence
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, tests]
core: true
---

## Criterion

When:
A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `.guppi/guppi/materialize.py`, `fenced_value` of `.guppi/guppi/ratified.py`, `plan_prose` and `check_pairs` of `.guppi/guppi/prespec.py`, the check of `ratification` in `.guppi/guppi/casecheck.py`, `ledger_lines` of `.guppi/guppi/ledger.py`, or the class `fence` of `.guppi/guppi/lint.py`.

Then:
A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
**＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
**＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
**＋** `fence_breaks` is built on `fence_opening` and `closes_fence`, so each break it reports is a line these readers keep as content, or an end of section they reach inside a fence.
**＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
**＋** Every one of these readers takes the judgment from the functions of `.guppi/guppi/materialize.py`, and they all give the same answer for the same text.
**－** No reader keeps a fence pattern or a test on three backticks of its own.

## Result

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
