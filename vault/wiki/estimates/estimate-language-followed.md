---
type: estimate
kind: QA
status: pending
target: "[[rule-language]]"
purpose: The section stands in CLAUDE.md and a session follows it — English in the repository, Russian in the chat, slugs and paths unchanged
method: one reading by hand in the next session — the section in CLAUDE.md, the session's commit, Spec and chat against it
checked: 2026-09-26
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
**＋** The chat with the owner is Russian: the name of a Case, its `context`, `problem` and `recommend`, and the agent's own text.
**＋** The name, `context` and `problem` of a Case are English in `raw/<date>/<hi HHMM>/spec.md`.
**＋** A Case's `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat and enter `raw/<date>/<hi HHMM>/spec.md` unchanged.
**＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
**－** A short-form Case of `vault/wiki/case-schema.md` is not Russian in the chat: it stands there in English, as `raw/<date>/<hi HHMM>/spec.md` holds it.
**－** The rule speaks of the language, not of the Case form — the form is `vault/wiki/case-schema.md`.

## Result

2026-09-26, CLAUDE.md lines 5–9, commit 54509ed, the diff, raw/2026-09-26/1745/spec.md and the chat of session 1745 read by hand; the repository is English (spec.md 0 Cyrillic lines of 677), but Case 441 was shown in the chat with its name, context, problem and recommend in English, and the agent's own Russian text transliterates hook, commit, skill, insight and Case

## History

- 2026-09-20 created · [[decision-case-272.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L21
- 2026-09-24 updated: the Criterion replaced whole — given, when, then and tasks English in the chat (case 387.1) · [[decision-case-387.1]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L37
- 2026-09-27 updated: the Criterion replaced whole — the name, context and problem are English in the Spec with no translation step since Case 441; a short-form Case is English in the chat (case 446) · [[decision-case-446]]
