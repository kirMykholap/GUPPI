---
type: rule
kind: Leaf
purpose: Keeps the repository in English and the chat with the owner in Russian, with slugs, paths and quotations unchanged in either
status: draft
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: ["[[estimate-language-followed]]"]
origin: raw/2026-09-20/1308/ledger.md#case-272.2
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Purpose

Keeps the repository in English and the chat with the owner in Russian. Until case 272 the
rule was a section of the Render of `rule-claude-md`: a standing condition with no page and
no Estimate. A Case is discussed in Russian and enters the Spec in English (case 123); the
manner of the English that lands in the vault — ASD-STE100 Simplified Technical English —
is the `## Language` section of `case-schema.md`, which this rule does not repeat.

## Render

<!-- rule-language -->
## Language

English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic.
<!-- /rule-language -->

## History

- 2026-09-20 created · [[decision-case-272.2]]
- 2026-09-20 estimate estimate-language-followed added · [[decision-case-272.2]]
