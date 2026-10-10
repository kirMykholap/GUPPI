---
type: decision
case: "147.9"
status: archived
update: ["[[rule-render-harness]]", "[[rule-ask]]", "[[rule-documentation]]"]
origin: raw/2026-09-14/1633/ledger.md#case-147.9
sprint: migration
created: 2026-09-14
tags: [harness, render, session, workflow, librarian]
---

## Context

`guppi index` writes four `wiki/<category>-index.md` — one line `slug: purpose` per live page (`root_cause` for lessons, `pattern` for insights, a `· deferred_by:` tail), `cleanup` rewrites them, `make lint` checks them with `index --check`. Only agents read them: `ask-guppi` (its first input, `@rules-index.md`) and the librarian at the index check and the synthesis. The owner does not read them.

## Problem

An index is derived from the frontmatter, and one Grep gives the same line: `^(purpose|deferred_by):` over `vault/wiki/rules/` — `rules/rule-x.md:purpose: …`. Four files, a script, a test, a `--check` and a Rule page hold what the agent gets with a command. Decide: remove the indexes; define the "index line" as the Grep line; rewrite the clauses of six Rules and §11.

## Given

`rule-render-harness` line 22: "the renderer runs with lint and the indexes"; `rule-ask` Purpose line 22: "the indexes and pages never enter the caller's"; `rule-documentation` line 94: "reads four inputs" (pre-task).

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-147.9
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
