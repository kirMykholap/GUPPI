---
title: "Tightening the gate reddened the suite's own fixtures, and only the suite found it"
type: lesson
status: archived
authority: fixture-corpus-tightening
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "scripts/vault-check-selftest.sh"]
tags: [harness, testing, vault]
---

# What happened, 2026-08-19

The per-folder key-set gate made `sprint:` required on every page
([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]). **The suite's fixtures predate that
requirement and carry no `sprint:`**, so every page the suite plants went red, and **nine cases that
expected green failed.**

**The gate itself was verified four ways against the real tree and every new verdict was made to
fire.** Nothing about the change was wrong. What broke was the corpus the tests build for
themselves.

**Verified not pre-existing** by running the same suite against the pre-change scripts, where those
nine pass ([[a-case-that-passes-before-the-change-tests-nothing]]).

# The reason it is worth a page: the session's own subject arrived from the blind side

**"Repair the corpus before you tighten the predicate" was this session's central ordering**, applied
deliberately to `wiki/` and forgotten entirely for the fixtures
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). The pages a suite plants **are
a corpus**, held to the same schema, and they are the one corpus nobody browses.

**A rule with a known migration order has two corpora and only one of them is visible.** The visible
one is repaired because a gate reddens it in front of you; the invisible one is repaired after the
suite tells you, if the suite is run.

# Why only the suite could find it

`vault-check.sh` over the real tree exits 0 — the fixtures are not in `wiki/`. A plant-and-revert
proof of the new verdict fires, correctly. `vault-inject.sh --check` is unaffected. **Every
instrument except the suite says the change is clean**, and it is clean, for everything except the
instrument that says otherwise.

**That makes the suite non-optional after a schema change, not merely advisable.** Its cost is the
argument against running it every time — measured at eight minutes and scaling with rule pages
([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]) — and a change to what a page must
carry is exactly the case that repays it.

# The repair, and the shape it left

Four fixtures gained `sprint:`, two cases were inverted, and `empty_vault()` now mirrors the
`_schema.yaml` files off the pristine copy — **the third thing in that one function which has to be
swept rather than listed** ([[vault-scripts]], [[a-fixture-must-materialise-what-the-subject-reads]]).
A fourth will make that function the thing to read before adding anything to the vault's layout.

# A ruling can abolish a case's subject, and the repair is conversion rather than deletion — 2026-08-21

**Confining `governs:` to `wiki/rules/` left the case *a concept page that renders* testing a page
that cannot exist** ([[governs-is-a-property-of-wiki-rules-alone]]). The obvious move is to delete
it.

**It was converted instead: same subject, reversed verdict — the case now asserts that the schema
refuses such a page.** Deleting it would have left nothing in the suite asserting that what used to
be legal no longer is, and *that* is precisely the assertion a rule change owes the suite. A ruling
removes a behaviour; the case that tested the behaviour is the only thing positioned to test its
removal.

**Five runs across the change, and the check was never wrong in any of them**:
**136 → 132/9 → 133/8 → 141/0 → 140/1 → 141/0**. Every red was a fixture the tightened rules had
outgrown, and the one miss in the fifth reading was the converted case before its assertion was
turned over.

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
