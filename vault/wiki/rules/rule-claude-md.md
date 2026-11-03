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
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render]
core: true
---

## Purpose

Prevents the system prompt from holding a line nobody ratified. `CLAUDE.md` is the
one file every session reads first. The file is the Render of this page, whole, with `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` spliced into their markers; a change to it is an `update` of one of the four. The Render holds the description of the project and the three children; the glossary, `orchestration.md` and `ratification.md` arrive with `/hi`, the one rule opens `ratification.md`, and the Case schema reaches `case-guppi` alone. The heading and the description of the project stand between the lines `<!-- project-description -->` and `<!-- /project-description -->`: in the clean version of GUPPI a heading and a line that says the description is not set yet stand there, until the setup Case of a project writes its own description.

## Render

<!-- rule-claude-md -->
<!-- project-description -->
# Project

Project description: not set yet.
<!-- /project-description -->

The vault is `vault/`; its terms are `vault/wiki/glossary.md`. A working session opens with `/hi`.

<!-- rule-language -->

<!-- rule-agent-writing -->

<!-- rule-one-judgment-one-implementation -->
<!-- /rule-claude-md -->

## How it works

Rendered in full into `CLAUDE.md`; each child — `rule-language`, `rule-agent-writing`, `rule-one-judgment-one-implementation` — splices into its marker line. The file is the system prompt of every session and of every subagent, so it holds what each of them needs and no more: the description of the project and the three standing rules. The glossary, `orchestration.md` and `ratification.md` arrive with `/hi` through `rule-internal-context`, and the one rule opens `ratification.md`. `rule-language` and `rule-agent-writing` have this page as their parent.

## History

- 2026-11-03 shipped with GUPPI
