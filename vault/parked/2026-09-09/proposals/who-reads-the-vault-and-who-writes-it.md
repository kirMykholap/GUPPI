---
title: "Who reads the vault and who writes it — the agent architecture behind the reading dispatches"
type: proposal
status: current
authority: agent-architecture-design
basis: human
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", "docs/who-reads-the-vault.md"]
tags: [agents, vault, process]
---

# What it would be

**Five actors, one writer.** The owner asked for the whole design in one place; the session wrote it,
and he ordered it saved to `docs/who-reads-the-vault.md` as the worked example of what a full proposal
looks like before the librarian compiles it. **This page is that compilation**, and it is not a copy —
one section of the document is false and is excluded rather than carried, below.

| Actor | What it is |
|---|---|
| **the session** | plans, writes code, runs the checks, reads the diff, commits. Never writes the vault. Holds the conversation with the owner, which is the only place a ruling is made |
| **`vault-librarian`** | knows how to search the vault and how to write it, and carries no goal of its own. Dispatches its own readers, waits, writes, and returns once |
| **`vault-ask`** | the single search entry point, forked. Finds and reports; writes nothing. Everyone uses it, the librarian included |
| **the decisions agent** | reads `wiki/decisions/` and returns one row per decision. Writes nothing |
| **the lessons agent** | groups `wiki/lessons/` by meaning and drafts the proposal that would retire each group. Writes only into `docs/` |

**Its governing sentence is that the verdict and the pen are held by different parties**, which is the
review rule applied to judgement ([[the-verdict-and-the-pen-are-held-by-different-parties]]).

# What is built and what is not

**Built on 2026-08-29** — the librarian's dispatch, both reading agents, and the two `/ingest` steps
that use them ([[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]],
[[the-decisions-agent]], [[the-lessons-agent]]).

**Not built** — `vault-ask` as `context: fork`, which is the single-entry-point half. It has no S3
item and no page of its own; the fork's mechanics are recorded at
[[a-forked-skill-starts-empty-and-a-subtask-fork-inherits-everything]] and the ruling that clears one
obstacle at [[the-feedback-region-leaves-vault-ask-and-the-destination-leaves-the-rules-governs-list]].

**Also not built** — the frontier section the brief would generate
([[the-frontier-is-a-general-working-concept-and-a-sessions-list-lives-in-the-brief]]).

# The section of the source document this page does not carry

> [!CAUTION] `docs/who-reads-the-vault.md` IS FALSE WHERE IT WIDENS `decided_by:`
> The document, at line 152 and in the artifact published from it, says `decided_by:` becomes legal in
> `entities/` and `concepts/`. **The owner ruled the opposite later the same session** — a decision
> that produced another entity goes to `archive/`, and if it produced a proposal the proposal is what
> gets built ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).
> **The widening is not compiled here as a live design**, and correcting the document is owed and was
> not done. That file is outside the vault and is not the librarian's to edit.

**How it was caught is the part worth keeping.** The session designed the widening, recommended it,
and the owner accepted it — and `/pre-task` then found that he had ratified the *narrowing* three
times, most recently on 2026-08-28 in words denying the premise directly. **It was stopped one step
before it was built**, after the document had been written and published.

**And the cost the design named only on one side**: widening the field would open a route by which a
**live** prohibition is archived because an entity page pointed at it, and `/pre-task` does not read
`archive/`.

# What it would take, and what is open

**A `context: fork` `vault-ask`, and the arguments it needs passed explicitly.** A forked skill has no
conversation history; everything the caller wants known travels as arguments, and what is not passed
does not exist. That is the contract and it is the line most likely to be got wrong in the building.

**The arithmetic, still.** This architecture *adds* reading dispatches to every session — measured on
its first run at 281k tokens across the two readers — inside a topic opened to reduce per-session
cost. **Nothing measures what the librarian stops reading** because the folders were read for it, and
an earlier attempt to net the two summed an isolated subagent's budget into the librarian's and was
wrong ([[a-subagent-cannot-report-its-own-cost]]).

**What a reading agent's failure does to the librarian** is undesigned.

# What it obliges

**Nothing in it may move the one-writer clause.** Every dispatch leaving the librarian goes to
something that reads and comes back, including — once `vault-ask` is the one way in — its own
searching ([[the-librarian-writes-unattended]], [[the-one-writer-rule-covers-the-registers-too]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`
and `docs/who-reads-the-vault.md`, whose `decided_by:` section is excluded as false.)*

# The `vault-ask` half was built — 2026-08-30, and the *Not built* list above is corrected here

**`.claude/skills/vault-ask/SKILL.md` is `context: fork`, `agent: Explore`, `background: false`, and
no longer dispatches the librarian.** It is the first `context: fork` in this repository
([[the-vault-ask-skill]]).

**The `Not built` list above still names it and is left standing rather than reworded**, because it is
the record of what was owed. **What is now unbuilt of this design is the frontier section the brief
would generate, and nothing else.**

**The owner arrived at the same design independently and the vault did not tell him it was already
written.** He said «поиск по vault должен происходить через vault-ask… Он не должен диспатчить
бибилотекаря. Это должен быть скилл с context:fork» — which is this page's own actor table and its
`Not built` line. **The session found that only after he had reformulated it.** The design had no
sprint item and no page of its own, so the store held it and nothing surfaced it: **a proposal that
carries a design is only found by whoever thinks to look in `proposals/`.**

**The obstacle this page named was cleared in the right order.** The feedback region left the skill
first and the destination left the rule's `governs:` afterwards — the order fixed on 2026-08-29,
because the reverse leaves an orphan region in a file the injector no longer writes
([[the-feedback-region-leaves-vault-ask-and-the-destination-leaves-the-rules-governs-list]]).

**The arithmetic this page asks for is still not done.** The dividend of the fork is unmeasured and the
measurement is named — the first real fork run against a librarian dispatch on the same question
([[the-dividend-of-the-forked-vault-ask-is-unmeasured]]). **And what a reading agent's failure does to
the librarian is still undesigned.**

**The `decided_by:` correction is still owed at its destination.** `docs/who-reads-the-vault.md:150-153`
still says the field becomes legal in `entities/` and `concepts/`. **Third session owed**, and that
file is outside the vault and is not the librarian's to edit.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
