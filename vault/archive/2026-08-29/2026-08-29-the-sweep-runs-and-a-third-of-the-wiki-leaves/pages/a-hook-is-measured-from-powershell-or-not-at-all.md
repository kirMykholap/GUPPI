---
title: "A hook is measured from PowerShell or not at all, because piping from Git Bash gives it an empty payload"
type: lesson
status: archived
authority: hook-measurement-harness
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1", "scripts/hook-selftest.ps1"]
tags: [harness, testing, agents]
---

# What happens

**Piped from Git Bash, `[Console]::In.ReadToEnd()` receives nothing.** The hook reads an empty
payload, matches nothing, and **exits 0 in silence**.

**The shipping hook does the same on the same harness.** So *"it printed nothing"* was a reading of
the harness and not of the guard being measured, and the first instrument in a latency run lied
about whether the branch fired at all.

**Verified as pre-existing**, not introduced by the branch under test.

# Why the silence is the trap

**Every failure this harness can produce looks identical to the correct behaviour of a hook whose
path does not match.** A guard is *supposed* to print nothing on a non-matching path, so an empty
payload produces exactly the output a working guard produces — with no exit code, no warning and no
line to grep.

**The known-good control is what separates them** ([[a-known-good-component-locates-the-fault-in-the-harness]]):
run a subject that must speak through the same harness, and if it is silent too, the harness is the
subject.

# What was done instead

**The branch was proved to fire before it was timed.** 1188 characters of rule text delivered on
`probe/RUNBOOK.md`, nothing on `src/jobhunt/web/app.py`, and the shipping hook silent on the same
path ([[a-case-that-passes-before-the-change-tests-nothing]]).

**That assertion lives inside the measurement harness**, which is the general form:
[[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]].

# The family

**And the carrier that broke the guard is the same class one level down**: a literal backslash
does not survive a heredoc in this shell, which shipped a hook that parsed clean and was silently
absent ([[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]]).

**The instrument, not the evidence** — this project's recurring diagnosis
([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]],
[[a-test-that-fails-for-its-own-reasons-proves-nothing]]). What is specific here is the rule of
thumb, and it is short enough to remember: **exercise a hook from PowerShell, never through a pipe
from another shell.**
