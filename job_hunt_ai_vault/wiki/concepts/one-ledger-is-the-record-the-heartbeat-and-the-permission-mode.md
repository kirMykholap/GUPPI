---
title: "One ledger is the record of a skipped ritual, the heartbeat of the hooks, and the mode the session started in"
type: concept
status: current
authority: ledger-jobs
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, agents, process]
---

# The jobs, and the last of them paid on its first row

**The record of a skipped ritual** is what it was built for
([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**The heartbeat** is the second job and it answers a question nothing else in this repository can:
**a session that edited files and left no line has hooks that never loaded.** No reading of
`.claude/settings.json` can detect that, because the file on disk is correct in exactly that case
([[claude-code-config-loading]], [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**The permission mode the session actually started in** is the third, and it paid immediately: the
session reported `auto` while the repository's settings said otherwise, which is how
[[the-vs-code-extension-reads-its-starting-mode-from-user-settings]] was found at all.

# The heartbeat has to key on a line a hook writes

**Keyed on *has this session any line at all*, it would be missing in precisely the sessions that
performed the ritual before their first edit** — which is the intended order — because the
`pre-task` row is written by `scripts/record-pre-task.ps1`, a script the session runs, and not by a
hook.

**So the heartbeat reads the rows a hook wrote and ignores the rest.** A liveness signal that is
absent when the system is behaving best is worse than none: it trains its reader to explain it away
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

# One file rather than three

**Nothing here needed a second artefact.** The rows carry an `event` column, and each job is a
different question asked of the same rows — which is why the columns are the design and the
consumers are not ([[the-pre-task-ledger]]).

# The third job paid again the next night, and it is the only instrument for it — 2026-08-20

**The mode a session really started in is visible through this ledger and through nothing else.**
The previous session's rows carry `auto`; the fourth session of 2026-08-20 carries `plan`, and then
`acceptEdits` after the owner switched by hand.

**No hook event fires when the permission mode changes**
([[no-hook-event-fires-when-the-permission-mode-changes]]), so the mode is recorded only when some
*other* hook fires and reads it out of its payload. The record is therefore a sequence of
observations at unrelated moments rather than a log of transitions — enough to answer *what was it
at this edit*, and not *when did it change*.

**That is the difference between an instrument and a log**, and it is worth stating because the rows
look like a log. A reader who takes the gap between two differing rows as the moment of the switch
will be wrong by however long the hooks were quiet.
