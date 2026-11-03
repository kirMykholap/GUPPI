---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: Whether generate leaves every line of the sprint page in place, a milestone item put off in many sessions in a row included, so that a line moves only by a Case
method: "uv run --project .guppi pytest .guppi/tests/test_generate.py -k moves_no_line; then by hand, the History of entity-sprint-<id> after the librarian's run of a later session: no line of generate on a move"
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi generate` runs over the vault with one live page `entity-sprint-<id>`, and the `frontier.md` of three or more sessions in a row, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names an item of its `## Milestones` in a code span.

Then:
After the run, `## Milestones` and `## Backlog` of `entity-sprint-<id>` stand as before it, each line in its place, unless an entry of the run changes the page.
**＋** A milestone whose items were all put off keeps its heading under `## Milestones`.
**＋** `.guppi/guppi/generate.py` writes no line about a move into the History of `entity-sprint-<id>`, and it prints no such line on stdout.
**＋** A line of `entity-sprint-<id>` moves only through an entry of a Case the person ratified, an `update` that `generate` applies like any other.
**－** `rule-sprint` and `rule-page-generation` name no move of a sprint line by `generate`.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
