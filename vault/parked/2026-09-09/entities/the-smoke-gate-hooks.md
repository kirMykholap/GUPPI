---
title: "The smoke gate's hooks, and what each of them cannot do"
type: entity
status: current
authority: smoke-gate-hooks
basis: code
sprint: S3
created: 2026-08-26
sources: [".claude/hooks/remind-the-smoke.ps1", ".claude/hooks/record-the-smoke.ps1", ".claude/hooks/gate-the-handoff.ps1", ".claude/hooks/pre-task-state.ps1", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [harness, agents, testing]
---

# What they are

**Three hooks, built and registered 2026-08-26, all writing to and reading from the ledger that
already existed** ([[the-pre-task-ledger]]). Together they are what makes `make smoke` an
obligation rather than a habit
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

| file | event, matcher, narrowing | what it does | what it cannot do |
|---|---|---|---|
| `remind-the-smoke.ps1` | `PostToolUse` / `Skill`, narrowed to `retro` | tells the agent to start `make smoke` in the foreground, and demands a `VAULT-FEEDBACK` block per turn | never refuses — `PostToolUse` fires after the act |
| `record-the-smoke.ps1` | `PostToolUse` / `Bash`, narrowed to a `make smoke` or `make suite` command | writes `smoke:<exit code>` | never refuses, never reads an exit code directly |
| `gate-the-handoff.ps1` | `PreToolUse` / `Skill`, narrowed to `handoff` | refuses while the path is closed | says nothing about the product suite, which is outside `smoke` |

**`gate-the-handoff.ps1` is the second hook in this repository that can refuse**, and the refusal is
argued against the three conditions on its own page
([[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]],
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

# There is no fourth registration, and the write row comes from a hook that already ran

**`check-the-journal.ps1` writes `write:<path>` before any of its own narrowing**, because it is
already registered on `Write|Edit` and already runs on every write
([[the-journal-gate-hook]]). A further PowerShell spawn on the write path is a cost this harness has
measured and refused once already ([[the-plan-check-hook]]).

# `Get-HandoffRefusal` is where the inference lives

**`.claude/hooks/pre-task-state.ps1` derives `SmokeAt`, `SmokeCode` and `WritesAfterSmoke` from the
rows, and `Get-HandoffRefusal` turns them into one of three refusals or `$null`**
([[the-pre-task-state-library]]). The gate hook itself compares nothing
([[the-smoke-gate-records-observations-and-the-reader-derives-the-refusal]]).

# `git check-ignore` is spawned once, at the gate, over the whole list

**Asking it per edit would put a git process on every `Write` and `Edit` in the repository to guard
one event at the end of a session.** So the question is asked once, when `/handoff` is attempted,
over the paths written since the last green run.

**The paths go as arguments and never through `--stdin`, in chunks** — a measurement rather than a
preference, and the `--stdin` form fails in the dangerous direction
([[git-check-ignore-stdin-receives-nothing-through-a-windows-powershell-pipe]]).

**If git cannot be run at all, every write counts.** A gate that fails towards refusing costs a
three-minute run; one that fails towards opening costs the thing it guards.

# What has been observed, and what has not

**The whole chain ran live on the day it was built.** The reminder fired on that session's own
`/retro` — a registration written mid-session, which is one observation against the reading that
hooks are read at session start ([[claude-code-config-loading]]). The recorder wrote `smoke:0` rows
for two foreground runs. `/handoff` **passed** the gate on a green row newer than the last write.

**A refusal has still never been observed on a real `/handoff`.** Every red state is held by
selftest cases and by nothing else, which is the half that matters and is stated on the decision
page rather than left to be discovered.

**A backgrounded `make smoke` writes no row.** The recorder now returns a note naming the cause and
the fix, and the reminder demands the foreground, because the consequence otherwise arrives at
`/handoff` with no clue why
([[an-instrument-that-fails-towards-nothing-to-do]]).

**The reminder carries no duration**, deliberately: a quoted figure in a hook message is a number
nothing keeps true ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# `TaskCompleted` is not built on, deliberately

**It is listed in the event set and has no documented schema**, so nothing here observes a background
run's completion. **A backgrounded `make smoke` is guarded by two messages and no mechanism** — the
reminder's demand for the foreground, and the recorder's note when it sees one anyway.

**Building on an undocumented event was rejected** against the cheaper repair of making the silence
audible ([[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]]).

# `remind-the-smoke.ps1` lost the feedback demand — 2026-08-29

**It had been carrying half of the `VAULT-FEEDBACK` requirement** and now carries none: the whole
requirement lives in `remind-the-feedback.ps1`, registered on two events
([[the-feedback-requirement-is-owned-by-one-hook-and-registered-on-each-event-it-needs]], [[the-feedback-reminder-hook]]).

**What it keeps is the smoke half**, unchanged — the gate's demand, the foreground demand, and the
note when it sees a background run anyway.

**Both hooks spoke on the `/retro` that opened the closing ritual**, which is how the new
`PostToolUse` registration was observed to take effect with no restart.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# The recorder writes a green row for a run that never happened — 2026-08-29

**`record-the-smoke.ps1:90` matches `SMOKE-EXIT:\s*(\d+)` against a command's OUTPUT, last match
wins.** It cannot tell a `make smoke` run from a shell command that merely *printed* the marker, so
**`cat` of a page documenting the marker writes a `smoke:0` row**, and
[[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]] reads that row as permission to
hand off.

**Three live pages carry the matching form, once each** — `wiki/entities/the-makefile.md:83`,
`wiki/proposals/make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation.md:317`,
and `wiki/decisions/the-smoke-runner-is-built-first-thing-next-session.md:119`. **Four more live
occurrences are one edit from matching**, kept harmless by an accident of spelling.

**Three false green rows stand in the ledger for 2026-08-29.** One at `08:32:22`, written by a session's
`cat` of two of those pages — `/handoff` would have opened on it. **Two more at `22:09:43` and
`22:09:58`, written by [[the-lessons-agent]]'s read-only `grep` while it was counting the occurrences
above** — the defect firing on the investigation of the defect, from inside a subagent that holds no
write tool.

**The journal's own count of this is wrong in both halves** — it says two pages, two occurrences each —
and the correction is on the proposal.

**Same class as the `--list` sweep counting the comment that quotes its own literal**
([[a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep]]), and the repair is
designed rather than built: [[an-instrument-that-hunts-a-literal-excludes-the-corpus-that-documents-it]].

**`SUITE-EXIT:` has the identical shape and its occurrences have not been counted.**

# Narrowed 2026-08-30, and what the narrowing does not close

**`record-the-smoke.ps1:59` went from `\bmake\b` to `make\s+(smoke|suite)\b`.** The command test was
never absent — that is what the session first told the owner and `/pre-task` corrected. **It was
loose**, and the repair was to tighten line 59 rather than add a branch at line 90.

**Proved rather than assumed.** Against the offending command the old pattern returns `True` and the
new one `False`, so the selftest case **failed before the change**. `hook-selftest.ps1` gained a case
reading a vault page whose slug begins `make-`. **HOOK-SELFTEST: caught 218, missed 0**, up from 217.

**What it does NOT close, named here rather than left to be rediscovered:** a command whose own text
contains `make smoke` still files a row if its output carries the marker — so a `grep` for that phrase
over such output is still a false green.

**And the fix was proved live rather than by absence.** The ledger row for that day's real `make
smoke` reads `smoke:0` with the genuine invocation in its command column. **A fix that silenced the
recorder entirely would look identical to a clean tree in every other reading**, so the positive
evidence is the only evidence that distinguishes them.

**owner:** «делаем сегодня».

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`
and from this ingest's own dispatch; extended 2026-08-30.)*
