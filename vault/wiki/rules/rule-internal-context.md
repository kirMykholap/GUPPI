---
type: rule
kind: Leaf
purpose: Prevents work starting without the current sprint and the previous session's handover
status: draft
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
@vault/wiki/glossary.md
<!-- /rule-internal-context -->

## How it works

`case-schema.md` is listed since case 273: the Render of `rule-case-protocol`, it reaches
a working session here and not through `CLAUDE.md`, so a session without `/hi` carries no
Case text. `glossary.md` is listed since case 288.1: it left the `@` import of `CLAUDE.md`,
which every subagent loads and none of them needs. The category schemas are not listed:
they are read when a page of their category is written. After a compaction `guppi recall`
prints the paths of these lines back (case 287).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
- 2026-09-20 updated: case-schema.md joins the imports of /hi; the glossary stays with CLAUDE.md (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-21 updated: the glossary is the fourth @ line — it arrives with /hi and reaches no subagent, which pays for CLAUDE.md alone (case 288.1) · [[decision-case-288.1]]
- 2026-09-21 status: built → draft · cascade
