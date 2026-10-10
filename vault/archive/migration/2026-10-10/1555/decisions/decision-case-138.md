---
type: decision
case: "138"
status: archived
update: ["[[insight-workflow-contract-change-leaves-its-derived-text-stale]]"]
origin: raw/2026-09-14/1229/ledger.md#case-138
sprint: migration
created: 2026-09-14
tags: [harness, render, workflow]
---

## Context

An Insight of severity 3, three children, all before 2026-09-12: Estimate criteria described the old contract after 15.1 (session A); `CLAUDE.md` was edited by hand as a file item while `rule-case-protocol`, whose Render it was, stayed (I); the live clauses of two Estimates were written against the files before the librarian applied the pages, and the first render broke them (J). Pattern: a derived text has no pointer to its source, and nothing checks the pair. Proposal: at pre-task, for each changed slug the Estimates whose criterion quotes it; for each `file` the Rule whose `governs` names it; a change without its pair is a finding.

## Problem

The path half is done: 59.6 — the `guard` hook refuses a hand edit of a governed file; 59.8 — `CLAUDE.md` is rendered from `rule-claude-md`/`rule-case-protocol`, a file item on it is impossible; pre-task `check_governed` — an `update` with `file:` on a path a live Rule `governs` is a finding. The criterion half is closed differently from the Proposal: since 72.1 the criterion is the Case's `when`/`then`, copied by the scripts as `### case N` blocks; `contract: changed` appends a block and sets `pending` by machine, `{supersedes}` removes the old block; 88.2 took the last stale live clause out of the prose. There is no hand-written criterion text left to go stale. No new child since 09-12 — seven sessions under the new model. Decide: is the Insight actioned.

## Given

`insight-workflow-contract-change-leaves-its-derived-text-stale`: `open`, `severity: 3`, children `lesson-estimates-criterion-stale-after-contract-change`, `lesson-render-governed-file-updated-as-rule-class-file`, `lesson-estimates-live-clause-stale-at-first-render`; all `clustered`, the last of 2026-09-12.
**＋** `rule-governed-files-hook` (`guard` on `Edit|Write|MultiEdit`, 59.6): a hand edit of a file a Rule governs is refused; `rule-claude-md` (59.8): `CLAUDE.md` is a Render, not a Rule-class file.
**＋** `rule-prespec` `built`, `estimate-prespec-reconciles` `passed`: `check_governed` — "an `update` item with `file:` on a path a live Rule page `governs`" — a finding (59.6).
**＋** `case-schema.md`, "`when` and `then` are the criterion" (72.1): the scripts copy `when`/`then` as a `### case N` block; `contract: changed` appends a block and sets `pending`; `{supersedes:case N}` removes a block; "nothing is signed in two wordings".
**＋** `estimate-claude-md-rendered`: 88.2 — "the stale live clause of case 59.8 leaves the Criterion prose"; passed today.
**＋** The cascade of 104.2: the three children go `archived`.
**－** An Insight is not a Leaf: no `contract`, no Estimate.
**－** The `## Criterion` prose of the older Estimates (before 72.1) stays as context; nothing checks it — and nothing reads by it: readings go by the blocks.

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-138
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
