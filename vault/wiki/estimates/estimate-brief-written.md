---
type: estimate
kind: QA
status: pending
target: rule-brief
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

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## Result

live 2026-09-10: brief.md holds the five sections in order; Deferred has 6 items, each with its postponement count carried from the previous brief plus one; every near entry (3), every incomplete entry, the failed old-harness entry and the lint output are under Flags; no unparsed line existed; the brief states facts and flags, the one imperative is an item for the next session; sprint.md is unchanged, as the handoff asked

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L92
- 2026-09-14 criterion: case 124.1 added · [[decision-case-124.1]]
