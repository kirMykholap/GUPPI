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
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness]
core: true
---

## Purpose

Prevents work starting without the current sprint and the previous session's handover. Both are vault files, both fail the same way — missing file or wrong path — so they are one rule rather than two. Were `orchestration.md` and `ratification.md` imported by `CLAUDE.md` rather than listed here, a session without `/hi` would carry their text too. Were `case-schema.md` listed, every working session would carry the form of a Case that only `case-guppi` needs, and that agent reads it itself. Were `glossary.md` in the `@` import of `CLAUDE.md` rather than here, every subagent would load it, and none of them needs it. A category schema on this list would load text that a session needs only when it writes a page of that category, and it is read then. A file left off this list is missing after a compaction too, since `guppi recall` prints back the paths of these lines. Without `where-to-stop.md` after `orchestration.md`, Plan Mode, which plans with the person the run from the approved Spec to the librarian, would not hold the conditions on which that run stops for the person, and the main agent could promise the person a turn inside it.

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

- 2026-11-03 shipped with GUPPI
