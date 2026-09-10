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

List every decision ratified in this Plan Mode, one line each: slug — decision type —
purpose. Dispatch the `ask-guppi` agent once with that list and the question: which of
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
