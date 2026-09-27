---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint]]"
purpose: A milestone item passed over in three sessions in a row goes to the Backlog by generate, never by hand
method: pytest tests/test_generate.py, the tests of the move, plus one reading of the History of the sprint page after the librarian's run
checked: 2026-09-23
origin: raw/2026-09-23/0034/ledger.md#case-354.1
sprint: migration
created: 2026-09-23
tags: [sprint, harness]
---

## Criterion

When:
`uv run guppi generate` has applied every entry of the run and has run the cascade.

Then:
For every item under `## Milestones` of `entity-sprint-<id>`, the script reads the `frontier.md` of `vault/raw/` and `vault/archive/`, from the newest session to the oldest by date and `HHMM`. It counts the lines whose title, the text before the first ` · `, holds one of the item's slugs in a code span.
**＋** A `[-]` line adds one. That is an item put off, closed `· sprint · defer`, `· backlog · kept` or `· defer case N`. An `[x]` line stops the count. A session without such a line is passed by.
**＋** At a count of 3 or more, the item's line leaves its milestone, unchanged, for the end of `## Backlog`.
**＋** The History of the sprint page gets the line `moved to the Backlog: <slug> passed over in <N> sessions in a row — <HHMM>, … · generate`, and stdout gets one line on the move.
**－** An open `[ ]` line is not counted.
**－** A note is not counted and not moved; a note is a line with no `[[slug]]` before the ` — `. The items of `## Backlog` and `## Closed` are not counted.

## Result

2026-09-23, uv run pytest tests/test_generate.py -k "move or passed_over or milestone": 7 passed; the History of entity-sprint-migration after the librarian's run of 0034: "moved to the Backlog: rule-work-mode passed over in 29 sessions in a row — 0034, …, 0652 · generate" and the same for rule-subagent-guppi; both lines stand unchanged at the end of ## Backlog

## History

- 2026-09-23 created · [[decision-case-354.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L35
- 2026-09-27 updated: the Criterion replaced whole — a line put off under the closers of case 451, Given lifted into When and Then (case 451.7) · [[decision-case-451.7]]
