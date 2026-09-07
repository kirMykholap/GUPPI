---
title: "The ingest rewired so the session dispatches and the librarian writes what comes back"
type: proposal
status: archived
authority: ingest-rewiring-design
basis: human
sprint: S3
created: 2026-08-28
decided_by: [[the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return]]
superseded_by: [[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]]
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, agents, process]
---

> [!WARNING] REVERSED 2026-08-29
> The decision this design was built on was reversed by the owner the next day: the **librarian**
> dispatches the reading agents and returns once. Read
> [[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]] instead. What is below is kept
> because the party that dispatches is the whole of what it designed, and the argument for the other
> arrangement is still the thing a reader may want.

# The order it would run in

1. **The session collects the material** — the journal, the tree comparison, the feedback drain.
2. **The librarian is dispatched once and writes `lessons/` and `decisions/`**, then returns.
3. **The session dispatches the lessons agent and the decisions agent in parallel**, both reading
   only, which is what makes the parallel half legal
   ([[dispatch-librarians-in-parallel-only-for-reading]]).
4. **The session hands their verdicts to the librarian in a pass of its own**, which sets the marks
   and regenerates the brief.

**The session dispatches because the librarian cannot**: `.claude/agents/vault-librarian.md:4`
carries `Read, Grep, Glob, Bash, Write, Edit` and neither `Agent` nor `Task`
([[vault-librarian]], [[the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return]]).

# What it would change in the file

**`.claude/skills/ingest/SKILL.md` today is one dispatch and one instruction.** The rewiring makes
it four steps with two dispatch points, and the instruction the librarian is given has to be split
in two — the writing half and the verdict-filing half — because the same agent is dispatched twice
with different work.

**Step 12, the archive of the source, stays last.** It moves the path `vault-coverage.sh` reads, and
that ordering is decided ([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]]).

# What it costs, unpriced

**An ingest is already the most expensive ritual here** — 271,465 tokens in 34m08s on 2026-08-26 for
one source, 477,941 in 70 minutes for two. **This adds two reading dispatches and a second librarian
round trip on top**, and no reading of the whole arrangement exists
([[agent-round-trip-cost]]).

# What is open

**Whether the two reading agents can genuinely run in parallel.** Nested dispatch has never been
measured here, and the parallel rule permits it only while both read — which is decided, but the
harness behaviour is not observed ([[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]]).

**What happens when a reading agent returns nothing.** The ingest must still finish, and no step
here says whether an empty verdict set is a pass or a fault.

**And whether the brief is regenerated before or after the verdicts land.** It is derived and is
written last, so a verdict pass after it would leave it one ingest behind
([[journal-vault-brief-each-artefact-has-one-owner]]).
