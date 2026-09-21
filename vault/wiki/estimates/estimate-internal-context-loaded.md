---
type: estimate
kind: QA
status: pending
target: "[[rule-internal-context]]"
purpose: The text of sprint.md, brief.md, case-schema.md and glossary.md is present in the first turn's context after /hi, without a read call
method: one reading at the /hi of a session, by hand
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Criterion

Given:
The `purpose` of an Estimate is the line the index is built from, not the Criterion; `set.purpose` changes no promise.
**＋** An `update` of a rule's Purpose touches no Estimate (187).
**＋** The Criterion of `estimate-generate-ticks-the-spec` is 286's, of `estimate-internal-context-loaded` 288.1's, both `pending`.

When:
Someone reads the index line of an Estimate, or the Purpose of `rule-case-protocol`.

Then:
The `purpose` of `estimate-generate-ticks-the-spec`: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading across the Specs of raw/ — never a line of a later or a superseded Case. The `purpose` of `estimate-internal-context-loaded`: the text of sprint.md, brief.md, case-schema.md and glossary.md is present in the first turn's context after /hi, without a read call. The Purpose of `rule-case-protocol`: "loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md` (cases 273.1, 288.1)".
**－** The Criterion and the `status` do not change.

## Result

2026-09-20, the /hi of session 1749 read by hand: sprint.md, brief.md and case-schema.md present in the first turn in that order, expanded by the @ lines of the SKILL, no read call; the glossary through CLAUDE.md

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-20 updated: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three texts expanded, case-schema.md the third (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L1
- 2026-09-21 updated: the Criterion replaced whole — four texts expanded, glossary.md the fourth (case 288.1) · [[decision-case-288.1]]
- 2026-09-21 updated: the purpose by the Criterion of 288.1 (case 290.3) · [[decision-case-290.3]]
