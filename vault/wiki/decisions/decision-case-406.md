---
type: decision
case: "406"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-case-form]]"]
origin: raw/2026-09-24/2214/ledger.md#case-406
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Context

The agent writes counts in the story sections of a Case: how many lines a journal has, how many Estimates are touched. A count goes stale first. An item is added or removed, the count stays in the text and goes into the Spec and onto the Decision page. In session 1916 this was a source of errors. `CLAUDE.md` already says that a count comes from the run that printed it. But a Case is written before the run and edited after it, and nothing checks the count in it. Today the Language paragraph of the Render of `rule-case-protocol` forbids in the story sections a count of sentences, line numbers and quotations. It does not forbid a count of items. The rule goes into `case-schema.md`, not into `CLAUDE.md`: `CLAUDE.md` works without GUPPI too, and only `/hi` loads the Case schema. `estimate-case-protocol-case-form` stands `pending`. Case 396.1 of the conserved Spec of session 1916 already replaces its Criterion whole. This Case takes the `when` and `then` of 396.1 and extends the line on `context`, so the Spec of 1916 is applied first. An `update` with a `ref`, no vault query. `frame-guppi` found no contradiction. The other Estimates of the rule speak of other things, and this Case does not touch them. `estimate-agent-writing-followed` speaks of the width of a claim in any text of the agent, which this Case does not change, so it is not touched either.

## Problem

The rule does not forbid a count of items in `context`, `problem` and `recommend`. A stale count goes into the Spec and onto the Decision page, and neither the ratification nor a script catches it.

## Given

`rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the Sections table and the Language paragraph on the story sections.
**＋** `estimate-case-protocol-case-form` — the Estimate whose Criterion is replaced.
**＋** `rule-agent-writing` — the writing rule in `CLAUDE.md`: a count comes from the run that printed it.

## History

- 2026-09-25 created · raw/2026-09-24/2214/ledger.md#case-406
