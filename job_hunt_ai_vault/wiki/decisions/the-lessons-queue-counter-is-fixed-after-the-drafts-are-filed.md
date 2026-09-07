---
title: "The lessons-queue counter is fixed after the drafts are filed, and the queue's fall is recorded as an artefact"
type: decision
status: current
authority: lessons-queue-counter-order
binding: deferral
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/lessons-queue.py"]
tags: [vault, process, testing]
---

# The ruling, 2026-08-26

**`scripts/lessons-queue.py`'s counter — which reads *cited by a rule or a proposal* as *handled* —
is fixed after the drafts are filed, as an S3 item.** *(owner selected it.)*

**And the queue's fall from 104 is recorded as an artefact rather than as progress.** Filing the
five proposals the collector returned moves roughly 25 lessons out of the queue without any of them
being acted on ([[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]]).

# Why the order is this way round

**Fixing the instrument first would delay the writing the instrument exists to prompt.** The five
drafts were ready, the owner had ruled they be filed rather than held
([[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]), and the
counter's defect costs a misread number rather than a wrong page.

**The cost of this order is stated rather than absorbed**: the queue reading taken after the filing
is not comparable with the one before it, and any reading of *progress* across that boundary is
false. **This page is the note that makes the discontinuity legible**
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# Rejected

**Rejected: fixing the counter first, so the filing could be measured.** He took the simpler order
and accepted an unusable number for one cycle.

# What it obliges

**One S3 item**: teach the counter to see `decisions/` as a citer, and to distinguish *cited* from
*acted on*. **The floor it cannot reach is a second, separate item** — about a tenth of the queue
records a method that worked rather than a failure, and no proposal can ever drain those.

# The item was done on 2026-08-26, and its effect was three times what anybody expected

**Both halves landed in one edit to `scripts/lessons-queue.py`**: `decisions/` is read as a citer, and
the answer is printed as `CITED` beside `LANDED`
([[the-lessons-queue-counter-prints-cited-and-landed-apart]]).

**The queue fell from 100 to 37.** Neither this page nor the plan that executed it named a size for
the effect, and **120 of 165 lessons turned out to be cited by a decision**.

**That is a miss worth naming rather than a happy result.** A deferral that orders a repair without
estimating what the repair changes cannot be sequenced against anything, and this one moved the
single number the whole exercise is judged by
([[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]]).

**The floor item is still open and untouched.**

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
