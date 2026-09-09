---
title: "The brief carries the commit it was generated at, because a stale brief looks exactly like a fresh one"
type: decision
status: current
authority: brief-staleness
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: [".claude/skills/ingest/SKILL.md", ".claude/hooks/session-brief.ps1", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md"]
tags: [vault, process]
---

# `generated-at:` is the second line of the brief

**Decided 2026-08-13**, by the whole-branch review's loop lens. Two lines sit immediately under the
title — the short commit id of `HEAD` at the moment the brief is written, and the journal it was
written from:

```
# Brief — 2026-08-13
generated-at: 76df44e
ingested: 2026-08-13-second-brain-phase-2.md
```

They must stay within the brief's **first six lines**, which is all the hook reads: further down,
a line beginning `ingested:` is quotation rather than a stamp.

**Rejected: trusting the ingest to be the last thing a session does.** It was not, for six commits
of the very branch that built this vault. The brief that shipped in the middle of it said task 10
was not done, the skills were uncommitted and `sprint.md` did not exist — all three false by the
time anyone read it, and a session believing them would either redo finished work or "restore" a
file it thought had been truncated.

## The failure this closes is that the two states are indistinguishable

A brief overtaken by six commits **reads exactly like one generated a minute ago**. Nothing in the
text says which it is, the reader has no reason to suspect it, and it is the first thing they read,
so everything after inherits it. The ingest skill's own words for that state are *"the worst
available outcome"*.

[[session-hooks]] makes it mechanical, and says so above the brief with the number of commits in
between and the `git log` command that lists them.

## Two failures, reported separately, because they are different

- **commits have landed since the brief was written** — an ingest ran, and then work landed after
  it;
- **`ingested:` is not the newest journal in `raw/handoffs/`** — no ingest ran at all; the last
  session wrote its handoff and stopped.
  *(**That is not what the hook has asked since 2026-08-17** — it asks for sidecar absence, and of
  `ingested:` only whether the file it names exists. See the correction at the foot of this page.)*

**Neither comparison may use a file's mtime**, and that is the second decision on this page:
a `git checkout` rewrites every timestamp, and a fresh clone rewrites them in index order, which
made the mtime version of the journal check fire on every single clone. A commit id and a file name
are the two things a checkout does not touch.

## What it obliges, and the way it is got wrong

**Run `git rev-parse --short HEAD` at the moment the brief is written**, and never carry the
previous brief's stamp forward. The brief is derived and regenerated whole
([[journal-vault-brief-each-artefact-has-one-owner]]); copying its stamp is the same act as hand-editing it, and it
leaves the one human-readable answer to *"when was this written"* pointing at the wrong session.
**And name the journal in `ingested:` exactly as the file is named** — that line the hook does
compare, and a typo in it warns for ever.

The stamp is a signal for the reader, not a gate: staleness is reported, never enforced.

## What the stamp cannot answer, and what asks the question instead

**`generated-at:` is not compared to `HEAD`, and the reason is arithmetic.** A brief is generated
and *then* committed, so the stamp is **one commit behind by construction** — comparing it would
warn on every session for ever, which is the false-alarm failure this vault has already written
down twice ([[vault-scripts]], on why two of its conditions are advisories rather than errors).
The first version of the check did exactly that, and it was found and removed within the hour, on
2026-08-13, by the session that had written it.

This is one of **two** staleness checks, and they run at different moments and ask different
questions — the other is step 8 of `/ingest`, before the brief is even written:
[[staleness-checks-run-at-different-times-and-ask-different-questions]].

**Staleness is asked of git history instead**: the commit that carries `brief.md` is the zero
point, and the question is how many commits have landed after it. A brief with **uncommitted**
changes is newer than any commit and is therefore never stale.

`generated-at:` stays, and its job is now precisely stated: **provenance a human can read without
running git.** `ingested:` is the one line the hook still compares, by name.
*(**False since 2026-08-17.** See the correction at the foot of this page.)*

The general form is worth more than the incident: **a self-describing stamp cannot report on
events that happen after it is written.** Ask the artefact that records order — here, git — and use
the stamp for what a stamp is good at.

## It is a seam, which is why no per-task review found it

Nothing was wrong with the ingest, with the brief's shape, or with the hook. What was wrong was the
join between them — the assumption that the last thing to run is the thing that records where work
stands. That is the argument for the whole-branch review at three lenses being kept:
[[how-a-slice-is-executed]].

# Correction: the hook stopped comparing `ingested:` by name on 2026-08-17

**Two sentences on this page describe a comparison the hook no longer performs.** They said that
`ingested:` is *"the one line the hook still compares, by name"*, and that a mismatch against the
newest journal means no ingest ran at all. **`.claude/hooks/session-brief.ps1` selects by sidecar
absence** — it asks which journals have no `<name>.coverage.tsv` beside them, and asks of
`ingested:` only whether the file it names **exists**
([[the-sidecar-is-the-single-definition-of-compiled]], [[session-hooks]]).

**Why the change was made and why this page did not follow it:** a date prefix orders sessions only
while there is one a day, and two journals of 2026-08-16 made the sort return the earlier one. The
hook was repaired that day. The prose here, and the identical sentence in
`.claude/skills/ingest/SKILL.md`, were not — the skill's copy was repaired on 2026-08-20 in
`abd2a53`, and this page was found by the librarian at a `/pre-task` while that repair was being
made.

**The stamp's own job is unchanged**, and so is everything this page decides: `generated-at:` is
provenance a human can read without git, neither comparison uses mtime, and staleness is reported
rather than enforced. **What went false is the description of a mechanism, in a page whose subject
is something else** — which is the exact failure class this store keeps meeting, a copy going stale
where nothing checks copies ([[no-rule-reads-a-harness-file]],
[[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

**No rule page governs the brief's shape**, so a change to the hook reaches neither the skill nor
this page. The durable repair is a `wiki/rules/` page rendering a region into
`.claude/skills/ingest/SKILL.md`, and it is designed nowhere
([[the-harness-is-compiled-not-maintained]]).

**Reported as a miss on 2026-08-20 and corrected here rather than rewritten**: the page is
`basis: human` and the sentences above are left standing with a flag, because what a decision said
at the time is the record ([[the-region-coverage-figure-is-dated-where-it-stands]]).
