---
type: rule
kind: MOC
purpose: Prevents the system prompt from holding a line nobody ratified
status: built
enforcement: render
governs: CLAUDE.md
render_mode: full
parent: "[[rule-harness]]"
children: ["[[rule-language]]", "[[rule-agent-writing]]", "[[rule-one-judgment-one-implementation]]"]
estimates: ["[[estimate-claude-md-rendered]]"]
origin: raw/2026-09-12/ledger.md#case-59.8
sprint: migration
created: 2026-09-12
tags: [harness, render]
core: true
---

## Purpose

Prevents the system prompt from holding a line nobody ratified. `CLAUDE.md` is the
one file every session reads first; until this page it was hand-written around one
rendered section, and a ratified sentence went into the file instead of the page
(case 56). Now the file is the Render of this page, whole, with `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` spliced into their markers; a change to it is an `update` of one of the four. The Render holds the description of the project and the three children; the glossary, `orchestration.md` and `ratification.md` arrive with `/hi`, the one rule opens `ratification.md`, and the Case schema reaches `case-guppi` alone (cases 272, 273.3, 288.3, 595).

## Render

<!-- rule-claude-md -->
# GUPPI

A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. The vault is `vault/`; its terms are `vault/wiki/glossary.md`. A working session opens with `/hi`.

<!-- rule-language -->

<!-- rule-agent-writing -->

<!-- rule-one-judgment-one-implementation -->
<!-- /rule-claude-md -->

## How it works

Rendered in full into `CLAUDE.md`; each child — `rule-language`, `rule-agent-writing`, `rule-one-judgment-one-implementation` — splices into its marker line. The file is the system prompt of every session and of every subagent, so it holds what each of them needs and no more: the description of the project and the three standing rules. The glossary, `orchestration.md` and `ratification.md` arrive with `/hi` through `rule-internal-context`, and the one rule opens `ratification.md` (cases 288, 595). `rule-language` and `rule-agent-writing` have this page as their parent (since case 272; the section "Migration mode", carried from the hand-written file of 2026-09-12, left with case 288.3, each of its items a Rule with a Render of its own by then, and "Commands" left with it — `make style` before a commit is `rule-retro`'s, and "no new dependencies" came with the file in case 59.8 and was never decided on its own; `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`).

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
- 2026-09-20 status: draft → built · cascade
- 2026-09-21 updated: the Render is the title, the description of the project and the two markers — the import, What is loaded here, the index paragraph, Migration mode and Commands leave; the one rule to the schema (case 288.3) · [[decision-case-288.3]]
- 2026-09-21 status: built → draft · cascade
- 2026-09-21 status: draft → built · cascade
- 2026-09-22 updated: CLAUDE.md names the glossary alone; the map is gone (case 318) · [[decision-case-318]]
- 2026-09-23 child rule-one-judgment-one-implementation added · [[decision-case-360]]
- 2026-09-23 updated: the third child rule-one-judgment-one-implementation, its marker in the Render (case 360) · [[decision-case-360]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-27 deferred · [[decision-case-454]]
- 2026-09-27 defer by decision-case-454 superseded · [[decision-case-459]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-02 updated: the texts that arrive with /hi are orchestration.md and ratification.md, the one rule opens ratification.md (case 595.4) · [[decision-case-595.4]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-02 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the history of the page stands in the bracket of its pointers · [[decision-case-809]]
