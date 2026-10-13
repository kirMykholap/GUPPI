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
core: true
---

## Purpose

Prevents work starting without the current sprint and the previous session's handover.
Both are vault files, both fail the same way — missing file or wrong path — so they are
one rule rather than two.

## Render

<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/backlog.md
@vault/wiki/brief.md
@vault/wiki/orchestration.md
@vault/wiki/where-to-stop.md
@vault/wiki/ratification.md
@vault/wiki/glossary.md
<!-- /rule-internal-context -->

## How it works

`orchestration.md` and `ratification.md` are listed in place of `case-schema.md` (since case 595; `case-schema.md` was listed from case 273): they reach a working session here and not through `CLAUDE.md`, so a session without `/hi` carries none of their text, and the form of a Case, `case-schema.md`, reaches only `case-guppi`, which reads it itself. `glossary.md` is listed here and not in the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs (since case 288.1). The category schemas are not listed:
they are read when a page of their category is written. After a compaction `guppi recall`
prints the paths of these lines back (case 287). `where-to-stop.md` is listed after `orchestration.md` (since case 689.1): the run from the approved Spec to the librarian stops for the person only on its conditions, and Plan Mode, which plans that run with the person, holds the same list, so the main agent promises no turn of the person inside it.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
- 2026-09-20 updated: case-schema.md joins the imports of /hi; the glossary stays with CLAUDE.md (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-21 updated: the glossary is the fourth @ line — it arrives with /hi and reaches no subagent, which pays for CLAUDE.md alone (case 288.1) · [[decision-case-288.1]]
- 2026-09-21 status: built → draft · cascade
- 2026-09-21 status: draft → built · cascade
- 2026-09-27 updated: /hi loads backlog.md after sprint.md (case 451.12) · [[decision-case-451.12]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-10-02 updated: /hi loads orchestration.md and ratification.md in place of case-schema.md (case 595.4) · [[decision-case-595.4]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-02 status: draft → built · cascade
- 2026-10-06 updated: /hi loads where-to-stop.md after orchestration.md (case 689.1) · [[decision-case-689.1]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: each pointer stands in a bracket of its own · [[decision-case-809]]
