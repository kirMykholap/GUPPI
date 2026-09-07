---
title: "A check that passed for the wrong reason becomes a rule verified by removal"
type: lesson
status: archived
authority: checks-that-pass-vacuously
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [testing, vault]
---

# Six of them, and the count is the finding

Not six failures — six checks reporting **green while examining nothing, or the wrong thing**.
**Five are from the session of 2026-08-13; the first is older**, from the slice that built the two
pages, where it stood for a slice and a half:

1. the htmx swap-target invariant, satisfied by `<div id="collection">` written in **prose inside a
   script comment** ([[an-example-inside-a-code-block-satisfies-a-search]]);
2. the vault's link check, satisfied by **its own schema's examples**, `[[old-page]]` and
   `[[new-page]]`;
3. the same check, satisfied by a link written in **inline code** — an illustration of the syntax,
   not a link;
4. `VAULT-CHECK: ok` printed after an unquoted `$(find ...)` **word-split a path containing a
   space**: every read failed and the script examined nothing;
5. a **0-byte file** at the vault root satisfying a wikilink to a page that did not exist — the
   link resolved, the reader arrived at nothing, and because the file sat outside `wiki/` every
   other rule skipped it too;
6. **orphan pages regressing from 7 to 11 inside the wave that was fixing them**, because splitting
   one page into six turned one orphan into five, and nothing was watching.

The fifth is the sharpest: **it was introduced by the very commit whose message was about this
class of failure.**

## The rule, and why it is a rule and not an intention

**Every one of them is now a rule, and every rule was verified by removal** — the thing it should
catch was introduced, the check went red, then the thing was taken away and it went green
([[vault-scripts]], where `scripts/vault-check-selftest.sh` now does that mechanically — **61 of
61, 0 missed, measured 2026-08-15** by `bash scripts/vault-check-selftest.sh`; this line said 53
until 2026-08-14 and **55** until 2026-08-15, and both were true when written. Third value on one
line in two days, which is the shape [[a-stated-count-drifts-from-the-list-it-heads]] is about —
and the second time this particular line has been the instance).

**Five of the six live in `scripts/vault-check.sh`. The first does not**: its guard is a `pytest`
assertion in `tests/integration/test_web_vacancies.py`, which strips `<script>` blocks on **both**
the declaration side and the presence side before looking for a swap target. Same rule, different
build — and worth stating, because "it is in vault-check.sh" would send anyone re-checking it to
the wrong file.

**The orphan rule caught the next page written, within a minute of being added.** That is the
difference between a rule and an intention: an intention is a sentence in a document that the next
tired session will not re-read, and a rule fails the build.

**A seventh instance is one level up and is not in the list above**, because its subject is a
check rather than a document: the acceptance file states the answers it grades, so the vault can
satisfy it without being read — [[an-instrument-that-contains-its-own-answers-can-be-gamed]].

The general form is [[a-test-green-under-any-implementation]] — a test green under any
implementation is worse than no test — and the text-matching special case, with its own tally, is
[[an-example-inside-a-code-block-satisfies-a-search]]. What this class costs when the check is
prose rather than code: [[a-boundary-stronger-in-prose-than-in-code]].

## A seventh, and it is the delegating rule silenced by an empty stub — 2026-08-21

**Measured: with a zero-byte `scripts/vault-authority.sh`, rule 13 of the gate printed not one
line.** It ran, produced nothing, and reported nothing — so every case written for it would have
passed having tested nothing. **Rules 12 and 13 both ask their question by running a script**, which
is a shape this store chose deliberately and for good reasons
([[a-check-asks-by-running-the-writer-it-checks]]); the cost of that shape is that the check's
evidence is only as real as the tool's contents.

**The selftest's own sandbox manufactures exactly such stubs.** Its placeholder loop materialises
every path a page cites in `sources:` as an empty file, and both tools are cited. **What protected
them was only that the explicit `cp` runs before that loop and the loop leaves a real file alone** —
an ordering nobody had stated, on a page that had already named the hazard in the other direction
([[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]).

**The repair is a guard rather than a case**: the suite refuses to run at all if either delegating
tool is empty. A case would have to be written per rule, and the failure is a property of the
sandbox rather than of any one rule ([[vault-scripts]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
