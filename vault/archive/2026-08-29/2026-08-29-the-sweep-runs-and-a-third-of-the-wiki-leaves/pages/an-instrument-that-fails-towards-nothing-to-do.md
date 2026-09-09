---
title: "An instrument that fails towards *nothing to do* is the dangerous direction to fail in"
type: lesson
status: archived
authority: instrument-failure-direction
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-archive.sh"]
tags: [harness, process, testing]
---

# The instance

`scripts/vault-archive.sh` escaped paths for `sed`. **The backslashes did not survive being written
into the file**, `probe/RUNBOOK.md` became `probe&RUNBOOK&md`, and the script reported

> **cited by 0 page(s)**

about **nine** pages that cite it ([[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[a-path-is-never-a-pattern]]).

**Caught only because the number was checked against a hand count** made before anything moved.

# Why the direction matters more than the failure

**Zero findings looks exactly like a clean tree.** An instrument that fails towards *nothing to do*
produces the output its user most wants to see, and nothing about that output invites a second
look. An instrument that fails towards *everything is broken* is investigated within the minute.

**So the design question for any detector is: which way does it fail when it fails?** And the
answer for a text-rewriting tool is almost always *towards zero*, because a broken pattern matches
nothing.

# The defence that worked, twice

**An independent count of what the instrument should have found, made before running it.** Here,
nine pages by hand. Elsewhere in the same session, the score line asserted to exist before anything
was read off a suite's output
([[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]).

**The same class, in the same store:** a suite whose counters lived in backgrounded subshells would
have printed `caught 0, missed 0` and exited 0
([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]); a `uniq -d` over a truncated match
reported duplicates that were not there
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

## One level down: the instrument can be a test, and the output it fakes is `caught N, missed 0`

**A selftest case pinned the sentence a refusal opens with and never read the command inside it.**
`scripts/hook-selftest.ps1` asserted the literal `THE CONDITION IS`, which survived intact while the
command beside it was mangled — **70 caught, 0 missed, over a refusal nobody could act on**
([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

**Same direction, different instrument.** A suite reporting zero misses is the output its reader most
wants to see, and nothing about it invites a second look. **The defence is the same one that worked
here twice**: prove the assertion can fail before believing it passed
([[a-case-that-passes-before-the-change-tests-nothing]]).

**And a third shape of the same failure, met the same session:** a `grep -n` printing one line was
read as a count, twice in forty minutes, and a first match is always smaller than a count
([[a-grep-that-prints-one-line-is-a-report-about-the-first-match-and-not-a-count]]).

# A fourth shape, and it is the cheapest to guard against — 2026-08-26

**A grep that returns zero deserves one second of disbelief.** `grep -c "^decision:"` over
`.superpowers/sdd/vault-feedback.md` returned **0**, and was one sentence away from being reported as
*the file is empty*. **The records begin with `- `.**

**The zero was true about the pattern and false about the question**, which is the same defect this
page names in three other shapes: an instrument that answers a narrower question in the voice of the
one that was asked ([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]]).

**The guard is a second's doubt and one line of the file.** A zero from a search is the answer most
worth spot-checking, because it is the only one that costs nothing to accept and everything to be
wrong about.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*

## A fifth shape: a suite that asserts no total cannot tell a case that did not run from one that passed — 2026-08-26

**`scripts/hook-selftest.ps1` reported `caught 169, missed 0` and exited 0 about a run in which five
of its cases never executed.** They were written as `LedgerText -match "x"`, which PowerShell parses
as a call rather than a comparison, so `Check` was handed a string where it takes a boolean, refused
to bind, and **neither counter moved**
([[a-statement-starting-with-a-bare-word-is-a-command-call-in-powershell]]).

**Nothing in the file asserted a total, so a case that vanished looked exactly like a case that
passed.** That is this page's own direction one level further in: the previous shape was a case that
*ran* and asserted the wrong thing; this one is a case that did not run at all, and the score line
shrank without saying so.

**The guard is not a count, deliberately.** An expected total would be a number every new case has
to update, which is the drifting-list shape this store repairs by deletion
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]). It asks the platform instead —
`$Error` filtered on `ParameterArgumentTransformationError*` — and fails a case of its own when the
list is non-empty. **The defence is still the one this page names: prove the assertion can fail
before believing it passed**, and the guard was proved by leaving a mis-parsed case in place.

**And the evidence was on the console the whole time.** Every run that session was piped through
`grep`, which is a reading of the filter's guesses and not of the report
([[a-truncated-report-hides-the-line-it-was-run-for]]).
