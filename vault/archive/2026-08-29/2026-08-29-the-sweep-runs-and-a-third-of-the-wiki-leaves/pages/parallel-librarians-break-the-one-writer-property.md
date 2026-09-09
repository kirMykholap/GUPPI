---
title: "The one-writer property is a convention about who is dispatched, and a parallel fan-out breaks it silently"
type: lesson
status: archived
authority: one-writer-guarantee
basis: measurement
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md"]
tags: [vault, agents]
---

# Nothing serialises two librarians

**Observed 2026-08-14.** Four `vault-librarian` agents were dispatched **at once** for the
acceptance run. Two of them independently widened the `frontend` tag in `tags.md`, and the second
reported that the file **had changed underneath it between its read and its write**.

Both writes survived. That was luck: each agent happened to re-read immediately before writing and
to append surgically. A read-modify-write of the whole file — which is the obvious way to edit a
register — would have silently dropped the other's paragraph, and **nothing in this store would
have noticed**, because the result is a well-formed `tags.md` that passes every rule in
`vault-check.sh`.

## The guarantee's real shape

"The librarian is the only writer of `wiki/`" is a **convention about who is dispatched**, not an
enforced lock:

- there is no lock, no lease and no serialisation anywhere in the design;
- the `PreToolUse` guard cannot help — a payload does not say *who* is writing, and it never blocks
  ([[session-hooks]], [[the-librarian-writes-unattended]]);
- `git diff` — the mechanism that replaced asking permission — shows the **surviving** text. A lost
  update leaves no trace in it, because the losing write never happened.

**One writer at a time is a different claim from one writer**, and only the second was ever
written down.

## `tags.md` is the lost-update target specifically

It is the file **every** librarian wants: a question in Russian that reaches nothing ends in
widening an alias list ([[aliases-carry-the-question-across-languages]]), so any fan-out of
question-answering agents converges on the same few lines. `log.md` is next, for the same reason at
lower frequency. Wiki pages are comparatively safe — two agents rarely want the same page — which
is exactly why the danger sits where nobody was looking.

## What to do until something enforces it

**Dispatch librarians in parallel only for reading.** A fan-out that answers questions is fine;
the moment those agents may write, they are contending. If a parallel run must be allowed to write,
the cheap discipline is the one that accidentally saved this run: **re-read immediately before
writing, and append rather than rewrite** — never hold a copy of a register across a long turn.

`/vault-lint` is where an enforcement mechanism, if one is ever wanted, would be proposed; it is
not an ingest's call.

## The reading half was exercised for the first time — 2026-08-20

**Six read-only subagents were dispatched in parallel against `wiki/`, one per folder**, and this
page's rule is what permitted it without a new decision: *dispatch librarians in parallel only for
reading*.

**Nothing wrote.** Each scout collected what its folder held and reported; the librarian remained
the single writer ([[the-librarian-writes-unattended]]), and the design that would make this routine
keeps that property by writing to intermediate files
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]).

**Measured: 249 s of wall clock for 1028 s of work, 4.13x** ([[agent-round-trip-cost]]). **And the
correctness gain arrived before the timing one** — two scouts independently found a hole in work
already reported as verified ([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

**The lock built the same day protects the write half rather than restricting this one**: it
narrows on `subagent_type: vault-librarian`, and a read-only scout is not one
([[the-librarian-lock-hook]]).

## The sentence became a rule and now renders — 2026-08-20

**The owner asked for it while remembering that it already existed here**, and it does, verbatim,
under *What to do until something enforces it*. It is now
[[dispatch-librarians-in-parallel-only-for-reading]], `governs: CLAUDE.md`, `render: region`, and
its text reaches every session rather than waiting for someone to find this page.

**It qualifies on *irreversible if missed***, the second half of the core criterion
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]) — which is what this
page's own measurement established in 2026-08-14: a lost update leaves no trace in a diff, a log or
the gate.

**This page keeps `authority: one-writer-guarantee` and the rule carries `governs:` instead**, so
the pair does not read as two answers to one question ([[rules-becomes-a-type-of-its-own]]). The
incident, the measurement and why `tags.md` is the target specifically stay here.

**The other half of the pair was answered differently and on the same day**: the owner declined to
read diffs and accepted that risk, on the asymmetry that a diff-reading failure is findable and a
concurrency failure is not
([[the-out-of-band-write-pair-is-answered-by-a-rule-and-a-declined-risk]]).
