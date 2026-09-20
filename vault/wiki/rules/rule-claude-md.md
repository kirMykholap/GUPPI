---
type: rule
kind: MOC
purpose: Prevents the system prompt from holding a line nobody ratified
status: draft
enforcement: render
governs: CLAUDE.md
render_mode: full
parent: "[[rule-harness]]"
children: ["[[rule-language]]", "[[rule-agent-writing]]"]
estimates: ["[[estimate-claude-md-rendered]]"]
origin: raw/2026-09-12/ledger.md#case-59.8
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Purpose

Prevents the system prompt from holding a line nobody ratified. `CLAUDE.md` is the
one file every session reads first; until this page it was hand-written around one
rendered section, and a ratified sentence went into the file instead of the page
(case 56). Now the file is the Render of this page, whole, with `rule-language` and `rule-agent-writing` spliced into their markers; a change to it is an `update` of one of the three. The Render imports [[glossary]] and points at [[index]]; the Case schema is the Render of `rule-case-protocol`, loaded by `/hi` (cases 272, 273.3).

## Render

<!-- rule-claude-md -->
# GUPPI

A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into.
The vault is `vault/`; its map is `vault/wiki/index.md`. Nothing in the vault or the codebase
changes without a Decision ratified by the human. You have full autonomy over *how* to
implement something once its contract is ratified, and none over the contract itself. When you
are unsure whether something needs ratification: it does. The vault is the only memory: write no note outside the repository — not the harness's local memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).

## What is loaded here

The glossary arrives through the import below, so the terms are present from the first turn
without a read. The shape of a Case — `vault/wiki/case-schema.md`, the Render of
`rule-case-protocol` — arrives with `/hi`, which opens a working session; a session without
`/hi` holds no Case.

@vault/wiki/glossary.md

`vault/wiki/index.md` is not imported: it is the map of the vault and the rules that hold in
every phase, read section by section when a section is needed (§0 the one rule, §1 layout,
§2 Case protocol, §3 decisions, §4 ledger, §5 routing, §6 splitting, §7 estimates, §8 lessons
and insights, §10 librarian, §11 indexes, §12 where content comes from).

## Migration mode, since 2026-09-09

This repository is being moved from its earlier model onto the one in `index.md`. Until the
move closes:

- **The state a session starts from is `vault/wiki/brief.md`.** Read it first; nothing prints
  it yet. `vault/wiki/sprint.md` names the slices and what closes the sprint.
- **The ledger hook exists since Slice 1.** Lines are emitted in a ```` ```LEDGER ```` block
  in the reply and the `Stop` hook writes them into `vault/raw/<date>/<hi HHMM>/ledger.md`, the session's folder (case 103.1), each
  prefixed with the time of writing. The lines of 2026-09-09 written by hand before it
  carry no time; that is how the two are told apart.
- **The rituals of the new model exist since Slice 3.** `/retro` (the person, or the agent once the Spec's tasks are ticked), `/handoff` (the
  agent, refused by `guppi gate` while the tree is dirty), then the `librarian-guppi` agent:
  `materialize`, index check, synthesis, `generate`, `cleanup`, brief, commit. Pages are no
  longer written by hand; `brief.md` is written by the librarian. `docs/migration/` still
  holds the drafts of Work Mode and the plan of the move.
- **Each slice is its own Plan Mode and its own approval.** The approved plan is copied to `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder, by the `PostToolUse ExitPlanMode` hook `guppi spec` since Slice 2 (the folder since case 73); the Specs of Slices 0–2 were copied by hand.

<!-- rule-language -->

<!-- rule-agent-writing -->

## Commands

`make help` lists the targets. `make style` must be clean before every commit. Add no new
dependencies, Python or otherwise.
<!-- /rule-claude-md -->

## How it works

Rendered in full into `CLAUDE.md`; each child — `rule-language`, `rule-agent-writing` — splices into its marker line. The
`@` lines are text here and imports for Claude Code. The section "Migration mode"
is carried from the hand-written file as it stood on 2026-09-12 and leaves with the
migration, by an `update` of this page. `rule-language` and `rule-agent-writing` have this page as their parent since case 272; the renderer splices each into its marker. `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`.

## History

- 2026-09-12 created · [[decision-case-59.8]]
- 2026-09-12 estimate estimate-claude-md-rendered added · [[decision-case-71.1]]
- 2026-09-12 updated: the Migration paragraph names the session's folder (case 73.10) · [[decision-case-73.10]]
- 2026-09-12 updated: the stale sentence on rule-case-protocol's parent corrected (case 77) · [[decision-case-77]]
- 2026-09-12 deferred · [[decision-case-84]]
- 2026-09-12 defer by decision-case-84 superseded · [[decision-case-88.1]]
- 2026-09-12 updated: the live clause of the CLAUDE.md reading is a standing rule, read against the two pages that render it (case 88.2) · [[decision-case-88.2]]
- 2026-09-13 updated: the Migration paragraph names the session ledger (case 109.2) · [[decision-case-109.2]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: a Case is discussed in the chat in Russian and enters the Spec in English; the plan the owner approves is the Spec (case 123) · [[decision-case-123]]
- 2026-09-14 updated: the hub file linked for the graph (case 149.4) · [[decision-case-149.4]]
- 2026-09-14 updated: the agent may call /retro after Work Mode (case 150.1) · [[decision-case-150.1]]
- 2026-09-20 updated: the memory sentence in the first paragraph; Language and Style leave the Render for the children rule-language and rule-agent-writing, marker lines in their place (case 272.1) · [[decision-case-272.1]]
- 2026-09-20 child rule-language added · [[decision-case-272.2]]
- 2026-09-20 child rule-agent-writing added · [[decision-case-272.3]]
- 2026-09-20 updated: the Case protocol leaves CLAUDE.md — no marker, no import of the schema; the glossary stays; children rule-language and rule-agent-writing (case 273.3) · [[decision-case-273.3]]
- 2026-09-20 status: built → draft · cascade
