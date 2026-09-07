---
title: "A planted offender is only proved by reading the planted file back"
type: lesson
status: current
authority: plant-and-revert
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, process]
---

# Two plants silently failed to plant, in one session

**A `perl` substitution and a PowerShell `.Replace` both left their target unchanged.** Neither
errored. The check was then run against an unmodified file, passed, and **the green run proved
nothing at all** — it proved the tree was still green, which it was before the plant.

**Both were caught by reading the planted file back**, and only by that.

# Why the idiom needs the read-back to mean anything

The plant-and-revert idiom exists because some verdicts cannot be exercised in a sandbox and must
be proved in the real tree
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]). Its whole
value is the claim *this check fires on this defect*. **If the defect was never introduced, the
claim is `true` for the wrong reason** — the same shape as a case passing on an exception it was
not testing ([[a-fact-about-code-was-generalised-from-its-neighbour]]).

**The plant-and-revert idiom is only as good as reading back what was planted**, and that half is
what saved it twice on the day it failed twice.

# The shape of the check

```
plant  ->  READ BACK AND ASSERT THE CHANGE IS THERE  ->  run  ->  revert  ->  read back again
```

It is an assertion inside a measurement harness, applied to the setup step rather than to the
result ([[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]), and it fails in
the safe direction: a plant that did not take is reported instead of being counted as a pass.

## The no-op run is the same defence with nothing planted — 2026-08-20

**Before translating `tests/integration/test_migrations.py`, the replacement tool was run over the
file with no replacements and `git diff` was read: empty.** That is what established that reading and
rewriting the file does not itself convert a `w/crlf` working copy against an `i/lf` index
([[line-endings-make-git-status-overstate-what-changed]]).

**It is the same move as reading a planted offender back**, minus the offender: the instrument is
exercised on a known answer before it is trusted on an unknown one. **Both were run this session and
both paid** ([[a-case-that-passes-before-the-change-tests-nothing]]).

**And the same tree supplied a fixture nobody had to plant at all** — the owner's file move made the
gate red for a real reason, which is what the librarian lock's acceptance test needed
([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).

# A third plant failed to plant, and this time nothing was read back at all — 2026-08-23

**A planted-offender case ran against a guessed filename.** `sed` reported *no such file*, the case
reported nothing whatever, and the run looked like a case with nothing to do rather than a case that
had not run.

**This is the page's own rule met from the other side.** The two earlier instances were plants that
silently did not change the file; this one is a plant that silently did not reach a file. **Reading
the planted file back would have caught all three**, and in this case the read would have failed
outright.

**The output is the hazard, not the typo.** A case that produces no line is the same shape as a case
that passed, and a suite reporting nothing about a case it never executed is
[[an-instrument-that-fails-towards-nothing-to-do]] inside the instrument that is supposed to catch
exactly that.

**The cheap defence is the one already written here**: exercise the instrument on a known answer
before trusting it on an unknown one — and for a plant, that means the filename is taken from the
tree rather than guessed ([[a-case-that-passes-before-the-change-tests-nothing]]).

# A third instance, 2026-08-30, and it carries a repair detail this page had not got

**The first draft of two repeal fixtures put their citing line into `index.md`.** `consider_page`'s
holder test greps `$VAULT/wiki` **alone**, so both cases were refused on the **first** precondition
while claiming to test the **third**, and reported `MISSED` for a reason that had nothing to do with
the mechanism under test.

**The repair is more specific than "put the citer in the right place".** The citer must sit **under
`wiki/`** and must name the slug as **bare text, not a `[[wikilink]]`** — because the page it names is
about to move to `archive/`, and a wikilink to it would then sweep as broken. **Two constraints, and
the second one only appears in fixtures for a page that is leaving.**

**The suite now carries three recorded instances of this class**, all found by reading the plant back
rather than by any check.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
