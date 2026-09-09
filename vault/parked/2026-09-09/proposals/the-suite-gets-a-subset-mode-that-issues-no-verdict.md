---
title: "The suite gets a mode that runs a subset and issues no verdict"
type: proposal
status: current
authority: gate-subset-mode
basis: inference
sprint: S3
created: 2026-08-25
decided_by: [[the-gate-flag-fork-is-recorded-and-nothing-is-built]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [harness, vault, testing]
---

# What it would be

**A mode of `scripts/vault-check.sh` that runs a subset of the rules, never prints `VAULT-CHECK: ok`,
and always exits 0.** The suite calls it where it needs one rule exercised; a human never does.

**It stands outside the prohibition on hiding a verdict behind a flag, on the same ground `--rules`
does**: a mode that issues no verdict has no verdict to hide
([[the-rules-flag-is-a-mode-rather-than-a-filter-and-stands-outside-the-flag-prohibition]],
[[the-tag-density-advisories-move-behind-lint]]).

# Why this shape rather than the flag

**The flag that skips the two delegated rules would have to overturn a live prohibition**, and the
owner could not decide that fork ([[the-gate-flag-fork-is-recorded-and-nothing-is-built]]). This
shape needs no overturn.

# What must be read before it is built

**Whether each selftest case asserts on an output line or on the exit code.** A mode that prints
differently moves every case that asserts on output, and the suite is the instrument two of S3's four
acceptance criteria are decided by ([[a-fixture-owns-every-end-of-what-it-asserts]]).

# What is open

- **Which subset.** Nothing names the rules a fast mode would run.
- **What it saves.** The gate's delegated rules cost 5.1 s of 15.3 s and the suite runs the gate
  about 171 times, but no reading exists for a subset mode because none exists
  ([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]]).

# It became a blocker rather than an optimisation — 2026-08-26

**The smoke runner needs a narrowed `vault-check-selftest.sh` and there is no flag for one.** That
makes this page's subject the thing standing between the owner's ruling and a working smoke run
rather than a way to make an existing run cheaper
([[the-smoke-runner-is-built-first-thing-next-session]]).

**The three cheap selftests go into smoke whole** — `hook-selftest.ps1` at 2m17s,
`session-dialogue-selftest.py` at 52 cases, `vault-measure-selftest.py` at 59. **Only this one needs
narrowing, and the reason is structural**: it is the only suite that copies the corpus per case
([[the-selftest-is-a-mutation-test-of-the-gate]]).

**"Which subset" is answered differently now, too.** The smoke selection is **named by the session**
that made the edits, over a floor that always runs — not derived, because a derived selection fails
towards green.

**It goes into the proposal page that settles the check system as a whole**, which is next session's
first work ([[a-proposal-page-settles-who-runs-which-check-and-when]]).

# The section above is false in its first sentence, and the flag it says does not exist is at line 31 — read off the script 2026-08-26

**"The smoke runner needs a narrowed `vault-check-selftest.sh` and there is no flag for one" was
already untrue when it was written.** The section is left as it stands and answered here
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**`--only <pattern>` is parsed at `scripts/vault-check-selftest.sh:31`**, landed in the session of
2026-08-24 (commit `d6bceb2`, timestamped 2026-08-25 00:21), and was used twice in the session of
2026-08-26. It skips a case before it costs anything, and it prints a tally that names itself as a
filtered one — *this is not a reading of the suite*.

**Two of this page's open questions are answered by what shipped, and one is not.**

| open question | state |
|---|---|
| *which subset* | answered by the arrangement: a floor always runs, and the pattern is named by the session ([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]) |
| *what it saves* | still open. No reading of a narrowed run against a full one exists |
| *whether each case asserts on output or on exit code* | still open as a question about the **gate's** subset mode, which is what this page proposes |

**What is discharged is the blocker, not this page.** The narrowing that shipped is on the **suite**
— it chooses which cases run. What this page proposes is a mode of the **gate** that runs a subset of
the *rules*, and nothing of that exists. `scripts/vault-check.sh` still evaluates every rule on every
one of the suite's invocations, which is the term the cost actually sits in
([[the-selftest-is-a-mutation-test-of-the-gate]],
[[every-recorded-fix-for-the-suite-attacks-a-constant-and-the-corpus-is-the-term-that-grows]]).

**So this stays `current` and stops being urgent.** It is an optimisation again rather than the thing
standing between a ruling and a working run.

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
