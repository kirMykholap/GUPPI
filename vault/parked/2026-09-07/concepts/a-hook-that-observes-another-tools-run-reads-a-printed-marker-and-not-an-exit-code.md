---
title: "A hook that observes another tool's run reads a printed marker, and not an exit code"
type: concept
status: current
authority: observed-run-verdict-source
basis: code
sprint: S3
created: 2026-08-26
sources: [".claude/hooks/record-the-smoke.ps1", "Makefile", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [harness, agents, testing]
---

# The inversion, and why it is one

**The two gate hooks in this repository run the check themselves, so its exit code is theirs to
read.** `record-the-smoke.ps1` does not: it observes somebody else's tool call, and **what a
`PostToolUse` payload carries about a shell command is not a contract this repository controls.**

**So the writer prints a line that cannot be mistaken for prose** — `make` emits
`SMOKE-EXIT: <n>` immediately before exiting with the same number — **and the hook reads that
line.** One reader of one condition: two readers of the same condition disagree eventually, and this
project has the scar ([[a-check-asks-by-running-the-writer-it-checks]],
[[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]).

# No marker means no row, and that fails in the safe direction

**A run that was interrupted, killed, crashed or backgrounded prints nothing the recorder can read**,
so nothing is recorded, so the gate says no smoke has run and asks for one.

**Recording an absent marker as a pass would open the gate on a run that never finished**, which is
the failure this arrangement is chosen against.

**The dangerous half is not the missing row but the missing explanation.** A session that
backgrounded the run meets the consequence at `/handoff`, refused with no green row and no clue why —
so the recorder speaks when it sees a backgrounded run rather than leaving it to be discovered at the
gate ([[an-instrument-that-fails-towards-nothing-to-do]]).

# What the payload actually showed

**`PostToolUse` is documented to fire for background tasks. What the documentation does not say is
WHEN**, and the observed payload settles it in one direction: it carries `run_in_background`, a task
id and an output path, **and no verdict** — consistent with firing at launch and inconsistent with
firing at completion.

**Whether it fires a second time at completion is not established.** Nobody has looked, and if it
does, a recorder reading the output file becomes a real option rather than a guess.

# Where else this applies

**Any hook narrowed to a command it did not run is in this position.** The rule generalises: if the
verdict has to survive a tool boundary the repository does not own, **make the writer print it**, and
read the printed thing.

# The limit this page did not state, and it is the whole defect — 2026-08-29

**The arrangement is sound about *trusting* the marker and silent about *who printed it*.** A printed
marker survives the tool boundary, as above — and it also survives being quoted by a document, being
`cat`ed by a reader, and being grepped for by an agent investigating the marker itself.

**`record-the-smoke.ps1` reads the marker out of any command's output**, so three live pages that
document `SMOKE-EXIT:` each write a green row when read, and three such rows stand for 2026-08-29
([[the-smoke-gate-hooks]], [[an-instrument-that-hunts-a-literal-excludes-the-corpus-that-documents-it]]).

**So the rule stated above needs a second clause**: make the writer print it, read the printed thing,
**and be able to say that the writer is what printed it.** The payload already carries the command
string, which is where that clause would go.

**And this page carries one of the occurrences** — `SMOKE-EXIT: <n>` at line 20 — one edit away from
matching the pattern itself.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
