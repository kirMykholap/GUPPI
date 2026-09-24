---
type: decision
case: "388"
status: current
update: ["[[rule-prespec]]", "[[estimate-prespec-reconciles]]", "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"]
supersedes: ["[[decision-case-380]]"]
origin: raw/2026-09-23/1859/ledger.md#case-388
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness, ledger, tests]
---

## Context

The agent writes bookkeeping facts into a `context` — a page's status, a count, a case number, "no page holds this" — from memory or from a narrow search, and they can be wrong. Both live lessons of the Insight `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` are about a `context`: Case 363 and Case 378. Ask-guppi found both at pre-spec, though it was not told to read the `context`. The text rule of `rule-agent-writing` (case 359) does not hold the facts in memory. Case 380 deferred the Insight; this Case takes it up. Also, before dispatching ask-guppi the agent writes a list of the decisions (cases 198, 203.2): a copy of the plan written by hand, while ask-guppi can read the plan and the pages itself; only the slugs of the deferred decisions are needed, for case 186.2. At the pre-spec of this session the agent, on its own, answered the findings with one report — each finding numbered, the fix it proposed or why it was known, and two decisions for the person — before it showed the changed Cases; the person found the step right and asked for it to be written; the skill does not hold it. The translation step 387.4 adds belongs to this Criterion too. The Criterion of `estimate-prespec-reconciles` describes the steps of the skill and is replaced whole. Every item is an `update` with a `ref`.

## Problem

Is the text rule enough against facts wider than their check, or is a check due — and where?

## Given

`insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — the Insight the Case sets `actioned`.
**＋** `lesson-case-context-claim-wider-than-its-search` — its live child.
**＋** `lesson-case-context-bookkeeping-written-from-memory` — its live child.
**＋** `rule-prespec` — its Render is `.claude/skills/pre-spec/SKILL.md`, which dispatches `ask-guppi`.
**＋** `estimate-prespec-reconciles` — the Estimate of the steps of that skill.
**＋** `rule-agent-writing` — the text rule in `CLAUDE.md`: a claim no wider than its check.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-388
