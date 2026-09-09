---
title: "DIVERGENCE: the librarian ran the archiver that the approved plan gave to the session"
type: decision
status: archived
authority: archiver-runner-divergence
basis: human
binding: divergence
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md", "scripts/vault-archive.sh"]
tags: [vault, agents, process]
---

# The rule, and what was done against it

**The approved plan divided the work: the librarian writes `wiki/` and the registers, and the session
runs `scripts/vault-archive.sh`.** The librarian ran it.

**Reported in the turn it happened, not before it.**

# Why

**The ordering interleaves a register write and a move four times.** Each page leaving `wiki/` needs
its citations rewritten, its register line adjusted and then the script run, and the next page's move
depends on the previous one having landed. **Splitting that across three dispatches costs more than
the separation protects** — a librarian round trip costs 15-30 minutes whatever it is given
([[agent-round-trip-cost]]).

# What the division actually protects, and why it is unaffected

**The rule is that `wiki/` has one writer**, and it had one throughout: the party that ran the script
is the same party that writes `wiki/`. **The plan's division was about who performs a step, not about
who may write** ([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]).

**The script itself refuses more than a session would.** It will not release a page without a live
page naming it, and not a refused proposal without `decided_by:`, so the protection that matters
lives in the tool rather than in whose hand runs it
([[vault-archive-sh]], [[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]]).

# The rejected alternative

**Return, hand the script back to the session, and be dispatched again for the next register write.**
Three dispatches for one ordered sequence.

# What it obliges

**A plan that divides an interleaved sequence between two parties is the thing to catch at planning
time**, not at execution. The division was written as if the archive moves were a block at the end;
they are not, and the page ordering is what makes them not.

**Reporting in the turn is the floor and it was met.** A divergence taken silently and found later is
the failure this record exists to be measured against
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).
