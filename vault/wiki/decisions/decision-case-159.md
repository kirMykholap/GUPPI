---
type: decision
case: "159"
status: current
update: ["[[rule-case-protocol]]", case-schema]
origin: raw/2026-09-15/1110/ledger.md#case-159
sprint: migration
created: 2026-09-15
tags: [session, workflow, ledger]
---

## Context

A Case is seven sections in blockquotes; the shape is set in `case-schema.md` and in the Render of `rule-case-protocol`, which lands in `CLAUDE.md`. On the first three sections the rule says one phrase — "in plain words"; the operands ＋/－ are defined as "one more condition" and "a limit"; `then` holds both behaviour and bookkeeping — the contract mark, the Estimate block, the reading. The Spec is the same Case in English plus the `then` and `tasks` blocks the scripts read. Today a Case in the chat is hard to read: the story is written in the language of the contract, `then` drowns in bookkeeping, slugs and bold mix.

## Problem

What a Case in the chat should look like to be readable, without changing what the scripts read from the Spec.

## Given

`rule-case-protocol` (`draft`, `render` → `CLAUDE.md`, `estimates: [estimate-case-protocol-loaded]`, `pending` by 157): the paragraph "A Case renders as…" sets the blockquotes, the operands, the sub-cases and the preview in `ratification`; the paragraph "The Spec is written…" the `tasks` block of the Spec.
**＋** `case-schema.md` (Rule-class, applied by hand): the Sections table of seven rows, the paragraphs Operands, Language, Splitting, "The Spec is written…".
**＋** `guppi materialize` reads from the Spec the `when`/`then` blockquotes (into the criterion), the `then` block and `problem`; `guppi pretask --check` the `then` block; nothing reads the chat form.
**＋** Case 157 set the reply that acknowledges a ratification — a separate reply, not a Case.
**－** The Spec does not change its form: the same blockquotes in English, the `then` and `tasks` blocks; otherwise `materialize` would change.

## Criterion

- [[estimate-case-protocol-loaded]] § case 159

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-159
