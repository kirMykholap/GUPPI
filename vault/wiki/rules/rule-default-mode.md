---
type: rule
kind: Leaf
purpose: Keeps a session from writing anything before a Case is ratified
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, session]
core: true
---

## Purpose

Keeps a session from writing anything before a Case is ratified. Plan Mode is the
form of the whole model: the agent reads, forms Cases and waits for a sign-off, and
the harness enforces it rather than the agent's memory. `defaultMode` is one key,
but it decides what a session may do from its first turn, so it is a rule of its
own and not a line of the registry.

## Render

<!-- rule-default-mode -->
    "defaultMode": "plan",
<!-- /rule-default-mode -->

## History

- 2026-10-14 shipped with GUPPI
