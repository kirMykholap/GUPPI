---
type: decision
case: "113"
status: archived
update: ["[[lesson-agents-at-import-not-expanded]]", "[[lesson-agents-loaded-at-session-start]]", "[[lesson-agents-visible-in-session]]", "[[lesson-estimates-criterion-stale-after-contract-change]]", "[[lesson-hooks-exitplanmode-payload]]", "[[lesson-hooks-messagedisplay-cannot-block]]", "[[lesson-hooks-sessionstart-cannot-block]]", "[[lesson-hooks-stop-payload]]", "[[lesson-hooks-windows-stdin-encoding]]", "[[lesson-tests-cli-date-pinned]]"]
origin: raw/2026-09-14/0747/ledger.md#case-113
sprint: migration
created: 2026-09-14
tags: [harness, hooks]
---

## Context

F8 (d): ten lessons of sessions A–B, written by hand on 2026-09-09 and 2026-09-10 before the ledger hook and `materialize` existed. Nine have no `tags`; six of `kind: knowledge` have no `source`. 17 of the 116 lint findings.

## Problem

`tags` and `source` are judgments — which registered tags fit, where the knowledge came from — so nobody can fill them but a ratified `update`. Until then the lessons index carries nine untagged rows and six knowledge claims with no origin.

## Given

`lessons/schema.md`: `tags` required; `source` required when `kind: knowledge`, "url or reference — where the material came from". Existing sources are free references. Registered tags (`tags.md`): session, hooks, harness, ledger, git, github, workflow, render, librarian, tests.
**＋** The Slice 1 probe files the lessons name (`probe-Stop-6.json`, `probe-PostToolUse-1.json`) were removed with `raw/notes/` by case 100.6; the source says so.
**－** The two `tags` findings that remain after this Case are the placeholders of Case 107 (F4).
**－** No new tag is declared; `status`, `insight`, `root_cause` are untouched.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-113
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
