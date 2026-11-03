---
type: estimate
kind: QA
status: passed
target: "[[rule-ratification]]"
purpose: The one rule, the form of the ledger lines, atomicity and the harness are present in a session from the first turn after /hi, as one text, the Render of rule-ratification, repeated in no other file the session holds
method: uv run --project .guppi guppi render --check; by hand at a /hi of a later session, vault/wiki/ratification.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and orchestration.md
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness]
core: true
---

## Criterion

When:
`/hi` opens a session after `uv run --project .guppi guppi render` wrote `vault/wiki/ratification.md` from `rule-ratification`.

Then:
The context of the session holds `vault/wiki/ratification.md` from the first turn after `/hi`, expanded by `.claude/skills/hi/SKILL.md` with no read call.
**＋** `uv run --project .guppi guppi render --check` exits 0: the file equals the Render of `rule-ratification`, the text of `rule-atomicity` between its markers.
**＋** The file opens with the one rule and holds the form of the ledger lines, atomicity and the harness.
**－** `CLAUDE.md`, `vault/wiki/case-schema.md` and `vault/wiki/orchestration.md` repeat no paragraph of `vault/wiki/ratification.md`.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
