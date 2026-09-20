---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
method: one reading at the first /hi of a session, by hand, plus the preview cases of tests/test_ledger.py
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Criterion

Given:
A `full` page writes the whole file named by `governs`, without its outer markers; a child of a `full` page governs the same file as its parent, otherwise `render` errors (case 277).
**＋** The `children` of a Rule MOC is an ordered list, set explicitly.
**＋** `tests/test_render.py` fixes a `full` render into a file outside `.claude/`.

When:
The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

Then:
`vault/wiki/case-schema.md` equals the Render of `rule-case-protocol`; `render --check` exits 0; the file is no longer edited by hand — the hook refuses.
**＋** The schema holds one text: what stood in it, plus from the old Render — the Frontier `frontier.md` and the closing of its lines, Plan Mode not ending while a line is open; the acknowledging reply of four parts; the harness rendered from `rules/`, never by hand; `ask-guppi` before a `create` without a `ref`, the answer in `context`; the ledger mechanics — the `LEDGER` block, the `Stop` hook, `{tags}`, `{source}`, when each line is written, the refusal without `/hi`, a reply with the block ending in it, a block a tool call followed not lost before `Stop`.
**＋** The tick sentence in the wording of 270.2; the Language section of the schema on the manner of the English of the vault, the language of the repository and the chat being `rule-language`.
**＋** At `/hi` the agent states the LEDGER-block rule and the one-Case-at-a-time rule without a read call.
**－** Nothing of the schema is repeated in `CLAUDE.md`; `rule-case-protocol` is a child of `rule-plan-mode`, the last of its list.

## Result

2026-09-20, the first turn of session 0527 read by hand: the reply to /hi states the LEDGER-block rule and the one-Case-at-a-time rule without a read of the rule or of CLAUDE.md; the Spec named as raw/2026-09-20/0527/spec.md with its ## Deferred heading and the ticked boxes, the Frontier as raw/2026-09-20/0527/frontier.md; a reply with a LEDGER block ends in that text, the text before a tool call waits for the next Stop, no loss called before it, only a line missing there is a lesson; Work Mode ticks code, tests, migrations and readings, generate, render and sprint tick the page, render and sprint lines (cases 226, 250)

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.2
- 2026-09-12 updated: the then block form of case 72.1 joins the criterion; pending for the next session's reading · [[decision-case-72.1]]
- 2026-09-12 criterion: case 73.9 added · [[decision-case-73.9]]
- 2026-09-12 criterion: case 75.1 added · [[decision-case-75.1]]
- 2026-09-12 criterion: case 86 added · [[decision-case-86]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L43
- 2026-09-14 criterion: case 144.1 added · [[decision-case-144.1]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L6
- 2026-09-15 criterion: case 157 added · [[decision-case-157]]
- 2026-09-15 criterion: case 159 added · [[decision-case-159]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1448/ledger.md#L4
- 2026-09-15 status: passed → passed · raw/2026-09-15/1448/ledger.md#L5
- 2026-09-15 criterion: case 167 added · [[decision-case-167]]
- 2026-09-15 criterion: case 157 removed · [[decision-case-167]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L3
- 2026-09-16 updated: the Criterion replaced whole — the head text without the dead method clause, plus block 73.9; the other blocks move to their own Estimates (case 188) · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L37
- 2026-09-17 status: passed → passed · raw/2026-09-16/2238/ledger.md#L36
- 2026-09-18 updated: three lines added to the Criterion — the wait for the next Stop, no loss called before it, who ticks which line (cases 224.2, 233) · [[decision-case-224.2]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L1
- 2026-09-18 updated: one line of the Criterion — sprint is the third ticker (case 253.1) · [[decision-case-253.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0527/ledger.md#L1
- 2026-09-20 updated: the Criterion replaced whole — the tick sentence names generate on the read lines (case 270.2) · [[decision-case-270.2]]
- 2026-09-20 updated: the Criterion replaced whole — the schema is the Render of rule-case-protocol, loaded by /hi, and holds the ledger, Frontier and acknowledging-reply paragraphs (case 273.1) · [[decision-case-273.1]]
