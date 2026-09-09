---
title: "A fact about code was generalised from its neighbour, and a case passed for the wrong reason"
type: lesson
status: archived
authority: neighbour-generalisation
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", ".claude/hooks/vault-path.ps1", ".claude/hooks/check-the-journal.ps1", "scripts/hook-selftest.ps1"]
tags: [harness, testing, process]
---

# What was assumed

**`Find-Bash` was assumed to live in the shared `.claude/hooks/vault-path.ps1` because `Find-Vault`
does.** It was inside `.claude/hooks/check-the-journal.ps1`.

**One `grep -rn 'function Find-Bash'` settles it**, and that grep was not run. The generalisation is
the cheap kind: two functions with the same prefix, one known location, and the inference that the
other is beside it.

# What it cost, and the half that is worse

**Four lock cases missed** — the hook called an undefined function.

**And one passed for the wrong reason.** The *cannot measure* case went green on the
`CommandNotFoundException` thrown by the undefined function rather than on the absence of git
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). A green case that is green for the
wrong cause is worse than a red one: it is a case that will not notice when the thing it names
breaks.

# How the fix was confirmed

**By grepping the suite's output for that exception, not by re-reading the case.** After the move
the exception is absent from the run and the case is green for its own reason.

**Re-reading a case cannot tell you why it passed.** Only the run can, which is the general form:
when a case has been green for the wrong reason once, verify the repair against the *output* rather
than against the *source* ([[reverting-the-code-tells-you-whether-a-test-tests-anything]]).

# The move that fixed it was itself a divergence

`Find-Bash` was moved into the shared file mid-work and outside scope
([[do-not-change-a-working-file-mid-work]]). The two findings are separable: the assumption was an
error of method, the move was an error of process, and they happened to be about the same function.
