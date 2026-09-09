---
title: "The hook selftest could deliver no non-ASCII byte to any hook, and the case built on one accused a hook that was correct"
type: lesson
status: archived
authority: hook-payload-encoding
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/hook-selftest.ps1"]
tags: [harness, testing, process]
---

# What was wrong

**The payload went down a pipe between two PowerShell processes**, encoded by the parent's
`[Console]::OutputEncoding` — whose assignment at `scripts/hook-selftest.ps1:17` is wrapped in a
`try`/`catch` that swallows its own failure.

**A seven-character Russian quotation in guillemets arrived as eight question marks**, one per
character. The case built on it accused a hook that was correct.

**The file held zero non-ASCII bytes before this**, so nothing had ever asked — in a repository
whose entire feedback channel is the owner's Russian
([[english-in-the-repository-russian-with-the-owner]]).

# The repair

**The payload is written to a UTF-8 file and redirected into the child**, and the result is read
back with an explicit encoding. `RunCatch` no longer uses a pipe.

**Reading after: `caught 148, missed 0`, up from 144.** The change was one nobody asked for and the
owner let it stand ([[the-harness-changes-nobody-asked-for-stand]]).

# The general shape, which is not about PowerShell

**A test harness that has never carried a byte class cannot be assumed to carry it.** The suite had
144 passing cases and complete blindness to the one alphabet this project's rulings are written in.

**And the swallowed failure is the reason it stayed invisible**: a `try`/`catch` around an encoding
assignment converts a hard failure into a wrong answer, which is the direction that costs a
debugging pass instead of a line ([[windows-console-encoding]],
[[a-hook-is-measured-from-powershell-or-not-at-all]]).

**What it should have prompted:** the first case exercising a new byte class is a test of the
harness before it is a test of the thing. Here the harness was accused last and the hook first.
