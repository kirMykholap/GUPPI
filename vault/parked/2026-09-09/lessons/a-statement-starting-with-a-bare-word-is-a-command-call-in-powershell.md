---
title: "A statement starting with a bare word is a command call in PowerShell, so a comparison written without its `$` runs the function instead"
type: lesson
status: current
authority: powershell-command-mode-parse
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, testing, process]
---

# The incident, 2026-08-26

**Five cases of `scripts/hook-selftest.ps1` were written as `LedgerText -match "x"`, meaning
*compare the result of that function against a pattern*.** PowerShell read the statement in command
mode instead: a statement that begins with a bare word is a **command invocation**, so `LedgerText`
was called with `-match` and `x` as its arguments and the statement evaluated to whatever the
function returned — a string.

**`Check` takes a `[bool]`.** Handed a string it refused to bind, the case never executed, and
**neither counter moved**. The suite then printed `caught 169, missed 0` and exited 0, about a run
in which five of its cases had not happened.

**The intended form is `$(LedgerText) -match "x"` or a variable with its sigil.** Expression mode is
what the `$` buys; without it the parser is not comparing anything.

# Why nothing caught it

**A suite that asserts no total cannot tell a case that did not run from one that passed.** Both are
silence, and the score line reports the smaller number with the same confidence it reports the right
one ([[an-instrument-that-fails-towards-nothing-to-do]]).

**The error was on the console and was filtered out.** Every run of the suite that session was piped
through `grep`, so the binding failures printed and were never read
([[a-truncated-report-hides-the-line-it-was-run-for]]).

# The guard that was added, and why it is not a count

**It asks the platform whether any argument failed to bind** — `$Error` filtered on
`ParameterArgumentTransformationError*` — and reports a case of its own when the list is non-empty.

**An expected-total assertion was rejected deliberately.** A number in the file is a number every
new case has to update, which is the drifting-list shape this store repairs by deletion rather than
by extension ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[a-stated-count-drifts-from-the-list-it-heads]]).

**After the repair the same suite reports `caught 175, missed 0` in 42 s** — the five cases that had
been invisible, plus the guard, which is a case like any other.

# What follows

**This is another parsing trap this repository has paid for in PowerShell**, alongside a backtick
inside a double-quoted string and a BOM written in front of the first field
([[a-backtick-in-a-double-quoted-powershell-string-is-an-escape]],
[[add-content-utf8-writes-a-bom-in-front-of-the-first-field]]). The pattern is the same each time: a
form that is legal, means something else, and produces no diagnostic at the point it is written.
