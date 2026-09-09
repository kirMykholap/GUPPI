---
title: "A path is resolved by the program that opens it, not by the shell that launched it"
type: lesson
status: archived
authority: path-resolution-owner
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md"]
tags: [process, harness, testing]
---

# The assumption that failed three times in one day

**`/tmp` exists for Git Bash and does not exist for Windows Python.** The shell maps it; the program
the shell launches does not, and it is the program that opens the file.

The three, all on 2026-08-24:

- a Python script told to write `/tmp/...` — bash printed nothing wrong and Python failed;
- a redirect Python owned rather than bash, pointed at the same place;
- `echo` in bash collapsing a doubled backslash into invalid JSON for a hook payload, where the
  interpretation belonged to the JSON reader and not to `echo`.

**The three look like three different tools misbehaving and are one question asked wrongly**: *who
resolves this string?*

# Why it keeps happening here specifically

**This repository is driven from Git Bash on Windows and its programs are PowerShell, Python and
Windows binaries.** The shell's view of the filesystem and the program's view differ at exactly one
place — the paths the shell synthesises — and nothing in a command line marks which side owns a
given argument ([[tmpdir-is-empty-in-this-shell-so-a-path-built-from-it-lands-at-the-root]],
[[a-hook-finds-bash-by-walking-up-from-git]]).

# The rule that follows

**Write a path in the vocabulary of the program that will open it**, and when in doubt let the
program produce it: `tempfile` in Python, `[System.IO.Path]::GetTempPath()` in PowerShell,
`mktemp -d` in bash. Measured the same day: **`mktemp -d` and `GetTempPath()` land in the same
place**, `C:\Users\kir\AppData\Local\Temp`, so the two agree once each is asked in its own language
([[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]).

**It belongs to the family this store keeps re-recording** — a tool eating what was written to it —
and it is the half of the family that generalises rather than the half that is one tool's quirk
([[prose-does-not-survive-a-shell-command-string]],
[[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]]).
