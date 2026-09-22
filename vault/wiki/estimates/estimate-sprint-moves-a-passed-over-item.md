---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint]]"
purpose: A milestone item passed over in three sessions in a row goes to the Backlog by generate, never by hand
method: pytest tests/test_generate.py, the tests of the move, plus one reading of the History of the sprint page after the librarian's run
origin: raw/2026-09-23/0034/ledger.md#case-354.1
sprint: migration
created: 2026-09-23
tags: [sprint, harness]
---

## Criterion

Given:
`generate` is the only writer to `wiki/`, the sprint page `entity-sprint-<id>` included.
**＋** A milestone item is a line under `### <name>` in `## Milestones`; its pages are every `[[slug]]` before the first ` — `, by `sprint.item_slugs` (case 313).
**＋** Every session writes `frontier.md` into its folder; `guppi archive` moves the folder whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`.
**＋** A Frontier line is closed `[-]` when its item was put off (`· sprint`, `· defer case N`), and `[x]` when it was taken up (`· case N`, `· work`).
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault.

When:
`guppi generate` has applied every entry of the run and run the cascade.

Then:
For every item under `## Milestones`, the script reads the `frontier.md` of `raw/` and of the archive, from the newest session to the oldest by date and `HHMM`, and counts the lines whose title — the text before the first ` · ` — holds one of the item's slugs in a code span.
**＋** A `[-]` line adds one; an `[x]` line stops the count; a session without such a line is passed by.
**＋** At a count of 3 or more, the item's line leaves its milestone, unchanged, for the end of `## Backlog`.
**＋** The History of the sprint page gets the line `moved to the Backlog: <slug> passed over in <N> sessions in a row — <HHMM>, … · generate`, and stdout one line on the move.
**－** An open `[ ]` line is not counted.
**－** A note — a line with no `[[slug]]` before the ` — ` — is not counted and not moved; the items of `## Backlog` and `## Closed` are not counted.

## History

- 2026-09-23 created · [[decision-case-354.1]]
