---
type: entity
kind: MOC
purpose: GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint, the glossary and the graph of the links between pages and harness files, and in the repository of GUPPI also that repository on GitHub
status: built
children: ["[[entity-sprint]]", "[[entity-glossary]]", "[[entity-guppi-repository]]", "[[entity-link-graph]]"]
estimates: ["[[estimate-guppi-tests-green]]"]
rules: ["[[rule-harness]]"]
code_ref: [.guppi/guppi/, .claude/]
origin: raw/2026-09-22/0014/ledger.md#case-306.2
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
core: true
---

## Purpose

GUPPI: a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. Its parts are the sprint as a kind (`entity-sprint`), the glossary (`entity-glossary`) and the graph of the links between the pages and the harness files (`entity-link-graph`), the things of GUPPI that are not rules (as set in case 967.1). In the repository of GUPPI itself, a third part is that repository on GitHub, `entity-guppi-repository`, whose rules are its own; the clean version of GUPPI does not hold that page (as set in case 795.1). `rule-harness` is its guard: the tools of the harness kept equal to the pages that describe them. In a project that uses GUPPI, this page stands beside the root of the product and keeps GUPPI's own machinery apart from it (as set in case 306.2).

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
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 updated: GUPPI is described as a harness and a vault, true in any project that uses it · [[decision-case-822.7]]
- 2026-10-31 defer by decision-case-616 superseded · [[decision-case-955]]
- 2026-10-31 updated: the question of the future shape of GUPPI is settled by the sprint plugin: GUPPI goes on as a harness and ships as a Claude Code plugin · [[decision-case-955]]
- 2026-10-31 estimate estimate-guppi-keeps-no-defer-of-its-shape added · [[decision-case-955]]
- 2026-10-31 status: built → draft · cascade
- 2026-10-31 status: draft → built · cascade
- 2026-10-31 child entity-link-graph added · [[decision-case-967.1]]
- 2026-10-31 updated: the graph of the links between pages and harness files is a part of GUPPI · [[decision-case-967.1]]
- 2026-10-31 estimate estimate-guppi-keeps-no-defer-of-its-shape archived · cleanup
