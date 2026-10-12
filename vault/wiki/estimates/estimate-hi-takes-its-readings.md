---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint and those of an Estimate of the live sprint page, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates of its open W lines
method: by hand, the text of the skill file rendered from rule-skill-hi, or, at the Retro of the session that changes it, the new Render of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-12
origin: raw/2026-09-29/1134/ledger.md#case-508.1
sprint: migration
created: 2026-09-29
tags: [session, harness, workflow]
---

## Criterion

When:
The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

Then:
Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
**＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
**＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
**＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
**＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
**＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
**＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
**－** It reads no transcript of an earlier session.
**－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
**－** A `W` line of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose reading cannot run now stays open under `## Work` and is no Cases line. It waits for the moment that `rule-retro` sets for it. The agent judges this from the `target` of the page of that Estimate, with no judgment of whether the work is done.
**－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
**－** The Frontier is still assembled with no page opened. Only the reading step opens pages: the page of the Estimate of each open `W` line.
**－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

## Result

2026-10-12, Retro of session 1449, by hand: the Render of rule-skill-hi in vault/wiki/rules/rule-skill-hi.md with the two replace pairs of case 778 in spec.md, each old string found once on the page, read against the Criterion of case 778 — the reading step opens the page of the Estimate of each open W line and judges from it whether its reading runs now; a W line of an Estimate whose target is the live sprint page and whose reading cannot run now stays open under Work with no Cases line, judged from the target with no judgment of done; the exception of the close of a sprint, the A lines, the closers, the LEDGER block, no transcript and the Frontier assembled with no page opened stand as before

## History

- 2026-09-29 created · [[decision-case-508.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L30
- 2026-09-30 updated: the Criterion replaced whole — the Ask lines put to the person in the first reply, the answer written as the reading line (case 531.13) · [[decision-case-531.13]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1306/ledger.md#L45
- 2026-09-30 status: failed → passed · raw/2026-09-30/1736/ledger.md#L18
- 2026-10-03 updated: the Criterion replaced whole — /hi reads a moment of an earlier session from its transcript (case 613.2) · [[decision-case-613.2]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — /hi reads no transcript, and an open Work line it cannot read becomes a Cases line (case 670.5) · [[decision-case-670.5]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L5
- 2026-10-08 updated: the Criterion replaced whole — an Ask line that waits for the close of a sprint, or the session after it, stays open and is not asked; the purpose set anew · [[decision-case-732]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/0213/ledger.md#L7
- 2026-10-10 updated: the Criterion replaced whole — the readings come with the Frontier, which at an opening is not the first reply · [[decision-case-769.3]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L36
- 2026-10-12 updated: the Criterion replaced whole — an open W line of an Estimate of the live sprint page whose reading cannot run now stays open under Work and is no Cases line · [[decision-case-778]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1449/ledger.md#L8
