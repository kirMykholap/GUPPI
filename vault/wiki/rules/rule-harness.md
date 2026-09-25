---
type: rule
kind: MOC
purpose: Prevents the tools of the harness from drifting apart from the pages that describe them
status: draft
children: ["[[rule-render-harness]]", "[[rule-settings]]", "[[rule-lint]]", "[[rule-page-schemas]]", "[[rule-vault-layout]]", "[[rule-governed-files-hook]]", "[[rule-claude-md]]", "[[rule-bash-guard]]", "[[rule-tests-clock-pinned]]", "[[rule-context-size]]", "[[rule-page-read]]"]
estimates: ["[[estimate-harness-pipeline]]"]
applies_to: ["[[entity-guppi]]"]
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Purpose

Prevents the tools of the harness from drifting apart from the pages that describe
them. Three rules belong to no phase of the session: the renderer, the page
`.claude/settings.json` is assembled from, and lint. They run together in `make lint`, with the check of `rule-sprint` (a child of `rule-documentation`) between them, in this order: the harness files are checked against their pages, the sprint file against its page, the glossary file against its page, then the pages (cases 227, 306.5). Eight more belong here and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1).

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 estimate estimate-harness-pipeline added · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 child rule-governed-files-hook added · [[decision-case-59.6]]
- 2026-09-12 child rule-claude-md added · [[decision-case-59.8]]
- 2026-09-12 updated: two children outside the make lint pipeline — the guard hook and the CLAUDE.md page (case 66) · [[decision-case-66]]
- 2026-09-12 child rule-settings added · [[decision-case-85.2]]
- 2026-09-12 updated: rule-settings takes the slot of rule-hook-registry, which becomes its child (case 85.2) · [[decision-case-85.2]]
- 2026-09-12 updated: rule-settings takes the slot of the hook registry in the Purpose too (case 99) · [[decision-case-99]]
- 2026-09-14 child rule-bash-guard added · [[decision-case-127]]
- 2026-09-14 updated: the bash guard hook counted among the children outside the pipeline (case 132) · [[decision-case-132]]
- 2026-09-14 child rule-tests-clock-pinned added · [[decision-case-145.1]]
- 2026-09-14 updated: rule-tests-clock-pinned added (case 145.2) · [[decision-case-145.2]]
- 2026-09-14 updated: three rules in make lint, four outside it; the pipeline's Method without tests/test_index.py (case 153) · [[decision-case-153]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 child rule-index archived · cleanup
- 2026-09-15 status: draft → built · cascade
- 2026-09-18 updated: sprint --check joins make lint between render --check and lint (case 233.1) · [[decision-case-233.1]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-18 status: draft → built · cascade
- 2026-09-22 child rule-page-schemas added · [[decision-case-304.1]]
- 2026-09-22 updated: rule-page-schemas, the MOC of the six category schemas, after rule-lint (case 304.1) · [[decision-case-304.1]]
- 2026-09-22 updated: rule-harness is the guard of entity-guppi — the edge Rule → Entity (case 306.2) · [[decision-case-306.2]]
- 2026-09-22 status: built → draft · cascade
- 2026-09-22 child rule-vault-layout added · [[decision-case-315]]
- 2026-09-22 updated: rule-vault-layout, the layout of the vault, after rule-page-schemas (case 315) · [[decision-case-315]]
- 2026-09-22 updated: the glossary step of make lint and the fifth rule outside the pipeline (case 323) · [[decision-case-323]]
- 2026-09-23 status: draft → built · cascade
- 2026-09-24 child rule-context-size added · [[decision-case-392.1]]
- 2026-09-24 updated: the Purpose names the seven rules outside the pipeline (case 392.3) · [[decision-case-392.3]]
- 2026-09-24 status: built → draft · cascade
- 2026-09-25 child rule-page-read added · [[decision-case-420.1]]
- 2026-09-25 updated: the hooks of rule-page-read named among the rules outside the pipeline (case 420.2) · [[decision-case-420.2]]
