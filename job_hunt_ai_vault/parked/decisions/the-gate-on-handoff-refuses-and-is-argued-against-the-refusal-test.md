---
title: "The gate on `/handoff` refuses, and is argued against the refusal test rather than inheriting a licence"
type: decision
status: current
authority: handoff-gate-refusal
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: [".claude/settings.json", ".superpowers/sdd/pre-task-ledger.tsv", ".claude/hooks/check-the-plan.ps1", ".claude/hooks/check-the-journal.ps1", "scripts/hook-selftest.ps1", "CLAUDE.md"]
tags: [harness, agents, process]
---

# What was decided, 2026-08-26

**`.claude/hooks/gate-the-handoff.ps1` refuses.** A `PreToolUse` hook, matcher `Skill`, narrowed
inside the script to `handoff`, returning a denial while the path to `/handoff` is closed. The
arrangement it enforces, and the staleness rule it reads, are
[[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]].

**A hook is advisory unless its page argues all three conditions, and the argument is on a page and
never in the script's header**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[no-rule-reads-a-harness-file]]). This is that page. **The licence is argued here rather than
inherited** from the lock that refuses already — every dependent of the struck advisory rule was
re-argued rather than re-linked, and a new refusal is held to the same standard.

# The condition is measured, not judged

**It is a comparison of two rows in `.superpowers/sdd/pre-task-ledger.tsv`**: the exit code on the
latest `smoke:` row, and the timestamp of the latest `write:` row naming a path git does not
ignore. The hook opens the path only when the first is zero and its timestamp is the later one.

**No judgement enters at any point.** There is no reading of what was edited, no assessment of
whether a change was risky, no inference about whether the session meant to run the check. An exit
code is a number the shell returned, and the ledger's timestamps are fixed-width so that lexical
order is chronological order ([[the-pre-task-ledger]]).

**This is the same shape as the librarian lock**, which passes the condition because
`vault-check.sh` exits a code rather than an opinion ([[the-librarian-lock-hook]]).

# The measurement is reliable where the hook stands

**The rows are already in the file by the time the hook runs.** It stands at `PreToolUse` on the
`Skill` call and it only reads: the `smoke:` row was written by the recorder hook when `make smoke`
returned, and the `write:` rows by `.claude/hooks/check-the-journal.ps1` on the writes themselves.
The hook needs no write of its own at the moment it stands, so there is no act for a mode to
prevent.

**This is exactly where `check-the-plan.ps1` fails and this one does not.** That hook speaks rather
than refuses because a ledger row cannot be written in plan mode, and plan mode is the exact moment
the ritual it guards is placed — the measurement is unreliable *where it stands*
([[the-plan-check-hook]]). Nothing of that kind is in play at `/handoff`: the session is doing
ordinary work, the writes that produce the rows have already happened, and the file is on disk.

**Where it cannot measure it must allow and say so aloud** — the ledger file missing, or
unreadable. That is the rule's own clause and it is not optional; the lock already implements it,
printing `THE LOCK DID NOT RUN` and exiting zero when it cannot find `bash`
([[the-librarian-lock-hook]]).

# The refusal says how to clear it

**The message names the command — `make smoke` — and which of the three states the path is in:**

| state | what the message says |
|---|---|
| no `smoke:` row at all | smoke has not run this session; run `make smoke` |
| the latest `smoke:` row is non-zero | smoke is red; fix what it reported and run `make smoke` again |
| the latest `smoke:` row is zero but older than the last `write:` row | smoke is stale; files changed after it passed, so run `make smoke` again |

**Naming the state is what makes the refusal clearable rather than merely conditional.** A denial
that says only *the path is closed* leaves the session guessing between three different repairs,
and the guess is made at the end of a long session. It is the same reason the lock's denial carries
the gate's own output instead of a summary of it
([[a-refusal-is-conditional-or-absolute-and-nothing-else]]).

# What this does NOT establish, and it is the half that matters

**Matcher `Skill` is registered nowhere in `.claude/settings.json` today.** Checked 2026-08-26: the
file registers `Edit|Write`, `Agent|Task`, `ExitPlanMode` and `Write|Edit`, and the string `Skill`
does not occur in it. Neither does it occur in `scripts/hook-selftest.ps1`.

**That `Skill` is matchable at all IS established, and by measurement rather than by argument** — a
probe on `PreToolUse` with matcher `Skill|Write` returned `tool=Skill | event=PreToolUse |
skill=sprint | input_keys=args,skill`, with `Write` as a control known to fire, so the run could
tell *`Skill` is not matchable* from *the hook never loaded*
([[an-argument-can-be-true-of-one-surface-and-silent-about-another]], [[session-hooks]]). The probe
registration was removed and the settings file restored with no diff.

**What is unproven is the wiring in this repository's own settings**: that a registration written
into `.claude/settings.json`, narrowed to `handoff`, fires on a real `/handoff` and returns a denial
the caller sees. **A selftest case cannot prove it.** Hooks are read at session start
([[claude-code-config-loading]]), so nothing in the session that writes the registration can show
the matcher matching — which is precisely the gap the lock shipped with and named
([[the-librarian-lock-hook]]).

