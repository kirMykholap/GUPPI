---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-hi]]"
method: "one reading by hand at the first /hi of the next session, written into the estimate line; unit: the frontier findings of guppi pretask --check in tests/test_pretask.py"
origin: raw/2026-09-12/ledger.md#case-59.2
sprint: migration
created: 2026-09-12
tags: [session, harness, workflow]
---

## Criterion

Given:
`/hi` puts `sprint.md` into the context on the first turn; the Frontier is written to `raw/<date>/<hi HHMM>/frontier.md`, one line per item; `/pre-task` fails on an open line.
**＋** `sprint.md` shows the current milestone whole and a later one as one line.

When:
The person invokes `/hi`, and the agent assembles the Frontier.

Then:
The items of the current milestone are Frontier lines; a later milestone, the Backlog and Closed are not.
**＋** The other sources as today: an unfinished plan first, a hand edit from `Render:`, a failed pull and an unavailable `gh`, a `failed` reading and a lesson of the Tail, the readings `pending`, the flags of the brief; an item the person adds is a new line.
**＋** Each line `- [ ] F<n> — <title> · <source>`; closed as `[x] … · case N`, `[x] … · work` or `[-] … · defer case N`.
**－** A decision line of the Tail is not an item.

## Result

raw/2026-09-14/0747/frontier.md written at /hi with F1–F10, F11 and F12 added by the person and by the hi failure; at /pre-task every line closed as case N, work or defer case N; guppi pretask --check named the one malformed closing (F8) as a finding and printed none after the fix (blocks 73.3, 101.4)

## History

- 2026-09-12 created · [[decision-case-59.2]]
- 2026-09-12 criterion: case 73.3 added · [[decision-case-73.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L151
- 2026-09-13 criterion: case 101.4 added · [[decision-case-101.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L37
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-18 updated: the Criterion replaced whole — the Frontier from the current milestone, the lines and their closing kept (case 229.3) · [[decision-case-229.3]]
