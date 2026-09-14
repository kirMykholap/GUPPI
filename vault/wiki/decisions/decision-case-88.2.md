---
type: decision
case: "88.2"
status: current
update: ["[[rule-claude-md]]", "[[estimate-claude-md-rendered]]"]
supersedes: ["[[decision-case-84]]"]
origin: raw/2026-09-12/ledger.md#case-88.2
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Context

Both render readings failed in session J on their wording, not on the code. The live
half of `estimate-render-harness-reproduces` asks for a `git diff --stat` of the two
dropped marker lines of `hi/SKILL.md`; the live half of `estimate-claude-md-rendered`
asks the first render to leave a diff of marker lines only. Both were written in the Plan
Mode of session I against the tree as it stood; the librarian's run of the same session
wrote the text of cases 59.2, 59.5, 59.6, 62 and 66 into the Rule pages, and the render
of session J moved six files and 37 lines. Case 84 deferred the repair here.

## Problem

A live clause that describes one past state of the tree goes stale at the first change of
a page. Both have to say a standing rule, read against the pages that changed.

## Given

In both pages the stale sentence sits in the prose of `## Criterion`, not in a
`### case N` block: both Estimates are older than the derived-Criterion scheme of case
72. A `{supersedes:case N}` removes a block, so it cannot reach them; only an explicit
`replace` on the Estimate page can.
**＋** `estimate-render-harness-reproduces` is `failed`, its target `rule-render-harness`
(Leaf, `draft`, first Estimate). `estimate-claude-md-rendered` is `pending`, its target
`rule-claude-md` (MOC, `draft`, one Estimate). Both Rule pages carry
`deferred_by: [decision-case-84]`.
**＋** The unit halves of both criteria hold: `tests/test_render.py` is green. Only the
live half breaks.
**＋** Case 85.1 of this Spec already sets `estimate-render-harness-reproduces` `pending`
with a block of its own; the block of 88.1 sits beside it and says another thing — one is
the bare splice into a file that holds no comment, the other is what a render leaves in
the tree.
**＋** This is the class of
`insight-workflow-contract-change-leaves-its-derived-text-stale` (severity 3): the
contract moves and the derived text stays. Case 72 closed it for criteria born after it;
these two are older.
**－** The reading is taken in this session: Work Mode runs `uv run guppi render` for
85.2 anyway.

## Criterion

- [[estimate-claude-md-rendered]] § case 88.2

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-88.2
