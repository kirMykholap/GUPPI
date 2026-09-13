---
type: rule
kind: Leaf
purpose: Keeps a session from writing anything before a Case is ratified
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: rule-settings
estimates: [estimate-default-mode]
origin: raw/2026-09-12/ledger.md#case-85.4
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Purpose

Keeps a session from writing anything before a Case is ratified. Plan Mode is the
form of the whole model: the agent reads, forms Cases and waits for a sign-off, and
the harness enforces it rather than the agent's memory. `defaultMode` is one key,
but it decides what a session may do from its first turn, so it is a rule of its
own and not a line of the registry (case 85.4).

## Render

<!-- rule-default-mode -->
    "defaultMode": "plan",
<!-- /rule-default-mode -->

## Estimates

- [[estimate-default-mode]]

## Parent

- [[rule-settings]]

## History

- 2026-09-12 created · [[decision-case-85.4]]
- 2026-09-12 estimate estimate-default-mode added · [[decision-case-85.4]]
- 2026-09-13 status: draft → built · cascade
