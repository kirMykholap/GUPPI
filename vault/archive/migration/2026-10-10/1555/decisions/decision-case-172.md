---
type: decision
case: "172"
status: archived
update: ["[[rule-page-generation]]"]
supersedes: ["[[decision-case-148.1]]"]
origin: raw/2026-09-15/1448/ledger.md#case-172
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

Block 148.1 of `estimate-generate-writes` — the contract of the ref fields in the form `"[[slug]]"` and of the migration of 148.1 — ends with the line "**－** The body sections stay; no CLI probe." After 166.2 the sections go, and the line stays signed. Found at pre-task.

## Problem

Block 148.1 and block 166.2 say the opposite about the sections.

## Given

Block 148.1: `when` — generate or cleanup writes a page, a script reads one through `read_page`/`page_estimates`, the migration over `wiki/` and `archive/`; `then` — five lines on the fields, the readers, the migration, the tests and Obsidian, the last "The body sections stay; no CLI probe".
**＋** The sentence of 148.1 in the rule's text on the wikilink fields is right and does not change; an `update` needs a `replace` — the phrase "reads the same (case 148.1)" stands once on the page.
**－** The code of 148.1 does not change.

## Criterion

- [[estimate-generate-writes]] § case 172

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-172
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
