---
title: "The verdict and the pen are held by different parties, which is the review rule applied to judgement"
type: concept
status: current
authority: verdict-and-pen-separation
basis: human
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", ".claude/agents/decisions-agent.md", ".claude/agents/lessons-agent.md"]
tags: [agents, vault, process]
---

# The rule the agent architecture follows

**An agent that judged the corpus and then edited it would be countersigning its own testimony.** That
is the same sentence which makes the review of the librarian's work belong to whoever dispatched it —
the review that replaced asking permission belongs to the caller, never to the party being reviewed
([[the-librarian-writes-unattended]]).

**So the reading agents read and the librarian writes**, and their verdicts arrive as findings to act
on rather than as edits already made ([[the-decisions-agent]], [[the-lessons-agent]],
[[dispatch-librarians-in-parallel-only-for-reading]]).

# It is one round trip and not two

**The librarian dispatches its own readers, waits, writes, and returns once**
([[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]). The shape it replaced had the
session dispatch the readers and then dispatch the librarian, which is two round trips and one more
party holding a verdict it did not take.

**Parallel is safe here precisely because neither reader writes.** One reads `decisions/` and the
other `lessons/`; there is nothing to contend for, which is the condition the parallel-dispatch rule
already states.

# This ground replaced one that turned on a folder's size

**The lessons agent was dropped and then restored inside one session.** The first ground for dropping
it was the size of its input — `lessons/` at 18 pages after the sweep of 2026-08-29, against the 182
the collector's only earlier run had read. **A separate agent earns its existence only where its
output has a fixed checkable shape *and* its reading does not fit the caller's context**, and the
second clause fails at 18 pages.

**The restoration came from a question about its output rather than its input.** The owner asked who
would prepare the proposal from `lessons/` if the agent did not exist. The agent's job is grouping and
drafting; **drafting does not get cheaper as the folder shrinks.**

**A ground that turns on a folder's size goes stale when the folder changes; this one does not.** That
is why the separation of verdict from pen is written down as the governing sentence and the size
argument is recorded as withdrawn.

**The withdrawal is also a lesson about how the recommendation was made**: a cost argument was
advanced against a page whose product had not been read
([[a-recommendation-given-without-checking-its-subject-is-delivered-like-one-that-was-checked]]).

# What it does not settle

**It says nothing about cost.** Two reading dispatches plus a librarian round trip is more spend per
session, not less, and no page reconciles that against the optimisation the rewiring sits inside
([[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]], [[vault-scripts]]).

**And it does not reach the ordering problem.** A reader that grades something is supposed to run
after the last write to what it grades; at an ingest the librarian writes into the very folder the
decisions agent just judged, so a verdict is taken against the corpus as it stood when it read
([[the-audit-is-dispatched-after-the-writes]]). The arrangement is known and is answered by saying so
in `log.md` where a verdict and a write disagree, rather than by preferring one silently.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
