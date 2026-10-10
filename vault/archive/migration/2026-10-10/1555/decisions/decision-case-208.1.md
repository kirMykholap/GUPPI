---
type: decision
case: "208.1"
status: archived
update: [index, case-schema, estimates-schema, estimates-schema-yaml]
origin: raw/2026-09-16/1955/ledger.md#case-208.1
sprint: migration
created: 2026-09-16
tags: []
---

## Context

Case 204 signed: on an `update` of an Estimate a written `sections: Criterion` stands, as on a `create`. Three texts say otherwise: `index.md` §7 — "its `update` replaces the Criterion whole" with the Case's text, and §12 allows the written text on a `create` only (194.1); `case-schema.md` — "the scripts copy the Case's `given`, `when` and `then` … replacing what stood there", and below: "an `update` of an Estimate carries `slug`, `set`, `change`; the scripts replace its Criterion with the Case's `given`, `when` and `then`"; the Render of `rule-case-protocol` — "the scripts copy them whole, replacing what stood there" — which is `CLAUDE.md`, changed only through an `update` of the page. `rule-case-protocol` carries four Estimates; the sentence is read by `estimate-case-protocol-case-form` (a Case in the chat carries the whole contract in `given`, `when`, `then`), `pending`, its reading not taken; the other three are not touched. Two more findings: `estimates/schema.md` and `schema.yaml` point at "case 191" as the one that builds `checked` and the recut — 191 is superseded by 203.2; and the Render of `rule-prespec` after the two `replace` of 203.2 still says "and the question: which of these contradict…", while the `then` of 203.2 speaks of two questions — the second is named only inside the sentence on the list.

## Problem

The next agent reads the behaviour ratified in 204 from `CLAUDE.md`, `index.md` and `case-schema.md` — and reads the old one. The pointers at 191 lead to an archived decision page. The dispatch sentence of the pre-task Render does not match its own Criterion. The question: how 204 reaches the three texts that override it, and how the two small findings close.

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-208.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
