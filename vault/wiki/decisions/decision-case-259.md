---
type: decision
case: "259"
status: current
defer: ["[[rule-pretask]]", "[[rule-pretask-hook]]"]
origin: raw/2026-09-20/0527/ledger.md#case-259
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness, hooks]
---

## Context

The skill `/pre-task` — the Render of `rule-pretask` — checks the ratified set before the Spec is approved; the hook `guppi pretask` on `PreToolUse ExitPlanMode` (`rule-pretask-hook`) gates the approval on it. The person keeps the name "pre-task" for the query before a Case and wants the check named "pre-spec" everywhere the name is visible: the skill `/pre-spec`, the page slugs `rule-prespec`, `rule-prespec-hook`, `estimate-prespec-reconciles`, `estimate-prespec-checks-the-plan`, `estimate-prespec-hook-gates`, the module `guppi/prespec.py`, the command `guppi prespec`, the event-log mark `prespec`, the tests; the word in the Renders of `rule-skill-hi`, `rule-case-protocol`, `rule-ask`, `rule-hook-registry`, `rule-retro-commit`, in `glossary.md`, `case-schema.md`, `index.md`, and in the prose and Criteria of the live pages. Lessons and Insights keep their slugs: no decision creates or deletes them. Case 258 of this session builds the mechanism, an `update` with `rename`, and its Estimate is read live on the first real rename.

## Problem

Case 257 was drafted as five `update` items with `rename` plus the code, the Renders and a one-off migration of the word; it is not ratified in this session so that the mechanism of 258 is built and tested before it is used, and so that the Spec of this session stays buildable. The rename is the first item of the next session.

## Deferred

### [[rule-pretask]]

rename to rule-prespec by an update with rename (case 258), with the skill /pre-spec, the module guppi/prespec.py, the command guppi prespec, the mark prespec, the three Estimates and the word in every Render and live page; the first item of the next session

### [[rule-pretask-hook]]

rename to rule-prespec-hook in the same Case as rule-pretask; the refusal names /pre-spec, the mark it looks for is prespec

## History

- 2026-09-20 created · raw/2026-09-20/0527/ledger.md#case-259
