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
@vault/wiki/case-schema.md
<!-- /rule-internal-context -->

## How it works

`case-schema.md` is listed since case 273: the Render of `rule-case-protocol`, it reaches
a working session here and not through `CLAUDE.md`, so a session without `/hi` carries no
Case text. The glossary and the category schemas are not listed: the glossary arrives
through `@import` in `CLAUDE.md`, the schemas are read when a page of their category is
written.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
- 2026-09-20 updated: case-schema.md joins the imports of /hi; the glossary stays with CLAUDE.md (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
