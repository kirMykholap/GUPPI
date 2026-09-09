---
title: "The ingest rewired so the librarian dispatches the reading agents and returns once"
type: proposal
status: implemented
authority: ingest-rewiring-design
basis: human
sprint: S3
created: 2026-08-29
decided_by: "[[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]"
supersedes: "[[the-ingest-rewired-so-the-session-dispatches-and-the-librarian-writes]]"
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/skills/ingest/SKILL.md", ".claude/agents/vault-librarian.md"]
tags: [vault, agents, process]
---

# The order it would run in

1. **The session collects the material** — the journal, the tree comparison, the feedback drain — and
   dispatches the librarian **once**, handing it the workflow.
2. **The librarian dispatches the decisions agent and the lessons collector itself**, and waits for
   their verdicts.
3. **The librarian writes** — the pages, the registers, the log, the brief — using what came back.
4. **The librarian returns once.** The session reviews afterwards, with `git diff`, `log.md`, the gate
   and the coverage report.

**One librarian dispatch, not two and not three.** That is the sentence the ruling turns on
([[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]).

# What it would take

**One entry in a tool list.** `.claude/agents/vault-librarian.md:4` reads
`tools: Read, Grep, Glob, Bash, Write, Edit`; adding `Agent` is the whole mechanical obstacle. Claude's
documentation says subagents may call subagents, which is the owner's cited ground.

**The process text moves into `.claude/skills/ingest/SKILL.md` and out of the agent file**, which is a
separate ruling of the same day
([[the-librarian-agent-file-carries-capabilities-and-the-ingest-process-lives-in-the-skill]]).

**The reading agents are unchanged.** They read and return; nothing about the one-writer clause moves
([[the-decisions-agent-that-reads-the-folder-and-returns-a-verdict-per-decision]],
[[dispatch-librarians-in-parallel-only-for-reading]]).

# What is open

**Nested dispatch has never been measured in this repository.** Whether a subagent's subagent reports
usage anywhere the main session can see it is unknown, and a subagent cannot see its own cost
([[a-subagent-cannot-report-its-own-cost]]).

**The arithmetic nobody has reconciled.** `/ingest` costs 271,465 tokens and 34m08s for one source
today. This design adds two reading dispatches — 143–230k for the decisions agent, and 388,649 tokens
and 17m23s for the lessons collector's only real run — plus a second librarian round trip, **at every
session**. Items 34 to 36 therefore raise the per-session cost that the optimisation topic's third
member exists to lower, and no page in the vault reconciles the two.

**What the librarian does when a reading agent fails** is undesigned. The session-dispatches shape had
the session's own error handling for free; here the failure is inside an agent that must still return
a coherent answer ([[a-dead-subagent-can-be-resumed-instead-of-re-dispatched]]).

# What it replaces

**The design where the *session* dispatches and the librarian writes what comes back.** That proposal
was written on 2026-08-28 and its causing decision was reversed the next day; it is retired rather than
corrected, because the party that dispatches is the whole of what it designed
([[the-ingest-rewired-so-the-session-dispatches-and-the-librarian-writes]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# Built, and the first run is this — 2026-08-29

**`status: implemented`.** S3 item 36 landed as commit `b3ebc52`: `.claude/agents/vault-librarian.md`
carries `Agent` in `tools:` and a table of the two subagents it may dispatch, and
`.claude/skills/ingest/SKILL.md` gained step 2b — dispatch both readers before any write — and step
3b. The four-step order at the head of this page is what ran
([[the-decisions-agent]], [[the-lessons-agent]], [[vault-librarian]]).

**It stays in `wiki/` while it is tested for having a live page that names it**, which is what the
`implemented` mark opens rather than closes; the archiver refuses the move without one and the refusal
is the test ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

## What the open questions read as after one run

**Nested dispatch reports its usage to the dispatching agent.** A subagent still cannot see its own
cost, but the librarian saw both of its readers' — 151,592 tokens / 69 tool uses / 10m24s for the
decisions agent, 129,641 / 43 / 9m19s for the lessons agent — which is the first time a figure of this
kind has reached `log.md` without passing through the main session
([[a-subagent-cannot-report-its-own-cost]]).

**The arithmetic is still unreconciled and is now larger, not smaller.** 281k tokens of reading were
added to an ingest, against a design whose parent topic is reducing per-session cost. **What nobody has
measured is the other half**: what the librarian no longer reads because the folders were read for it.

**What the librarian does when a reading agent fails is still undesigned**, and neither reader failed.

*(The `implemented` mark and this section compiled from
`raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
