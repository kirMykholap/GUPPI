---
title: "Read-only scouts, one per `wiki/` folder, dispatched ahead of the librarian"
type: proposal
status: deprecated
authority: scout-dispatch-design
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md"]
tags: [agents, vault, retrieval]
superseded_by: [[the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched]]
---

# The design, raised by the owner 2026-08-20 and not built

**Read-only subagents, one per `wiki/` folder, dispatched in parallel.** Each collects only what its
folder holds against the units being compiled, and **writes it to an intermediate file**. The
librarian then reads those files and does its work.

**Writing stays with the one writer.** The scouts never write the wiki, so the design does not
weaken [[the-librarian-writes-unattended]] and does not pre-empt [[the-librarian-lock-hook]].

**And it is already permitted rather than new**:
[[parallel-librarians-break-the-one-writer-property]] rules *"dispatch librarians in parallel only
for reading"*.

# What it costs, measured rather than argued

**Six read-only `Explore` subagents, one per folder, dispatched together against six real claims:**

| folder | wall clock |
|---|---|
| rules | 89 s |
| proposals | 127 s |
| entities | 181 s |
| decisions | 185 s |
| concepts | 197 s |
| lessons | 249 s |
| **batch** | **249 s for 1028 s of work — 4.13x** |

A batch is as long as its slowest member. **592k subagent tokens over 203 tool uses**, recorded as
observed and neither converted to money nor restated as a rate
([[a-subagent-cannot-report-its-own-cost]]).

**The figure that decides the design is the per-dispatch floor, and it is 1.5 to 4.2 minutes, not
15 to 30.** That larger range belongs to a librarian doing full work and cannot be assumed of a
scout ([[agent-round-trip-cost]]). **So the fixed cost does not dominate** — which is the outcome
the design needed and did not have when it was raised.

# What it bought before it bought any time at all

**The scouts found a defect in work the session had already verified and reported as done**, and a
third of them refuted the *shape* of the proposed fix by citing a recorded lesson
([[a-hole-was-shipped-in-work-already-reported-as-verified]],
[[a-guard-remembered-per-file-is-forgotten-in-the-next-file]]).

**That is the half of the case that does not depend on the timing holding.**

# What is open

- **What fraction of a librarian round trip is read-only search.** Still owed, and **still free to
  collect**: the librarian's own tool calls are in its transcript. Without it, 4x on the reading
  half buys an unknown share of the whole.
- **What the librarian does with six intermediate files** — whether reading them costs less than
  the searching they replace, or merely moves it.
- **Whether a scout's answer is trustworthy without the librarian's own narrowing.** The scouts
  were given claims, not questions, and the store's retrieval discipline is written for a reader
  who walks links ([[the-folder-is-the-first-narrowing]]).

# What not building it costs

**The ingest stays one long round trip.** Nothing else; there is no correctness cost, because the
scouts' correctness contribution can be had by dispatching them for a single question at any time.

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# The figure this page said was owed arrived, and it does not carry the timing case — 2026-08-20

**What fraction of a librarian round trip is read-only search**, from the ingest's own self-report:
79 calls, 41 read-type against 38 write-type, **first write 4m34s into a 24m30s run — 19% of elapsed
time before writing began**, the only counted figure among them. **11 of the 41 reads came after
writing started and are reads of its own output**, which no scout dispatched in advance can perform.
**Its estimate of the scoutable share is 20–30%**, and it is a self-report, weaker than the harness
figures beside it ([[a-subagent-cannot-report-its-own-cost]]).

**The arithmetic, on this page's own 4.13x:** 20–30% scoutable removes **15–23% of the wall clock —
three to five minutes of twenty-four** — and the six scouts that buy it cost **592k tokens against
the 224k the whole ingest cost.**

> **So the timing case for scouts does not survive its own measurement.** The correctness case —
> which found the `MIGRATION_CHECK` hole — stands on its own and is untouched
> ([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

**And the denominator this page argues against has moved.** *15 to 30 minutes* is the cost of an
**ingest**, not of a dispatch: a `/pre-task` question cost **5m54s** and a narrow write **1m24s**,
both from the harness ([[agent-round-trip-cost]],
[[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]). **A narrow librarian
dispatch is already inside this page's scout floor of 1.5–4.2 minutes**, which weakens the
comparison in both directions and is the reason a re-pricing is on the deferral list rather than
done here ([[the-deferrals-of-this-session-go-onto-the-sprint]]).

**Still `current` and still unbuilt**, and the librarian does not retire a proposal on arithmetic —
refusing it is the owner's ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# Refused, not built — 2026-08-21

**owner: ретайрить как отклонённый.** This page is retired to `archive/` and the refusal is
[[the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched]].

**What closed it was the consumer, not the arithmetic.** The arithmetic had already failed above, in
this page's own last section. What the session of 2026-08-21 added is that the phase a scout was to
perform became a script call: `scripts/vault-catalogue.sh` prints page, `authority` and `title` for
the whole corpus in **1.66 s**, and `/pre-task` now runs it in the caller's own context
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]], [[vault-scripts]]).

**The correctness case is not refused and is not retired with the timing case.** It stands where it
was found ([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

**Nothing on this page lived only here**, which is the check owed before a retirement
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]); the successor names where each
part is.
