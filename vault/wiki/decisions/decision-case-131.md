---
type: decision
case: "131"
status: current
update: [rule-page-generation]
origin: raw/2026-09-14/1029/ledger.md#case-131
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

The `change` of the 114 entry in session M's Spec is the single word "the" (a truncated phrase); `generate` wrote `- 2026-09-14 updated: the · [[decision-case-114]]` into the History of `rule-page-generation` and into `log.md`. The `replace` of 114 applied; only History and `log.md` carry the fragment (brief, Flags).

## Problem

History is the record of what each Case did; the line "updated: the" says nothing. `replace` does not reach History (130), and "appended by hook, never by an agent" is the rule a one-off migration is the only way out of.

## Given

`rule-page-generation` (`Leaf`, `built`): already an `update` by 124.2 and 130.1 in this session — a third entry on one page in ledger order, allowed; line 118 of History is `- 2026-09-14 updated: the · [[decision-case-114]]`.
**＋** The `change` of 114 in `raw/2026-09-14/0747/spec.md` is not edited: the Spec is the record of what was signed.
**－** `log.md` is not a page and has no schema; it stays as it is.
**－** The Frontier line F10 closes on this Case; the rest of F10 is `work` and Slice 5.

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-131
