---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
method: "by hand at the first run from /work to the librarian after the render: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line"
checked: 2026-09-29
origin: raw/2026-09-23/1355/ledger.md#case-376
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

Then:
Retro shows the person no report and asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md`, takes the readings whose moment has come, and decides which lessons to write.
**＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
**＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
**＋** One reply ends Retro: it carries one `LEDGER` block with every reading and lesson of `/work` and Retro, and asks the person nothing.
**＋** After that reply, in the same turn, the agent commits the session folder and calls `/handoff`.
**－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
**－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`.
**－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

## Result

2026-09-29, by hand at the /retro of session 1753: the frontier was one numbered list with the two lines under it (23 boxes, seven read slugs), Ratified one line of ids from the tail, What is not done each number with its end; but item 1 named the reading L4 and item 8 the readings W12 and W15, which What got done named again as L4, L23 and L24, and What got done named the commit as coming after the approval instead of the commit

## History

- 2026-09-23 created · [[decision-case-376]]
- 2026-09-25 updated: the Criterion replaced whole — a third mark in the opening list: a read line whose reading waits for a later session (case 428.4) · [[decision-case-428.4]]
- 2026-09-27 status: pending → failed · raw/2026-09-27/1819/ledger.md#L39
- 2026-09-27 updated: the Criterion replaced whole and the purpose rewritten — the frontier numbers only what needs an end; the close holds the Case ids, what got done and the numbers with their ends (case 468.1) · [[decision-case-468.1]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/1318/ledger.md#L39
- 2026-09-28 updated: the Criterion replaced whole — a frontier item names no end; What is not done holds the proposed end of each number with no ledger line number; the frontier and the close stand in one reply (case 483) · [[decision-case-483]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1753/ledger.md#L29
- 2026-09-30 renamed from `estimate-retro-report-holds-each-fact-once` · [[decision-case-531.1]]
- 2026-09-30 updated: renamed from estimate-retro-report-holds-each-fact-once and the Criterion replaced whole — no report and no approval: one reply of lines, a commit on green, then /handoff; the promise of each fact once moves to estimate-handoff-holds-each-fact-once (case 531.1) · [[decision-case-531.1]]
