---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: What the main agent alone does is present in a session from the first turn after /hi, as one text, the Render of rule-orchestration, repeated in no other file the session holds
method: uv run --project .guppi guppi render --check; by hand at a /hi of a later session, vault/wiki/orchestration.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and ratification.md
checked: 2026-10-02
origin: raw/2026-10-02/1834/ledger.md#case-595.2
sprint: migration
created: 2026-10-02
tags: [session, harness]
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

2026-10-02, the /hi of session 2049: `uv run guppi render --check` exit 0; vault/wiki/orchestration.md in the first turn's context, expanded by the @ line of .claude/skills/hi/SKILL.md, no read call of the agent; it holds Plan Mode and the Frontier, the dispatch of case-guppi, the showing and signing of a Case, the moment of each ledger line, the short form and the acknowledging reply; a paragraph comparison script over CLAUDE.md, orchestration.md, ratification.md and case-schema.md (blocks of 40 characters or more, headings and markers dropped) printed 0 shared paragraphs for each pair

## History

- 2026-10-02 created · [[decision-case-595.2]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L1
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
