---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

The brief is the whole handover between sessions; a flag left out is debt nobody sees.

## Criterion

After a live librarian run: brief.md holds the five sections in order; the deferred
list has at most seven items, each with its postponement count; every entry marked
incomplete, failed, near or unparsed in the yaml appears under flags, as does the
lint output; the brief states no decision; sprint.md changed only if handoff.md
asked, and as it asked.

### case 124.1

When:
The librarian writes `brief.md` by its frame (the Render of `rule-brief`).

Then:
The Deferred item of the Render reads: "Deferred: at most seven items — one per target of a `defer` entry in the yamls the walk named, every item of the previous brief's list whose decision no `supersedes` retired, and every Insight whose `status` is `open`. Rank by `severity` — the Insight's own, or that of the Insight related to a deferred Case — then by the number of briefs the item has stood in: the previous brief's count plus one. An Insight's line carries its slug, its `severity`, its `pattern` and its Proposal in one or two sentences; in Plan Mode it is a Case whose `recommend` starts from that Proposal, and it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its target."
**＋** `estimate-brief-written` gets a `### case 124.1` block, `pending`; read against the brief of the next librarian's run: the `open` Insights stand in Deferred by severity, with a count.
**－** `{supersedes:case 119}`: `decision-case-119` is superseded, `rule-brief` loses `deferred_by`.

### case 168

When:
The librarian writes `brief.md` by its frame.

Then:
The second section of the brief is "Readings due": after `generate`, every Estimate whose `status` is `pending` or `failed` — one line per `### case N` block: the Estimate, the block, the rule that stands `draft`, and where it is read — from the unticked `- [ ] read …` line of the session's Spec, or from the `Method` of the page when there is none.
**＋** A `failed` one stands first, with the result of its reading in one line.
**－** Nothing from the previous brief; the "not done" of the handoff stays in "Where things stand"; the section "What the next session does first" is retired.

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## Result

block 168: the brief of session S, read by hand: "Readings due" is its second section, after `generate` 3 `pending` and 0 `failed`, one line per block — the Estimate, the block, the rule standing `draft`, and where it is read: 175 and 169.1 from the unticked lines of `1809/spec.md`, 168 from the page's `Method`; no `failed` line; nothing from the previous brief; the "not done" stays in "Where things stand"; no section "What the next session does first"; the five sections in order

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L92
- 2026-09-14 criterion: case 124.1 added · [[decision-case-124.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L5
- 2026-09-14 status: passed → passed · raw/2026-09-14/1633/ledger.md#L1
- 2026-09-15 criterion: case 168 added · [[decision-case-168]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L3
