---
type: rule
kind: Leaf
purpose: Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint
status: built
enforcement: render
implementation_ref: [guppi/sprint.py, tests/test_sprint.py, .claude/settings.json]
governs: .claude/skills/sprint-open/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
estimates: ["[[estimate-skill-sprint-open-asks-the-opening-questions]]", "[[estimate-skill-sprint-open-starts-at-hi]]"]
origin: raw/2026-10-08/2352/ledger.md#case-743.6
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
---

## Purpose

Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint. Until case 743 nothing set what the opening Case asks, and the steps of the turn of a sprint stood in `orchestration.md`, which every session loads. The skill loads only in the session that opens a sprint: the `UserPromptSubmit` hook `guppi sprint --hi` tells the agent at `/hi` to start it when `vault/wiki/sprint.md` marks the last sprint closed ([[rule-sprint]], case 743.5), and the person may type it too. The backlog is not gone through: the opening Case says how many items it holds and asks whether to take any (case 743.6). The close line it writes starts [[rule-skill-sprint-close]] in the session that closes the sprint.

## Render

<!-- rule-skill-sprint-open -->
---
name: sprint-open
description: "Open the next sprint. Run it when the hook on /hi says that no sprint is open, or when the person types /sprint-open."
---

No sprint is open: the first heading of `vault/wiki/sprint.md` marks the last sprint closed. This session opens the next one. The ledger hook refuses each decision line but a `defer` until a `create` of a page `entity-sprint-<id>` stands, so the opening Case is the first Case the session ratifies.

1. Assemble the Frontier as `/hi` sets it: the line `open the next sprint` of the brief stands first under `## Cases`, and no item of the closed sprint and no conserved Spec stands there.
2. When the person takes up that line, dispatch `case-guppi` for it as `vault/wiki/orchestration.md` sets it, and write into the prompt of the call that the opening Case asks the person, in its rounds:
   - the id of the sprint, which names the page `entity-sprint-<id>`;
   - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
   - its Definition of done, one Estimate per condition, which the page lists in `estimates`;
   - the first milestone and its items, under `## Milestones`;
   - whether to take any item of `vault/wiki/backlog.md` into the sprint: the Case says how many items the file holds, and goes through no item the person does not name.
3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from it.
4. The skill decides none of the answers: `case-guppi` puts each to the person, and the person ratifies the opening Case as any other.
<!-- /rule-skill-sprint-open -->

## History

- 2026-10-09 created · [[decision-case-743.6]]
- 2026-10-09 estimate estimate-skill-sprint-open-asks-the-opening-questions added · [[decision-case-743.6]]
- 2026-10-09 estimate estimate-skill-sprint-open-starts-at-hi added · [[decision-case-743.7]]
- 2026-10-09 updated: the parent is rule-session-start, as case 743.6 set it (case 746.1) · [[decision-case-746.1]]
- 2026-10-09 status: draft → built · cascade
