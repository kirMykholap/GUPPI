---
title: "The smoke gate records observations and the reader derives the refusal"
type: concept
status: current
authority: smoke-gate-inference
basis: code
sprint: S3
created: 2026-08-26
sources: [".claude/hooks/pre-task-state.ps1", ".claude/hooks/gate-the-handoff.ps1", ".superpowers/sdd/pre-task-ledger.tsv", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [harness, agents, process]
---

# The split

**The event column of the ledger records an observation and nothing else** — `smoke:<code>` when a
run returned, `write:<path>` when a file was written. **The conclusion is derived by the reader**:
`Get-HandoffRefusal` in `.claude/hooks/pre-task-state.ps1` turns the rows into one of three refusals
or into `$null`, which is the open path.

**That is the pre-task ledger's own philosophy and it is why no seventh column was added.** Every
reader of that file splits by position, and a column carrying a conclusion would be a second place
where the conclusion lives ([[the-pre-task-ledger]], [[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

# Three states, not two

| state | what the ledger looks like | why "run smoke" is not the whole instruction |
|---|---|---|
| never run | no `smoke:` row | the session does not know the check exists |
| run red | latest `smoke:` is non-zero | go back into the retro and fix what it found |
| run green, then written over | a `write:` row after the latest green `smoke:` | the run is evidence about a tree that no longer exists |

**Telling them apart is the whole of the design.** The reader is an agent that has to know what to
do next, and the refusal text differs in all three
([[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]]).

# `WritesAfterSmoke` is emptied by a smoke row rather than filtered afterwards

**A green run says the tree was sound at that instant and says nothing about anything after it**, so
the reader needs the writes that came after and never the ones before. The list is cleared as the
`smoke:` row is read, in one pass over the file.

**That is what makes the second run of a fix loop clear the first run's writes with nobody comparing
timestamps.** The loop the owner described — red, fix, run again, green, handoff — produces several
`smoke:` rows in a session, and a filter applied afterwards would have to decide which run each write
belonged to.

# The rule reads the latest row and not any row

**A green row early in the day would otherwise license every write after it.** The owner ruled the
strict reading on the ground he named himself: he had not accounted for there being several smoke
runs in one session, which is exactly what the fix loop produces
([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]]).

**A write only counts if git does not ignore its path.** An explicit list of checked directories was
rejected: a hand-kept list drifts and `git check-ignore` is derivable
([[a-copied-list-drifts-and-a-sweep-cannot]]). `.superpowers/sdd/` carries its own `.gitignore`
holding `*`, so `/retro`'s own transit files do not close the path it just opened — verified rather
than assumed, and without that clause the ritual would invalidate its own run every time.
