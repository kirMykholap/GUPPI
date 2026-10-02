---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: What the main agent alone does is present in a session from the first turn after /hi, as one text, the Render of rule-orchestration, repeated in no other file the session holds
method: uv run guppi render --check; by hand at the first /hi of a later session after the render, vault/wiki/orchestration.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and ratification.md
origin: raw/2026-10-02/1834/ledger.md#case-595.2
sprint: migration
created: 2026-10-02
tags: [session, harness]
---

## Criterion

When:
`/hi` opens a session after `uv run guppi render` wrote `vault/wiki/orchestration.md` from `rule-orchestration`.

Then:
The context of the session holds `vault/wiki/orchestration.md` from the first turn after `/hi`, expanded by `.claude/skills/hi/SKILL.md` with no read call.
**＋** `uv run guppi render --check` exits 0: the file equals the Render of `rule-orchestration`, its language placeholders filled from `rule-guppi-config`.
**＋** The file holds what the main agent alone does: the Frontier and Plan Mode, the dispatch of `case-guppi`, the showing and the signing of a Case, the moment each ledger line is written, the short form of a defer and the acknowledging reply.
**－** `CLAUDE.md`, `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` repeat no paragraph of `vault/wiki/orchestration.md`.

## History

- 2026-10-02 created · [[decision-case-595.2]]
