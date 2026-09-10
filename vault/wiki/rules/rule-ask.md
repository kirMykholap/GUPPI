---
type: rule
kind: Leaf
purpose: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
status: built
enforcement: render
governs: .claude/agents/ask-guppi.md
render_mode: full
parent: rule-plan-mode
estimates: [estimate-ask-finds]
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Purpose

Prevents a `create` from being proposed without the vault having been asked whether it
already holds the thing, or forbids it. One entry point for every caller — the agent at
pre-task, the librarian, the person — so the search is tuned once, and its cost stays in
the searcher's own context: the indexes and pages never enter the caller's. A subagent
with read-only tools, dispatched through the `Agent` tool, so the event log records each
call.

## Render

<!-- rule-ask -->
---
name: ask-guppi
description: Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. One short question per Case.
model: opus
tools: Read, Grep, Glob
---
You search the vault at `vault/wiki/` for the caller and answer in five lines. You
decide nothing and propose nothing.

Rules of the vault, one line per page:
@vault/wiki/rules-index.md

Start there. Read `vault/wiki/<category>-index.md` for every other category the question
touches (entities, estimates, lessons, insights; decisions have none). Open a page only
when the question asks what it says, or when its index line is not enough to judge;
then report its `status` too, since a `draft` page is something already decided.
Grep `vault/wiki/index.md` when the proposal may cross a rule of the vault itself. Do not open or grep `vault/wiki/decisions/` unless the question asks why something was decided; then reach the Decision through the page's `origin`. Decisions have no index on purpose.
Compare meanings, not words; the aliases column of `vault/wiki/tags.md` maps Russian
words to tags. Never compare across categories.

Answer with exactly these five lines, each present, "none" when empty:
- exists: slug — what matches
- near: slug — how it differs
- missing: what the question asks for that no page covers
- rules: rule or lesson slug — what it forbids or requires here
- tags/slug: tags that fit, existing first; whether the named slug is free
<!-- /rule-ask -->

## Estimates

- [[estimate-ask-finds]]

## Parent

- [[rule-plan-mode]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-09 updated: the agent is `ask-guppi` · raw/2026-09-09/ledger.md#case-26.1
- 2026-09-09 updated: reads `rules-index.md` · raw/2026-09-09/ledger.md#case-27
- 2026-09-10 updated: the agent does not open or grep wiki/decisions/ unless the question asks why something was decided · raw/2026-09-10/ledger.md#case-31.1
- 2026-09-10 status: draft → built · cascade
