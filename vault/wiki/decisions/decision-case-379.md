---
type: decision
case: "379"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-ledger-line-form]]"]
supersedes: ["[[decision-case-377.2]]"]
origin: raw/2026-09-23/1355/ledger.md#case-379
sprint: migration
created: 2026-09-23
tags: [session, workflow, ledger]
---

## Context

The mark `{addresses:<lesson slug>}` stands on a decision line when the lesson line already stands in the ledger; a lesson written after its fix has no place for the mark, and the synthesis opens the Insight again. Case 377.2 fixed this in the old model: it appended lines inside the Criteria of `estimate-case-protocol-ledger-line-form` and `estimate-case-protocol-loaded`. Case 378.4 refuses a pair inside a Criterion, and by Case 378.5 `loaded` is no longer touched by a change of a Render; the ledger line of 377.2 on `loaded` stands already and is undone only by a supersede. So this Case replaces 377.2 whole; 377.2 leaves the Spec. The Criterion of `estimate-case-protocol-ledger-line-form` is replaced whole: the form of a decision line, today in its Given, moves to its Then; its `purpose` and `method` follow the promise — how the agent writes the lines, not what a document says. `rule-case-protocol` stands `draft`; `estimate-case-protocol-loaded` is not touched by 378.5; `-case-form` and `-acknowledging-reply` speak of other things.

## Problem

A lesson written after the decision that closed its cause has no place for the mark, so the synthesis opens its Insight again and a Case is spent on a fact the yaml already holds.

## Given

`rule-case-protocol` — the ledger paragraph of the Render `vault/wiki/case-schema.md`.
**＋** `estimate-case-protocol-ledger-line-form` — the promise: its Criterion, `purpose` and `method` replaced.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-379
