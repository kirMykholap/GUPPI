---
type: entity
kind: MOC
purpose: GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub
status: built
children: ["[[entity-sprint]]", "[[entity-glossary]]"]
estimates: ["[[estimate-guppi-tests-green]]"]
rules: ["[[rule-harness]]"]
code_ref: [.guppi/guppi/, .claude/]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Purpose

GUPPI: a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of GUPPI that are not rules. In the repository of GUPPI itself, a third part is that repository on GitHub, `entity-guppi-repository`, whose rules are its own; the clean version of GUPPI does not hold that page. `rule-harness` is its guard: the tools of the harness kept equal to the pages that describe them. In a project that uses GUPPI, this page stands beside the root of the product and keeps GUPPI's own machinery apart from it.

## History

- 2026-11-03 shipped with GUPPI
