---
type: rule
kind: Leaf
purpose: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
status: built
enforcement: render
governs: .claude/skills/pre-task/SKILL.md
render_mode: full
parent: rule-plan-mode
estimates: [estimate-pretask-reconciles]
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Purpose

Prevents a set of ratified decisions from reaching the Spec with a contradiction between
them or with the vault. The per-Case question to `ask-guppi` asks "does this exist"; this
one asks, once, "does this set hold together". The skill records its own run through a
`!` substitution, which is what the pre-task hook looks for, and whoever calls it — the
agent through the `Skill` tool or the person — leaves the same line.

## Render

<!-- rule-pretask -->
---
name: pre-task
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---
Recorded: !`uv run guppi event pretask --session "${CLAUDE_SESSION_ID:-}"`

Run `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line
for every decision line of this session that has no item under its own Case in the plan,
for every item that has no line, for every line of `raw/<hi date>/<hi HHMM>/frontier.md` (the session's folder, case 73) still open or closed by a Case the plan does not hold, for every ratified Case with a line of a kind other than `defer` and no `tasks` block (a defer-only Case has no work, case 74), for every Estimate a `then` block creates or sets `pending` that no
task names, for every `file` item on a path a Rule page governs, for every Leaf `create` item without `method`, for every Leaf `update` item without `contract`, for every Case with two or more Leaf items that create or say `contract: changed` (split the Case), for every derived Estimate slug that names an existing page while the item has no `estimate_slug`, and for every `update` with `contract: changed` whose page carries no Estimate or more than one while the item names no `estimate_slug` (case 90.2); an Estimate has no line of its own (case 72.5). It also runs every record line of the session's window through `materialize.parse_line` and prints one line for each that does not parse, with its date and line number (case 75.2). Fix the plan, the frontier or the line for each, then run it again until it prints nothing.

List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; for an `update` that changes a page's contract, add the page's `estimates` and whether the Case updates their criterion — an Estimate whose criterion quotes the changed wording and has no update line is a finding. Dispatch the `ask-guppi` agent once with that list and the question: which of
these contradict a page of the vault, a rule of `index.md`, or each other. Raise each
finding as a Case, or say in one line why it is already known. Then exit Plan Mode again.
<!-- /rule-pretask -->

## Estimates

- [[estimate-pretask-reconciles]]

## Parent

- [[rule-plan-mode]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
- 2026-09-09 updated: dispatches `ask-guppi` · raw/2026-09-09/ledger.md#case-26.1
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a Case changing a page's contract names the page's Estimates; a stale criterion is a finding · [[decision-case-53.2]]
- 2026-09-12 updated: the skill runs guppi pretask --check on the plan file before ask-guppi; every decision line since hi has its item under its own Case, every item its line (the command lives in guppi/pretask.py under rule-pretask-hook, case 66) · [[decision-case-59.1]]
- 2026-09-12 updated: the check also reads the session's frontier.md — an open line or a closing Case absent from the plan is a finding (case 59.2) · [[decision-case-59.2]]
- 2026-09-12 updated: a Case without tasks and an Estimate without its reading task are findings (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: a file item on a governed path is a finding — a rendered file has no file route (case 59.6) · [[decision-case-59.6]]
- 2026-09-12 deferred · [[decision-case-68]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 updated: findings for a missing method, a missing contract, two contracts in one Case and a colliding derived slug; no line for an Estimate (case 72.5) · [[decision-case-72.5]]
- 2026-09-12 updated: the frontier of the session's folder (case 73.4) · [[decision-case-73.4]]
- 2026-09-12 defer by decision-case-68 superseded · [[decision-case-74]]
- 2026-09-12 updated: a Case with work, not a Case with lines: the defer-only exemption of the code is the wording (case 74, supersedes 68) · [[decision-case-74]]
- 2026-09-12 updated: a ledger line of the window that does not parse is a finding (case 75.2) · [[decision-case-75.2]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: a fifth form finding: the Estimate of a contract change is named when the page's list does not name it alone (case 90.2) · [[decision-case-90.2]]
- 2026-09-12 updated: the item's key is named estimate_slug, as case 86 ratified (case 99) · [[decision-case-99]]
