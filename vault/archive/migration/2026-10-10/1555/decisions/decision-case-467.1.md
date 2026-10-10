---
type: decision
case: "467.1"
status: archived
create: ["[[estimate-prespec-requires-a-backlog-item-decided-on-its-page]]"]
update: ["[[rule-prespec]]", "[[rule-case-protocol]]"]
origin: raw/2026-09-27/2050/ledger.md#case-467.1
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness, ledger]
---

## Context

`vault/wiki/backlog.md` has no state of its own. `guppi backlog` rewrites it whole from the pages that carry `deferred_by`, the open Insights, the `## Backlog` section of the sprint page, and the folders that hold `carry.md`. An item leaves when its source changes. For a deferred page, a Case carries `{supersedes:case M}`, and `generate.clear_deferred_by` then removes Decision M from `deferred_by`. The file changes only in the librarian's run and in `carry`, never while a session runs. The person saw a count that did not move because they read the file before the librarian's run over session 1819. That run took it from 19 to 16 items: cases 459, 462 and 463 removed `rule-claude-md`, `rule-one-judgment-one-implementation` and `rule-page-generation`. The cleared Insights of session 1255 are `actioned`, and neither is in the file.
The mechanism has two gaps. First, no script checks that a Case which takes an item from the backlog supersedes its defers. Case 429 asks for this, but `prespec` checks only the closer word of a `backlog` line. Second, `clear_deferred_by` clears every target in the superseded Decision's `defer` list. Case 220 and case 243 each defer both `rule-git-context` and `rule-github-issues`, so deciding one page would remove the other from the backlog undecided. Clearing page by page brings up a third point. Cases 459 and 462 decided their items with no decision line on the deferred page. From now on, a Case that decides a backlog item names the page on a decision line. When nothing on the page changes, an `update` with only `change` is enough; it applies and writes a History line, as case 439 showed.
The vault's answer: both new Estimates carry a `ref`, so no vault query is needed. A Glob of `vault/**/` finds no page for either slug.
What the frame changes: the sentence of `rule-case-check` "the Frontier left to `/pre-spec`", the case-429 paragraph of `rule-case-protocol`, the finding list in the Render of `rule-prespec`, the sentence of the `rule-backlog` Purpose on how an item leaves, the docstrings of `guppi/casecheck.py` and `guppi/generate.py`, and the `supersedes` line of the Criterion of `estimate-generate-writes-the-decision-page`. The hook of 467.2 is the only hook on `SubagentStop`. 467.1 and 467.2 apply one rule to the page of a `backlog` line: some Case among Case N and its sub-cases both names the page on a decision line other than a `defer` and carries each `{supersedes:case M}`. 467.1 applies it at pre-spec to the Case the closed line names. 467.2 applies it before showing, to each top-level Case of the answer that names the page.
Estimates not touched, and why:
- `estimate-prespec-checks-the-frontier` speaks of boxes and closers.
- `estimate-case-check-sends-back-a-faulty-case` promises that `judge` runs and that a finding goes back, not which checks it holds.
- The Criterion of `estimate-ratification-ledger-line-form` promises the `{supersedes}` blocks of a deferred decision taken up, which stays true. The added requirement, the page named on a decision line, is held by the new `estimate-prespec-requires-a-backlog-item-decided-on-its-page`.
- `estimate-backlog-renders` and `estimate-backlog-checks-the-file` promise the render from `deferred_by` and its check, which stay true. The update of the `rule-backlog` Purpose touches neither.
- `estimate-generate-cascades` archives a superseded Decision and leaves `deferred_by` alone.
- Line 32 of `estimate-git-context-current` records the past supersede of case 106 by case 115.

Not done:
- no checkboxes in `backlog.md`, and `guppi/backlog.py` is unchanged;
- `insight-hi-skill-substitution-checked-by-a-model-call` stays until a Case rewrites its Pattern and Proposal with `{supersedes:case 448}`;
- a `defer` of an Estimate or a lesson still writes no `deferred_by` (no case exists);
- a Decision superseded for one of its pages is archived by the cascade in the same run, while a page of its `defer` list that the Case did not name still links to it in `deferred_by`; lint accepts the link, and a later supersede still reaches the Decision, since `generate.find` reads the archive.

## Problem

A Case can decide a backlog item without retiring its defers, and nothing catches it. A Case that retires a defer shared by two pages clears both, although it decided one. The item should leave the backlog exactly when a Case decides it, page by page, and a Case that fails to make it leave should be sent back before it is ratified.

## Given

`rule-prespec` — the pre-spec check; its Render is the skill
**＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from `rule-prespec`, which lists the findings
**＋** `guppi/prespec.py` — `judge` and `check_frontier`, where the new function lives
**＋** `tests/test_prespec.py` — the tests of the check
**＋** `vault/raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session, whose lines name the source and the closer
**＋** `rule-case-protocol` — its case-429 paragraph says how a deferred decision is taken up; its Render is `vault/wiki/case-schema.md`
**＋** `estimate-prespec-requires-a-backlog-item-decided-on-its-page` — the new promise

## History

- 2026-09-27 created · raw/2026-09-27/2050/ledger.md#case-467.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
