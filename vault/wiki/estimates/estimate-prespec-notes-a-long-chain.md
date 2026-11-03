---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A chain of more than seven ＋ lines is named without blocking the Spec
method: pytest .guppi/tests/test_prespec.py on a temp plan
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`guppi prespec --check` reads a plan where the `given` or the `then` of a Case holds more than seven `**＋**` lines.

Then:
`guppi prespec --check` prints a line opening with `note:`, with the Case number and the section.
**－** A `note:` line is not a finding and does not change the exit code.
**＋** The agent answers a `note:` line in one line in the chat; the run is repeated while findings remain.

## Result

2026-09-23, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
