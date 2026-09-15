---
type: rule
kind: MOC
purpose: Prevents the system prompt from holding a line nobody ratified
status: built
enforcement: render
governs: CLAUDE.md
render_mode: full
parent: "[[rule-harness]]"
children: ["[[rule-case-protocol]]"]
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
(case 56). Now the file is the Render of this page, whole, with the Case protocol
spliced from `rule-case-protocol`; a change to it is an `update` of one of the two. The Render imports [[glossary]] and [[case-schema]] and points at [[index]].

## Render

<!-- rule-claude-md -->
# GUPPI

A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into.
The vault is `vault/`; its map is `vault/wiki/index.md`. Nothing in the vault or the codebase
changes without a Decision ratified by the human. You have full autonomy over *how* to
implement something once its contract is ratified, and none over the contract itself. When you
are unsure whether something needs ratification: it does.

## What is loaded here

The glossary and the Case schema arrive through the imports below, so the terms and the shape
of a Case are present from the first turn without a read.

@vault/wiki/glossary.md

@vault/wiki/case-schema.md

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

<!-- rule-case-protocol -->

## Language

English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic.

## Style

Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
sentences, active voice, a common word over a term. Give the answer first. Say what is done
and what is not done; never leave the not-done implied.

## Commands

`make help` lists the targets. `make style` must be clean before every commit. Add no new
dependencies, Python or otherwise.
<!-- /rule-claude-md -->

## How it works

Rendered in full into `CLAUDE.md`; `rule-case-protocol` splices into its marker. The
`@` lines are text here and imports for Claude Code. The section "Migration mode"
is carried from the hand-written file as it stood on 2026-09-12 and leaves with the
migration, by an `update` of this page. `rule-case-protocol` has this page as its parent since case 66 and is its one child; the renderer splices it into the marker.

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
