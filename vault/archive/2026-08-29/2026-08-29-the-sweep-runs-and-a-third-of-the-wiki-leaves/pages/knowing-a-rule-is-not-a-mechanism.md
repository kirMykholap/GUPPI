---
title: "Knowing a rule is not a mechanism, and the unchecked half of the title rule keeps producing violations"
type: lesson
status: archived
authority: knowing-versus-checking
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
tags: [vault, testing, process]
---

# Two measurements, one rule, one year apart in nothing but a day

**First.** Rule 10 of `vault-check.sh` exists because the librarian wrote a title carrying a
measurable quantity **one day after writing the rule forbidding it**
([[a-title-names-what-is-counted-instead-of-counting-it]],
[[the-title-check-asks-and-does-not-judge]]).

**Second, measured 2026-08-18.** The rule was extended to filenames on 2026-08-17
([[the-title-rule-extends-to-filenames]]); the check reads `title:` only. **11 filenames of 259
carry a quantity.** Nine predate the rule entirely, **two were created 2026-08-17** — the day it was
extended — and none was minted on 2026-08-18. The two that git dates 2026-08-18 were added by
`e51d390` at 00:00:38, which is the previous day's ingest.

**So the filenames are exactly where the titles were before they were checked**: a decision exists,
a check does not, and violations arrive from the party that wrote the rule.

# What the second measurement adds to the first

**The first could be read as carelessness.** The second cannot: it is the same rule, the same
author, held in the same session, with the half that is checked producing zero violations and the
half that is not producing two on the day it was extended.

**The variable is the check, and nothing else.** Rule 10 fired four times at the 2026-08-17 ingest —
two pages retitled, two answered in `quantity:` — while the unchecked half accumulated silently.

# The consequence for how a rule is landed here

> **A rule extended without its check is a rule that has not been extended.**

The remedy is already scheduled and deliberately split in two: **the filename detector is built
next session, separately from the eleven renames**, because only address-moving waits on the
rewriter-and-detector pair and the detector waits on nothing
([[a-rewriter-must-be-paired-with-a-detector]]). Ordering the detector first is the same argument
that put the fifth verdict before the first rule migration
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]) — **a corpus nobody can legally fix
is worse than one nobody is checking.**

This is the same family as [[no-rule-reads-a-harness-file]] and
[[the-hook-was-stricter-than-the-rule-it-enforced]]: what holds is what runs.

# Two miscounts in one session, both in measurements about the session's own record — 2026-08-21

**A measurement about attribution was reported with its two figures swapped, by the session
diagnosing exactly that failure class.** *28 English blocks* was said and written where 28 is the
Russian count and **25** is the English one. It reached chat, `.superpowers/sdd/vault-feedback.md`,
`.claude/skills/retro/SKILL.md` and a plan before being caught; all four were corrected.

**Then the count of the retro's own verdicts was miscounted too** — twenty-two said in chat against
twenty-one in the file — and **the file was corrected from a script rather than from the
conversation**, which is the only reason the second one was caught at all
([[a-stated-count-drifts-from-the-list-it-heads]]).

**This is the argument that the remedy has to be mechanical rather than attentive, made against the
party that had spent the session making it.** Care did not survive one session in which care was the
subject ([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# The session argued in prose what it broke in code — 2026-08-22

**Three instruments failed towards *nothing to report* in one session**, while that session spent its
day writing comments about exactly that class:

| the instrument | what it failed to say |
|---|---|
| `scripts/vault-authority.sh` | it ran half of a two-flag command and exited 0 ([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]]) |
| `scripts/vault-check-selftest.sh` | two cases ran, passed, and were never counted ([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]) |
| the sandbox's `governs:` reader | a third parser nobody had counted ([[the-count-of-a-fields-readers-lives-nowhere]]) |

**Each was caught by a different mechanism than attention** — arithmetic, a red tree, and running the
decider once on the day it was named. **That is the argument itself**: this page says knowing a rule
does not enforce it, and a session that knew the rule well enough to write it down three times
shipped two violations of it in the same hours.

**Three counting errors in the same session, all in measurements about the session's own record**,
and none was caught by reading carefully: the attribution split, the retro's verdict count and the
hook registration count. **The one that matters for design is that the corrected figure was written
into three files by hand** — one wrong reading propagated in a single step and no check anywhere
would have noticed ([[a-copied-list-drifts-and-a-sweep-cannot]],
[[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).
