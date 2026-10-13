---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the main agent ask the sprint id first, then the opening Case dispatched as Case <id>-1 before any Frontier, ask its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line
method: by hand, at the Retro of this session, the new Render of rule-skill-sprint-open in raw/<date>/<hi HHMM>/spec.md read against the Criterion
checked: 2026-10-13
origin: raw/2026-10-08/2352/ledger.md#case-743.6
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
---

## Criterion

When:
The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

Then:
Before any Frontier is assembled and before any dispatch, the main agent asks the person in one plain question for the id of the sprint, which names the page `entity-sprint-<id>` and starts with the GitHub name of its author, such as `kir-plugin`, with lower-case letters, digits and hyphens and no dot.
**＋** The main agent then dispatches `case-guppi` with the Case id `<id>-1` for the line `open the next sprint` of the `Cases` of Next session in `vault/wiki/brief.md`, with the id of the sprint and the questions of the opening in the prompt of the call: its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
**＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
**＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
**＋** The opening Case is the first Case the session ratifies.
**－** No Frontier is assembled, written to `raw/<date>/<hi HHMM>/frontier.md` or shown, and no other item is taken up, before the person ratifies the opening Case.
**－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
**－** The skill decides none of the answers: the main agent asks the person for the id, and `case-guppi` puts each other question to the person in a round.

## Result

2026-10-13, Retro by hand: the Render of rule-skill-sprint-open in spec.md (case 788.3) has the main agent ask the sprint id first, dispatch the opening Case as <id>-1 and case-guppi ask the goal, the Definition of done, the first milestone and the backlog

## History

- 2026-10-09 created · [[decision-case-743.6]]
- 2026-10-09 status: pending → failed · raw/2026-10-08/2352/ledger.md#L37
- 2026-10-09 updated: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.2) · [[decision-case-746.2]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L17
- 2026-10-10 updated: the Criterion replaced whole — the opening Case is dispatched before any Frontier · [[decision-case-769.1]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L35
- 2026-10-13 updated: the Criterion replaced whole — the main agent asks the sprint id before the dispatch, and the opening Case is Case <id>-1 (case 788.3) · [[decision-case-788.3]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L49
