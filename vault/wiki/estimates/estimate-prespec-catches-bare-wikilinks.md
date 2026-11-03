---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A bare `[[slug]]` in the plan file that names no page is a finding of pre-spec before the Spec is approved
method: pytest .guppi/tests/test_prespec.py, the tests of check_bare_links
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness, tests]
core: true
---

## Criterion

When:
The person invokes `/pre-spec`, and `guppi prespec --check <plan> --session <id>` reads the plan file.

Then:
One line `case N: [[slug]] outside a code span names no page` is printed for every `[[slug]]` in the plan file outside a code span — in the blockquotes and in the strings of the `then` blocks — that has no live or archived page.
**＋** A slug a `create` of the same plan carries, and a hub file of `wiki/` by its stem or its path, are not a finding.
**＋** One line per slug and Case, however many times it stands.
**－** A `[[slug]]` inside backticks, and inside a fenced block tagged other than `then`, is not read.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
