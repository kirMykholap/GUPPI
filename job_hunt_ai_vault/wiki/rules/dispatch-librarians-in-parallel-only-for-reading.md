---
title: "Dispatch librarians in parallel only for reading"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "[[parallel-librarians-break-the-one-writer-property]]", "CLAUDE.md"]
decided_by: [[the-out-of-band-write-pair-is-answered-by-a-rule-and-a-declined-risk]]
tags: [vault, agents, harness]
---

# What travels

<!-- text -->
**Dispatch librarians in parallel only for reading.** A fan-out that answers questions is fine; the
moment those agents may write, they are contending. If a parallel run must be allowed to write,
re-read immediately before writing and append rather than rewrite — never hold a copy of a register
across a long turn.
<!-- /text -->

**The sentence is cited, not invented.** It has existed verbatim since 2026-08-14 on
[[parallel-librarians-break-the-one-writer-property]], under *What to do until something enforces
it*, and the owner asked for it to become a rule while remembering that it already existed:

> **owner:** «Записать правилом: "параллельно — только на чтение". Но у нас уже было это правило,
> если я правильно помню. Если было - настало время выносить это в `CLAUDE.md`.»

The only edit the slice makes to that page's words is dropping *"the cheap discipline is the one
that accidentally saved this run"*, which is a fact about one incident and not an instruction.

# Why it cannot wait for a question

**It qualifies on the second half of the core criterion — *irreversible if missed***
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]). A lost update to
`tags.md` leaves **no trace in a diff, a log or the gate**: the losing write never happened, and the
result is a well-formed register that passes every rule in `vault-check.sh`.

That is not a hypothesis. Four librarians were dispatched at once on 2026-08-14, two of them
independently widened the same tag, and **both writes survived by luck** — each happened to re-read
immediately before writing ([[parallel-librarians-break-the-one-writer-property]]).

**A hook cannot enforce it**: a `PreToolUse` payload does not say who is writing
([[session-hooks]], [[the-librarian-writes-unattended]]). The lock built on 2026-08-20 narrows on
`subagent_type: vault-librarian` and protects the write half rather than restricting the read half
([[the-librarian-lock-hook]]).

# What it does not forbid

**Reading in parallel is permitted and has been exercised.** Six read-only scouts, one per folder,
ran against `wiki/` on 2026-08-20 — 249 s of wall clock for 1028 s of work — and nothing wrote
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]], [[agent-round-trip-cost]]).

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]) — into a paired comment named for this page's slug
([[a-region-is-a-paired-comment-named-for-a-rule]]). The region was marked and the injector run in
the same change this page landed in.

**It entered `CLAUDE.md` on the same day another rule left it**, and that is one criterion applied
twice rather than a reversal ([[a-rule-applied-in-opposite-directions-on-one-day-is-not-a-reversal]]).

# What is on the lesson instead of here

[[parallel-librarians-break-the-one-writer-property]] answers `authority: one-writer-guarantee` and
carries the incident, the measurement and why `tags.md` is the target specifically. This page
carries the instruction and carries `governs:` in place of an `authority:`, so the pair does not
read as two answers to one question ([[rules-becomes-a-type-of-its-own]]).

**The decision that both halves of the out-of-band write pair were answered together** — this rule,
and the owner's declining to read diffs — is
[[the-out-of-band-write-pair-is-answered-by-a-rule-and-a-declined-risk]].
