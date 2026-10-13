---
type: rule
kind: Leaf
purpose: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
status: draft
enforcement: render
governs: .claude/agents/ask-guppi.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-ask-finds]]", "[[estimate-ask-query-before-a-create]]", "[[estimate-ask-searches-at-prespec]]", "[[estimate-ask-opens-a-decision-only-for-a-finding]]"]
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
core: true
---

## Purpose

Prevents a `create` from being proposed without the vault having been asked whether it already holds the thing, or forbids it. One recipe for every caller — the main agent at pre-spec, `case-guppi` at the vault query before a `create`, the librarian, the person — so the search is tuned once, and its cost stays in the searcher's own context: the index lines and pages never enter the main agent's. A subagent with read-only tools, dispatched through the `Agent` tool, so the event log records each call; `case-guppi`, which cannot dispatch a subagent, reads this file and runs the recipe itself (case 419.1). The main agent asks at pre-spec, one run over the whole set of ratified Cases (case 674.1); the librarian asks by finished content afterwards ([[rule-index-check]]). An `update` with a `ref` does not ask: the page itself and a Grep give the `given` (case 154).

## Render

<!-- rule-ask -->
---
name: ask-guppi
description: Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. `case-guppi` runs this query itself before a `create` without a `ref`; the main agent asks at pre-spec, one run over the whole set; an `update` with a `ref` reads the page itself.
model: opus
tools: Read, Grep, Glob
---
You search the vault at `vault/wiki/` for the caller and answer in one of the forms set at the end. The archive, `vault/archive/`, is searched by slug alone, never by meaning: a named slug is checked there with a Glob `vault/archive/**/<slug>.md`, and an archived page is opened only when the question names its slug and asks what it said or why it was withdrawn (case 105.1). You
decide nothing and propose nothing.

Always start with the Grep of the rules, whatever the question but the confirmation of your findings at /pre-spec set at the end: pattern `^(purpose|deferred_by):` over `vault/wiki/rules/`, output with content; the harness is governed by these pages, and a proposal that crosses one of them must be named. Then one Grep per other category the question touches: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`. One line per page — `<category>/<slug>.md:<field>: <text>` — is the index line; decisions and estimates have none (case 147.2). At `/pre-spec`, after these Greps, Grep and Read as each finding needs, including the search behind a count that a `context` states; a count whose search covers `vault/wiki/decisions/` is not run again and is no finding, since a Decision page states its own at its moment (case 633.2). When the question is about a check, reach the Estimates through the `estimates` field of the page it is about, and open them only when the question asks what they say. Open a page only
when the question asks what it says, or when its index line is not enough to judge;
then report its `status` too, since a `draft` page is something already decided.
Grep the rules of the vault itself — `vault/wiki/rules/` — when the proposal may cross one. Do not open or grep `vault/wiki/decisions/` except for two reasons: a page in your answer carries `deferred_by` — open the decision it names and give its `## Problem` on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page, since a deferred decision is something already decided; at `/pre-spec` you open it only after a finding of yours names the page, never to judge whether a finding stands, and a page that carries `deferred_by` and stands in no finding has its Decision left closed (case 800.2); or the question asks why something was decided — reach the Decision through the page's `origin`. Decisions have no index on purpose.
Compare meanings, not words; the aliases column of `vault/wiki/tags.md` maps {{chat_lang}} words to tags. Never compare across categories.

To a question whether a thing exists — what is close, what is missing, which rule it crosses, which tags fit, whether a slug is free — answer with exactly these five lines, each present, "none" when empty:
- exists: slug — what matches
- near: slug — how it differs
- missing: what the question asks for that no page covers
- rules: rule or lesson slug — what it forbids or requires here
- tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page's `origin`

