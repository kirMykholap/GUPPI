---
title: "`$TMPDIR` is empty in this shell, so a path built from it lands at the filesystem root"
type: lesson
status: archived
authority: tmpdir-unset
basis: measurement
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md"]
tags: [harness, process, testing]
---

# What was measured, 2026-08-23

**`$TMPDIR` is empty in this shell.** A background run of the selftest was told to write to
`"$TMPDIR/selftest-full.txt"`, which expanded to `/selftest-full.txt` — the filesystem root. The
write was refused by permissions, the run produced nothing, and **six minutes were lost** before
anyone looked at where the output had been asked to go.

# Why it cost six minutes rather than six seconds

**A background run reports when it finishes, and this one finished.** There was no error in the
foreground and no output to read; the only symptom was a file that was not there, which is
indistinguishable from a run that has not got that far yet.

**It is [[an-instrument-that-fails-towards-nothing-to-do]] with the instrument being the
redirection itself.** An unset variable inside a quoted path does not fail — it shortens the path,
silently, into a different valid path.

# The rule

**Write the scratchpad path in full.** No variable, no expansion, no assumption that the shell this
project is driven from carries the environment a POSIX shell usually does — it is Git Bash on
Windows and it does not.

**And the general form: `set -u` does not protect a path.** An empty expansion of a *set* variable
is not an unset variable, so the shell option that catches the second says nothing about the first.
The cheap check is to `echo` the path once before the run that uses it, which is the same habit
that answers the backslash and the apostrophe — build the literal, then look at it
([[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]).
