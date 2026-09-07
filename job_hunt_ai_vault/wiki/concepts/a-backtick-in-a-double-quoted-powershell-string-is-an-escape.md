---
title: "A backtick inside a double-quoted PowerShell string is an escape, and it eats the command it was quoting"
type: concept
status: current
authority: powershell-backtick-escape
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", ".claude/hooks/lock-the-librarian.ps1", ".claude/hooks/check-the-journal.ps1"]
tags: [harness, testing, process]
---

# The mechanism

**In a double-quoted PowerShell string the backtick is the escape character.** Markdown's
code-span delimiters are backticks. Put a shell command in a code span inside a refusal message and
the two conventions collide:

| written | what reaches the caller |
|---|---|
| `` `bash scripts/vault-check.sh` `` | `ash scripts/vault-check.sh` |

**Both delimiters and the `b` are eaten.** `` `b `` is a backspace, and a backtick before a space is
an escaped space. **Comments are unaffected** — only string literals — which is why reading the file
looks reassuring.

**The fix is doubling the backticks.** Single quotes would also work where no interpolation is
needed.

# Where it was found, and it had shipped

**Three live occurrences, all the same phrase**: `.claude/hooks/lock-the-librarian.ps1` in both the
deny branch and the cannot-measure branch, and `.claude/hooks/check-the-journal.ps1`
([[the-librarian-lock-hook]], [[the-journal-gate-hook]]).

**It fired that way the one time the lock has ever fired**, and the owner read a refusal naming a
command that does not exist ([[a-refusal-is-conditional-or-absolute-and-nothing-else]]).

**A selftest case was watching and saw nothing**, because it pinned the sentence rather than the
command ([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

# The class it belongs to

**An escape does not survive into a command in this shell**, and the failure is always towards
something plausible rather than towards an error
([[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[prose-does-not-survive-a-shell-command-string]]).

**The structural answer, where one is available, is to need no escape** — which is what
`scripts/vault-archive.sh` did when it stopped letting a regular expression see a path
([[a-path-is-never-a-pattern]]). A refusal message has no such escape hatch, so here the defence is
an assertion on the literal command ([[an-instrument-that-fails-towards-nothing-to-do]]).
