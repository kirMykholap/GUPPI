---
type: estimate
kind: QA
status: passed
target: rule-ask
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Context

The agent replaces reading category folders by hand. What has to hold is that it finds a
page by meaning in either language, names the rule a proposal crosses, and costs the
caller nothing but its five lines; and two things nobody measured yet — whether `@`
expands in an agent file, and what one dispatch costs in tokens.

## Criterion

Three live dispatches once the indexes exist: a question about an existing page, in
English, names its slug under `exists`; the same question in Russian names the same slug;
a proposal crossing a known rule (a `SessionStart` hook meant to block) names the rule or
lesson under `rules`. Each answer is the five lines, no index or page text reaches the
caller's context, each dispatch is in the event log; the reading records whether `@`
expanded and the tokens of one dispatch.

### case 105.1

When:
A question to `ask-guppi` names a slug.

Then:
The `tags/slug` line says one of three: `free`; `live` (with the category); `archived at <path> by [[decision-case-N]]` — by a Glob `vault/archive/**/<slug>.md`, `N` from the `origin` of the page found.
**＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn; it answers from its Result, `origin` and History.
**＋** `estimate-ask-finds` gets a `### case 105.1` block, `pending`.
**－** The archive is not searched by meaning: the `exists` and `near` lines are live pages only.

## Method

Three readings by hand in one session, written into the estimate line — the exception the
Method rule allows.

## Result

block 105.1: ask-guppi asked for estimate-agents-at-import-not-expanded answered "archived at vault/archive/migration/2026-09-11/estimates/… by [[decision-case-53.1]]", opened the archived page because the question asked what it said, answered from its origin and History (no Result on the page); five lines, 4 tool uses, 18895 tokens; the pretask dispatch (17 items, 91955 tokens) answered per item in the five lines too

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 105.1 added · [[decision-case-105.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L39
