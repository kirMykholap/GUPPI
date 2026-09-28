---
type: estimate
kind: QA
status: passed
target: "[[rule-language]]"
purpose: The section stands in CLAUDE.md with the languages set in rule-guppi-config, and what a session writes into the repository is in the documentation language, slugs and paths unchanged
method: one reading by hand in the next session — CLAUDE.md against the Render of rule-guppi-config, and the session's commit, Spec and Case files against the section
checked: 2026-09-28
origin: raw/2026-09-20/1308/ledger.md#case-272.2
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

When:
The render writes `CLAUDE.md` from `rule-language` and the Render of `rule-guppi-config`, and a session writes into the repository.

Then:
`CLAUDE.md` holds the `## Language` section of `rule-language`, with the names of the languages that `rule-guppi-config` sets as `documentation_lang` and `chat_lang` where its Render holds the placeholders.
**＋** Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec in `raw/<date>/<hi HHMM>/spec.md` — is in `documentation_lang`.
**＋** A Case built by `case-guppi` is in `documentation_lang` whole — its name, `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks` and `ratification` — in `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and its name, `context` and `problem` are in `documentation_lang` in `raw/<date>/<hi HHMM>/spec.md`.
**＋** Its `given`, `when`, `then` and `tasks` enter `raw/<date>/<hi HHMM>/spec.md` unchanged.
**＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language.
**－** The language of the agent's own text in the chat is not read: a reply in a language other than `chat_lang` is not a failure of this promise.
**－** The rule speaks of the language, not of the Case form: the form is `vault/wiki/case-schema.md`.

## Result

2026-09-28, by hand, session 2000: CLAUDE.md names English and Russian in `## Language`; commit cb12283, raw/2026-09-28/2000/spec.md and cases/case-482..485.md are English, and prespec --check printed no language finding; every given, when and then line of the four Case files stands unchanged in spec.md (17, 20, 91, 77 lines, 0 missing)

## History

- 2026-09-20 created · [[decision-case-272.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L21
- 2026-09-24 updated: the Criterion replaced whole — given, when, then and tasks English in the chat (case 387.1) · [[decision-case-387.1]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L37
- 2026-09-27 updated: the Criterion replaced whole — the name, context and problem are English in the Spec with no translation step since Case 441; a short-form Case is English in the chat (case 446) · [[decision-case-446]]
- 2026-09-27 updated: the Criterion replaced whole — a built Case English whole in its file, a short Russian text in the chat (case 452.5) · [[decision-case-452.5]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/0000/ledger.md#L31
- 2026-09-28 updated: the Criterion replaced whole — the languages come from rule-guppi-config, and the language of the agent's text in the chat leaves the promise (case 476.4) · [[decision-case-476.4]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L20
