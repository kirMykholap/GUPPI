---
title: "The smoke runner is built first thing next session, its selection is named by the session rather than guessed, and a floor always runs"
type: decision
status: current
authority: smoke-runner-build-order
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check-selftest.sh", "scripts/hook-selftest.ps1"]
tags: [testing, harness, vault]
---

# The ruling, 2026-08-26, in his own words

> **owner:** «Строим обязательно. Это первый вопрос на следующую сессию!»

**A smoke runner is built, and it is the next session's first work.** It is the fast run over what the
session actually touched ([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]]).

# The design the session recommended, which he did not contradict

**The selection is named by the session, not guessed.** The session made the edits and passes what it
touched as an argument. **A session that edited rule 15 and ran rule 11's case proves nothing, and
nothing would catch that** — an inferred selection fails towards a green run
([[a-case-that-fails-for-its-own-reason-tests-nothing-either]]).

**One case is too thin.** A **floor** runs always, plus whatever the session names.

**Composition:** the three cheap selftests **in full** — `hook-selftest.ps1` at 2m17s,
`session-dialogue-selftest.py` at 52 cases, `vault-measure-selftest.py` at 59 — plus
`vault-check-selftest.sh` **narrowed**.

**Only the last is expensive, and the reason is structural**: it is the only one that copies the
corpus per case ([[the-selftest-is-a-mutation-test-of-the-gate]]).

# What it is blocked on

**A narrowing flag on `scripts/vault-check-selftest.sh` that does not exist.** Its shape is already
designed and not built ([[the-suite-gets-a-subset-mode-that-issues-no-verdict]],
[[the-suite-gets-a-narrowed-fast-mode-and-one-full-run-at-the-end]]).

# The gap it leaves in the meantime

**For one more session there is no cheap check at all.** A session either runs the hour-long suite or
runs nothing — which is what made the suite's removal from the session loop and this build one
decision rather than two ([[the-suite-stops-running-every-session]]).

# Rejected

**Rejected: inferring the selection from the diff.** It is the shape that fails towards green.
**Rejected: a single case per run**, for the same reason.

# The composition was widened by the owner — 2026-08-26

**`gate` and `style` were added to the run**, so `smoke` is now the gate, then ruff over `src` and
`tests`, then the three cheap selftests whole, then `scripts/vault-check-selftest.sh --only`. His
ground: one command should cover the whole repository cheaply
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

**This widens the composition clause above and overturns nothing else on this page.** *A floor
always runs* and *the selection is named by the session rather than guessed* both stand exactly as
written, and the arrangement page restates them rather than replacing them. The clause above is
left as it was, because a widening is dated beside the text it widened and never written over it.

**What it was blocked on is no longer blocking.** `--only <pattern>` exists on
`scripts/vault-check-selftest.sh`, and the make variable carrying it is `ONLY=`.

# The blocker was discharged two days before the page said it blocked anything — read off the script 2026-08-26

**The section headed *What it is blocked on* is false and was false when it was written.** It is
left standing above and answered here, because a record of what a session believed is not repaired
by rewriting it ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**`--only <pattern>` is parsed at `scripts/vault-check-selftest.sh:31`**, beside `--list`, under an
argument contract that refuses an unknown flag with exit 2. Three properties, read off the file:

- **it skips a case before it costs anything** — the filter sits at the top of every dispatcher, so
  a skipped case never copies the corpus and never runs the gate
  ([[a-filter-sits-at-the-top-of-a-dispatcher-and-still-takes-the-case-number]]);
- **an empty pattern matches everything**, so a bare run needs no branch and is unaffected;
- **the tally says what it is not.** A filtered run prints
  `caught N, missed M - FILTERED by --only '<pattern>', K case(s) skipped; this is not a reading of
  the suite`, which is the same refusal-to-issue-a-verdict the proposal designed
  ([[the-suite-gets-a-subset-mode-that-issues-no-verdict]]).

**It landed in the session of 2026-08-24**, in commit `d6bceb2`, timestamped 2026-08-25 00:21 — that
session ran past midnight, and the script's own comment dates the argument contract to 2026-08-24.
**This session used it twice.**

**So the blocker is discharged rather than stale.** Nothing had to be built for it; what was missing
was a reading of the script. **The page recording the blocker was written on 2026-08-26 by a session
that had the flag available**, which is the shape worth keeping: a blocker asserted from a design
document instead of from the tree ([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

**And *The gap it leaves in the meantime* is spent with it.** *For one more session there is no cheap
check at all* described a session that never happened: `make smoke` exists, runs the floor with no
pattern, and was measured green
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

# It is built, and every clause of this page survived the build — 2026-08-26

**`make smoke` exists**, and the three clauses this page settled all hold in the file that runs it
([[the-makefile]]):

- **the floor always runs** — with no `ONLY=` the gate, `style` and the three cheap selftests still
  run, and that is a legal run rather than a degraded one;
- **the selection is named by the session** — `ONLY=<pattern>` is typed by whoever runs it and is
  never inferred from a diff;
- **the composition** is this page's three cheap selftests plus the narrowed suite, **widened by the
  owner with `gate` and `style`** so one command covers the repository cheaply
  ([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

**The blocker this page carried was never real**: `--only` had been in
`scripts/vault-check-selftest.sh` since 2026-08-24, and the clause is struck on the sprint rather than
here ([[the-suite-gets-a-subset-mode-that-issues-no-verdict]]).

**Measured: `SMOKE-EXIT: 0` in 66-70 s with no slice.** The narrowed suite adds about two minutes, and
its floor alone is 101 seconds
([[an-estimate-can-be-wrong-in-its-reasoning-and-not-only-in-its-number]]).
