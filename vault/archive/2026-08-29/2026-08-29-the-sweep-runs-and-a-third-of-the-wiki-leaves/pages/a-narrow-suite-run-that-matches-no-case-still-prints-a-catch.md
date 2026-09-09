---
title: "A narrow suite run that matches no case still prints a catch, and it reads as a pass"
type: lesson
status: archived
authority: selftest-only-filter
basis: code
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The defect

**`--only` on `scripts/vault-check-selftest.sh` is a substring glob, not a regular expression.**
Line 255 is `*"$ONLY"*`. A pattern written with alternation — vertical bars — matches nothing at all.

**And the inline cases bypass the filter entirely.** So a run that selected no case still reports
`caught 1, missed 0 - FILTERED`, and the one comes from a case the filter never saw.

# Why that is worse than an error

**It reads as a successful narrow run.** The session of 2026-08-28 came within a step of accepting
it as the verification of its three new cases. Nothing in the output distinguishes *I ran your
cases and they passed* from *I ran none of them*
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**The failure direction is the dangerous one**: an empty selection resolves towards green, which is
the class this store keeps meeting ([[a-fixture-must-materialise-what-the-subject-reads]]).

# What was actually run, and what it does not license

**`--only processed` caught 3 and missed 0; `--only archived` caught 4 and missed 0.** Those matched
and are real. **Neither is a reading of the suite**, and the whole suite was not run on 2026-08-28
([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]]).

# What is owed

**Fix it or document it as a defect** — the flag is either a glob that says so in its usage line, or
a matcher that reports how many cases it selected. **A filter that cannot report an empty selection
is the same instrument as no filter**, and the subset mode already designed for this suite says the
run issues no verdict at all ([[the-suite-gets-a-subset-mode-that-issues-no-verdict]],
[[a-filter-sits-at-the-top-of-a-dispatcher-and-still-takes-the-case-number]]).
