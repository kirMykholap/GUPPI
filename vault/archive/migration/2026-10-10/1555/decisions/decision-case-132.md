---
type: decision
case: "132"
status: archived
update: ["[[rule-retro-commit]]", "[[rule-event-log]]", "[[rule-harness]]", "[[rule-retro]]", "[[rule-brief]]", "[[rule-ledger-tail]]"]
origin: raw/2026-09-14/1029/ledger.md#case-132
sprint: migration
created: 2026-09-14
tags: [session, workflow, hooks, harness, git, render, librarian, ledger]
---

## Context

`ask-guppi` read the plan whole (the dispatch of case 128). Its findings: (1) `sections: Language` in 123 — `## Language` lies inside the Render markers of `rule-claude-md`; `split_sections` gives it to the Render block, a `sections` entry would add a second section and `CLAUDE.md` would not change. (2) The `old` of 124.2, "a `defer` marks its target `deferred_by`", came from the docstring of `generate.py`; the page has no such phrase; the whole 124.2 entry would fail. (3) `sections: Addressed by` in 124.2 is an Insight section, not a Rule one; the Rule page would gain a stray section. (4) 122 leaves `rule-retro-commit` false: "Any other skill or tool: exit 0". (5) 122 and 125 give the event log a second job while `rule-event-log` says "Its one governance job is to carry the `hi` mark". (6) 130.1 said "`generate` takes it no more" — wrong: `generate` skips `applied` only; 112.6 fails once more in the librarian's run (a flag), then `archive` moves `0747` on `superseded_by`. (7) `rule-harness` Purpose: "Two more belong here and run in no pipeline" — three after 127. (8) `rule-retro` Purpose: "a line of today's ledger" — 109.1 promised "this session's", the page did not change. (9) `rule-brief` Purpose: "every deferred item lives on as a draft page" — an Insight in Deferred is no draft page. (10) `rule-ledger-tail` names `/hi` alone; 126 adds `/retro`.

## Problem

Four amendments touch blocks already signed; they cannot change silently. Six pages need new `update` entries, all `contract: same`: no contract changes, the text that became false does.

## Given

Every `old` text below was checked on its page (`rule-retro-commit` 28, `rule-event-log` 22–23, `rule-harness` 20–22, `rule-retro` 24, `rule-brief` 21–22, `rule-ledger-tail` 19, `rule-claude-md` 73–75, `rule-page-generation` 44 and 51).
**＋** `rule-retro-commit`: `estimate-retro-commit-gates` says "another skill or another tool, exit 0 whatever the tree" — on the tree that stays true; the refusal of 122 is on another ground; `contract: same`.
**＋** `rule-event-log`, `rule-retro`, `rule-brief` already get an `update` in this session (125, 126, 124.1) — a second entry on a page in ledger order, allowed; `rule-page-generation` gets a block amendment, not a new entry.
**－** No new Estimate block: no `when` or `then` changes.

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-132
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
