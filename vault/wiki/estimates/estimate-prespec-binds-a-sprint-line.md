---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Frontier line of the sprint closed by a Case is a finding of prespec --check unless that Case updates the sprint page; a line left [-] with sprint · defer needs nothing
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint · defer` line, a line whose source segment is not `sprint` while the word stands inside the slug of its title
checked: 2026-09-27
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, sprint]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` reads a line of the session's Frontier whose source segment, the one before the closer, is `sprint`.

Then:
A line closed `[x] … · sprint · case N` needs an `update` item of `entity-sprint-<id>` under Case N, in the parent or in any sub-case. Without one, it is the finding `frontier: C<n> closes a sprint item with case N, no update of the sprint page under Case N`.
**＋** A line closed `[-] … · sprint · defer` needs nothing and is no finding. The item stays in its milestone until `generate` moves it to the `## Backlog` of `entity-sprint-<id>` after three such sessions in a row.
**－** A line whose source segment is not `sprint` is read by the other checks of the Frontier. The word inside the slug of a title is not the source.

## Result

2026-09-27, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
