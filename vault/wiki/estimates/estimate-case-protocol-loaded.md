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
`case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`; the hook refuses a hand edit.
**＋** The one rule stood as the first paragraph of `CLAUDE.md` until this Case (59.8, 272.1).
**＋** `guppi render --check` keeps the file equal to the page.

When:
The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

Then:
`case-schema.md` opens with the section "The one rule" right under its title: nothing in the vault or the codebase changes without a Decision ratified by the human; the agent has full autonomy over how to implement something once its contract is ratified, and none over the contract itself; when unsure whether something needs ratification, it does; the vault is the only memory — no note outside the repository, what is worth keeping is a `lesson` line or a Case on a Rule page (272.1).
**＋** The paragraph after it says, as before, that the schema is the Render loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, and that a session without `/hi` holds no Case.
**＋** `render --check` after the render exits 0.
**－** The other sections of the schema do not change; the description of the project is not in the schema.

## Result

2026-09-20, uv run guppi render --check exit 0, tests/test_ledger.py green, case-schema.md as loaded at the /hi of session 2106 read by hand: the schema holds the Frontier and the closing of its lines, the acknowledging reply of four parts, the harness rendered from rules/, ask-guppi before a create, the ledger mechanics, the tick sentence of 270.2, the Language section naming rule-language, the form of the render and sprint lines in the Spec paragraph; rule-case-protocol the last child of rule-plan-mode; CLAUDE.md repeats no paragraph of the schema — its Migration mode section names the LEDGER block in one sentence as the fact that the hook exists since Slice 1, not as the rule

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
- 2026-09-21 status: pending → passed · raw/2026-09-20/2106/ledger.md#L1
- 2026-09-21 updated: the Criterion replaced whole — the schema opens with the one rule, the glossary among the files /hi loads (case 288.2) · [[decision-case-288.2]]