**The acceptance is a restart**: in a fresh session with the ledger holding no green `smoke:` row,
invoke `/handoff` and see the refusal. **Until that acceptance passes, this hook is not enabled.**
A refusal that is silently absent looks exactly like a refusal with nothing to say
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

# Rejected

**Rejected: an advisory reminder in place of a refusal.** The reminder already exists — it is the
hook on `/retro` — and a second one at `/handoff` would fire at the exact moment a session is out of
patience. `/handoff` is the point of no return: it hands the journal to the librarian, and after it
there is nothing to return to.

**Rejected: a bypass flag.** The only moment anybody wants one is the moment the block is working.

**Rejected: putting the argument in the script's header.** That is where it does not belong, by the
rule this page exists to satisfy — a harness file is not read by anyone deciding whether the
refusal is licensed ([[no-rule-reads-a-harness-file]]).

# It was registered in the session that wrote it, against the plan, and the owner ratified that — 2026-08-26

*(the owner ratified it after the fact.)*

**The section above says *until that acceptance passes, this hook is not enabled*, and the approved
plan said the registration waits for the restart acceptance. The registration was written in the
same session as the script.** The owner was told and ratified it the same day, so this is a
divergence with a ruling on it rather than a defect left standing.

**The ground is a selftest case, not a judgement about risk.** `every hook script is either
registered or dot-sourced`, in `scripts/hook-selftest.ps1`, refuses the unregistered state — a script
on disk that nothing loads is exactly what that case exists to find. **Leaving the hook unregistered
to satisfy the plan would have left the suite red for the length of the wait.**

**And the case is a property rather than a list, which is what closed the alternative.** Its own
comment argues against giving it an exemption list: a register with an exemption list stops being a
register, because the next unregistered script is added to the list instead of being fixed
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]],
[[a-declaration-that-silences-a-check-must-expire-or-be-re-derived]]).

**The restart acceptance is still owed and nothing here discharges it.** What changed is when the
registration lands, not whether the wiring is proved: hooks are read at session start
([[claude-code-config-loading]]), so the run that shows the matcher matching is still a later session
than the one that wrote it.

**The gap that made this decidable at all was in the plan.** It ordered a wait for something a
session cannot perform, and the check that would notice the wait was already in the suite — the plan
and the harness disagreed and nothing reconciled them until the suite went red
([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

# The ground this page twice gives for the wait is false, and the `Skill` acceptance passed live — 2026-08-26

**Twice above this page says *hooks are read at session start*, and concludes that the run showing
the matcher matching must be a later session than the one that wrote it. It was not.**

**Measured the same day: `.claude/hooks/remind-the-smoke.ps1` was registered on matcher `Skill`
during the session of 2026-08-26 and fired on that same session's `/retro`.** So a settings change
takes effect without a restart here, at least for a `PostToolUse` hook, and the acceptance the
sentence deferred was available on the spot
([[claude-code-config-loading]]).

**The two sentences are left standing and answered here**, because they are the reasoning the
deferral was taken on and rewriting them would hide the fact that a decision rested on a false
premise ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**What this does and does not discharge.** The acceptance owed *by this page* is `gate-the-handoff.ps1`
returning a denial the caller sees on a real `/handoff` with no green `smoke:` row — **that has not
been observed** and stays owed. What is discharged is the *reason given* for why it could not be
observed in one session.

**And it strengthens the paragraph directly above rather than weakening it.** That paragraph records a
plan ordering a wait for something a session cannot perform; the wait was for something a session
**could** perform, which is the same defect one degree worse.

# The instrument behind *a path git does not ignore* had to be repaired — 2026-08-26

**The condition above reads the latest `write:` row naming a path git does not ignore, and the
obvious way to ask that question is broken on this host.**
[[git-check-ignore-stdin-receives-nothing-through-a-windows-powershell-pipe]]: piped into `--stdin`
the command exits `1` and prints nothing, which is indistinguishable from *no path was ignored*.

**It fails in the direction that closes this gate for ever.** With nothing ignored, every write into
`.superpowers/` counts as a real write, no `smoke:` row can ever be the later one, and `/handoff` is
refused with a message the session cannot act on. **The argument form is used instead**, and a
selftest case is what found it.

# The chain ran live and the gate PASSED; the refusal is still unobserved — 2026-08-26

**`/handoff` was attempted at the end of the session that built the hook, with a green `smoke:0` row
newer than the last write, and the gate let it through.** So the open path is measured.

**Every closed path is still held by selftest cases alone.** No real `/handoff` has been refused, and
the three refusal texts have been read by nobody who needed them. That is what this page's *what this
does NOT establish* section names, and the live pass does not discharge it — passing proves the hook
runs and reads the ledger, not that it refuses correctly.

**The reminder fired on the same session's `/retro`**, so the whole three-hook chain is live rather
than pending ([[the-smoke-gate-hooks]], [[claude-code-config-loading]]).
