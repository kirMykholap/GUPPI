---
title: "Rotation is a whole-file move and never a read-modify-write, because that is what the append-only ledger exists to protect"
type: concept
status: current
authority: ledger-rotation-mechanism
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, testing]
---

# The mechanism, and the alternative it refuses

**`Invoke-LedgerRotation` moves the whole file** into `.superpowers/sdd/ledger/` and opens a fresh
one ([[the-ledger-archive-directory]]). It never reads the ledger, filters it and writes it back.

**Two writers appending short lines do not lose each other's.** A read-modify-write between them
silently would: the second writer's copy of the file predates the first writer's line, and the
rewrite drops it with no error anywhere. Append-only is the property the ledger was built on, and a
retention mechanism is exactly where it would be given away
([[the-pre-task-ledger]]).

# The reader's race was already handled, and in the ratified direction

**`Read-LedgerState` reads this file 71 to 108 times a session** — the measured write-path frequency
of a working session. A read landing between the `Test-Path` and the `Get-Content` of a rotation
hits that function's `try`/`catch`, gets a fresh state, and **asks for the ritual again**.

**That is the direction a guard is allowed to be wrong in**, and it is the same reasoning the
lexical timestamp comparison uses when a pre-task and an approval land inside one second
([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**The race was not designed away for this feature.** It was already handled, which is why rotation
could be added without a lock — and a mechanism that needs no new failure handling is the evidence
that the earlier design was right, not a reason to stop looking.
