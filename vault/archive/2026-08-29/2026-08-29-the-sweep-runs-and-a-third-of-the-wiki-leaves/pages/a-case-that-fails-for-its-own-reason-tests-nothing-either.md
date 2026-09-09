---
title: "A case that fails for its own reason tests nothing either, which is the mirror of the case that passes before the change"
type: lesson
status: archived
authority: case-fails-for-its-own-reason
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness]
---

# What happened

**Making `render:` required broke the gate's selftest before a new case was written.**
`plant_rule_page` mints a rule page and did not carry the field, so **every region case would have
failed on a field it is not about**
([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]).

**Two planters were fixed.** The cases then reported on what they were written to report on.

# The shape

**The known half of this is [[a-case-that-passes-before-the-change-tests-nothing]]** — a case that
was already green proves nothing about the change beneath it. **This is its mirror: a case that is
red for a reason of its own proves nothing either**, and it is worse in one respect, because a red
suite is read as a finding about the subject.

**The common cause is a fixture that has drifted from what the subject now requires**
([[a-fixture-must-materialise-what-the-subject-reads]],
[[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]). A schema change is
the standard trigger: the planter writes a page the gate no longer accepts, and every case built on
that planter reports the planter.

# The defence, and it is cheap

**When a change makes a field or a key required, the fixtures that mint that record are part of the
change.** Not a follow-up and not a repair — the same edit, because between the two edits the suite
is red for a reason nobody can read off the failure line.

**And a red suite gets one question before it gets a diagnosis**: is this case failing about its
subject, or about itself? ([[a-test-that-fails-for-its-own-reasons-proves-nothing]],
[[reverting-the-code-tells-you-whether-a-test-tests-anything]])
