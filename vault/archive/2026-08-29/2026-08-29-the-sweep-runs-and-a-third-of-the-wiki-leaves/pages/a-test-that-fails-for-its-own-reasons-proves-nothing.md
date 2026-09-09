---
title: "A test that fails for its own reasons proves nothing about its subject"
type: lesson
status: archived
authority: test-fails-for-itself
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "scripts/hook-selftest.ps1", ".claude/hooks/check-the-journal.ps1"]
tags: [testing, harness]
---

# Twice in one session, 2026-08-17, and the hook was fine both times

| what was done | what it looked like | what it was |
|---|---|---|
| a hand-written JSON payload piped from bash into `powershell -File` | the new hook is broken | the **payload** was malformed. `ConvertTo-Json` fixed it, and the known-good guard had been equally silent ([[a-known-good-component-locates-the-fault-in-the-harness]]) |
| the no-git case stripped `PATH`, then invoked `powershell` by name | the no-bash branch is broken | the test could not find **its own interpreter**. It now resolves it through `$PSHOME` |

**Both times the first reading was "the hook is broken", and both times the hook was fine.**

# The shape to recognise

A negative result from a test has two possible causes and only one of them is about the subject.
**The second cause is invisible precisely when the test is new**, because nothing has ever proved
that the harness can produce a positive result at all.

Two cheap defences, both used the same day:

- **run a known-good subject through the same harness** before believing a negative;
- **prove the test in both directions** — the fix to the `SessionStart` sort defect was proved to
  fire and to stay quiet before it was committed ([[session-hooks]]).

This is the same family as [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]], seen from
the other end: there a check passed while checking nothing, here a check failed while testing
nothing. **The instrument, not the evidence** — the third and fourth instances in this project of
that diagnosis ([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).
