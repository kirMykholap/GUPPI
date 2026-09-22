---
type: decision
case: "335"
status: current
update: ["[[rule-prespec]]", "[[estimate-prespec-checks-the-plan]]"]
origin: raw/2026-09-22/1724/ledger.md#case-335
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, tests]
---

## Context

A Frontier line is `- [x] C<n> — <title> · <source> · <closer>`. Case 314.2 asks that a line closed `· case N` whose segments hold `sprint` carry an `update` of the sprint page under that Case. The code tests it as `any("sprint" in s for s in segments[:-1])` — a substring over every segment but the closer. Today that gave a false finding on C6: its source is `brief`, but its title holds the slug `estimate-sprint-migration-index-dissolved`, and the word was found inside the slug. Six live Estimates carry `sprint` in their slug, so it returns.
`rule-prespec` stands `built`, and its Render carries the same wording in prose — the fifth place of this session's changes on that page, meeting none of the other four. The findings of the Frontier belong to `estimate-prespec-checks-the-plan`, which case 327 already changes in the neighbouring line of the Criterion.

## Problem

The check judges by a substring over the whole line instead of the field meant for it — the class of C12. An item that came from the brief is declared an item of the sprint because of the name of the page it speaks about.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-335
