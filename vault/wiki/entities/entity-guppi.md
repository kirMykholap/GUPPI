---
type: entity
kind: MOC
purpose: GUPPI as the thing this repository builds — the harness and the vault it keeps; its parts the sprint, the glossary and the repository of GUPPI on GitHub
status: built
children: ["[[entity-sprint]]", "[[entity-glossary]]", "[[entity-guppi-repository]]"]
estimates: ["[[estimate-guppi-tests-green]]"]
rules: ["[[rule-harness]]"]
deferred_by: ["[[decision-case-616]]"]
code_ref: [guppi/, .claude/]
origin: raw/2026-09-22/0014/ledger.md#case-306.2
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
core: true
---

## Purpose

GUPPI as the thing this repository builds: a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. Its parts the person named: the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules, and the repository of GUPPI on GitHub (`entity-guppi-repository`), whose rules are its own (case 795.1). `rule-harness` is its guard: the tools of the harness kept equal to the pages that describe them. In a developer's vault this page stands beside the root of the product and keeps GUPPI's own machinery apart from it (case 306.2).

## History

- 2026-09-22 created · [[decision-case-306.2]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-22 rules: [rule-harness] · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-03 deferred · [[decision-case-616]]
- 2026-10-13 child entity-guppi-repository added · [[decision-case-795.1]]
- 2026-10-13 updated: the repository of GUPPI on GitHub is a part (case 795.1) · [[decision-case-795.1]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
