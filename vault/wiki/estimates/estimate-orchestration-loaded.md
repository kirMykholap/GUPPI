---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: What the main agent alone does is present in a session from the first turn after /hi, as one text, the Render of rule-orchestration, repeated in no other file the session holds
method: uv run --project .guppi guppi render --check; by hand at a /hi of a later session, vault/wiki/orchestration.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and ratification.md
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness]
core: true
---

## Criterion

When:
`/hi` opens a session after `uv run --project .guppi guppi render` wrote `vault/wiki/orchestration.md` from `rule-orchestration`.

Then:
The context of the session holds `vault/wiki/orchestration.md` from the first turn after `/hi`, expanded by `.claude/skills/hi/SKILL.md` with no read call.
**＋** `uv run --project .guppi guppi render --check` exits 0: the file equals the Render of `rule-orchestration`, its language placeholders filled from `rule-guppi-config`.
**＋** The file holds what the main agent alone does: the Frontier and Plan Mode, the dispatch of `case-guppi`, the showing and the signing of a Case, the moment each ledger line is written, the short form of a defer and the acknowledging reply.
**－** `CLAUDE.md`, `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` repeat no paragraph of `vault/wiki/orchestration.md`.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
