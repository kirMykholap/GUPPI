---
type: decision
case: "326"
status: archived
update: ["[[rule-page-generation]]", "[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-22/1724/ledger.md#case-326
sprint: migration
created: 2026-09-22
tags: [harness, workflow, ledger]
---

## Context

`tick_read` walks the Specs of `raw/`: the Spec beside the yaml first, then the folders of the other sessions, oldest first — and stops at the first that holds a line of the slug; inside it every line of that slug is ticked, because "one reading is of the page, whose Criterion is one, however many Cases of the session touched it" (case 312). The archive is not read. When a promise is changed twice in two sessions, the line of the older Spec no longer belongs to its Case and no new reading reaches it: session 0014 left two such lines, 1105 and 1544, and today's reading of `estimate-harness-pipeline` would leave the second of them open.
`rule-page-generation` stands `draft` with nine Estimates; the promise of the ticker is `estimate-generate-ticks-the-spec`, `passed`, read 2026-09-22; its Criterion covers the page lines as well as the reading lines, so the Case changes a part of it with a `replace` pair, as case 296 allows. The other eight Estimates of `rule-page-generation` are not touched.

## Problem

The `read` line of the older Spec never closes: its Criterion is gone, and a new reading never reaches it. Refusing the form is no answer — the second Case is at no fault, the promise honestly changed twice, and the older line could only be resolved by editing another session's Spec, which its own rule does not allow.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-326
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
