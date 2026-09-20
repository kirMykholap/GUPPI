---
type: decision
case: "155"
status: current
update: ["[[rule-ask]]", "[[rule-prespec]]"]
supersedes: ["[[decision-case-154]]"]
origin: raw/2026-09-15/1110/ledger.md#case-155
sprint: migration
created: 2026-09-15
tags: [session, workflow, harness]
---

## Context

The description line of the Render of `rule-ask` says "One short question per Case". `CLAUDE.md` (the Render of `rule-case-protocol`) already says otherwise: a question before a `create` without a `ref`, and `/pre-task` asks once for the set. Session P dispatched `ask-guppi` six times, four of them before an `update` with a `ref`, about 355k tokens in subagents; there the page itself and two Greps would have given the `given`. Case 154 deferred the decision to this Plan Mode.

## Problem

Whether the text of `rule-ask` follows the practice: one question before a `create` without a `ref`, one at pre-task, an `update` with a `ref` reads the page itself. The Purpose of `rule-prespec` carries the same phrase, "The per-Case question to `ask-guppi`".

## Given

`rule-ask` (`draft`, `deferred_by: [[decision-case-154]]`, `render`, governs `.claude/agents/ask-guppi.md`): description "… One short question per Case."; its Purpose names the callers — the agent at pre-task, the librarian, the person — and does not say "per Case".
**＋** `rule-case-protocol` → `CLAUDE.md` line 88: "Before a `create` without a `ref`, ask the vault first … Dispatch the `ask-guppi` agent with one short question." — the `create` moment is ratified there already.
**＋** `rule-prespec` Purpose, line 20: "The per-Case question to `ask-guppi` asks "does this exist"; this one asks, once, "does this set hold together"."
**＋** `index.md` §11: "One tool, two moments: pre-task queries by intent before a decision exists; the librarian queries by finished content afterwards" — no conflict, unchanged.
**＋** An `update` with a `ref`: by this decision itself, the pages were read and `ask-guppi` was not dispatched.
**－** `estimate-ask-finds` `passed` at 11:1x today (147.2); `contract: same` does not touch it.

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-155
