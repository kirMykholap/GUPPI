---
title: "A column a human reads must mean what it says, and `not owed` is not `a pre-task ran`"
type: lesson
status: archived
authority: ledger-column-honesty
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, testing]
---

# The defect, 2026-08-20

**The `pre_task` column of the ledger was written from the branch's own question** — *is anything
owed here?* — rather than from the fact a reader would take it for
([[the-pre-task-ledger]]).

**The two come apart on the second write of a session that skipped the ritual**, where nothing is
owed **only because the advisory was already spent**. The column then says `true` about a session
that never ran a pre-task.

# How it was found, and that is the part worth keeping

**By reading the live ledger, not by a test.** The tests asserted **behaviour** — that the hook
speaks once and then stays quiet — and every one of them was green. **The defect was in the
record**, which no behavioural assertion looks at.

**A record and a behaviour need separate instruments.** A suite that exercises a mechanism proves
what it does; whether what it wrote down is true of the world is a different question, and the
cheapest way to ask it is to read the artefact once with human eyes
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

# The general form

**A column is an assertion about the world, and a branch condition is a statement about the code's
state.** Where a value is written straight out of the condition that produced it, the column
inherits the condition's meaning and loses its own — and nothing announces the substitution, because
the code is correct.
