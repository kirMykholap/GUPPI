---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint]]"
purpose: A milestone the move left with no line leaves the Milestones, so the next one becomes current
method: pytest tests/test_generate.py, the tests of the move
origin: raw/2026-09-23/0034/ledger.md#case-354.2
sprint: migration
created: 2026-09-23
tags: [sprint, harness]
---

## Criterion

Given:
The current milestone is the first `### ` under `## Milestones` with an item not done, or with no item (case 229.3); `/hi` takes the Frontier from the current milestone only.
**＋** By 354.1, `generate` moves the line of an item from its milestone to `## Backlog`.
**＋** A note — a line with no `[[slug]]` before the ` — ` — is not moved and keeps its milestone open (case 313).
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault.

When:
`guppi generate` moves, by 354.1, the last item line out of a milestone.

Then:
The heading `### <name>` of that milestone leaves `## Milestones`; the next milestone becomes the current one.
**＋** The History of the sprint page gets the line `milestone <name> left the Milestones: its items moved to the Backlog · generate`, and stdout one line.
**－** A milestone with no item before the run stays: rule 229.3 does not change for it.
**－** A milestone where a note is left stays.
**－** Nothing is written to `## Closed`: nothing of that milestone was built.

## History

- 2026-09-23 created · [[decision-case-354.2]]
