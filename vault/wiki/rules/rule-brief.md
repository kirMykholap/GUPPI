---
type: rule
kind: Leaf
purpose: Prevents the next session from starting without the facts and the flags of this one
status: draft
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: ["[[estimate-brief-written]]"]
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Purpose

Prevents the next session from starting without the facts and the flags of this one,
written to [[brief]]. [[brief]] is a shop window, not storage: every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and pre-task finds it there. So the deferred list is capped, the flags are not,
and nothing in the brief is a decision.

## Render

<!-- rule-brief -->
Brief. Run `make lint` and keep its output. Rewrite `vault/wiki/brief.md` in full,
with these sections in this order:
- Where things stand: from the "What actually got done" section of `handoff.md` and
  the counts of the yaml, pages created and updated per category.
- Readings due: after `generate`, every Estimate whose `status` is `pending` or `failed` — one line per Estimate: the Estimate, the rule that stands `draft`, and where it is read, from the unticked `- [ ] read …` line of the session's `spec.md` or, when there is none, from the page's `method` (case 200.3); a `failed` one first, with the result of its reading in one line; nothing from the previous brief (case 168).
- Deferred: at most seven items — one per target of a `defer` entry in the yamls the walk named, every item of the previous brief's list whose decision no `supersedes` retired, and every Insight whose `status` is `open`. Rank by `severity` — the Insight's own, or that of the Insight related to a deferred Case — then by the number of briefs the item has stood in: the previous brief's count plus one. An Insight's line carries its slug, its `severity`, its `pattern` and its Proposal in one or two sentences; in Plan Mode it is a Case whose `recommend` starts from that Proposal, and it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its target.
- Flags, no limit: entries marked `incomplete`, `failed`, `near` or `unparsed`;
  failed Estimates; MOC candidates; stale defers; contradictions; the lint output.
- Readings at the close: `make test`, `make lint`, page counts.
When a fact the brief needs is in no input — the status of an Estimate, the severity
of an Insight — read it from the page and name the page in the report. Write facts
and flags only. Add no decision and no judgment of the work. A handoff flag that asks for a change of the sprint goes into Flags as a Case of the next Plan Mode; the sprint page changes by a Case, and `vault/wiki/sprint.md` is written by `guppi sprint`, never by you (case 209.6).

The brief has a second writer, the skill `carry` (`rule-carry-over`): it writes the same frame in the short shape — Where things stand names the conserved Spec by path, its Cases and what is not done on it; Readings due and Readings at the close are omitted; Deferred is the previous brief's list as it stands plus the `defer` items of this Spec by slug; Flags say what the vault does not know about this session; no cap of seven and no ranking (case 190.4).
<!-- /rule-brief -->

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
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the hub file linked for the graph (case 149.4) · [[decision-case-149.4]]
- 2026-09-15 updated: the second section is Readings due, sourced from the pending and failed Estimates after the run and the Spec's reading lines; What the next session does first retired (case 168) · [[decision-case-168]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-16 status: draft → built · cascade
- 2026-09-16 updated: the brief has two writers — the librarian and /carry; the short shape omits the sections of a run that did not happen and names the conserved Spec (case 190.4) · [[decision-case-190.4]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: the second writer and the short shape of the brief, one paragraph at the end of the Render (case 196.3, the text of 190.4) · [[decision-case-196.3]]
- 2026-09-16 updated: Readings due one line per Estimate, no block, the page's method field (case 200.3) · [[decision-case-200.3]]
- 2026-09-17 updated: the librarian never edits sprint.md — a sprint change is a Case, the file is the render of guppi sprint (case 209.6) · [[decision-case-209.6]]
