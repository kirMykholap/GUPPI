---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether the session that closes sprint plugin runs /sprint-close from the close line up to the end of Work Mode with no step done or fixed by hand
method: "by hand, at the end of Work Mode of the session that closes entity-sprint-plugin: its frontier.md, ledger, spec.md and transcript"
origin: raw/2026-10-10/1713/ledger.md#case-756.2
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow]
---

## Criterion

When:
In the session that closes `entity-sprint-plugin`, the person takes up the line ``the close of `plugin` — `/sprint-close`, a session of its own`` of its `## Milestones`; at the end of Work Mode someone reads that session's `frontier.md`, ledger, `spec.md` and transcript.

Then:
From that line to the end of Work Mode, no step of `/sprint-close` of `.claude/skills/sprint-close/SKILL.md` is done or fixed by hand outside what the skill sets.
**－** The steps the skill sets are not part of this promise: `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups` hold them.
**－** The move of the pages to the archive in the librarian's run is not part of this promise: `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` holds it.

## History

- 2026-10-10 created · [[decision-case-756.2]]
