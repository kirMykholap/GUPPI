---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A bare `[[slug]]` in the plan file that names no page is a finding of pre-spec before the Spec is approved
method: pytest tests/test_prespec.py, the tests of check_bare_links
checked: 2026-09-29
origin: raw/2026-09-20/0958/ledger.md#case-264.2
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness, tests]
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

2026-09-29, uv run pytest tests/test_prespec.py -k bare: 4 passed

## History

- 2026-09-20 created · [[decision-case-264.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L26
- 2026-09-28 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.5) · [[decision-case-484.5]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L33
