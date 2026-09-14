---
type: decision
case: "130.1"
status: current
update: ["[[rule-page-generation]]"]
supersedes: ["[[decision-case-112.6]]"]
origin: raw/2026-09-14/1029/ledger.md#case-130.1
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

Entry 112.6 of `raw/2026-09-14/0747/materialize.yaml` is `failed`: the `replace` on `rule-page-generation` did not find its `old`. The reason: the text "History and log lines end with `· [[decision-case-N]]` when a decision exists" stands only in the History line of 2026-09-11 (line 95), and `generate.replace` skips History (`generate.py:519`); line 44 of the body is already in backticks, and lint does not count it (`CODE_SPAN`, `lint.py:57`). Seven `ref` findings of lint: the History line of `rule-page-generation` and the Given of `decision-case-112.1`–`112.6`, which quote the same line without backticks. The librarian repairs no yaml (rule-documentation); `archive` keeps `0747`: "1 entries not applied".

## Problem

The literal has to be quoted where `replace` does not reach — in History and in six decision pages; and the failed entry has to leave the count, or session M never moves into the archive. `mark_superseded` (`materialize.py:654`) marks `superseded_by` on the entries of its own yaml only.

## Given

`rule-page-generation` (`Leaf`, `built`, `estimate-generate-writes` `passed`; already an `update` by 124.2 in this session — a second entry on one page in ledger order, allowed): History is "appended by hook, never by an agent" — the hand edit of line 95 is ratified here as a one-off migration; the decision pages 112.1–112.6 quote the line in their Given without backticks, the same migration by hand; `decision-case-112.6` goes `superseded` by the cascade and into the archive.
**＋** `rule-materialize` (`Leaf`, `built`, `estimate-materialize-assembles`, `estimate-materialize-walks-dates` `passed`): "a later `supersedes` adds `superseded_by` to the earlier entry and changes nothing else" — today within one yaml only; `units_with(project_dir, "materialize.yaml")` already lists every yaml; `archive.kept_reason` takes `superseded_by` as done.
**＋** `rule-lint` is not changed: a code span is no ref already, a History ref is a ref, as designed (72.6).
**－** Entry 112.6 stays in the yaml as it is, with `failed` and `superseded_by`; `generate` skips `applied` entries only (`generate.py:815`), so the librarian's run of this session retries it, fails it once more — exit 1, a flag — and `archive` then moves `0747` on the `superseded_by` mark (pre-task finding 6 of case 132).
**－** The Frontier line F9 closes on this Case.

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-130.1
- 2026-09-14 updated: the quoted literal decision-case-N wrapped in backticks, a lint ref finding; no content change (case 140) · [[decision-case-140]]
