---
title: "A non-zero exit from `vault-check.sh` no longer names one event"
type: concept
status: current
authority: gate-exit-ambiguity
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check.sh", ".claude/hooks/check-the-journal.ps1", ".claude/hooks/lock-the-librarian.ps1"]
tags: [harness, vault, testing]
---

# The two events

| exit | means |
|---|---|
| **1** | the vault is red — a `note` fired |
| **2** | a usage error — an unrecognised argument ([[the-gate-exits-on-a-usage-error-with-a-code-of-its-own]]) |

**Both consumers of the gate's exit code read any non-zero as *the vault is red*.**
`.claude/hooks/check-the-journal.ps1` and `.claude/hooks/lock-the-librarian.ps1` both do.

# Why it cannot fire today, and why that is not a fix

**Neither consumer passes an argument.** So the ambiguity is real and unreachable, and it is held
apart by a property of the callers rather than by anything in the protocol.

**It is named as a known boundary rather than repaired**, because the repair is a second reader of
one condition — each consumer learning to distinguish 1 from 2 — and this store has that scar:
two readers of one condition drift, and the drift is invisible until they disagree
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**What makes it safe to leave is that it is written down.** An unreachable defect nobody has
recorded is the same thing as an unknown one
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

# What would move it

A consumer that starts passing `--lint`. `/vault-lint` is the only caller that does, and it is a
skill rather than a hook, so it reads the output rather than the code
([[the-tag-density-advisories-move-behind-lint]]). **The day a hook wants the flag, this boundary
becomes live.**
