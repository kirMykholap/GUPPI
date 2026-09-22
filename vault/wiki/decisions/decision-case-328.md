---
type: decision
case: "328"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-cascades]]"]
origin: raw/2026-09-22/1724/ledger.md#case-328
sprint: migration
created: 2026-09-22
tags: [harness, workflow, ledger]
---

## Context

The cascade of `generate` builds its map of Estimates from the live files of `wiki/estimates/` and already passes over a slug with no page. An Estimate a `delete` of the same run marked `archived` is still a file in that folder, and still a slug in the target's list — and it spoils the count: `all_passed` is false and the page falls back to `draft`. The slug is taken out of the list by `cleanup`, which runs after `generate`, so until the next run the rule stands `draft` while every live promise is `passed`. This is the lint finding on `rule-materialize`: its eleven live Estimates are all `passed`, and the twelfth, retired by case 320, dragged the page down with it.
`rule-page-generation` stands `draft` with nine Estimates; the promise of the cascade is `estimate-generate-cascades`, `passed`. Case 326 of this session changes the sentence on the ticker of the same page — another place, no overlap. The mechanism of the cascade is not spelled out on the page, which points at the docstring of `guppi/generate.py`, so the Criterion is what changes and the page takes a History line.

## Problem

Deleting an Estimate drops its target to `draft` for a whole session, though every live promise of the target holds. The symptom heals itself — tonight's run sees eleven `passed` and returns `built` — but it returns with every later `delete` of an Estimate, and each time it costs a lint finding, a flag in the brief and an item of the Frontier.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-328
