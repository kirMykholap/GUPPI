---
type: estimate
kind: QA
status: passed
target: "[[rule-ratification]]"
purpose: The one rule, the form of the ledger lines, atomicity and the harness are present in a session from the first turn after /hi, as one text, the Render of rule-ratification, repeated in no other file the session holds
method: uv run guppi render --check; by hand at a /hi of a later session, vault/wiki/ratification.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and orchestration.md
checked: 2026-10-02
origin: raw/2026-10-02/1834/ledger.md#case-595.3
sprint: migration
created: 2026-10-02
tags: [session, harness]
---

## Criterion

When:
`/hi` opens a session after `uv run guppi render` wrote `vault/wiki/ratification.md` from `rule-ratification`.

Then:
The context of the session holds `vault/wiki/ratification.md` from the first turn after `/hi`, expanded by `.claude/skills/hi/SKILL.md` with no read call.
**＋** `uv run guppi render --check` exits 0: the file equals the Render of `rule-ratification`, the text of `rule-atomicity` between its markers.
**＋** The file opens with the one rule and holds the form of the ledger lines, atomicity and the harness.
**－** `CLAUDE.md`, `vault/wiki/case-schema.md` and `vault/wiki/orchestration.md` repeat no paragraph of `vault/wiki/ratification.md`.

## Result

2026-10-02, the /hi of session 2049: `uv run guppi render --check` exit 0; vault/wiki/ratification.md in the first turn's context, expanded by the @ line of .claude/skills/hi/SKILL.md, no read call of the agent; it opens with the one rule and holds the ledger line form, the text of rule-atomicity between its markers and the harness; the same paragraph comparison script printed 0 shared paragraphs with CLAUDE.md, orchestration.md and case-schema.md

## History

- 2026-10-02 created · [[decision-case-595.3]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L2
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
