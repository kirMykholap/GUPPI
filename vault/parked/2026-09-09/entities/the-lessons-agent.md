---
title: "The `lessons-agent` — it reads past `lessons/`, because a lesson leaves when a page outside that folder cites it"
type: entity
status: current
authority: lessons-agent-file
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", ".claude/agents/lessons-agent.md", "archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns.md"]
tags: [agents, vault, process]
---

# The file

**`.claude/agents/lessons-agent.md`, written 2026-08-29**, 65 lines,
`tools: Read, Grep, Glob, Bash, Write`. It is the only reading dispatch here that holds `Write`, and
the reason is narrow: **its `Write` is for one thing, a proposal draft under `docs/`.** It writes
nothing into the vault — not `wiki/`, not the registers.

**A draft returned inside an answer is re-typed by whoever received it, and re-typing is where a
quotation stops being one.** That is the ground for the file rather than the returned-text
alternative.

## Its read scope is three folders, and that is the design

**`wiki/lessons/` together with `wiki/rules/` and `wiki/proposals/`.** A lesson leaves the folder when
a page *outside* `lessons/` cites it, so the citing folders are part of the subject: a pass reading
only `lessons/` cannot tell a lesson that is already handled from one that is waiting
([[a-citation-from-a-decision-takes-a-lesson-out-of-the-queue]],
[[lessons-become-a-queue-drained-into-proposals]]).

## What it does, and what comes back

1. **Groups the lessons by meaning** — not by date and not by tag. A group is a set one proposal would
   answer together.
2. **Rejects the singletons out loud**, because that list is the argument for the next run's shape.
3. **Drafts one proposal per group into `docs/`**, in the shape `wiki/proposals/` uses.
4. **Names, per group, the lessons it would retire.**

It returns the groups, the path of each draft, the singletons with why each grouped with nothing, and
what it could not judge — a lesson passed over in silence being one the librarian will assume was
cleared.

## Why it exists at all, and the ground that was withdrawn

**The judgement is separated from the pen.** The agent's job is grouping and drafting, and drafting
does not get cheaper as the folder shrinks ([[the-verdict-and-the-pen-are-held-by-different-parties]]).

**It was dropped and then not dropped inside one session, and the ground moved.** The first ground was
the size of its input — `lessons/` at 18 pages after the sweep of 2026-08-29, against the 182 the
collector's only earlier run read. That ground was withdrawn when the owner asked who would prepare
the proposal if the agent did not exist. **A ground that turns on a folder's size goes stale when the
folder changes; this one does not.**

# Its design was carried by no live page until this one

**The page that held it, `the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns`,
is in `archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/`.** It left
`wiki/` because four live proposals name it in `decided_by:` — a hook register, a `PreToolUse` net, a
plant-and-revert helper and a CR-byte census — and **every one of those is a draft it produced.** None
of them describes it.

**That is `caused` read as `carried`**, and it is the sharpest instance of the class the archival
criterion has: `decided_by:` records causation and the criterion reads it as carriage
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**So its read scope and its `docs/` destination were asserted nowhere live** between the sweep and this
page.

# The first run under this name, 2026-08-29

**129,641 tokens, 43 tool uses, 9m19s**, over 18 live lessons plus `rules/` and `proposals/`. Against
the collector's only earlier run — 388,649 tokens, 55 tool uses, 17m23s over 182 lessons — which
measures a smaller folder and not a cheaper agent.

**It returned four groups and one singleton, and drafted two proposals**, declining to draft the other
two and saying why: one group's remedy is a discipline already stated three times, and the other
argues against a criterion that is mid-flight.

**It corrected the journal it was given, twice.** The smoke-marker count was wrong in both halves —
three live pages carry the matching form once each, not two pages twice — and the page carrying the
unreachable-verdict claim is a live decision rather than a lesson.

**And the defect it was measuring fired on it.** Two rows stand in
`.superpowers/sdd/pre-task-ledger.tsv` at `2026-08-29T22:09:43` and `2026-08-29T22:09:58`, both
`smoke:0`, both written by the read-only `grep` it ran to count the occurrences — **from inside a
subagent holding no write tool** ([[the-smoke-gate-hooks]]).

# What it says will happen and did

**A draft proposing a harness change trips the subagent instruction-shaped-output filter.** The file
tells the agent to expect it, to say what it meant plainly, and neither to smuggle it past nor to drop
the finding.

# The split is strictly worse for tokens, and that was never the argument for it

**The session that built this agent let the split sound like an economy measure early on and withdrew
that ground later, but never stated plainly that it is WORSE.** It is.

**Each subagent pays its own setup** — finding the vault, reading its `CLAUDE.md`, building its own
picture of the corpus — **which the librarian would not pay.** Together the two agents cost **281,233
tokens and about twenty minutes** on their first run.

**And the cost is ADDITIVE, not substitutive.** Step 2b runs **before** the librarian's existing work
and removes no reading from it. `/ingest` hands both agents only the decisions and lessons **the
handoff carries**, and the librarian's own input has always been the handoff rather than the folders —
**so there was no reading to move off it.**

**What the split actually buys is two things, neither of them tokens**: context pressure taken off the
librarian, and a verdict from a party that does not hold the pen
([[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]).

**The one real overlap is `proposals/`**, read by this agent and by the librarian both, and nobody has
measured it.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`, extended 2026-08-30.)*
