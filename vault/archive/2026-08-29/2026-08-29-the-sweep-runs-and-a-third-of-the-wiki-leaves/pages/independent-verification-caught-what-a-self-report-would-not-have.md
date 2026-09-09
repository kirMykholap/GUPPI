---
title: "Independent verification caught what a self-report would not have"
type: lesson
status: archived
authority: self-report-verification
basis: measurement
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "job_hunt_ai_vault/sprint.md", "scripts/vault-check.sh"]
tags: [vault, process, testing]
---

# The incident, 2026-08-28

**The librarian struck 23 answered items in `sprint.md` by writing over line ranges taken from a
section it had read unnumbered, and clobbered three items in doing so** — numbers 16, 17 and 18 of
*Carried from S2*. It caught the loss itself, restored from a backup and rewrote the pass under a
guard.

**The session did not accept the report.** It proved the repair against `HEAD` token by token: all
20,916 tokens of the file at `65f19ec` present and in order, 981 added, and the list of item numbers
identical.

# Why the report alone would not have been enough

**A confession names what its author noticed.** The question a reader has is whether anything else
went with it, and that is a different question from *did I notice a loss*.

**Nothing mechanical would have said so.** `scripts/vault-check.sh` does not read `sprint.md` at all
— the register has no schema and no page behind it — **so the gate was green in both states**, before
the clobber and after it. There was no instrument to consult
([[a-gate-guarantees-agreement-never-truth]]).

# What it obliges

**Assert that a range starts with the line you think it does, before writing it**, and compare a
before-and-after tally of anything numbered. That guard is what the repair pass ran under and it is
cheap: `grep -cE '^ *[0-9]+\. '` over the file, twice.

**Prefer an append to a range write on a register.** The failure is a property of addressing text by
line number in a file that was read without them, and a plan of this session cited a line number
that had already moved for the same reason
([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

**And it is one of the grounds the decisions agent was ruled read-only on**: a writer with nothing
between it and a shared register is the shape that produced this
([[the-decisions-agent-reads-only-and-runs-at-every-ingest]]).
