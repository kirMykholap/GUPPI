---
title: "A process is measured with the stdin it will have, or the number is not about it"
type: lesson
status: current
authority: measurement-invocation-shape
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", ".claude/hooks/serve-the-rule.ps1", ".claude/hooks/ask-the-vault.ps1"]
tags: [testing, harness, agents]
---

# The incident, 2026-08-30

**A new `PreToolUse` hook was measured at 99 ms for a bare PowerShell spawn and 141 ms for the hook,
and the design was decided on those figures.** Both were taken from a terminal, with no stdin.

**A hook is always handed its payload on stdin.** Measured through a pipe, which is the only shape it
ever runs in, on the same machine with two checks running in the background:

| what | measured |
|---|---|
| a bare `powershell -NoProfile -File` spawn | **359 ms** |
| `.claude/hooks/serve-the-rule.ps1` | **750–930 ms** |
| the existing `.claude/hooks/ask-the-vault.ps1`, same load | **941 ms** |

**The earlier pair is void, not merely low.** It was taken in a shape the subject never runs in, so
it is not a reading of the subject at all.

# What it costs, which is more than the error

**A measurement taken in the wrong shape is worse than no measurement, because it is trusted.** The
decision to build the hook as a separate program was argued partly on the 141 ms figure — *"against a
write path that fires 71 to 108 times in a working session"* — and that argument was made against a
number six times too small. The conclusion survived; the ground under it did not.

**The load matters too and is not separated here.** Both new figures were taken with two background
checks running, so they are an upper bound rather than a quiet-machine reading, and re-taking them on
an idle machine is owed.

# The general form

**Before quoting a number about a process, ask what the process is handed when it really runs** — its
stdin, its environment, its working directory, its concurrency. Each of those is part of the subject,
and a reading that omits one is a reading of something else
([[measuring-a-copy-of-a-script-placed-somewhere-else-measures-nothing]], which is the same failure
along the *location* axis rather than the *invocation* axis).

**And this store has now been bitten by the same descriptor twice in one day.** The other half is
that leaving stdin open is what hangs a suite outright
([[backgrounding-a-task-that-reads-standard-input-is-what-hangs-it]]).

# Re-measured 2026-08-31, and the two readings cannot both be about the same subject

**389–478 ms on the write path and 392–450 ms on the read path, with 36 pages in `wiki/rules/`**,
taken through a pipe. The figure recorded above is **750–930 ms at 17 pages**. **The folder doubled and
the cost fell by roughly half.**

**The plan had named the hook's cost as a regression and expected roughly a doubling at seventy rule
pages.** It did not appear. **A predicted regression that does not show up is still a reading worth
writing down** — otherwise the only record of the prediction is a plan nobody re-reads, and the next
person prices the same change from the same guess.

**This session cannot say which of the two figures is wrong**, and it did not spend the session finding
out. The candidates are the ones this page already names: a different machine load, a different
invocation shape, or the owed idle-machine re-take that has never been done. **The owed re-take is what
decides it**, and until then the honest statement is that one reading is not of the same subject as the
other.

**What is not in doubt is the direction of the arithmetic that mattered.** The matcher was deferred on
the premise that `Read` is the most frequent tool call; it is the fourth, at about a third of the
`Edit|Write` path ([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).
Registering it added about a third to a hook whose per-call cost had halved.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
