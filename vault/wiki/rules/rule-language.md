---
type: rule
kind: Leaf
purpose: Keeps the repository in the documentation language and the chat with the owner in the chat language, both set in rule-guppi-config, a built Case whole in the documentation language in the file sent to the person, with slugs, paths and quotations unchanged in either
status: built
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, render, workflow]
core: true
---

## Purpose

Keeps the repository in the documentation language and the chat with the owner in the chat language, `documentation_lang` and `chat_lang` set in `rule-guppi-config` and rendered into `guppi.toml` — English and Russian in this project. A Case is discussed in Russian and read in English, whole, in the file the agent sends the person; the
manner of the English that lands in the vault — ASD-STE100 Simplified Technical English —
is the `## Language` section of `case-schema.md`, which this rule does not repeat.

## Render

<!-- rule-language -->
## Language

{{documentation_lang}} for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. {{chat_lang}} for chat with the owner; a Case is {{documentation_lang}} whole — its name, `context`, `problem` and `recommend` too — in the file the agent sends the person and in the Spec, and the chat holds a short {{chat_lang}} text on each Case and sub-case, its ledger lines in {{documentation_lang}} as the file holds them; a short-form Case is {{documentation_lang}} in the chat, as the Spec holds it. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. Technical terms in {{documentation_lang}} are not transliterated in {{chat_lang}} text. The two languages are set in `rule-guppi-config`, rendered into `guppi.toml`.
<!-- /rule-language -->

## History

- 2026-10-14 shipped with GUPPI
