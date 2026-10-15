---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: The form of a Case stands in one text, the Render of rule-case-protocol, which /hi does not load and the main agent does not read, with nothing of orchestration.md or ratification.md repeated in it and nothing of it repeated in CLAUDE.md
method: uv run --project .guppi guppi render --check; by hand after the librarian's render, case-schema.md, orchestration.md and ratification.md compared paragraph by paragraph, and at the first /hi of a later session the first turn's context and the main agent's read calls in the transcript
checked: 2026-10-02
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Criterion

When:
`uv run --project .guppi guppi render` wrote `vault/wiki/case-schema.md` from `rule-case-protocol`, and a session opened by `/hi` dispatches `case-guppi` by `.claude/agents/case-guppi.md`.

Then:
`uv run --project .guppi guppi render --check` exits 0: the file equals the Render of `rule-case-protocol`, its language placeholders filled from `rule-guppi-config`.
**＋** The file holds the form of a Case: its sections, operands and language, the `then` block, the task lines, the taking up of a deferred decision, the sub-cases and the slug.
**＋** `.claude/skills/hi/SKILL.md` holds no `@` line for `vault/wiki/case-schema.md`, and the main agent reads none of it in the session.
**－** The file repeats no paragraph of `vault/wiki/orchestration.md` or `vault/wiki/ratification.md`, and `CLAUDE.md` repeats none of its paragraphs.

## Result

2026-10-02, the /hi of session 2049: `uv run guppi render --check` exit 0; the @ lines of .claude/skills/hi/SKILL.md name six files, case-schema.md not among them; the first turn's context holds no case-schema.md and the agent made no Read call on it; a script opened it and printed counts only: 21 paragraphs, 0 shared with CLAUDE.md, orchestration.md or ratification.md, and the words given, when, then, tasks, ratification, operand, language, sub-case, slug and deferred present

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
- 2026-09-21 status: pending → passed · raw/2026-09-21/1315/ledger.md#L1
- 2026-09-21 updated: one line of the Criterion — the Spec paragraph names the field-only update of an Estimate (case 294) · [[decision-case-294]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L1
- 2026-09-22 updated: one line of the Criterion — the Spec paragraph says a Case superseded in its own session leaves the Spec (case 299.1) · [[decision-case-299.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L1
- 2026-09-22 updated: one line of the Criterion — glossary the fourth ticker (case 306.6) · [[decision-case-306.6]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L83
- 2026-09-23 updated: the Criterion names reword among the keys of an update and the two steps of the author (case 353) · [[decision-case-353]]
- 2026-09-23 updated: the Criterion names the row of ratification (case 355.1) · [[decision-case-355.1]]
- 2026-09-23 updated: the Criterion names the sub-cases shown in one reply (case 355.2) · [[decision-case-355.2]]
- 2026-09-23 updated: the Criterion names the open Cases line of the Plan Mode paragraph (case 356.1) · [[decision-case-356.1]]
- 2026-09-23 updated: the Criterion names the closer sprint of the Plan Mode paragraph (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 updated: the Criterion names the heading of a Case in the Render (case 368) · [[decision-case-368]]
- 2026-09-23 updated: the Criterion names the sub-points of tasks in the Render (case 370) · [[decision-case-370]]
- 2026-09-23 updated: the Criterion names the showing again after the agent's own finding in the Render (case 373) · [[decision-case-373]]
- 2026-09-25 updated: the Criterion replaced whole — the Render present from the first turn after /hi and equal to the page, the journal of its paragraphs out (cases 378.5, 396.2) · [[decision-case-396.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L48
- 2026-10-02 updated: the Criterion replaced whole - the file holds the form of a Case alone and is not loaded by /hi (case 595.6) · [[decision-case-595.6]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L5
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
