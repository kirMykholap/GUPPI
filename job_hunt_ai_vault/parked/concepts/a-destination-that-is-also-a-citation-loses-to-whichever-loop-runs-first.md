---
title: "A destination that is also a citation loses to whichever loop runs first"
type: concept
status: current
authority: sandbox-loop-ordering
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# Two loops, one file, and the order decided which version of it existed

The selftest's sandbox construction has two loops that materialise paths the corpus names:

- the **`sources:` placeholder loop**, which creates an empty file for every path a page cites, so that
  rule 5b does not redden the pristine copy;
- the **`governs:` loop**, which copies the **real** destination whole, because a rule's destination has
  to arrive carrying the region it holds ([[a-fixture-must-materialise-what-the-subject-reads]]).

**`CLAUDE.md` is both.** It is a `governs:` destination for nine rules and a `sources:` citation on
current pages.

With the placeholder loop first, `$PRISTINE/CLAUDE.md` was created **zero bytes**. The `governs:` loop
then opened with `[ -e "$PRISTINE/$dest" ] && continue` and skipped the destination it exists to
materialise. **The real file was never copied.**

# The comment ten lines above the guard had already said so

> *"An empty placeholder would satisfy the path and fail the comparison, which is a green that means
> nothing."*

**The failure mode was understood, written down beside the code, and defeated by the ordering** — which
is the part worth keeping. A `[ -e ]` guard encodes *somebody has already made this*; it cannot encode
*somebody has already made this **properly***, and nothing in the loop's own text is wrong.

# The fix is ordering rather than a stronger test

**Run the `governs:` loop first.** The `sources:` loop already guards with `[ -e ] ||` and will not
clobber what the first loop wrote, so one reordering satisfies both.

**Rejected: testing `[ -s ]` instead of `[ -e ]`.** An empty file can be a legitimate destination. What
is actually true is not *a destination is non-empty* but **the real file wins over a placeholder
standing in for it** — and ordering states that directly, while a size test states a proxy for it.

# What it was and was not the cause of

This ordering bug is real and fixing it moved the suite from `24` caught to `86`. **It was published as
*the* cause and it was not one** — the renamed vault was, and the remaining thirty-four were behind it
([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]],
[[the-first-published-diagnosis-can-be-a-real-defect-and-still-not-the-cause]]).

# The count in the example moved, and the mechanism did not — 2026-08-20

**`CLAUDE.md` is a `governs:` destination for eight rules now, not nine**, since the AST boundary
rule left for `.claude/rules/ast-boundaries.md`
([[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]]). Counting the records rendered into
it rather than the rules, it is ten.

**Nothing about the ordering bug changes.** `CLAUDE.md` is still both a destination and a citation,
which is the only property the failure needed, and the fix is still the ordering rather than a
stronger test.

**And the class has a new member**: `.claude/rules/ast-boundaries.md` is a destination that is also
cited in `sources:`, and `.claude/rules/_probe-paths.md` is a citation that cannot be deleted for
exactly that reason ([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]). A sandbox
that materialises both will meet this ordering again.
