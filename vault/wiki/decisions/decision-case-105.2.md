---
type: decision
case: "105.2"
status: current
update: [rule-materialize]
origin: raw/2026-09-13/ledger.md#case-105.2
sprint: migration
created: 2026-09-13
tags: [harness, workflow, ledger]
---

## Context

Case 94 (`rule-ask`, deferred as 65, 80, 94): `ask-guppi` reads the four live indexes and never `vault/archive/`; the slug of an archived page comes back as free. The talk of this session gave the rule: the archive is searched by slug, never by meaning. An archived slug is taken — decision pages, the `children` of Insights and History point at it. The main agent has two ways out: another slug, or restore the page and fix it at once.

## Problem

Three places do not know that an archived slug is taken. `ask-guppi` answers "free". `materialize.page_exists` (`materialize.py:335`) marks such a `create` `exists` and `generate` skips it in silence — the page of the new Case is not made, the data is lost. `generate.find` (`generate.py:229`) looks in `wiki/<category>/` only: an `update` of an archived page — the one way to bring it back (`cleanup` restores a page whose status is no longer `archived`) — fails with "no such page".

## Given

Ask-guppi (the first question of the session): 94 is the one defer on `rule-ask`; `rule-ask` (`built`, `render_mode: full`, `governs: .claude/agents/ask-guppi.md`, `tools: Read, Grep, Glob`, Estimate `estimate-ask-finds`, `deferred_by: [decision-case-94]`). Its Render: "You search the vault at `vault/wiki/` for the caller", the answer line "tags/slug: tags that fit, existing first; whether the named slug is free".
**＋** `materialize.page_exists`: a live page of the category or any `<slug>.md` under the archive → `exists: true` (lines 380–384, and 513–514 for the derived Estimate). A page carries `origin` with `#case-N`; a placeholder carries the case of its defer (101.1 fills it through a `create` — not `exists`, since the Case differs).
**＋** `generate.find` walks `CATEGORIES` under `wiki/`; `update`, `estimate`, `delete` and `defer` go through it. `cleanup.restore` (`cleanup.py:105`) already brings back a page under the archive whose status is not `archived`.
**＋** `rule-materialize` has two Estimates (`estimate_slug: estimate-materialize-assembles`); `rule-page-generation` two (`estimate-generate-writes`, its fourth block of the session after 101.1 and 104.x).
**＋** The glossary row `Index, ask-guppi` — "the search agent over them, one entry point" — gains one phrase; `index.md` §3 "query the vault before a create" stays.
**－** The archive is not searched by meaning: no `exists` or `near` on an archived page; the librarian's index check and the synthesis do not change.
**－** The agent never reads the `raw/` of the archive; `rule-pretask` does not change — it checks the slug through the answer of `ask-guppi`.

## Criterion

- [[estimate-materialize-assembles]] § case 105.2

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-105.2
