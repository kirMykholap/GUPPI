---
type: rule
kind: Leaf
purpose: Prevents the next session from starting without the facts and the flags of this one
status: draft
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: rule-documentation
estimates: [estimate-brief-written]
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Purpose

Prevents the next session from starting without the facts and the flags of this one.
The brief is a shop window, not storage: every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and pre-task finds it there. So the deferred list is capped, the flags are not,
and nothing in the brief is a decision.

## Render

<!-- rule-brief -->
Brief. Run `make lint` and keep its output. Rewrite `vault/wiki/brief.md` in full,
with these sections in this order:
- Where things stand: from the "What actually got done" section of `handoff.md` and
  the counts of the yaml, pages created and updated per category.
- What the next session does first.
- Deferred: at most seven items — one per target of a `defer` entry in the yamls the walk named, every item of the previous brief's list whose decision no `supersedes` retired, and every Insight whose `status` is `open`. Rank by `severity` — the Insight's own, or that of the Insight related to a deferred Case — then by the number of briefs the item has stood in: the previous brief's count plus one. An Insight's line carries its slug, its `severity`, its `pattern` and its Proposal in one or two sentences; in Plan Mode it is a Case whose `recommend` starts from that Proposal, and it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its target.
- Flags, no limit: entries marked `incomplete`, `failed`, `near` or `unparsed`;
  failed Estimates; MOC candidates; stale defers; contradictions; the lint output.
- Readings at the close: `make test`, `make lint`, page counts.
When a fact the brief needs is in no input — the status of an Estimate, the severity
of an Insight — read it from the page and name the page in the report. Write facts
and flags only. Add no decision and no judgment of the work. Change
`vault/wiki/sprint.md` only when `handoff.md` tells you to, and only as it says.
<!-- /rule-brief -->

## Estimates

- [[estimate-brief-written]]

## Parent

- [[rule-documentation]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 estimate estimate-brief-written added · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a fact no input carries is read from the page and named · [[decision-case-54]]
- 2026-09-12 updated: the Deferred list comes from the defer entries of the yamls and the previous brief, not from the handoff (case 59.5) · [[decision-case-59.5]]
- 2026-09-14 deferred · [[decision-case-119]]
- 2026-09-14 defer by decision-case-119 superseded · [[decision-case-124.1]]
- 2026-09-14 updated: every open Insight stands in the Deferred list of the brief, ranked by its severity, with a count of the briefs it stood in, and is a Case of the next Plan Mode (case 124.1) · [[decision-case-124.1]]
- 2026-09-14 updated: an open Insight in Deferred is a live page, not a draft placeholder (case 132) · [[decision-case-132]]
- 2026-09-14 status: built → draft · cascade
