---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
method: "by hand at the first run from /work to the librarian after the render: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-01
origin: raw/2026-09-23/1355/ledger.md#case-376
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

Then:
Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
**＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
**＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
**＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
**－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
**＋** After that reply, in the same turn, the agent commits the session folder and calls `/handoff`.
**－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
**－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead.
**－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

## Result

2026-10-01, by hand, the transcript of session 4ba72976 from the call of /retro at 03:09:42, its ledger, git log and raw/2026-09-30/2356/handoff.md: one reply ended Retro with one LEDGER block of the six readings and the lesson and asked nothing; the code was committed as f7581b07 on make style clean and make test 1034 passed; the session folder was committed as 0e65b085 and /handoff called in the same turn, after the refusal of guppi onward; no defer and no stop; the reading only the person can take is a line of Ask the person; but the reply showed the person a report, five headed parts in English (What I built, Left open, Readings taken, Not taken yet, One lesson) before the LEDGER block, and the event log from 03:09:42 to 03:11:02 holds no read of work.md, which the agent wrote at 02:59:28

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
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L5
- 2026-10-01 updated: the Criterion replaced whole — the reply that ends Retro holds one sentence in the language of the chat that names the commit and the LEDGER block, no heading, list or other paragraph; work.md the agent wrote or changed in the same turn counts as read (case 569.1) · [[decision-case-569.1]]
