---
title: "A rule that touches every page makes every unrelated test fragile, and the fix is in the harness rather than the rule"
type: concept
status: current
authority: global-rule-test-coupling
basis: code
sprint: S1
created: 2026-08-15
sources: ["scripts/vault-check.sh", "scripts/vault-check-selftest.sh", "archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md"]
tags: [testing, vault]
---

# Fourteen cases failed at once, and none of them was about the catalogue

Rule 9 of `vault-check.sh` asks one question — *is `catalogue.md` what
`scripts/vault-catalogue.sh` produces?* — and it asks it of the whole corpus. Adding it on
2026-08-15 broke **14 selftest cases in a single commit**, every one of them testing something
else: a missing `decided:`, a duplicate `authority`, an orphan. The selftest works by mutating a
throwaway copy of the vault, and **any mutation makes the catalogue stale**, so a rule that reads
every page turns every mutation into a second, unintended violation.

## The shape of the coupling

A check whose input is *the whole store* has an implicit dependency on every test that changes the
store. The dependency is invisible until it fires, and when it fires it fires everywhere at once,
which reads like the new rule being broken rather than like the harness being incomplete.

**The fix belongs in the harness, not in the rule.** The wrappers regenerate the catalogue *after*
the mutation and before the check — the same courtesy the harness already extended to the source
placeholders it creates for `sources:` paths that point outside the vault. Weakening rule 9 to
ignore the selftest's own writes would have been the other option, and it is the one that leaves a
rule which cannot fail.

**The two cases that are actually about the catalogue deliberately do not use the wrappers**,
because a wrapper that repairs staleness cannot be used to test that staleness is detected. That is
the general form: *the harness may hide a global rule from every test except the ones that assert
it.*

## Why this is worth a page rather than a commit message

Two of this vault's standing rules are exactly this shape and will meet the same problem the day
they are extended: the **orphan** rule reads every link register, and the **tag** rules read every
page's frontmatter. The next global rule added here will break the suite in the same way, and the
question to ask first is *which cases are now coupled to it*, not *why is my rule failing*.

It also sits on top of a live trap: the catalogue must never join the link registers, or the orphan
rule would keep passing and prove nothing — and the case that holds that line is one of the two
that must not be wrapped ([[the-catalogue-is-generated-not-maintained]], [[vault-scripts]]).

A suite where a green run means nothing is the failure this whole family is about
([[a-test-green-under-any-implementation]], [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## The cost was paid back on 2026-08-17, and the shape returned the same day

**Rule 9 is retired** with the file it guarded ([[the-page-list-is-a-query-not-a-generated-file]]),
and the `regen_catalogue` wrapper went with it. The numbers this page argued from are now the
numbers of a thing that no longer exists: **rule 9 broke 14 unrelated selftest cases when it was
added, and its wrapper cost 43 seconds of the suite's 201, measured.**

**Rule 12 is the same shape** — it asks its question by regenerating over the whole store
([[a-check-asks-by-running-the-writer-it-checks]]) — and it reached exactly **one** case on the day
it was written, **only because no region exists yet**. The coverage advisory reads `0 of 13`.

**So the coupling is deferred, not avoided.** When markup begins, the question to ask of a red
suite is **which cases are now coupled** — not why rule 12 is failing. That is the sentence this
page exists to have ready in advance, and it is written down now rather than rediscovered under a
red run.

## The coupling arrived on 2026-08-17, exactly as this page said it would, and the number is measured

**The first rule migration coupled three existing cases**, and the question the session asked was the one
written above — *which cases are now coupled* — rather than *why is rule 12 failing*.

| Case | Why the migration broke it | The repair |
|---|---|---|
| `inject_vault_relative` | it needed a path that does **not** resolve at the repository root, and `CLAUDE.md` now does | the case moved to `index.md` |
| the coverage case | it asserted `cover 1 of`, **a number that moves with every migration** | it now asserts that the file it marked stopped being listed as unmarked |
| `empty_vault` | it left a governed file carrying a region whose page it had just deleted | it sweeps the regions out too |

**The second repair is the one worth keeping.** An assertion on a coverage *number* is an assertion about
the whole corpus; an assertion that *this file left the unmarked list* is about the case's own mutation.
That is the same move as re-deriving a count instead of carrying it
([[a-stated-count-drifts-from-the-list-it-heads]]).

**Measured after: 99 caught, 0 missed, up from 97.** And the cost this page could not predict is the wall
clock: rule 12 asks by running the injector, the injector spawns two processes per rule page, and the
suite went from ~200 s to **8m04s** at nine rule pages
([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

**A second fragility of the same family surfaced with it, in the fixture rather than the assertions**: the
sandbox created placeholders for `sources:` paths and none for `governs:` destinations, so the first real
rule page would have reddened the pristine copy before a single case ran
([[a-fixture-must-materialise-what-the-subject-reads]]). **The question to ask of a schema that grows a
path-valued field is what the harness has to create now** — the fixture-side twin of *which cases are now
coupled*.

## The coupling arrived twice for one field on 2026-08-21, and the second wave is the interesting one

**Making `authority:` required coupled every fixture that plants a page, in two waves rather than
one.**

- **Wave one is the schema.** Nine cases planted a page without `authority:` and went red on rule 2.
  This is the coupling this page already describes, and it behaved exactly as described.
- **Wave two is the admission rule itself.** Once those pages carried a slug, **rule 13 reddened them
  again** because the slug sat in no family in `authority.md`
  ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**Wave two is a rule reaching into the suite and saying something about the corpus: a fixture that
plants a page and not its register entry is testing a store this project would refuse.** That is a
different claim from *a global rule makes unrelated tests fragile* — the fixture was not merely
incidentally caught, it was **wrong**.

**Repaired with a `plant_slug` helper the fixtures call**, which is the harness-side fix this page
argues for rather than a softening of the rule.

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
