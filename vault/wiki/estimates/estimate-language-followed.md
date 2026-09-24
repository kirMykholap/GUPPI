---
type: estimate
kind: QA
status: pending
target: "[[rule-language]]"
purpose: The section stands in CLAUDE.md and a session follows it — English in the repository, Russian in the chat, slugs and paths unchanged
method: one reading by hand in the next session — the section in CLAUDE.md, the session's commit, Spec and chat against it
checked: 2026-09-20
origin: raw/2026-09-20/1308/ledger.md#case-272.2
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

When:
A session starts with `CLAUDE.md`, and the agent writes into the repository or into the chat.

Then:
Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec — is English.
**＋** The chat with the owner is Russian: the name of a Case, its `context`, `problem` and `recommend`, and the agent's own text.
**＋** A Case's `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat and enter the Spec unchanged.
**＋** The name, `context` and `problem` are translated into English in the Spec before its approval.
**＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
**－** The rule speaks of the language, not of the Case form — the form is `vault/wiki/case-schema.md`.

## Result

2026-09-20, CLAUDE.md lines 41–45, commit 3f53aa6, raw/2026-09-20/1749/spec.md, frontier.md and the chat of session 1749 read by hand: the section stands in its marker; the commit message, the Spec, the frontier, the code and its docstrings are English; the chat with the owner is Russian, every Case discussed there in Russian in all its sections and entered into the Spec in English; slugs, field names, ledger lines, paths and the quoted replace strings unchanged in both; no technical term transliterated

## History

- 2026-09-20 created · [[decision-case-272.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L21
- 2026-09-24 updated: the Criterion replaced whole — given, when, then and tasks English in the chat (case 387.1) · [[decision-case-387.1]]
