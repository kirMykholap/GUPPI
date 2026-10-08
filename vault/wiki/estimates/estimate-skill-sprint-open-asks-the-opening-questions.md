---
type: estimate
kind: QA
status: failed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case of a sprint ask its id, its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line, with the Frontier assembled as /hi sets it
method: by hand, at the Retro of the session that creates it, the new Render of rule-skill-sprint-open in the Spec read against the Criterion
origin: raw/2026-10-08/2352/ledger.md#case-743.6
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
---

## Criterion

When:
The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

Then:
The main agent assembles the Frontier as `rule-skill-hi` sets it, the line `open the next sprint` first under `## Cases`.
**＋** When the person takes up that line, the main agent dispatches `case-guppi` with the questions of the opening in the prompt of the call: the id of the sprint, its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
**＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
**＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
**＋** The opening Case is the first Case the session ratifies.
**－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
**－** The skill decides none of the answers: `case-guppi` puts each to the person in a round.

## Result

2026-10-09, Retro, not read: uv run guppi materialize --date 2026-10-08 --show marks both create entries of rule-skill-sprint-open (ledger lines 15 and 27) incomplete: [type], since the then block of 743.6 holds no type: rule, so the page and the skill are not built

## History

- 2026-10-09 created · [[decision-case-743.6]]
- 2026-10-09 status: pending → failed · raw/2026-10-08/2352/ledger.md#L37
