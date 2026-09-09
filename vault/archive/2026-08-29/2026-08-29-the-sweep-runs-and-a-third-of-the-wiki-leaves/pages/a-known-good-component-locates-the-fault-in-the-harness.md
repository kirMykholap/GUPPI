---
title: "Running a known-good component through the same harness locates a fault in the harness"
type: lesson
status: archived
authority: known-good-probe
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/hooks/check-the-journal.ps1", "scripts/hook-selftest.ps1"]
tags: [testing, harness]
---

# The incident, 2026-08-17

A new hook appeared **silent** on a deliberately malformed journal. The obvious next move is to read
the new hook again.

**The cheap move was to feed the same payload to the guard that had worked for four days.** Its
silence was identical — which pointed at the payload in one step, and the payload was indeed
malformed ([[a-test-that-fails-for-its-own-reasons-proves-nothing]]). Built with `ConvertTo-Json`
instead of by hand, both hooks spoke.

# Why it is worth a page

**A new component and a new test arrive together**, so when nothing happens there are two suspects
and the new one attracts all the attention. Substituting a component with a known history holds the
harness constant and splits the space in half for the price of one command.

**Reusable, and stated as a rule: when a new thing looks broken, put an old thing through the same
test before believing the test.** The corollary is the reason this project keeps its selftests
runnable in isolation — a known-good subject has to be *available*, which is a property of how the
tests are written rather than a matter of luck ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

The same session met the general form of this twice, and both times the first reading was "the hook
is broken": [[a-test-that-fails-for-its-own-reasons-proves-nothing]].
