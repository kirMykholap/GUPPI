---
title: "The brief has no active-tasks section, because a section that never says anything trains the reader past it"
type: decision
status: current
authority: task-tracker-boundary
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-14
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, process]
supersedes: [[active-tasks-stay-empty-until-a-tracker-exists]]
---

# The section is removed, not kept empty

**Decided by the owner on 2026-08-14.** The brief's `Active unblocked tasks` section is **deleted
from the shape**, and must not be reinstated by a later ingest.

**Rejected: keeping it permanently empty** — which is what [[active-tasks-stay-empty-until-a-tracker-exists]]
decided on 2026-08-13 and why that page is now retired. A section printed at the start of every
session that reads *"None. No tracker is wired in"* is read once and skipped for ever, and skipping
is a habit that does not stay inside one section.

**The shape after this decision** is: `Alarms` (only when one holds), `Sprint`, `State`, `What must
not be broken`, `Hooks for this work`.

## What did *not* change, and it is the larger half of the old decision

The division of ownership stands: **the tracker owns task status; the vault owns what we learned
from a task.** A hand-maintained task list inside a derived artefact would be a second copy of
something that changes hourly, and it would be the copy people read. When a tracker arrives, the
brief **quotes its output verbatim** and never paraphrases it — a paraphrase of a task list is a
stale task list with a confident tone. Only the placeholder is gone.

## Why the earlier argument was right about the handoff and wrong about the brief

*Librarian's reading, marked as such.* The retired page justified the empty section by analogy with
[[the-handoff-template-maps-onto-the-categories]], where an absent section is never noticed as
missing while one reading "none" asks a question every time. **The analogy breaks on who writes
it.** A handoff section is written by a session that has to answer it, so an empty one extracts the
word *none* from someone who might otherwise have said nothing. A brief section is **derived** —
nobody is asked, and the placeholder answers itself. The same words do opposite work depending on
which side of [[journal-vault-brief-each-artefact-has-one-owner]] they sit on.

## Obliges

- `/ingest` step 9 carries the shape, and the removal is written there as an instruction rather
  than an omission, so that regenerating the brief cannot quietly restore it;
- when a tracker is installed, this decision is what has to be revisited — the section returns with
  content or not at all.
