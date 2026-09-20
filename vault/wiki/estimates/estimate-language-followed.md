---
type: estimate
kind: QA
status: pending
target: "[[rule-language]]"
purpose: The section stands in CLAUDE.md and a session follows it — English in the repository, Russian in the chat, slugs and paths unchanged
method: one reading by hand in the next session — the section in CLAUDE.md, the session's commit, Spec and chat against it
origin: raw/2026-09-20/1308/ledger.md#case-272.2
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

Given:
The conditions of the parent.
**＋** `rule-language` is a Leaf, `enforcement: render`, `render_mode: partial`, `governs: CLAUDE.md`, a child of `rule-claude-md`; its Render is the section `## Language` inside the marker `<!-- rule-language -->`.

When:
A session starts with `CLAUDE.md`, and the agent writes — into the repository or into the chat.

Then:
Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the Spec — is English; the chat with the owner is Russian, a Case is discussed in the chat in Russian in all its sections and enters the Spec translated.
**＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
**－** The rule speaks of the language, not of the Case form — the form is `case-schema.md`.

## History

- 2026-09-20 created · [[decision-case-272.2]]
