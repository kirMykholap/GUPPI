---
title: "The `decisions-agent` — its modes, its verdicts, and the class no check will ever find"
type: entity
status: current
authority: decisions-agent-file
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", ".claude/agents/decisions-agent.md"]
tags: [agents, vault, process]
---

# The file

**`.claude/agents/decisions-agent.md`, written 2026-08-29**, 105 lines, `tools: Read, Grep, Glob,
Bash`. **It has no write tool at all**, which is the whole of its design: it judges and the librarian
writes ([[the-verdict-and-the-pen-are-held-by-different-parties]]).

It is the build of [[the-decisions-agent-that-reads-the-folder-and-returns-a-verdict-per-decision]],
with two changes the design did not carry — the cadence and the verdict names, both below.

## Two modes, and the mode is read from the prompt

| mode | what it reads | when it runs |
|---|---|---|
| **1 — the arrivals** | the decisions carried by one handoff | every ingest |
| **2 — the whole folder** | `wiki/decisions/` entire, grouped by the page each decision acts on | on demand, never as part of an ingest |

**If the prompt does not say which, the agent asks rather than guessing** — the two modes read
different amounts of the corpus and cost differently.

**Mode 1 is scoped to what arrived, never to the backlog.** That is the answer to the cadence
question the design left open, and it is the owner's: the folder grows faster than anyone reads it,
so the per-ingest read is the delta and the folder-wide read is a separate errand.

**Mode 2's job is the history a single pointer cannot carry.** Where two decisions act on one page
and neither supersedes the other, that is a finding to report rather than a choice to make.

## The five verdicts

| verdict | when it is given |
|---|---|
| `stands` | the constraint is still true and no other page carries it |
| `carried` | a live page already carries the claim — **and it is named** |
| `false` | the claim is no longer true; the successor is named, or its absence is stated |
| `undesigned` | a `binding: deferral` with no proposal and no rule naming it in `decided_by:` — a subject nobody has designed, not a decision about a design |
| `contradicts <slug>` | this page disagrees with another live page filed under a **different** `authority:` |

**The fourth verdict is called `undesigned` and never `topic`.** `topic` was the session's coinage and
appears nowhere in this corpus; the owner selected the other word before anything cited either.

**`contradicts` is the reason the agent exists.** Rule 3 of `bash scripts/vault-check.sh` compares two
`current` pages only under the *same* `authority:` slug, and is blind the moment two pages disagree
under different ones — it has nothing to compare. **Nothing mechanical will ever find that class**, so
a reader is the instrument.

**It returns only the rows carrying an action, plus the count of `stands` as a single number.** A
verdict of *everything is fine* repeated two hundred times is paid for by whoever reads it.

## The boundaries it may not widen, which are the owner's

- **A `prohibition` does not leave `wiki/` while it stands.** `false` and `undesigned` are not a route
  out for one that still binds.
- **A `deferral` leaves on the arrival of its term, and never on a citation**
  ([[a-decisions-archival-condition-is-read-off-its-binding]]).
- **Two clauses are mechanical and it is not asked about them**: a live page naming the decision in
  `decided_by:`, and `binding: divergence` — which currently selects nothing, the sweep of 2026-08-29
  having taken all 22 ([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**And it is told not to confuse `carried` with `caused`.** `decided_by:` means the page was *caused*
by the decision, not that it *carries the decision's claim*; a decision whose citing pages are drafts
it produced is not `carried`, and saying so is the finding.

## It writes nothing, and the shell prohibition is written into it

**No `sed -i`, no heredoc into a file, no short script that edits** — stated in the file because the
automated notice asking for shell writes reaches a subagent as readily as a session
([[file-content-is-written-with-the-tool-and-never-through-a-shell]]).

# The first run, 2026-08-29, and what it cost

**It was not dispatchable in the session that created it**, and it became dispatchable a few turns
later with no restart. Registration is delayed rather than deferred to the next session, and the delay
is unmeasured ([[claude-code-config-loading]]).

**Its first real dispatch was this ingest**, in mode 1 over nineteen arriving decisions:
**151,592 tokens, 69 tool uses, 10m24s.** It returned seven `contradicts` rows — six against the
arrivals and one pair it found on its own — twelve `carried` rows, and `stands: 8`.

**Mode 2 has still never run.** The live proof of the `contradicts` verdict against the two known
contradiction pairs was named in the approved plan as the check before an ingest, and it did not
happen: the agent was not dispatchable when the check was due.

**The verdicts were taken against the corpus as it stood when it read**, which is before this ingest
wrote into the folder it judged. That ordering is known and not worked around
([[the-audit-is-dispatched-after-the-writes]]).

# What it corrected in its first hour

**It found a live-versus-live pair nobody had asked it about** — `log.md` rotation, tied to the sprint
close by one live decision and to the session by one live proposal, neither naming the other. That is
the third instance of the slug-blind class the brief carries.

**And it caught a slug that resolves to nothing.** The journal cites
`the-verdict-comparing-a-markers-type-is-dropped-as-unreachable`; that string is a title, and the file
is [[the-unreachable-verdict-is-dropped-and-replaced]].

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
