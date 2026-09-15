---
type: rule
kind: Leaf
purpose: Prevents work starting without the current sprint and the previous session's handover
status: built
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: ["[[estimate-internal-context-loaded]]"]
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Purpose

Prevents work starting without the current sprint and the previous session's handover.
Both are vault files, both fail the same way — missing file or wrong path — so they are
one rule rather than two.

## Render

<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/brief.md
<!-- /rule-internal-context -->

## How it works

The glossary, `case-schema.md` and the category schemas are not listed here: they arrive
through `@import` in `CLAUDE.md`, and re-reading them would duplicate context that is
already present.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
