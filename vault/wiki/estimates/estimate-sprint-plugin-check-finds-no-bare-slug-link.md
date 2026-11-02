---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether guppi check prints no ref line for estimate-link-graph-prints-the-neighbours once the bare link of its Result stands in a code span, the rest of that page as it stood
method: "by hand, after the librarian's run that applies the update of estimate-link-graph-prints-the-neighbours: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md, the diff of the Result and of no field or Criterion, read against the Criterion, both outputs in the estimate line"
checked: 2026-11-02
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

## Result

2026-11-02, Retro of session 0039: uv run --project .guppi guppi check in Work Mode after the code tasks printed 9 lines, exit 1, none of them a ref line for estimate-link-graph-prints-the-neighbours; git log -p -1 -- vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md, commit 5d534880 (librarian, 2026-10-31), changes the ## Result alone — `[[slug]]` and the output of guppi links decision-case-966 put in code spans, "Retro of session 1831" written "Retro (session 1831)", the date, the commands, the counts and the outputs as they stood — and adds one History line of decision-case-973; status, Criterion and method unchanged

## History

- 2026-11-01 created · [[decision-case-973]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/0039/ledger.md#L14
