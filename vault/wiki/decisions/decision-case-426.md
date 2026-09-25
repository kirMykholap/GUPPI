---
type: decision
case: "426"
status: current
update: ["[[rule-prespec]]", "[[estimate-prespec-matches-lines-and-items]]"]
origin: raw/2026-09-25/1654/ledger.md#case-426
sprint: migration
created: 2026-09-25
tags: [session, workflow, harness]
---

## Context

`materialize` finds the item of a `then` block for a ledger line with the function `find_item`. The function searches by the kind of decision and the slug and takes the first item it finds. A ledger line answers one item. When a second item of the same kind and slug stands under one Case, `materialize` does not read it and marks nothing. So in Case 419.2 the second `update` of the page `rule-frame-check` was lost, the one that carried the `rename`. The Case schema asks for one item per target in each kind of decision. But no check refuses the second item.
The checks of the plan's lines and items are one module, `judge` in `guppi/prespec.py`; the comparison with the ratified copy runs outside it, in `check`. `guppi casecheck --subagent` on `SubagentStop` builds a Spec in memory from the answer of `case-guppi` and runs `judge`. That is the earliest place where the `then` block is seen: before the Case is shown to the person. After the ratification the `Stop` hook `guppi ratified` runs `judge` on each written Case. Then `/pre-spec` runs it. So the check goes into `check_lines` inside `judge`, and all three places get it by import. In `judge` the `then` block comes from `then_blocks`, which joins all fences tagged `then` of one Case. So the second item is found in another fence too. A separate check in `read_tasks` of `guppi/ratified.py` would see only the chat form. It would be a second copy of one judgment.
What the frame check showed. The Render of `rule-prespec` lists all findings of `--check`. Without the new finding that list becomes incomplete, so the Case changes the Render by one `replace` pair. That wording stands in the Render once. The Criterion of `estimate-prespec-matches-lines-and-items` speaks of the match of ledger lines and items, and that is exactly what the Case changes. So its Criterion is replaced whole by the `when` and `then` of this Case. The Criterion of `estimate-prespec-checks-the-form-of-an-item` speaks of the form of an Estimate item. The Criteria of `estimate-case-check-sends-back-a-faulty-case` and `estimate-spec-write-checks-the-written-case` speak of the findings of `judge` in general, of none in particular. These three are not touched. The Criterion of `estimate-generate-ticks-the-spec` says that two entries of one kind and slug in one Case tick two lines, in order: that stays true of `generate`, which does not change; after this Case such a pair no longer reaches it. The Purpose of `rule-case-check` and How it works of `rule-spec-write` say that the checks are imported. That stays true. The line of the schema "one entry per target" also stays true, and now it is checked. There is no `create` here, so no vault query is due.
What the Case does not do. `materialize` does not change: the Spec it reads has already passed `judge` three times. It reads older Specs as before. Whether they hold two items of one kind and slug, other than the Spec of session 1228, is not checked. To mark such an item in `materialize` is a separate promise of `rule-materialize`. If needed, that is a separate Case.

## Problem

Two items of one kind and slug can stand under one Case. No check refuses them, and `materialize` applies only the first without a word. It must be decided where and in what form a check refuses the second item.

## Given

`rule-prespec` — the rule of `/pre-spec`; its Render lists the findings of `uv run guppi prespec --check`
**＋** `.claude/skills/pre-spec/SKILL.md` — the file its Render writes
**＋** `estimate-prespec-matches-lines-and-items` — the promise that decision lines and items of the plan match
**＋** `guppi/prespec.py` — `judge` and its `check_lines`, which `guppi/casecheck.py` and `guppi/ratified.py` import
**＋** `tests/test_prespec.py` — the tests of `--check`
**＋** `tests/test_casecheck.py` — the tests of the check of an answer of `case-guppi` on `SubagentStop`
**＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — a `then` block holds one entry per target under each decision type

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-426
