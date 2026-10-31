---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether guppi check prints no ref line for estimate-link-graph-prints-the-neighbours once the bare link of its Result stands in a code span, the rest of that page as it stood
method: "by hand, after the librarian's run that applies the update of estimate-link-graph-prints-the-neighbours: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md, the diff of the Result and of no field or Criterion, read against the Criterion, both outputs in the estimate line"
origin: raw/2026-10-31/2307/ledger.md#case-973
sprint: plugin
created: 2026-10-31
tags: [sprint, harness]
once: true
---

## Criterion

When:
`uv run --project .guppi guppi check` runs the lint of `.guppi/guppi/lint.py` over the live pages of `vault/wiki/`, after the librarian's run that applies the `update` of `estimate-link-graph-prints-the-neighbours`.
**＋** The last change of the file of `estimate-link-graph-prints-the-neighbours` is read by `git log -p -1` on its path.

Then:
It prints no `ref` line for `estimate-link-graph-prints-the-neighbours`.
**＋** The `## Result` of `estimate-link-graph-prints-the-neighbours` holds `[[slug]]` inside a code span, and the date, the commands, the counts and the outputs of the readings it records as they stood.
**－** The status, the `## Criterion` and the `method` of `estimate-link-graph-prints-the-neighbours` do not change.

## History

- 2026-11-01 created · [[decision-case-973]]
