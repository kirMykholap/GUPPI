---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, in its first reply, each open W reading whose every moment is that /hi or came in an earlier session, reads each moment of an earlier session from the transcript of the latest session that held it, puts each open Ask line to the person as a question and writes the answer as its reading line, closes each line it ends, opens no page but the Estimates it reads, and leaves a reading with a moment not come, a transcript gone or a /hi run of its own
method: "by hand at a /hi of a later session whose open W lines hold a reading whose moment came in an earlier session: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-03
origin: raw/2026-09-29/1134/ledger.md#case-508.1
sprint: migration
created: 2026-09-29
tags: [session, harness, workflow]
---

## Criterion

When:
The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

Then:
In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose every moment, as its `method` names it, is this `/hi` or has come in an earlier session.
**＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method.
**＋** It reads each moment of an earlier session from the transcript of the latest session that held it, found by the session ids of `vault/raw/<date>/event_log.md`, and each part of the method from the session where its moment came.
**＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
**＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
**＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
**＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
**－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
**－** A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, is not taken, and its `W` line stays open.
**－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
**－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

## Result

2026-10-03, at the /hi of session 1416, the first reply of the /hi of session 1341 (transcript 26e79919, 13:41:40 to 13:49:40): before the question on the order it took the four readings whose moments came in session 0317, read from transcript 5b311f89, from raw/2026-10-03/0317/handoff.md and work.md and from the commands of each method, `git status` included; to choose them it read the method and Criterion of every pending Estimate and the History of 15; it wrote frontier.md at 13:48:54 with W6, W18, W20 and W29 closed `[x] … · work`, then a LEDGER block of four lines in a reply that ends in text, the ledger holding the four at 13:49:40; no repository file changed but frontier.md, the tree clean at 13:47:53; not exercised: an open A line, the Ask list held none

## History

- 2026-09-29 created · [[decision-case-508.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L30
- 2026-09-30 updated: the Criterion replaced whole — the Ask lines put to the person in the first reply, the answer written as the reading line (case 531.13) · [[decision-case-531.13]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1306/ledger.md#L45
- 2026-09-30 status: failed → passed · raw/2026-09-30/1736/ledger.md#L18
- 2026-10-03 updated: the Criterion replaced whole — /hi reads a moment of an earlier session from its transcript (case 613.2) · [[decision-case-613.2]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L2
