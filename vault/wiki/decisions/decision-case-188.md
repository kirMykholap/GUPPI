---
type: decision
case: "188"
status: current
create: ["[[estimate-case-protocol-case-form]]", "[[estimate-orchestration-acknowledging-reply]]", "[[estimate-ratification-ledger-line-form]]"]
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]", case-schema]
supersedes: ["[[decision-case-185]]"]
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Context

`rule-case-protocol` is a Leaf, `enforcement: render`, `governs: CLAUDE.md`,
`render_mode: partial`. Its Render is the "Case protocol" section of the system prompt —
the rule by which every Case is written. It carries one Estimate,
`estimate-case-protocol-loaded`, whose Criterion holds the head text and six `### case N`
blocks for six different actions, under one status and one `Result`. Case 185 deferred
this page to Slice 3d; this Case takes points 6, 7 and 9 of the model of 182. The vault
was asked: the three proposed slugs are free, and the `＋` line of block 144.1 belongs to
`estimate-claude-md-rendered`, so it is not carried over.

## Problem

The form of a Case makes the contract be written in two places and two shapes. `given`
collects the state of pages mixed with the conditions of the behaviour, while the Criterion
is built from `when` and `then` alone — so half of what is written never reaches the
promise. `tasks` carries `contract` and "block N" lines, the script's bookkeeping, which
the person signs without being able to check it. A `create` carries `method`,
`estimate_kind` and `estimate_slug` — three keys to derive an Estimate that point 9 says to
name outright. And this page's `## How it works` is a third copy of the promise beside the
Render.

## Given

The Criterion of `estimate-case-protocol-loaded` is the head text plus six blocks — 73.9,
75.1, 86, 144.1, 159, 167; its `Result` speaks only of 167.
**＋** the head text requires `method` on a `create` and block 86 requires `estimate_kind`
and `estimate_slug`; point 9 removes both.
**＋** block 73.9 has the same `when` as the head text: a session starts with `CLAUDE.md`.
**＋** blocks 75.1 and 144.1 promise one thing — the written shape of a ledger line — with
two readings.
**＋** the `＋` line of 144.1 on `CLAUDE.md` equalling the Render is the promise of
`estimate-claude-md-rendered`, not of this page.
**＋** the three slugs `estimate-case-protocol-case-form`, `-acknowledging-reply` and
`-ledger-line-form` are free in the vault and in the archive.
**＋** `rule-case-protocol` carries `deferred_by: decision-case-185`, and 185 defers this
page alone, so `{supersedes:case 185}` is safe here.
**＋** this page's `## How it works` carries two facts held nowhere else: the eight sections
arrive through the import of `case-schema.md`, and `parent` names the file the Render is
spliced into.
**－** 159, 167, 75.1 and 144.1 are not withdrawn: their content moves, and their Decision
pages stay live.
**－** under the new model moving a block needs no mechanism: the Criterion is replaced
whole and there are no blocks.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-188
