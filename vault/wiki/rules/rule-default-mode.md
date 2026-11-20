---
type: rule
kind: Leaf
purpose: Keeps a session from writing anything before a Case is ratified
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: ["[[estimate-default-mode]]"]
origin: raw/2026-09-12/ledger.md#case-85.4
sprint: migration
created: 2026-09-12
tags: [harness, session]
core: true
---

## Purpose

Keeps a session from writing anything before a Case is ratified. Plan Mode is the
form of the whole model: the agent reads, forms Cases and waits for a sign-off, and
the harness enforces it rather than the agent's memory. `defaultMode` is one key,
but it decides what a session may do from its first turn, so it is a rule of its
own and not a line of the registry (case 85.4). The agent writes nothing before a Case: at `/hi` in a folder that is no git repository, the person types `! git init -b main`, which Claude Code runs as the person's own shell command and not as a call of the agent, since a session of GUPPI needs a git repository, as `rule-git-context` sets it (as set in case 1036).

## Render

<!-- rule-default-mode -->
    "defaultMode": "plan",
<!-- /rule-default-mode -->

## History

- 2026-09-12 created · [[decision-case-85.4]]
- 2026-09-12 estimate estimate-default-mode added · [[decision-case-85.4]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-16 updated: one exception: git init -b main at /hi on the person's yes · [[decision-case-851.1]]
- 2026-11-20 updated: no write of the agent comes before a Case; the person makes the repository · [[decision-case-1036]]
