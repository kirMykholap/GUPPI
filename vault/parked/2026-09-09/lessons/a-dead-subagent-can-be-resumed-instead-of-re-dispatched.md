---
title: "A subagent that dies mid-answer can be resumed instead of re-dispatched"
type: lesson
status: current
authority: subagent-resumption
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md"]
tags: [agents, process]
---

# The incident, with its numbers

The librarian **died on a 529 after 24 tool calls and roughly 98k tokens**, having read the corpus
and produced nothing at all. Its whole cost had been paid and none of its output existed.

**Resuming the same agent reused that context.** A fresh dispatch would have paid for the reading a
second time.

## Why the default instinct is the expensive one

The instinct on a failed subagent is to dispatch it again with the same brief, because that is what
a failed command invites. But a librarian round trip costs 15–30 minutes and most of it is **reading
the corpus**, not writing the answer ([[agent-round-trip-cost]]). A death near the end of the read
is the worst possible moment to restart from zero, and it is also the most likely one, because the
context is largest there.

**The agent cannot tell you any of this itself** — a subagent cannot see its own usage
([[a-subagent-cannot-report-its-own-cost]]) — so the figure above reached the record only because
the harness reported it to the main session and the main session wrote it down.

## The rule

**On a transport failure — a 529, a timeout, a dropped stream — try resumption before dispatch.**
Re-dispatch is correct only when the *brief* was wrong, because then the reading was aimed at the
wrong question and re-reading is the point.

The distinction is worth stating because the two failures look identical from the outside: an agent
that returned nothing.
