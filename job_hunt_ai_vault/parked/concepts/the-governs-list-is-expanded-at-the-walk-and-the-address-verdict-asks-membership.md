---
title: "The `governs:` list is expanded at the walk, and the address verdict asks membership"
type: concept
status: current
authority: governs-list-expansion
basis: code
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, vault, record-schema]
---

# The expansion happens at the walk, not in the loop

**`governs_targets()` in `scripts/vault-inject.sh` turns each page carrying the field into one
`page<TAB>destination` line before the main loop reads it.** The loop body — about two hundred lines
of it — is untouched, and **it never learns that the field has a syntax**.

**That works because every `continue` in it already meant *abandon this destination and take the
next*,** which is exactly what it has to mean now. The refactor is the walk, not the body.

**The `grep -l` pre-filter is untouched**, and a page naming one destination still costs exactly one
iteration — so the wall-clock argument that filter was written for is unaffected
([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]).

# The address verdict asks membership rather than equality

**`govsplit()` in `scripts/vault-check.sh` emits the `governs|` fact once per destination**, and
rule 11 asks whether the region's address is **among** them.

**Reading the first destination was correct while a page could name one file, and silently wrong the
moment it could name two.** It would have accused the region sitting in the *other* governed file —
which is the one place this verdict has to stay quiet, because that region is right
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

# The parsers are written from the same rules and are deliberately not shared

Both are built from this list, and nothing else is legal:

- trim;
- strip one layer of quotes;
- split an inline list on commas;
- **a bare value is a list of one**, so the thirteen pages carrying the bare form parse without a
  special case.

**They are separate implementations on purpose.** This vault already derives its category words
identically in two places for the same reason: the check and the writer must be able to disagree
loudly rather than share a bug ([[a-check-asks-by-running-the-writer-it-checks]]).

**The block form is refused by both**, and the owner ruled that the refusal is red rather than
silent ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]). **The verdict is
owed**; refusing to parse is what exists today.

# The whole corpus cannot exercise this

**Every rule page here governs the file its own region already sits in**, so rule 11's address
comparison is reached by no page in the tree — making `govsplit` return nothing left the gate's
output byte-identical and its exit code 0. Three selftest cases now reach it
([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# There is a reader this page does not name — 2026-08-22

**The section above says *both* parsers and means the injector and the gate. A third exists.** The
sandbox builder inside `scripts/vault-check-selftest.sh` reads `governs:` with a scalar `sed` and was
not taught the list form on 2026-08-21 with the other two.

**It was found by the first rule page in the corpus to govern two files.** The loop that materialises
every governed destination was handed the literal string `[a/one.md, b/two.md]` as one destination,
created a file under that name, copied neither real destination, and rule 12 went red in every case —
**`caught 112, missed 44` against three real failures**
([[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

**The argument on this page is not disturbed.** Two implementations written from one set of rules
still beat one shared copy. **The cost it does not name is that a third is invisible until a page
exercises the difference**, and the count of readers lives nowhere
([[the-count-of-a-fields-readers-lives-nowhere]]).

**The sentence above is not edited**, because it was a true description of the two readers it was
written about ([[the-region-coverage-figure-is-dated-where-it-stands]]).

# The block-form verdict landed, and the corpus can now exercise the address comparison — 2026-08-22

**The section *The whole corpus cannot exercise this* has a customer.** A rule page naming two skill
files exists, so rule 11's membership test is reached by a real page rather than by selftest cases
alone ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

**And the owed verdict is built.** The block form is refused with a diagnosis of its own — a
`blockgoverns` verdict joining the existing frontmatter verdicts rather than taking a rule number,
on the precedent that a retired number is never reused
([[a-retired-rule-number-is-never-reused]]).
