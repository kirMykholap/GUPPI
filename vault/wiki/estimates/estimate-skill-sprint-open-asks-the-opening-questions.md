---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the person answer the open question on what the sprint is to build before anything else, taken from the reply that acknowledges the setup Case where one stands, then has the main agent propose the sprint id, dispatch the opening Case as Case <id>-1 with that answer before any Frontier, have it build the goal, the Definition of done and the milestone from the answer and ask whether to take an item of the backlog, and write the close line
method: "by hand, after the librarian's run of the session that replaces this Criterion: the Render of rule-skill-sprint-open in .claude/skills/sprint-open/SKILL.md, the Render of rule-skill-setup in .claude/skills/setup/SKILL.md and the sentence of rule-orchestration on the reply that acknowledges the setup Case in vault/wiki/orchestration.md read against the Criterion"
checked: 2026-11-03
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [sprint, workflow, harness]
core: true
---

## Criterion

When:
The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

Then:
Before any Frontier is assembled and before the skill dispatches anything, the person answers one open question on what the sprint is to build: what they want to build in it, how they see it and what should happen.
**＋** In a session where `/setup` of `rule-skill-setup` built the setup Case, since `guppi.toml` holds `setup_done = false`, the reply that acknowledges that Case asks that question, and the skill takes the person's answer and does not ask it again.
**＋** Right after that answer, the main agent proposes in one plain question the id of the sprint, which names the page of the sprint and starts with the GitHub name of its author, such as `kir-plugin`, with lower-case letters, digits and hyphens and no dot, and the person confirms it or gives another.
**＋** The main agent then dispatches `case-guppi` with the Case id `<id>-1` for the line `open the next sprint` of the `Cases` of Next session in the brief, with the id of the sprint, the person's answer and the parts of the opening that the opening Case builds from that answer in the prompt of the call: its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
**＋** The prompt asks that the opening Case say how many items the backlog holds and ask the person whether to take any of them.
**＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
**＋** The opening Case is the first Case the session ratifies, but for that setup Case, which comes before it.
**－** No Frontier is assembled, written or shown, and no other item is taken up, before the person ratifies the opening Case.
**－** The opening Case goes through no item of the backlog that the person does not name.
**－** The skill decides none of the answers: the main agent proposes the id and the person confirms or corrects it, and `case-guppi` asks the person in its rounds only what the answer leaves open.

## Result

2026-11-03, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
