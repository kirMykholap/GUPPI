---
title: "`raw/handoffs/` is swept whole today, and the forward-only clause of 2026-08-21 is overturned by the owner"
type: decision
status: current
authority: raw-sweep-backlog
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-archive.sh", ".claude/skills/ingest/SKILL.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-26, in his own words

> **owner:** «Тогда передай библиотекарю, что raw нужно почистить сегодня.»

**Every compiled journal leaves `raw/handoffs/` in this ingest**, not only the two it compiled.

# What it overturns, and the overturn is his

**The clause of 2026-08-21 said the opposite**, on his own word of that day — **сначала только
вперёд** — and step 12 of `/ingest` restates it: *"Only the source this ingest compiled. The 20
journals that accumulated before this step existed stay where they are — sweeping them is 480
`sources:` lines in one commit and is its own piece of work"*
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]], [[vault-archive-sh]]).

**That clause is struck rather than reinterpreted.** It was right about the size of the job and wrong
about when it would be done: five days of forward-only left twenty journals in the inbox, and he had
asked for them gone before — «сейчас в raw есть куча файлов, которые там лежат давным давно, хотя я
просил их убрать оттуда».

**The skill's step 12 is now false on this point.** It is a harness file the librarian does not
write, and correcting it is owed.

# Why it is the script and never a hand deletion

**He asked first whether he could simply delete the processed files himself.** The answer is no, and
it rests on a number rather than on caution.

**Measured 2026-08-26: 464 of the 682 live pages name a `raw/` file on their `sources:` line — 68% of
the corpus.** Hand-deletion would leave two thirds of the store pointing at nothing.

**The real width is larger than the 480-line figure the struck clause quotes**, which is the one place
the old reasoning also understated the job.

# The four constraints the run must respect

1. **A journal with no sidecar does not move.** Both of 2026-08-26's acquire theirs during this
   ingest, so the sweep runs after step 10 ([[the-sidecar-is-the-single-definition-of-compiled]]).
2. **Move and rewrite are one run.** Between them the gate is red, because a `sources:` path that
   resolves to nothing is a broken address rather than a wrong claim; a filesystem cannot make the
   pair atomic, so the script does both and then runs the gate itself.
3. **The rewrite is deliberately narrow** — only lines beginning `sources:`, only under `wiki/` and
   `archive/`. On 2026-08-19 a corpus-wide `sed` rewrote two **quotations** along with the addresses
   ([[sed-cannot-tell-an-address-from-a-quotation]], [[a-path-is-never-a-pattern]]).
4. **The recorded hazard on emptying `raw/handoffs/` is already repaired.** Two selftest cases used
   to depend on it being non-empty and failed loudly with the wrong diagnosis when it was not; both
   now plant their own file in `raw/notes/`, verified in `scripts/vault-check-selftest.sh` at this
   ingest ([[raw-gains-its-internal-structure-before-the-move]],
   [[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

# What is not in scope

**`raw/plans/`, `raw/specs/` and `raw/notes/`.** They hold frozen artefacts that are cited rather
than compiled, will never earn a sidecar, and a predicate widened to `raw/` would report them as
uncompiled forever ([[raw-holds-testimony-and-artefacts-are-frozen]]).

# What the sweep buys beyond an emptier inbox

**A non-empty `raw/handoffs/` starts meaning *work that was never compiled*** rather than *history
that piled up*. The uningested-journal alarm in `.claude/hooks/session-brief.ps1` reads sidecar
absence there, and it has had a permanent backlog to look past since the step existed
([[session-hooks]]).

# The sweep ran, and `raw/notes/` is deliberately left for the next session — the owner, 2026-08-26

> **owner:** «И еще заметил один момент: raw/notes остались. Это уже сделаем на следующей сессии»

**What ran:** 22 journals moved into `archive/`, **584 `sources:` lines rewritten**, each of the 22
runs exiting 0. Verified independently rather than assumed: **zero `sources:` lines naming
`raw/handoffs/` remain, and 680 name `archive/`.** The corpus stood at 722 live pages in 866 files,
and `authority.md` agreed with the tree on 706 slugs.

**What did not run:** `raw/notes/`. **Ten pages name it in `sources:`**, and two selftest cases now
plant their own file there, so **the folder cannot become empty without an edit to the suite** — a
sweep of it is not the same operation as this one was.

# The prose that names the old paths stays, and the repair is at the writer — 2026-08-26

**183 lines of prose in 124 pages still name `raw/handoffs/` paths that moved.** The set is not
homogeneous: **111 are the closing *Compiled from* signature and 72 are prose inside a claim**, and
part of the second group is **correct as written** — the address moved, not the sentence.

**They are not swept.** `sed` cannot tell an address from a quotation, and the detector that would
have was refused the same day on a measurement of nine pages
([[the-prose-path-detector-is-refused-on-its-own-measurement]]).

**The real repair is at the writer**: the librarian stops producing the signature at all, because
`sources:` already carries it machine-readably
([[the-librarian-stops-writing-the-compiled-from-signature]]).

**And the ground under the refusal moved by two orders of magnitude inside one session.** The
detector was refused on a population of nine with one true finding; hours later the same population
was 183. That is a measurement going stale faster than the decision resting on it, and it is recorded
here rather than treated as a reason to reopen anything
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).
