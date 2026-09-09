---
title: "A clean case built on a helper that plants a red tree can never be green"
type: lesson
status: archived
authority: clean-case-helper-choice
basis: measurement
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The incident, 2026-08-23

**A `run_clean` case was written on the `rule_page` helper and could not pass.** That helper plants
a rule page **without the region its destination needs**, and the gate is red on exactly that — so
the case asserted *nothing anywhere went red* over a tree the helper had just reddened.

**The helper that plants both ends is `region_resolves`.** The choice between the two is the whole
of the bug, and nothing in either name says which one leaves a green tree.

**Its companion red case was worse, not better.** It was red for two reasons at once — the planted
defect and the missing region — so it passed partly for a reason nobody chose, which is the shape
this store already has a page for
([[a-case-that-fails-for-its-own-reason-tests-nothing-either]]).

**Cost: one suite run, about thirty minutes**, to learn something a five-second read of the helper
would have said.

# The general rule

**A clean case constrains its fixture harder than a red one does.** A red case needs the tree to be
broken in the one way it names; a clean case needs it to be broken in **no** way at all, which is a
property of every helper it composes and of every rule the gate runs.

**So the helper for a clean case is chosen by what it leaves behind, never by what it plants.** The
question to ask of a fixture helper is not *does it create the thing I need* but *does the gate exit
0 over what it leaves* ([[a-fixture-must-materialise-what-the-subject-reads]],
[[hand-probe-a-new-mechanism-before-running-the-suite]]).

# Why the clean cases cannot simply be narrowed away

**`nothing anywhere went red` has no single rule to point at.** The cheap fix for the rest of the
suite — run one rule per case — cannot reach these, so they keep paying the full gate cost and stay
the cases most sensitive to an unrelated change
([[the-selftest-is-a-mutation-test-of-the-gate]],
[[a-rule-over-every-page-makes-every-test-fragile]]).
