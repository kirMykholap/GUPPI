---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether pre-spec reports a code fence that a replace or reword pair breaks, or that a sections value leaves broken, and stays silent on a break the page already held
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py .guppi/tests/test_prespec.py -k fence
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` applies the `replace` and `reword` pairs of the plan to copies of the pages in memory, and reads the `sections` values of the `create` and `update` items of its `then` blocks.

Then:
`fence_breaks` of `.guppi/guppi/materialize.py` takes the text of one section and gives each break in it: a line inside an open code fence that starts with a run of the fence's character at least as long as the fence and has text after the run, and a fence still open at the end of the section.
**＋** For each section a `replace` or `reword` pair changes, each break the section holds after the pair and did not hold before it gives one line: the Case, the page's slug, the section, and "a pair leaves a code fence with text after it" with the line, or "a pair leaves a code fence open at the end of the section".
**＋** Each break in the text of a `sections` value gives one line of the same form, with "a sections value leaves" in place of "a pair leaves".
**＋** Each such line is a finding: the check exits 1.
**－** A break that the section held before the pair gives no line.
**－** A run shorter than the fence it stands in, or a run of the other character, is content of the fence and no break.
**－** No page is written, and a `sections` value is judged on its own and not applied to the copies, so the anchors are judged as before.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
