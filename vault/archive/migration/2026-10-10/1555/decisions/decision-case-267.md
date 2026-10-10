---
type: decision
case: "267"
status: archived
update: ["[[rule-case-protocol]]", case-schema, "[[estimate-case-protocol-case-form]]"]
origin: raw/2026-09-20/0958/ledger.md#case-267
sprint: migration
created: 2026-09-20
tags: [session, workflow, ledger]
---

## Context

`context` has to tell a reader who has not opened the pages how the thing works today and where it goes wrong. Today the agent fills it with case numbers, page statuses and lists of Estimates — what the audit needs, not the reader — and the substance drowns. The rule allows it: it asks `context` to hold the state of the pages, the vault's answer and "which Estimates the Case touches and which it does not", without saying that this is one sentence and the mechanism comes first; and its cap of seven sentences per story section, checked by no script, packs a big Case into dense pointer sentences instead of shortening it. The text stands in the Render of `rule-case-protocol` (rendered into `CLAUDE.md`) and in `case-schema.md`; the promise on the form of a Case is `estimate-case-protocol-case-form`, the other three Estimates of the rule are not touched.

## Problem

The rule does not separate the substance from the bookkeeping in `context`, so the agent writes the bookkeeping; and its count of sentences bounds nothing the shape does not already bound. A wording is needed that makes the mechanism come first, limits the pointers, and drops the count.

## History

- 2026-09-20 created · raw/2026-09-20/0958/ledger.md#case-267
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
