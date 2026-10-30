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

Prevents work starting without the current sprint and the previous session's handover. Both are vault files, both fail the same way — missing file or wrong path — so they are one rule rather than two. Were `orchestration.md` and `ratification.md` imported by `CLAUDE.md` rather than listed here, a session without `/hi` would carry their text too (as set in case 595). Were `case-schema.md` listed, every working session would carry the form of a Case that only `case-guppi` needs, and that agent reads it itself (as set in case 595). Were `glossary.md` in the `@` import of `CLAUDE.md` rather than here, every subagent would load it, and none of them needs it (as set in case 288.1). A category schema on this list would load text that a session needs only when it writes a page of that category, and it is read then. A file left off this list is missing after a compaction too, since `guppi recall` prints back the paths of these lines (as set in case 287). Without `where-to-stop.md` after `orchestration.md`, Plan Mode, which plans with the person the run from the approved Spec to the librarian, would not hold the conditions on which that run stops for the person, and the main agent could promise the person a turn inside it (as set in case 689.1).

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
- 2026-10-30 updated: ## How it works left the Leaf, its reasons in the Purpose as the failures each line of the list prevents · [[decision-case-942.1]]
