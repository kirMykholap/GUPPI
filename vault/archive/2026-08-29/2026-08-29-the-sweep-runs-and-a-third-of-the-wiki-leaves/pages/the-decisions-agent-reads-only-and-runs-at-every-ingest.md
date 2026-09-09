---
title: "The decisions agent reads only, returns a verdict, and runs at every ingest"
type: decision
status: archived
authority: decisions-agent-scope
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/agents/vault-librarian.md"]
tags: [vault, agents, process]
---

# It runs at every ingest, not once over the backlog — 2026-08-28

> **owner:** «Ты сам говоришь, что добавилось 84 страницы за один раз. Значит агент по обработке
> решений нужен каждый Ingest, иначе рост слишком быстрый»

**His correction of the session**, which had proposed a single pass over the backlog. The ground is
the growth rate: a one-off reading returns the folder to where it started within a week.

# It reads only, and the librarian writes the statuses

*(the owner selected it, 2026-08-28, from a proposal built on two things.)*

**The parallel-dispatch rule.** An agent that writes `wiki/` contends with the librarian on the
shared registers, whatever folder it is scoped to
([[dispatch-librarians-in-parallel-only-for-reading]],
[[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]).

**And this session's own incident.** The librarian's line-range write clobbered three items of
`sprint.md`; a writer with no reader between it and the register is the shape that produced it
([[independent-verification-caught-what-a-self-report-would-not-have]]).

**So it returns a verdict per decision and the librarian sets the mark**
([[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]]).

# What it is given, and what it decides

**Two clauses are mechanical and it is not asked about them** — `decided_by:` and
`binding: divergence` ([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).
**Everything else is its judgement**, because no further mechanical predicate is coming.

**Its `binding:` boundaries are the owner's** and it may not widen them
([[a-decisions-archival-condition-is-read-off-its-binding]]).

# Not built, and what it costs to be wrong about

**Nothing exists**: no agent file, no dispatch, no run. The design is a proposal of its own
([[the-decisions-agent-that-reads-the-folder-and-returns-a-verdict-per-decision]]) and the
rewiring that would dispatch it belongs to `/ingest`
([[the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return]]).

**Its three measured inputs, 2026-08-28**: 120 prose-only mentions, 269 unprocessed decisions, and
424 link occurrences into deprecated pages.
