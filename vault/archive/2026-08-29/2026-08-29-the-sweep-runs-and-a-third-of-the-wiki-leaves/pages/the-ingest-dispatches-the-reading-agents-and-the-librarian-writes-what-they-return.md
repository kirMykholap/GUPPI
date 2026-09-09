---
title: "`/ingest` dispatches the reading agents, and the librarian writes what they return"
type: decision
status: archived
authority: ingest-dispatch-owner
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/agents/vault-librarian.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, agents, process]
---

# The ruling, 2026-08-28

*(the owner selected it, against his own original scheme, in which the librarian dispatched.)*

**The session dispatches; the librarian never does.** The order is: the session collects the
material, the librarian writes `lessons/` and `decisions/` and returns, the session dispatches the
lessons agent and the decisions agent in parallel — both reading only — and then hands their
verdicts to the librarian in a pass of its own.

# The three facts it was decided on, all measured this session

**The librarian carries no dispatch tool.** `.claude/agents/vault-librarian.md:4` lists
`Read, Grep, Glob, Bash, Write, Edit` — neither `Agent` nor `Task`
([[vault-librarian]]).

**Nested dispatch has never been measured in this repository.** Not once.

**And a dispatch costs 143,000–230,000 tokens**, from the twice-refused scouts design
([[the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched]],
[[agent-round-trip-cost]]).

# What it obliges

**`.claude/skills/ingest/SKILL.md` is rewired**, and the design of that rewiring is a proposal
rather than a record of anything built
([[the-ingest-rewired-so-the-session-dispatches-and-the-librarian-writes]]).

**The parallel half is legal because both agents read**
([[dispatch-librarians-in-parallel-only-for-reading]]). **The writing half stays serial and stays
the librarian's**, which is the property the whole store rests on
([[parallel-librarians-break-the-one-writer-property]]).

**And the librarian gains a return trip per ingest.** That is a cost nobody has priced: the
recorded ingest dispatches run 271,465 to 477,941 tokens each, so the pass that files the verdicts
is added to a figure already in that range
([[a-subagent-cannot-report-its-own-cost]]).
