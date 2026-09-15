---
type: decision
case: "164"
status: archived
update: ["[[rule-page-generation]]"]
supersedes: ["[[decision-case-124.2]]"]
superseded_by: ["[[decision-case-166.2]]"]
origin: raw/2026-09-15/1448/ledger.md#case-164
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

`rule-synthesis` tells the librarian, on the second lesson with the same root cause, to append to `materialize.yaml` a `create` in `insights` marked `librarian: synthesis` and one `update` per lesson. `guppi generate` lays the yaml entries into pages. Case 124.2 made an Insight the target of `update` and `defer` and fixed: "an Insight is neither created nor deleted through the yaml: a `create` or `delete` with an Insight as its target is a `generate` error". The code refuses every `create` in `insights` before it looks at the `librarian` mark. The last synthesis that applied — `insight-ledger-hi-tied-to-its-session-by-position` in `0747` — ran before 124.2. In the run of session Q the entry `insight-retro-typed-command-is-never-a-tool-call` was refused, and the two lesson `update`s applied before the refusal.

## Problem

`rule-synthesis` and block 124.2 contradict each other: the rule tells the librarian to create an Insight by a yaml entry, the contract of `generate` forbids it; two retro lessons stand `clustered` with an `insight` that names no page — 2 `ref` findings.

## Given

`rule-page-generation` (`built`, `check`, `estimates: [estimate-generate-writes, estimate-generate-walks-dates]`, both `passed`): the text of the rule does not name the Insight refusal; it lives only in the code and in block 124.2 of `estimate-generate-writes`.
**＋** `generate.create` refuses the whole category `insights` with the line `LIBRARIAN_ONLY`; `generate.delete` too; `generate` reads the `librarian` mark nowhere.
**＋** A synthesis entry: `kind: create`, `category: insights`, `origin` the lesson's ledger line, `librarian: synthesis`, no `line` and no `case`; a decision entry carries `line`, `case`, `decision`.
**＋** `tests/test_generate.py`: the test of 124.2 refuses a `create` of an Insight with `line` and `case`; no test seeds an entry with `librarian`.
**＋** An entry with `failed` and `kind` is retried by the next run of `generate`; the mark is dropped on apply (53.3).
**＋** `rule-synthesis` Render: "append to the yaml a `create` in `insights`…"; `insights/schema.md`: "Created by the librarian, never by a decision".
**－** `decision-case-124.2` is an `update` of one page, no `defer`; the supersedes clears nothing from `deferred_by`.

## Criterion

- [[estimate-generate-writes]] § case 164

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-164
- 2026-09-15 superseded by decision-case-166.2 · [[decision-case-166.2]]
- 2026-09-15 archived · superseded
- 2026-09-15 archived · cleanup
