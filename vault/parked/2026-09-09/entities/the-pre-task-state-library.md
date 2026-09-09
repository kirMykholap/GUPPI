---
title: "The pre-task state library"
type: entity
status: current
authority: pre-task-state-library
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, agents, process]
---

# What it is

**`.claude/hooks/pre-task-state.ps1` — a dot-sourced library, registered nowhere and required to
stay that way.** It sits under `.claude/hooks/` because it is a hook's code, and it is the one file
there that must never appear in `.claude/settings.json`.

It holds the ledger writer ([[the-pre-task-ledger]]); the session state derived from those rows and
the questions asked of it
([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]); the session
stamp, written and read; and the reader that strips the generated rule file down to its text
([[a-generated-rule-file-with-no-paths-carries-no-frontmatter]]).

# The failure mode it introduced

**A failed dot-source is swallowed by the `try` around it.** `.claude/hooks/ask-the-vault.ps1`
dot-sources this file, and a sandbox that did not materialise it did not fail — it went **quiet**:
the state stayed null, every new branch was skipped, and the suite printed the same count it prints
when the code works ([[a-fixture-must-materialise-what-the-subject-reads]]).

**The registration check is why it is named rather than assumed.** A file under `.claude/hooks/` is
expected to be either registered in `settings.json` or dot-sourced by something that is; this one is
the latter, and `scripts/record-pre-task.ps1` lives under `scripts/` precisely so that it owes
neither ([[the-plan-check-hook]]).

# Two functions joined it — 2026-08-20, fourth session

**`Invoke-LedgerRotation`** moves the whole ledger into `.superpowers/sdd/ledger/` and opens a fresh
file, called from the `SessionStart` hook and only when `source` is `startup`
([[rotation-is-a-whole-file-move-and-never-a-read-modify-write]]).

**`New-PreTaskState`** exists so the fresh state object is built in one place rather than two: a
field added later would otherwise reach one of the copies. **It was not in the approved scope**, and
extracting it is a recorded divergence
([[an-approved-scope-was-widened-by-a-helper-extraction-that-was-chosen]]) — the second one this file
has occasioned in four days, both of them for changes that were right.

**`Add-LedgerLine` changed signature**: its `pre_task` parameter is `[object]` rather than `[bool]`,
so an omitted argument writes `-` and the five existing callers are untouched
([[the-pre-task-column-gains-a-state-for-asserting-nothing]]).

# A third function joined it, and it is the first that returns a refusal — 2026-08-26

**`Get-HandoffRefusal($root, $state)` returns the reason the path to `/handoff` is closed, or `$null`
when it is open.** `.claude/hooks/gate-the-handoff.ps1` calls it and compares nothing itself
([[the-smoke-gate-hooks]]).

**The state object gained three fields**, filled by the same single pass over the ledger that fills
the rest: `SmokeAt`, `SmokeCode`, and `WritesAfterSmoke`. **The list is emptied by a `smoke:` row as
that row is read**, which is what makes the second run of a fix loop clear the first run's writes with
nobody comparing timestamps
([[the-smoke-gate-records-observations-and-the-reader-derives-the-refusal]]).

**It spawns `git check-ignore` — the only place in this library that spawns anything.** Once, over
the whole list, with the paths as arguments and in chunks; never through `--stdin`, which receives
nothing here and fails towards *nothing is ignored*
([[git-check-ignore-stdin-receives-nothing-through-a-windows-powershell-pipe]]).

**If git cannot be run at all, every write counts.** Failing towards a refusal costs a three-minute
run; failing towards an open path costs the thing the gate guards.

**Three refusal texts and not one**, because "run smoke" is the wrong instruction for two of the three
states this function tells apart.
