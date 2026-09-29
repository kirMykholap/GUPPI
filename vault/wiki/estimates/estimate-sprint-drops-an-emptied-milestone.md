---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: A milestone the move left with no line leaves the Milestones, so the next one becomes current
method: pytest tests/test_generate.py, the tests of the move
checked: 2026-09-29
origin: raw/2026-09-23/0034/ledger.md#case-354.2
sprint: migration
created: 2026-09-23
tags: [sprint, harness]
---

## Criterion

When:
`guppi generate` moves, after the cascade, the last item line out of a milestone of the sprint page into its `## Backlog`.

Then:
The heading `### <name>` of that milestone leaves `## Milestones`. The next milestone with an item not done, or with no item, becomes the current one.
**＋** The History of the sprint page gets the line `milestone <name> left the Milestones: its items moved to the Backlog · generate`, and stdout gets one line.
**－** A milestone with no item before the run stays.
**－** A milestone where a note is left stays. A note is a line that names no `[[slug]]` before its first ` — `, and it is never moved.
**－** Nothing is written to `## Closed`: nothing of that milestone was built.

## Result

2026-09-29, uv run pytest tests/test_generate.py -k "milestone or move": 7 passed

## History

- 2026-09-23 created · [[decision-case-354.2]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L36
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the current milestone and the note stated (case 491.3) · [[decision-case-491.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L35
