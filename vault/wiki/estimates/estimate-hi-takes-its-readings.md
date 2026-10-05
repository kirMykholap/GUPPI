---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, in its first reply, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person and writes the answer as its reading line, and opens no page but the Estimates it reads
method: by hand, the text of the skill file rendered from rule-skill-hi, or, at the Retro of the session that changes it, the new Render of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-03
origin: raw/2026-09-29/1134/ledger.md#case-508.1
sprint: migration
created: 2026-09-29
tags: [session, harness, workflow]
---

## Criterion

When:
The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

Then:
In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
**＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
**＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
**＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
**＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
**＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
**＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
**－** It reads no transcript of an earlier session.
**－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
**－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
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
- 2026-10-05 updated: the Criterion replaced whole — /hi reads no transcript, and an open Work line it cannot read becomes a Cases line (case 670.5) · [[decision-case-670.5]]
