---
type: rule
kind: Leaf
purpose: Prevents work starting without the current sprint and the previous session's handover
status: built
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
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

`orchestration.md` and `ratification.md` are listed in place of `case-schema.md`: they reach a working session here and not through `CLAUDE.md`, so a session without `/hi` carries none of their text, and the form of a Case, `case-schema.md`, reaches only `case-guppi`, which reads it itself. `glossary.md` is listed here and not in the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs. The category schemas are not listed:
they are read when a page of their category is written. After a compaction `guppi recall`
prints the paths of these lines back. `where-to-stop.md` is listed after `orchestration.md`: the run from the approved Spec to the librarian stops for the person only on its conditions, and Plan Mode, which plans that run with the person, holds the same list, so the main agent promises no turn of the person inside it.

## History

- 2026-10-14 shipped with GUPPI
