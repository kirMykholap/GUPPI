---
type: decision
case: "186.3"
status: current
update: ["[[rule-lint]]"]
origin: raw/2026-09-16/1034/ledger.md#case-186.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow]
---

## Context

`rule-page-generation` governs `guppi generate`. A `defer` on an existing page sets
`deferred_by` and appends History `deferred`; a `defer` without a `ref` writes a
placeholder page, `status: draft`, carrying the fields the Case gave. The Decision page
of the Case holds `Context`, `Problem` and `Given`. `rule-pretask` governs the pre-task
skill, which dispatches `ask-guppi` once with the plan file and the instruction to read
every Case there. `rule-lint` governs `guppi lint`, which reports missing schema fields
and orphans.

## Problem

The `purpose` of a `defer` — the one field that says what the postponed work is — reaches
no page when the defer names an existing page. It survives only in the session's
`materialize.yaml` and in the brief's Deferred list, which is capped at seven. The agreed
Estimate model of Slice 3d, 6203 characters, is written as the `purpose` of case 182 on
`rule-plan-mode` and is in no page of the vault. At the same time pre-task sends
`ask-guppi` into the body of every deferred Case of the plan, so a text another session
will ratify from the start is proof-read now; in session 2225 two points inside the
`purpose` of 182 were corrected this way. And the two placeholders that carry the oldest
defers are visible to lint only through eight findings that describe the wrong illness.

## Given

`guppi generate` on a `defer` with an existing page sets `deferred_by` and writes History
`deferred`; the entry's `purpose` is dropped.
**＋** without a `ref` the placeholder keeps `purpose` as its own field.
**＋** `purpose` is required on every `defer`: `materialize` marks the entry
`incomplete: [purpose]` without it.
**＋** the eight live defers carry a `purpose` of 141 to 6203 characters; the one of 182 on
`rule-plan-mode` runs to 25 lines.
**＋** `case-schema.md` says a deferred decision is taken up "from its page — `context` and
`problem` as they stand"; those are the sections of `decision-case-N`.
**＋** a Decision page requires `Context` and `Problem`, and allows `Given`, `When`,
`Criterion`, `Note`; it is in no index and is reached by pointer only.
**＋** the pre-task skill dispatches `ask-guppi` once with the list of decisions, the plan
file path, and the instruction to read every Case's `when`, `then` and `then` block.
**＋** a deferred Case sits in the plan under the `## Deferred` heading and holds
`context`, `problem` and a `then` block with `defer:`, `slug`, `type` and `purpose`.
**＋** `rule-work-mode` and `rule-subagent-guppi` are placeholders with 13 `deferred` lines
each in History; they produce eight lint findings — three `schema` each (`kind`,
`estimates`, `tags`) and one `orphan` each.
**＋** `rule-page-generation` carries two Estimates; `rule-lint` and `rule-pretask` carry
one each.
**＋** `rule-page-generation`, `rule-lint` and `rule-pretask` are all
`deferred_by: decision-case-182`, so Slice 3d rewrites them in this same session.
**－** `rule-ask` is not changed by this Case.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-186.3
