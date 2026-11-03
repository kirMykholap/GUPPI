---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the main agent ask the sprint id first, then the opening Case dispatched as Case <id>-1 before any Frontier, ask its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line
method: "by hand: the Render of rule-skill-sprint-open in .claude/skills/sprint-open/SKILL.md read against the Criterion"
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow, harness]
core: true
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

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
