---
type: decision
case: "128"
status: current
update: ["[[rule-prespec]]"]
supersedes: ["[[decision-case-121]]"]
origin: raw/2026-09-14/1029/ledger.md#case-128
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness]
---

## Context

At pre-task of session M the dispatch to `ask-guppi` carried one summary line per decision; four of its ten findings answered things the plan's `then` blocks already did (`lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary`). `rule-ask` says "one short question"; `rule-prespec` says "dispatch the agent once with that list". (Case 121 as it stands.)

## Problem

The agent judged pages against a paraphrase and could not see the planned wording. The information it lacked must be in the dispatch: the `then` blocks — `replace` pairs, `set`, `sections` — or the path of the plan file, since the agent has Read. (Case 121 as it stands.)

## Given

`rule-prespec` (`Leaf`, `built`, `render` into `.claude/skills/pre-task/SKILL.md`, `estimate-prespec-reconciles` `passed`, `deferred_by: [decision-case-121]`): the Render's paragraph — "List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; … Dispatch the `ask-guppi` agent once with that list and the question: which of these contradict a page of the vault, a rule of `index.md`, or each other".
**＋** `ask-guppi` (`rule-ask`): tools Read, Grep, Glob; reads the indexes, opens a page by slug. The plan file lies outside the repository (`~/.claude/plans/<name>.md`), but Read takes an absolute path; the agent knows it — it writes the file.
**＋** The `when` + `then` sections are the criterion of the Case (what reaches the Estimate); the `then` block is the page text. The first says which event the change is bound to, the second in which words; `ask-guppi` needs both to name a wrong wording and a wrong place alike (the owner's addition).
**＋** The lesson `lesson-pretask-dispatch-…` is `new`, without an Insight; this is its fix.
**－** `rule-ask` is not changed: one question per Case, one dispatch per pre-task, as before.
**－** The Frontier line F8 closes on this Case.

## Criterion

- [[estimate-prespec-reconciles]] § case 128

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-128
