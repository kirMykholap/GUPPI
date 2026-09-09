---
title: "The decisions agent that reads the folder and returns a verdict per decision"
type: proposal
status: implemented
authority: decisions-agent-design
basis: human
sprint: S3
created: 2026-08-28
decided_by: [[the-decisions-agent-reads-only-and-runs-at-every-ingest]]
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md"]
tags: [vault, agents, process]
---

# What it would be

**A reading subagent, dispatched by `/ingest` at every ingest**, that walks `wiki/decisions/` and
returns one verdict per page. **It writes nothing.** The librarian sets `status: processed` on what
it names ([[the-decisions-agent-reads-only-and-runs-at-every-ingest]],
[[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]]).

**Its shape is the lessons collector's**, which is the one reading dispatch this project has already
run ([[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]).

# What it is given

**Two clauses it is not asked about**, because they are mechanical: a live page names the decision
in `decided_by:`, and `binding: divergence`
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**Its boundaries on the rest, which are the owner's**: a `prohibition` does not leave while it
stands, a `deferral` leaves on the arrival of its term and never on a citation
([[a-decisions-archival-condition-is-read-off-its-binding]]).

**Three measured inputs, 2026-08-28**: 269 unprocessed decisions, 120 prose-only mentions by a live
proposal or rule, and 424 link occurrences into deprecated pages.

# What it would cost, and what nobody knows

**A dispatch costs 143,000–230,000 tokens here**, and the lessons collector's own first run cost
388,649 tokens across 55 tool uses in 17m23s over a smaller folder
([[agent-round-trip-cost]], [[a-subagent-cannot-report-its-own-cost]]).

**Its yield is unmeasured and the first run is the measurement.** The corridor *between 150 and 269
will remain* is the price of not having measured it, and it is written down rather than narrowed by
guessing.

# What is open

**Whether it reads the whole folder every ingest or only what arrived since the last one.** The
cadence ruling says every ingest; it does not say the scope of each run, and 329 pages read every
session is a different price from the delta.

**How its verdicts reach the librarian.** The lessons collector returns families and drafts in its
answer; a per-page verdict over hundreds of pages is a different payload, and nothing here has
carried one yet ([[the-ingest-rewired-so-the-session-dispatches-and-the-librarian-writes]]).

# Built, and two of its clauses were overtaken — 2026-08-29

**`status: implemented`.** `.claude/agents/decisions-agent.md` exists and has run
([[the-decisions-agent]]). It stays in `wiki/` while it is tested for a live page that names it, which
that entity page is.

> [!CAUTION] THE FIRST SENTENCE OF *WHAT IT WOULD BE* IS FALSE AS BUILT
> **"Dispatched by `/ingest` at every ingest, that walks `wiki/decisions/` and returns one verdict per
> page"** describes what is now **mode 2**, which runs on demand and is **not** part of an ingest. What
> runs at every ingest is **mode 1**, scoped to the decisions the handoff carries.
> The section *What is open* below asked exactly this — *whether it reads the whole folder every ingest
> or only what arrived since the last one* — and the owner answered it by splitting the agent in two.
> The archived page carrying his original ground, `the-decisions-agent-reads-only-and-runs-at-every-ingest`,
> is `status: archived` and so is never asked for a successor.

**Both open questions are answered.** The cadence, above. The payload: it returns **only the rows
carrying an action** plus the count of `stands` as one number, which is what made a per-page verdict
over hundreds of pages a shape a caller can read.

**The verdict names moved too.** Five verdicts, and the fourth is `undesigned` and never the session's
coinage `topic`.

**The yield is still unmeasured**, because mode 2 has never run — S3 item 39 stands and the corridor
*between 150 and 269 will remain* is untouched.

*(The `implemented` mark and this section compiled from
`raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
