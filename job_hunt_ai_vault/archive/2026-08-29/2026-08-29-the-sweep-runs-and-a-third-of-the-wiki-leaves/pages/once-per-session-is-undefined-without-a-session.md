---
title: "`once per session` is undefined without a session"
type: lesson
status: archived
authority: once-per-session-precondition
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, agents, testing]
---

# The defect, 2026-08-20

**The write net spoke on payloads carrying no `session_id`.** Its budget is one advisory per
session, and what spends the budget is a row keyed on the session — so with no key nothing is ever
spent, and the guard would have spoken **on every edit for the rest of the run**.

**That is the exact noise it was built to avoid**, attached to a ritual the reader cannot satisfy:
the advisory asks for a `/pre-task` and the record of having run one cannot be written.

**Eight selftest cases asserting the guard's silence went red at once, and they were right.** A
cluster of cases turning over together is a design statement, not eight defects
([[a-rule-over-every-page-makes-every-test-fragile]]).

# The general form

**A rate limit is a claim about a key.** *Once per session*, *once per file*, *once per run* each
presuppose that the key exists in the payload; where it does not, the limit is not merely loose, it
is undefined, and the code falls back to *every time* — the loudest possible behaviour, in the case
where the system knows least.

**The safe default is silence, and here it is also the ratified one**
([[the-write-net-requires-a-session-id]]).

# The opposite choice is made next door, on purpose

**The one-writer note repeats where this one does not, and the scoped-rule branch repeats too.** The
difference is the consequence of repeating: an unrepeated rule delivery is a rule that is not there
after a compaction ([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]),
while an unrepeated advisory is only a nag. **Annoying there, fatal here** — and the note that fires
about fifty times per ingest is the demonstration
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).
