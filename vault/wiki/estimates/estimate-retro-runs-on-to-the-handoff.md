---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply and each refused record line of a refusal of the ledger hook again in one reply that holds only them, a refused line that is no record left out, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
method: "by hand at a run from /work to the librarian: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-07
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

Then:
Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
**＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
**＋** The agent commits the work when `uv run --project .guppi guppi style` is clean and `uv run --project .guppi guppi test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
**＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
**－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
**＋** When the ledger hook refuses a line of that reply, the agent answers with a reply that holds only a `LEDGER` block with each refused record line written again; a refused line of the block that is no record, one that does not open with `- decision[`, `- estimate[` or `- lesson[`, is left out. No other `LEDGER` block follows the reply that ends Retro.
**＋** When no refused line is left to write, that answer holds no `LEDGER` block, and in it the agent commits the session folder and calls `/handoff`.
**＋** After that reply, or after the reply that answers a refusal of the ledger hook, in the same turn, the agent commits the session folder and calls `/handoff`.
**－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
**－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead. The answer to a refusal of the ledger hook is no stop.
**－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

## Result

2026-10-07, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
