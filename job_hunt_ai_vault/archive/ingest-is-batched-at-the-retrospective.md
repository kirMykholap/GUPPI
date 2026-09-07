---
title: "`/handoff` runs every session and `/ingest` is batched at the retrospective"
type: decision
status: deprecated
authority: ingest-cadence
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, process, agents]
superseded_by: [[ingest-runs-after-handoff-at-the-end-of-a-session]]
---

# Decided 2026-08-16: the journal is per session, the compilation is per sprint

> [!NOTE] CONTRADICTION — RESOLVED
> **Retired by the owner on 2026-08-17.** This page and
> [[ingest-runs-after-handoff-at-the-end-of-a-session]] were both `current`, both
> `basis: human` and both dated 2026-08-16 — two live answers to *when `/ingest` runs*. The
> later page stands: **`/ingest` runs after `/handoff`, at the end of every session**, which is
> the cadence the repository's `CLAUDE.md` has stated all along and the one every session has
> actually followed. The word underneath the disagreement was **"retrospective"**, which names
> two rituals here — the end of a session and the end of a sprint — and this page read it as the
> sprint one.
>
> **The measurement below is not retired with the cadence.** The successor carries it forward
> in the form that survived: *one dispatch, sources compiled one at a time inside it*. What is
> withdrawn is the claim that the dispatch itself is per sprint.

**`/handoff` still runs at the end of every session** — the journal is the only thing the next
session inherits, and nothing else in the repository carries the reasons.

**`/ingest` moves to the retrospective**, run once over every journal written since the last one.

**The reason is measured, not preferred.** A librarian dispatch costs 15–30 minutes and **the fixed
cost dominates** ([[agent-round-trip-cost]]): three journals compiled in one dispatch cost about
what one journal costs in its own. Paying that fixed cost once per session buys nothing a reader
can name.

This puts `/ingest` on the same cadence `/vault-lint` already has
([[lint-waits-for-an-open-sprint]]), which is the cadence the owner's instructions note asked for.

## What it obliges

**Uncompiled sources accumulate, and they accumulate visibly.** `vault-coverage.sh` reports per
source, so an uncompiled journal is a named file with a report of its own rather than a silent gap
([[ingest-is-units-and-verdicts]], [[handoff-retires-only-when-every-unit-has-a-verdict]]).

Two things get worse with the batch and are worth expecting rather than discovering:

- **The brief is regenerated less often**, so its growth signal is sampled less often
  ([[the-growth-signal-is-the-brief]]).
- **Step 8 of an ingest compares a journal against the tree**, and a journal compiled three
  sessions late is compared against a tree that has moved on
  ([[fidelity-to-a-source-and-fidelity-to-the-tree]], [[staleness-checks-run-at-different-times-and-ask-different-questions]]).
