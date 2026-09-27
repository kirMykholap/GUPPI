---
type: rule
kind: Leaf
purpose: Keeps the repository in English and the chat with the owner in Russian, a built Case English whole in the file sent to the person, with slugs, paths and quotations unchanged in either
status: draft
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: ["[[estimate-language-followed]]", "[[estimate-language-spec-prose-in-english]]"]
origin: raw/2026-09-20/1308/ledger.md#case-272.2
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Purpose

Keeps the repository in English and the chat with the owner in Russian. Until case 272 the
rule was a section of the Render of `rule-claude-md`: a standing condition with no page and
no Estimate. A Case is discussed in Russian and read in English, whole, in the file the agent sends the person (cases 123, 387.1, 452.5); the
manner of the English that lands in the vault — ASD-STE100 Simplified Technical English —
is the `## Language` section of `case-schema.md`, which this rule does not repeat.

## Render

<!-- rule-language -->
## Language

English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner; a Case is English whole — its name, `context`, `problem` and `recommend` too — in the file the agent sends the person and in the Spec, and the chat holds a short Russian text on each Case and sub-case, its ledger lines in English as the file holds them; a short-form Case is English in the chat, as the Spec holds it. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic.
<!-- /rule-language -->

## History

- 2026-09-20 created · [[decision-case-272.2]]
- 2026-09-20 estimate estimate-language-followed added · [[decision-case-272.2]]
- 2026-09-20 status: draft → built · cascade
- 2026-09-24 updated: a Case's given, when, then and tasks are English in the chat (case 387.1) · [[decision-case-387.1]]
- 2026-09-24 status: built → draft · cascade
- 2026-09-27 estimate estimate-language-spec-prose-in-english added · [[decision-case-445.4]]
- 2026-09-27 updated: the prose of a Case is Russian in the chat and English in the Spec, with no translation step before approval since Case 441; a short-form Case is English in the chat (case 446) · [[decision-case-446]]
- 2026-09-27 updated: a built Case is English whole in the file sent to the person; the chat holds a short Russian text and the ledger lines (case 452.5) · [[decision-case-452.5]]
