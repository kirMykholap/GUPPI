---
type: estimate
kind: QA
status: failed
target: "[[rule-language]]"
purpose: The section stands in CLAUDE.md and a session follows it — English in the repository, Russian in the chat, slugs and paths unchanged
method: one reading by hand in the next session — the section in CLAUDE.md, the session's commit, Spec and chat against it
checked: 2026-09-28
origin: raw/2026-09-20/1308/ledger.md#case-272.2
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

When:
A session starts with `CLAUDE.md`, and the agent writes into the repository or into the chat.

Then:
Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec in `raw/<date>/<hi HHMM>/spec.md` — is English.
**＋** The chat with the owner is Russian: the short text on each Case and sub-case that goes with its file, the name in its heading, a round of questions of `case-guppi` translated from the answer, and the agent's own text.
**＋** A Case built by `case-guppi` is English whole — its name, `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks` and `ratification` — in `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and its name, `context` and `problem` are English in `raw/<date>/<hi HHMM>/spec.md`.
**＋** The ledger lines of a Case's `ratification` stand in the chat in English as the file holds them, and its `given`, `when`, `then` and `tasks` enter `raw/<date>/<hi HHMM>/spec.md` unchanged.
**＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
**－** A short-form Case of `vault/wiki/case-schema.md` is not Russian in the chat: it stands there in English, as `raw/<date>/<hi HHMM>/spec.md` holds it.
**－** The rule speaks of the language, not of the Case form: the form is `vault/wiki/case-schema.md`.

## Result

2026-09-28, by hand, session 0000: the reply that acknowledged Case 471 was written in English in the chat — the heading `## Case 471 — ratified`, the labels **Changes:** and **Notes:**, the text and the Frontier; the person asked "а почему ты перешел на английский в чате?"; the repository, the Cases and the Spec stayed English

## History

- 2026-09-20 created · [[decision-case-272.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L21
- 2026-09-24 updated: the Criterion replaced whole — given, when, then and tasks English in the chat (case 387.1) · [[decision-case-387.1]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L37
- 2026-09-27 updated: the Criterion replaced whole — the name, context and problem are English in the Spec with no translation step since Case 441; a short-form Case is English in the chat (case 446) · [[decision-case-446]]
- 2026-09-27 updated: the Criterion replaced whole — a built Case English whole in its file, a short Russian text in the chat (case 452.5) · [[decision-case-452.5]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/0000/ledger.md#L31
