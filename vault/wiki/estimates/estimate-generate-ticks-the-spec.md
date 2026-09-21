---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading across the Specs of raw/ — never a line of a later or a superseded Case
method: pytest tests/test_generate.py with a Spec beside the yaml, plus one reading of this session's spec.md after the librarian's run
checked: 2026-09-20
origin: raw/2026-09-17/1119/ledger.md#case-226.1
sprint: migration
created: 2026-09-17
tags: [harness, workflow, ledger]
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

2026-09-20, uv run pytest tests/test_generate.py green; live — the librarian's run of session 1749 (commit 3d445a6) read by git show: the three Specs changed in ticks only (1749 13 lines, 1308 6, 0958 1); the reading of estimate-case-protocol-loaded (yaml line 6) skipped the read lines of 278 (first decision entry line 7) and 279.1 (line 9) in the 1749 Spec and ticked 1308:98, 1749:88 open; estimate-documentation-completes ticked 0958:308; lines 1-4 and 21 ticked 1308:627, 259, 1090, 367, 313; the folded create of 279.2 ticked 1749:129; the reading of estimate-retro-loads (line 20) ticked 1749:220 under 282, whose entries stand at 17-18, before it, and left 1308:132 open — by the rule of 280

## History

- 2026-09-18 created · [[decision-case-226.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L13
- 2026-09-20 updated: the Criterion replaced whole — an estimate entry and a create with a folded reading tick the read line, across the Specs of raw/ (case 270.1) · [[decision-case-270.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L53
- 2026-09-20 updated: the Criterion replaced whole — the read line of a later Case of the same unit is skipped by the ledger line numbers (case 280) · [[decision-case-280]]
- 2026-09-21 status: pending → passed · raw/2026-09-20/2106/ledger.md#L2
- 2026-09-21 updated: the Criterion replaced whole — the read line of a superseded Case is skipped by the marks of the yaml beside the Spec (case 286) · [[decision-case-286]]
- 2026-09-21 updated: the purpose by the Criterion of 286 (case 290.3) · [[decision-case-290.3]]
