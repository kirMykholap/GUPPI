---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: The form of a Case stands in one text, the Render of rule-case-protocol, which /hi does not load and the main agent does not read, with nothing of orchestration.md or ratification.md repeated in it and nothing of it repeated in CLAUDE.md
method: uv run --project .guppi guppi render --check; by hand after the librarian's render, case-schema.md, orchestration.md and ratification.md compared paragraph by paragraph, and at the first /hi of a later session the first turn's context and the main agent's read calls in the transcript
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi render` wrote `vault/wiki/case-schema.md` from `rule-case-protocol`, and a session opened by `/hi` dispatches `case-guppi` by `.claude/agents/case-guppi.md`.

Then:
`uv run --project .guppi guppi render --check` exits 0: the file equals the Render of `rule-case-protocol`, its language placeholders filled from `rule-guppi-config`.
**＋** The file holds the form of a Case: its sections, operands and language, the `then` block, the task lines, the taking up of a deferred decision, the sub-cases and the slug.
**＋** `.claude/skills/hi/SKILL.md` holds no `@` line for `vault/wiki/case-schema.md`, and the main agent reads none of it in the session.
**－** The file repeats no paragraph of `vault/wiki/orchestration.md` or `vault/wiki/ratification.md`, and `CLAUDE.md` repeats none of its paragraphs.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
