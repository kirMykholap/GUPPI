---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case of a sprint dispatched before any Frontier, ask its id, its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line
method: by hand, at the Retro of the session of case 769, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion
checked: 2026-10-10
origin: raw/2026-10-08/2352/ledger.md#case-743.6
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
---

## Criterion

When:
The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

Then:
Before any Frontier is assembled, the main agent dispatches `case-guppi` for the line `open the next sprint` of the `Cases` of Next session in `vault/wiki/brief.md`, with the questions of the opening in the prompt of the call: the id of the sprint, its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
**＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
**＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
**＋** The opening Case is the first Case the session ratifies.
**－** No Frontier is assembled, written to `raw/<date>/<hi HHMM>/frontier.md` or shown, and no other item is taken up, before the person ratifies the opening Case.
**－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
**－** The skill decides none of the answers: `case-guppi` puts each to the person in a round.

## Result

2026-10-10, Retro of session 1913, by hand: the new Render of rule-skill-sprint-open in spec.md (case 769.1) read against the Criterion — step 1 assembles no Frontier and takes up no other item before the opening Case is ratified; step 2 dispatches case-guppi at once with the id, the goal, the Definition of done, the first milestone and the count of backlog.md with the question; step 3 writes the close line; step 4 leaves every answer to the person and writes the Frontier before the reply that acknowledges the Case; the preamble keeps the opening Case first

## History

- 2026-10-09 created · [[decision-case-743.6]]
- 2026-10-09 status: pending → failed · raw/2026-10-08/2352/ledger.md#L37
- 2026-10-09 updated: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.2) · [[decision-case-746.2]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L17
- 2026-10-10 updated: the Criterion replaced whole — the opening Case is dispatched before any Frontier · [[decision-case-769.1]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L35
