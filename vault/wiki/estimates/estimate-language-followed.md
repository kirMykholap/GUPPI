---
type: estimate
kind: QA
status: passed
target: "[[rule-language]]"
purpose: The section stands in CLAUDE.md with the languages set in rule-guppi-config, and what a session writes into the repository is in the documentation language, slugs and paths unchanged
method: "by hand, after the close of a session: CLAUDE.md against the Render of rule-guppi-config, and the commit, the Spec and the Case files of that session against the section"
checked: 2026-09-28
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, workflow]
core: true
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

2026-09-28, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
