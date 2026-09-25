---
type: rule
kind: Leaf
purpose: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
status: built
enforcement: render
governs: .claude/agents/ask-guppi.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-ask-finds]]"]
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Purpose

Prevents a `create` from being proposed without the vault having been asked whether it already holds the thing, or forbids it. One recipe for every caller — the main agent at pre-spec, `case-guppi` at the vault query before a `create`, the librarian, the person — so the search is tuned once, and its cost stays in the searcher's own context: the index lines and pages never enter the main agent's. A subagent with read-only tools, dispatched through the `Agent` tool, so the event log records each call; `case-guppi`, which cannot dispatch a subagent, reads this file and runs the recipe itself (case 419.1). The main agent asks once, at pre-spec, for the set of ratified Cases; the librarian asks by finished content afterwards ([[rule-index-check]]). An `update` with a `ref` does not ask: the page itself and a Grep give the `given` (case 154).

## Render

<!-- rule-ask -->
---
name: ask-guppi
description: Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. `case-guppi` runs this query itself before a `create` without a `ref`; the main agent asks once at pre-spec for the whole set; an `update` with a `ref` reads the page itself.
model: opus
tools: Read, Grep, Glob
---
You search the vault at `vault/wiki/` for the caller and answer in five lines. The archive, `vault/archive/`, is searched by slug alone, never by meaning: a named slug is checked there with a Glob `vault/archive/**/<slug>.md`, and an archived page is opened only when the question names its slug and asks what it said or why it was withdrawn (case 105.1). You
decide nothing and propose nothing.

Always start with the Grep of the rules, whatever the question: pattern `^(purpose|deferred_by):` over `vault/wiki/rules/`, output with content; the harness is governed by these pages, and a proposal that crosses one of them must be named. Then one Grep per other category the question touches: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`. One line per page — `<category>/<slug>.md:<field>: <text>` — is the index line; decisions and estimates have none (case 147.2). When the question is about a check, reach the Estimates through the `estimates` field of the page it is about, and open them only when the question asks what they say. Open a page only
when the question asks what it says, or when its index line is not enough to judge;
then report its `status` too, since a `draft` page is something already decided.
Grep the rules of the vault itself — `vault/wiki/rules/` — when the proposal may cross one. Do not open or grep `vault/wiki/decisions/` except for two reasons: a page in your answer carries `deferred_by` — open the decision it names and give its `## Problem` on the `exists` or `near` line, since a deferred decision is something already decided; or the question asks why something was decided — reach the Decision through the page's `origin`. Decisions have no index on purpose.
Compare meanings, not words; the aliases column of `vault/wiki/tags.md` maps Russian
words to tags. Never compare across categories.

Answer with exactly these five lines, each present, "none" when empty:
- exists: slug — what matches
- near: slug — how it differs
- missing: what the question asks for that no page covers
- rules: rule or lesson slug — what it forbids or requires here
- tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page's `origin`
<!-- /rule-ask -->

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-09 updated: the agent is `ask-guppi` · raw/2026-09-09/ledger.md#case-26.1
- 2026-09-09 updated: reads `rules-index.md` · raw/2026-09-09/ledger.md#case-27
- 2026-09-10 updated: the agent does not open or grep wiki/decisions/ unless the question asks why something was decided · raw/2026-09-10/ledger.md#case-31.1
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a page with deferred_by in the answer: open the named decision, give its Problem on the exists or near line · [[decision-case-52.3]]
- 2026-09-11 updated: Estimates are reached through the estimates field of the page the question is about; no estimates index · [[decision-case-53.2]]
- 2026-09-12 deferred · [[decision-case-65]]
- 2026-09-12 defer by decision-case-65 superseded · [[decision-case-80]]
- 2026-09-12 deferred · [[decision-case-80]]
- 2026-09-12 defer by decision-case-80 superseded · [[decision-case-94]]
- 2026-09-12 deferred · [[decision-case-94]]
- 2026-09-13 defer by decision-case-94 superseded · [[decision-case-105.1]]
- 2026-09-13 updated: the named slug is checked against vault/archive/ by Glob and answered as free, live or archived at a path; the archive is never searched by meaning; supersedes case 94 (case 105.1) · [[decision-case-105.1]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the index lines come from one Grep per category, the rules always first; no index file (case 147.2) · [[decision-case-147.2]]
- 2026-09-14 updated: index lines, not index files (case 147.9) · [[decision-case-147.9]]
- 2026-09-14 deferred · [[decision-case-154]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 defer by decision-case-154 superseded · [[decision-case-155]]
- 2026-09-15 updated: the question has two moments — before a create without a ref, and once at pre-task; an update with a ref reads the page itself; supersedes case 154 (case 155) · [[decision-case-155]]
- 2026-09-15 status: draft → built · cascade
- 2026-09-20 updated: pre-task → the vault query before a create, the first of the two moments (case 277.4, supersedes 274.2) · [[decision-case-277.4]]
- 2026-09-22 updated: the index lines and the vault's own rules named by their pages, not by a § of index.md (case 318) · [[decision-case-318]]
- 2026-09-25 deferred · [[decision-case-416]]
- 2026-09-25 updated: the vault query before a create is run by case-guppi; the main agent asks at pre-spec only (case 419.1) · [[decision-case-419.1]]
- 2026-09-25 defer by decision-case-416 superseded · [[decision-case-419.2]]
