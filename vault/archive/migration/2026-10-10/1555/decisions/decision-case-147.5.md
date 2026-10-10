---
type: decision
case: "147.5"
status: archived
update: ["[[rule-documentation]]"]
origin: raw/2026-09-14/1633/ledger.md#case-147.5
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness, librarian, render]
---

## Context

`guppi index` writes four `wiki/<category>-index.md` — one line `slug: purpose` per live page (`root_cause` for lessons, `pattern` for insights, a `· deferred_by:` tail), `cleanup` rewrites them, `make lint` checks them with `index --check`. Only agents read them: `ask-guppi` (its first input, `@rules-index.md`) and the librarian at the index check and the synthesis. The owner does not read them.

## Problem

An index is derived from the frontmatter, and one Grep gives the same line: `^(purpose|deferred_by):` over `vault/wiki/rules/` — `rules/rule-x.md:purpose: …`. Four files, a script, a test, a `--check` and a Rule page hold what the agent gets with a command. Decide: remove the indexes; define the "index line" as the Grep line; rewrite the clauses of six Rules and §11.

## Given

`rule-index` `built`, `check`, `implementation_ref: [guppi/index.py, tests/test_index.py, Makefile]`, `parent: rule-harness`, `estimates: [estimate-index-lists]` `passed`; `rules-index.md`, `lessons-index.md`, `insights-index.md` live, `entities-index.md` empty.
**＋** `rule-ask` `built`, `render`, `governs: .claude/agents/ask-guppi.md`, `estimate-ask-finds`: "Rules of the vault, one line per page: @vault/wiki/rules-index.md. Start there. Read `vault/wiki/<category>-index.md` for every other category …"; "its index line is not enough to judge". The agent's tools are Read, Grep, Glob; no Bash. The harness is governed by Rule pages: a crossing with a rule the agent misses is a crooked system caught later.
**＋** `rule-index-check` `built`, `render` partial into the librarian, `estimate-index-check-merges`: "compare its `purpose` (`root_cause` for a lesson) with every line of `vault/wiki/<category>-index.md` of the same category"; "When the index line does not settle same or near, open the page". The librarian has Grep and Bash.
**＋** `rule-synthesis` `built`, `estimate-synthesis-clusters`: "compare its `root_cause` with every line of `lessons-index.md` and of `insights-index.md`, by meaning"; "that Insight stays live with its pattern in the index".
**＋** `rule-documentation` MOC `built`, `governs: .claude/agents/librarian-guppi.md`, `estimate-documentation-completes`: "Your inputs are four: … the four `vault/wiki/<category>-index.md` files, and `vault/wiki/tags.md`"; the four reasons to open a page — "an index line does not tell you …".
**＋** `rule-cleanup` `built`, `estimate-cleanup-moves`, purpose "… or the indexes from lagging behind the vault"; "Then the four indexes are rewritten with the writer of `guppi index`; an archived Estimate leaves no line, since estimates have none." Code: `cleanup.py` imports `index.plan` and calls `rewrite_indexes()`.
**＋** `rule-lint` `built`, `implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]`: "`make lint` runs it after `render --check` and `index --check` over the four index files; all three only report"; Makefile `lint:` — three commands; `test-harness` names `tests/test_index.py`.
**＋** `index.md` §11 "The indexes" — the definition, "what makes semantic checks affordable", "no `estimates-index.md`", "no `decisions-index.md`", "`ask-guppi` is the search mechanism over these indexes"; §10 lines 353, 355 "checks new pages against the indexes", "when the indexes reveal a duplicate"; the glossary row "Index, `ask-guppi`". `rule-harness.children` holds `rule-index`; `cleanup` removes an archived slug from the `children` of live pages.
**＋** The lint `ref` clause "every slug in `deferred_by` an existing decision page" does not depend on the index; `brief.md` "Readings at the close" names `guppi index --check` — not schema-governed, the librarian writes by its frame.
**－** `estimate-index-lists`: its target goes to the archive — deleted by the same Case. `guppi index` is called nowhere else (`cleanup` is the writer; removed).
**－** Rule-class files (`index.md`, `glossary.md`) — an `update` with `file`, by hand in Work Mode.

## Criterion

- [[estimate-documentation-completes]] § case 147.5

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-147.5
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
