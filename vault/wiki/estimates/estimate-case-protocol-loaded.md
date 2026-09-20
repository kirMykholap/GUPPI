---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: The Case schema is present in a session from the first turn after /hi, as one text — the Render of rule-case-protocol — and nothing of it repeated in CLAUDE.md
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
**＋** The presence of the schema's text in the first turn is checked by `estimate-internal-context-loaded`, not by this Estimate.
**＋** The tickers of `render` and `sprint` match a line that opens with a code span holding the command (case 235); `tests/test_render.py` fixes it.

When:
The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

Then:
`vault/wiki/case-schema.md` equals the Render of `rule-case-protocol`; `render --check` exits 0; the file is no longer edited by hand — the hook refuses.
**＋** The schema holds one text: what stood in it, plus from the old Render — the Frontier `frontier.md` and the closing of its lines, Plan Mode not ending while a line is open; the acknowledging reply of four parts; the harness rendered from `rules/`, never by hand; `ask-guppi` before a `create` without a `ref`, the answer in `context`; the ledger mechanics — the `LEDGER` block, the `Stop` hook, `{tags}`, `{source}`, when each line is written, the refusal without `/hi`, a reply with the block ending in it, a block a tool call followed not lost before `Stop`.
**＋** The tick sentence in the wording of 270.2; the Language section of the schema on the manner of the English of the vault, the language of the repository and the chat being `rule-language`.
**＋** The Spec paragraph of the schema names the form of the lines the command scripts tick: `- [ ] `uv run guppi render`: `<file>`` and `- [ ] `uv run guppi sprint`` — the command in the first code span; a line of another form stays debt at Retro.
**－** Nothing of the schema is repeated in `CLAUDE.md`; `rule-case-protocol` is a child of `rule-plan-mode`, the last of its list.
**－** The agent's reply to `/hi` does not have to restate the rules of the schema.

## Result

2026-09-20, uv run guppi render --check exit 0, tests/test_ledger.py 37 passed, case-schema.md and the /hi reply of session 1749 read by hand: the schema holds the Frontier, the acknowledging reply, the harness, ask-guppi, the ledger mechanics, the tick sentence of 270.2 and the Language section; rule-case-protocol the last child of rule-plan-mode; CLAUDE.md repeats none of it — but the /hi reply did not state the LEDGER-block rule and the one-Case-at-a-time rule; no instruction of the SKILL or the schema asks for that statement

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
- 2026-09-20 status: pending → failed · raw/2026-09-20/1749/ledger.md#L6
- 2026-09-20 updated: the Criterion replaced whole — the text of 278 plus the form of the render and sprint lines; the line on the agent stating two rules at /hi removed; purpose added (case 279.1, supersedes 278) · [[decision-case-279.1]]
