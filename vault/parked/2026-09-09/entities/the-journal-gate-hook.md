---
title: "`check-the-journal.ps1` — the gate that runs when a journal lands"
type: entity
status: current
authority: journal-gate-hook
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/hooks/check-the-journal.ps1", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, agents]
---

# The third hook, added 2026-08-17

Registered in `.claude/settings.json` as a **`PostToolUse` hook on `Write|Edit`** and narrowed
inside the script itself to `<vault>/raw/handoffs/*.md`. When a journal is written it runs
`scripts/vault-check.sh` and prints what the check found into the session's context. The other two
hooks, and what each of them cannot do, are [[session-hooks]].

**Post rather than Pre, and loud rather than blocking.** The condition being checked is the journal
*existing*, and it does not exist until the write has happened — so blocking is off the table for
the same reason that made the event a `PostToolUse` one. The hook's answer to that is volume: it
prints, and it prints into a channel the session cannot skip past.

**Why a hook and not a line in `/handoff`.** The skill carries that line too, and it is the only
one that works in a session that started before this file existed, because hooks are read at
session start ([[claude-code-config-loading]]). But a step written in a skill is prose, and **prose
does not stop an agent** — the same argument that put the title rule into the check instead of
leaving it in the vault ([[the-title-check-asks-and-does-not-judge]]).

## Three properties that are load-bearing rather than tidy

- **It derives `bash` instead of naming it**, by walking up from wherever `git` resolves —
  [[a-hook-finds-bash-by-walking-up-from-git]]. Finding none, it says **THE GATE DID NOT RUN** and
  why, because a guard that is silently absent is worse than none.
- **It reads the payload with `ConvertFrom-Json`, and normalises backslashes with `.Replace`.**
  Both are inherited scars of the `PreToolUse` guard rather than new caution ([[session-hooks]]).
- **The check's exit code is the arbiter, not a grep over its output.** Advisories print and do not
  fail, so only a non-zero exit interrupts. Two readers of one condition disagree eventually, and
  this project has that scar.

**It does not decide what a journal is.** The narrowing stops at the directory and the extension;
whether a file is a journal or a form is `vault-check.sh`'s question, answered by a property rather
than by a filename ([[a-journal-is-told-from-a-form-by-a-property-not-a-filename]]).

## What proving it cost, and what that taught

The hook looked silent on a deliberately malformed journal and was not: the hand-built JSON payload
was malformed, and the same payload silenced the four-day-old guard beside it
([[a-known-good-component-locates-the-fault-in-the-harness]],
[[a-test-that-fails-for-its-own-reasons-proves-nothing]]). `scripts/hook-selftest.ps1` covers it,
including the branch where `git` is off PATH — **caught 40, missed 0 on 2026-08-17**, up from 29 at
the start of that session.

**What it still does not gate is the ingest itself.** A journal that fails the check can still be
handed to the librarian, and the design that would refuse it is
[[a-lock-on-the-librarian-dispatch]].

## It caught the journal of 2026-08-20, and that is recorded because a working guard is invisible

**It fired on the write, named the two missing sections by name, and said to fix them before
`/ingest`.** Nothing else in the day's output mentioned it, which is the normal condition of a guard
that works — and the reason it is written down here at all.

**It is also independent evidence for the advisory channel split.** Line 108 of
`.claude/hooks/check-the-journal.ps1` had been filtering the gate's output with
`Where-Object { $_ -notmatch 'advisory' }` before showing it — the same conclusion the split reached,
fixed locally instead of at the source. **So the hook cannot break on that change**: what was removed
from a bare gate run is exactly what it was already discarding
([[the-tag-density-advisories-move-behind-lint]]).

**It reads the gate's exit code as a boolean**, which is now ambiguous by one value
([[a-non-zero-exit-from-the-gate-no-longer-names-one-event]]). It passes no argument, so it cannot
fire today.

## It carried the mangled-command defect too, and had since `8017f34`

**Its cannot-run branch announced `` `bash scripts/vault-check.sh` `` and delivered
`ash scripts/vault-check.sh`.** Same cause as the lock's, one file away: a backtick inside a
double-quoted PowerShell string is an escape
([[a-backtick-in-a-double-quoted-powershell-string-is-an-escape]]). **Verified as pre-existing by
`git log -S`**, which puts the phrase here at `8017f34` — so it stood through every session between.

**Fixed 2026-08-20 by doubling the backticks**, and a hardened selftest case now pins the literal
command rather than the words introducing it
([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

# It gained a second job, and the job is not its own — 2026-08-26

**It writes a `write:<path>` row into the pre-task ledger before any of its own narrowing**, so the
row exists for every file written and not only for a journal
([[the-pre-task-ledger]]).

**The row is read by the handoff gate**, which needs to know whether anything was written after the
last green `make smoke` ([[the-smoke-gate-records-observations-and-the-reader-derives-the-refusal]]).

**Why here rather than in a hook of its own**: this script is already registered on `Write|Edit` and
already runs on every write. A second registration would put another PowerShell spawn on that path to
serve one event at the end of a session, which is a cost this harness has measured and refused before
([[the-plan-check-hook]]).

**It still refuses nothing**, and the added row changes none of its own verdicts.