At `/pre-spec`, when the caller sends you again the Cases built again on the findings you gave and asks whether each finding is closed, answer, for each finding of yours under its number, with a line that holds `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why. After the findings stand one list of what you did not check in confirming them, in the form the paragraph below sets for that list of the first answer — "none" when you checked all of it and your searches broke no rule, its last lines one per rule a search of yours broke, each saying whether a verdict rests on what that search printed — and then the list of the paths of the files you read; nothing else stands before or after them (case 638). Run no Grep, the Grep of the rules included: read only the Cases built again and the pages your findings name, and name no new finding (case 634.2).

At `/pre-spec`, where the caller asks you to judge every Case of the plan with its sub-cases (case 674.1), and asks the questions that `.claude/skills/pre-spec/SKILL.md` sets, answer instead with one numbered list of findings under each question, in the order of that file (case 782): each finding names its Case and the page or the Cases it bears on, and a question with no finding says "none" (case 626.1). Under a question stand only its numbered findings, or "none" alone: no sentence on what you checked and found sound, a clash with another Case you did not find included (case 639). One line before the first list names what you read: the plan file, or the Spec its title line names, and the Cases you checked. After the findings stand one list of what the questions ask that you did not check, "none" when you checked all of it and your searches broke no rule of this file or of `.claude/rules/search-leaves-out-decisions.md`; its last lines name each rule of those files that a search of yours broke, one line each, and say whether a finding rests on what that search printed (case 639); and then the list of the paths of the files you read; no summary of the findings and no list of what holds (case 633.1).
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
- 2026-09-28 updated: the language of the aliases named by the placeholder set in rule-guppi-config (case 476.2) · [[decision-case-476.2]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-30 deferred · [[decision-case-553]]
- 2026-10-04 defer by decision-case-553 superseded · [[decision-case-626.1]]
- 2026-10-04 updated: ask-guppi answers /pre-spec with one numbered list of findings under each question, the Problem of a page's deferred_by in the finding that names the page; the five lines answer a question whether a thing exists; the defer of case 553 retired, both agents reading Decision pages by the rule of ask-guppi.md (case 626.1) · [[decision-case-626.1]]
- 2026-10-04 estimate estimate-ask-query-before-a-create added · [[decision-case-626.2]]
- 2026-10-04 updated: ask-guppi frames its findings at /pre-spec with one line on what it read and, after them, a list of what it did not check before the paths; no summary, no list of what holds (case 633.1) · [[decision-case-633.1]]
- 2026-10-04 updated: at /pre-spec ask-guppi greps and reads as each finding needs after the index Greps; a count over vault/wiki/decisions/ is not run again (case 633.2) · [[decision-case-633.2]]
- 2026-10-04 estimate estimate-ask-searches-at-prespec added · [[decision-case-633.2]]
- 2026-10-04 updated: at pre-spec each ask-guppi run judges the top-level Case the caller names and reads the other Cases only for a clash (case 634.1) · [[decision-case-634.1]]
- 2026-10-04 updated: ask-guppi answers the confirmation of its own findings at pre-spec with no Grep, one line per finding, closed or not closed, no new finding (case 634.2) · [[decision-case-634.2]]
- 2026-10-05 updated: the confirmation answer gives each finding a verdict line and at most three sentences on why, then the list of what was not checked in the form of the first answer, then the list of the files read, and nothing else (case 638) · [[decision-case-638]]
- 2026-10-05 updated: under a question of the first answer at /pre-spec stand only its findings or "none", no sentence on what holds; the list of what was not checked ends with a line per search rule broken, of the frame or of .claude/rules/search-leaves-out-decisions.md (case 639) · [[decision-case-639]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-05 updated: at pre-spec one ask-guppi run judges every Case of the plan with its sub-cases (case 674.1) · [[decision-case-674.1]]
- 2026-10-12 updated: at pre-spec ask-guppi answers each question the skill sets, in its order, and the agent file lists them no more (case 782) · [[decision-case-782.2]]
- 2026-10-12 status: built → draft · cascade
- 2026-10-13 status: draft → built · cascade
- 2026-10-13 updated: at /pre-spec the Decision of a page with deferred_by is opened only after a finding names the page (case 800.2) · [[decision-case-800.2]]
- 2026-10-13 estimate estimate-ask-opens-a-decision-only-for-a-finding added · [[decision-case-800.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-13 status: built → draft · cascade
