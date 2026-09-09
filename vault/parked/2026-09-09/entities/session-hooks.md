---
title: "The hooks that stand around a session, and what each of them cannot do"
type: entity
status: current
authority: session-hooks
basis: code
sprint: S0
created: 2026-08-13
sources: [".claude/settings.json", ".claude/hooks/session-brief.ps1", ".claude/hooks/ask-the-vault.ps1", ".claude/hooks/vault-path.ps1", "scripts/hook-selftest.ps1", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md"]
tags: [agents, vault]
---

# The two hooks

*(This page's title read "Two hooks stand around a session" until 2026-08-17, when a third joined
them and the count became the world's rather than the page's; it now reads "The hooks that stand
around a session, and what each of them cannot do". That record stood in a `quantity:` line until
2026-08-18, when the field was rejected and the rule left unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). It is kept here because a
title corrected in place is not a supersession, so nothing else in the store records that this one
changed ([[a-title-corrected-in-place-is-not-a-supersession]]). The heading above is the pair
registered on 2026-08-13, which is what the table below lists; the third hook and the fourth event
arrived later and have sections of their own.)*

Written 2026-08-13. Both are registered in `.claude/settings.json` and neither dispatches an
agent — a hook is a shell command whose stdout is injected, and it cannot call one.

| Hook | File | Matcher | What it does |
|---|---|---|---|
| `SessionStart` | `.claude/hooks/session-brief.ps1` | `startup\|resume\|clear\|compact` | prints `brief.md` into the new session's context, with staleness warnings above it |
| `PreToolUse` | `.claude/hooks/ask-the-vault.ps1` | `Edit\|Write`, narrowed again by path inside the script | injects a reminder before a rule-bearing file is written. **Advisory: it never blocks and always exits 0** |

`.claude/hooks/vault-path.ps1` is shared by both and must answer the same question the shell
scripts answer — see [[the-vault-directory]], where the two discovery idioms are written side by
side because they once disagreed.

`scripts/hook-selftest.ps1` exercises them: **29 of 29, re-measured 2026-08-15** — unchanged from
the reading of 2026-08-14 at `42f7a56`, and
the same count as on 2026-08-13 at `76df44e` — while `log.md` records 31 and [[vault-scripts]]
recorded 25, three numbers for one script inside one store
([[a-stated-count-drifts-from-the-list-it-heads]]). The
encoding case included and the one that matters among them — *a brief in its own commit must be
silent*. The journal of that day reports 25; the count moved twice the same evening as the
staleness check was rewritten, which is the reason this page names the commit it was measured at
and not only the date.

## They are PowerShell, and that is not a preference

**Decided 2026-08-13. Rejected: bash, like the other vault scripts** ([[vault-scripts]] — four of
them on that date, **five since 2026-08-15** when `vault-catalogue.sh` was added; this line read
"the four scripts" until then).

On this machine `bash` on the *system* PATH is the WSL shim in `WindowsApps`, and with no distro
installed it answers `execvpe(/bin/bash) failed`; Git's bash is not on PATH at all. **A hook is
spawned by the OS, not by the agent's own shell**, so it gets the broken one. PowerShell is always
there.

Two consequences follow and are already paid for:

- every `.ps1` here is **pure ASCII**, and non-ASCII test data is built from character codes,
  because **a `.ps1` without a BOM is read in the ANSI codepage** — the self-test broke on its own
  fixture before it reached a hook;
- both scripts set UTF-8 explicitly, output for the brief and input as well for the guard, which is
  handed JSON on stdin. The full rule and both failures: [[windows-console-encoding]].

## What the brief hook checks, and why it is two checks

It **prints; it never generates**. Generating would charge a round trip before the first line is
typed, and the brief is written at the end of the previous session while the owner can still see it
lie ([[journal-vault-brief-each-artefact-has-one-owner]]).

It reports two failures that look identical to a reader and are not. **The brief therefore carries
two stamps**, both in its first six lines, and both are read there only — anywhere else in a brief
they are quotation:

- **commits have landed since the brief was written** — asked of **git history**, not of the stamp:
  the commit that carries `brief.md` is the zero point, and a brief with uncommitted changes is
  never stale. `generated-at:` is *not* compared, and why not is
  [[the-brief-is-stamped-with-its-commit]];
- **`ingested:` names a journal that is not the newest** in `raw/handoffs/` — no ingest ran at all;
  the last session wrote its handoff and stopped.

**Neither comparison uses mtime.** The first version of the second one compared timestamps and
fired on **every fresh clone, deterministically**: git writes the working tree in index order, so
`brief.md` always lands microseconds before `raw/handoffs/…`. It printed *above* the warning that
matters, and a false alarm on top of a true one trains the reader past both. The first version of
the *first* one had the same disease from the other end — see the page above.

**Staleness is reported, never enforced.** A stale brief is still the best summary available; the
point is that the reader is told which parts to distrust. Two rules follow from that and are in the
code:

- **the brief is printed whatever else happens.** Every check sits in its own `try`/`catch` and can
  contribute at most a warning line. The first staleness check called `git` from inside the
  *printing* path, so on a machine where git is not on the hook's PATH — and a hook is spawned by
  the harness, not by an agent's shell — the session got a PowerShell error where its brief should
  have been. **A check that can cost the reader the thing it is checking is worse than no check.**
- **`\r` is stripped before the stamps are matched.** They are anchored with `$`, and a CRLF file
  leaves a carriage return before every line end, so the whole staleness check silently found
  nothing. Third time this project has met that character.

## What the guard cannot do

`.claude/hooks/ask-the-vault.ps1` cannot enforce the one-writer rule, because **a `PreToolUse`
payload does not say who is writing** — the librarian's writes and anyone else's are the same JSON.
It is a reminder, and the enforcement is `git diff` plus `log.md`, which `/ingest` now explicitly
asks the caller to perform: [[the-librarian-writes-unattended]].

Two details of it are load-bearing rather than tidy, both from defects:

- it parses the payload with `ConvertFrom-Json`, not a regex — a `Write` call carries the whole
  file body in the same object, so a file *containing* the text `"file_path": "…"` can redirect a
  greedy pattern onto a path that is nobody's business;
- backslashes are normalised with `.Replace`, not `-replace`, whose right-hand side is a regular
  expression in which a lone backslash is invalid. Written the other way it errored on every
  payload, printed nothing and still exited 0 — **a guard that was silently never there**
  ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

The matcher is narrow on purpose: a guard on every edit becomes a ritual performed without reading.

## Both hooks have now been observed firing — 2026-08-14

**The `SessionStart` hook fires.** The brief arrived in a session that asked for nothing, marked
`SessionStart:clear hook success:`, carrying the full text of `brief.md` and **no staleness
warnings** — which was also correct, the tree having stood still. So `$CLAUDE_PROJECT_DIR` **does**
expand in the shell the harness spawns hooks with on Windows, and the fallback path was not needed.

**The matcher that fired was `clear`.** `startup` shares the same matcher string and the same
command and has still **not** been observed on its own; nothing suggests it behaves differently,
and nothing has shown that it does not.

**The `PreToolUse` guard fires**, confirmed again the same day: twice on `CLAUDE.md`, once on
`Edit` and once on `Write`, injecting its advisory text. Advisory as designed — it did not block
and did not fail.

## The staleness warning fired for real — 2026-08-15

Until then the `SessionStart` hook had only ever been seen carrying a brief with **no** warnings,
which proves the hook runs and proves nothing about the check inside it. On 2026-08-15, on a
resume, it printed *"6 commits have landed since `36e9e4c`"* — **and the count was exact**.

Two properties were confirmed at once, both of them the load-bearing half of the design: it counts
from **the commit that carries `brief.md`**, not from the brief's own `generated-at:` stamp — which
is one commit behind by construction and would warn every session for ever — and it counts commits
rather than comparing an mtime ([[the-brief-is-stamped-with-its-commit]],
[[staleness-checks-run-at-different-times-and-ask-different-questions]]). A check never observed failing is not known to check
anything ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]); this one has now been
observed doing both.

The paragraph below is what stood here until that morning, kept because the diagnosis it carries is
the one to reach for if the hook ever stops arriving.

**The `SessionStart` hook had never been seen firing.** A hook is read when a session starts, and
this one was written by the session it would have served — the same rule as an agent definition,
[[claude-code-config-loading]], which until now recorded hooks as untested and said to assume they
follow it.

The `PreToolUse` guard **was** observed, on every write into `wiki/` during the first ingest. Only
the brief hook is outstanding, and it answers itself: if the brief arrived without anyone asking,
it fired.

**If it does not, the diagnosis is `.claude/settings.json`.** Both hooks are registered through
`$CLAUDE_PROJECT_DIR`, and whether that expands depends on the shell the harness spawns hooks with
on Windows. The fallback is a relative path, which works from the project root and fails from
anywhere else.

## A third hook joined them — 2026-08-17

**`PostToolUse` on `Write|Edit`, narrowed inside the script to `<vault>/raw/handoffs/*.md`:**
`.claude/hooks/check-the-journal.ps1` runs the vault gate the moment a journal lands. It has its own
page — [[the-journal-gate-hook]] — because it answers a different question from these two: not *what
does a session start and end with*, but *what happens when the one immutable artefact of a session
is written*.

Two facts from it belong here, beside the hooks they are about:

- **`bash` cannot be named on this machine and has to be derived**, by walking up from wherever
  `git` resolves ([[a-hook-finds-bash-by-walking-up-from-git]]). That is the same PATH problem this
  page records as the reason all of these are PowerShell, met from the other side: not *what can a
  hook be written in*, but *what can a hook call*.
- **`scripts/hook-selftest.ps1` is at 40 of 40**, measured 2026-08-17, up from 29 at the start of
  that session. The number moved because the third hook arrived with cases, including the branch
  where `git` is off PATH.

## The `SessionStart` staleness check was wrong about which journal is newest — fixed 2026-08-17

It took the newest journal as `Sort-Object Name -Descending | Select-Object -First 1` and compared it
against the brief's `ingested:`. **Two journals of one day sort by their slug, not by time.** With
`2026-08-16-the-harness-becomes-a-build.md` and `2026-08-16-the-structure-questioned.md` both
compiled, the sort returned the earlier one and the alarm fired on a journal that had been ingested
hours before. **A date prefix orders sessions only while there is one a day.**

**The check now asks whether each journal has a `.coverage.tsv` sidecar beside it** — a
file-existence test that no ordering can break, and one that also names *which* journals are
uncompiled instead of naming one. A second clause fires when the brief's `ingested:` names a journal
that does not exist, which is a brief to distrust outright.

It was **proved in both directions before committing**
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]), and it was written by the main session
rather than by the librarian, under the same permission as the title corrections
([[hand-edits-of-the-wiki-are-a-recorded-divergence]]).

**The rule this defect broke is one of this project's own**: an alarm that fires when nothing is
wrong is one you learn not to read — which is why it was fixed the day it was noticed rather than
filed.

## What none of the three can do

**Refuse an ingest.** The `PostToolUse` gate reports a malformed journal and cannot stop the
expensive step that follows it; the design that would is
[[a-lock-on-the-librarian-dispatch]]. **Refuse work outside a sprint** is the other one, and it
cannot live on `SessionStart` at all, because that event injects context and has no way to deny:
[[a-gate-that-refuses-work-without-an-open-sprint]].

## A fourth event was registered, and it is a measurement rather than a hook we keep — 2026-08-18

**`InstructionsLoaded` is a real harness hook event, not a name someone invented.** The corpus had
the name and nothing else. What it is:

- it carries **matchers by load reason**, `path_glob_match` among them — so a hook can tell *why*
  instructions were loaded, which is exactly the question a `paths:`-scoped rule raises;
- **its exit code is ignored.** It is observation only and cannot block a load, which puts it in the
  same class as the `PreToolUse` guard above: a reminder, never a gate.

**`.claude/hooks/instructions-loaded.ps1` and the `InstructionsLoaded` block in
`.claude/settings.json` exist only to serve the probe**, and both are cleared when it is spent
([[the-conditional-delivery-probe]]). They are listed here because a reader of this page counting
hook events would otherwise find one that no page explains.

**It is the second observable of a two-instrument measurement**, not the primary one: the primary is
a reader quoting a nonce, and the log exists so that *the rule did not load* can be told from *I did
not measure* ([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]).

## The `PreToolUse` guard turned out to be the answer to a question two sessions had been pricing — 2026-08-19

**Nothing about the hook changed. What changed is that somebody read this page.**

The owner had rejected `PreToolUse` on `Edit|Write` as the guard for a path-scoped rule, because *"it
fires on every edit and write, and scoping is the whole reason `.claude/rules/` with `paths:` was being
tried"*, and a previous session had queued a **latency measurement** to price it. **The table above
already says that `.claude/hooks/ask-the-vault.ps1` is registered under exactly that matcher**, and has
been since 2026-08-13.

**So a PowerShell process is already spawned on every Edit and Write in this repository.** The latency is
sunk, the measurement is not owed, and a guard for the post-compaction edit is **a fourth branch in a
script that already spawns** rather than a new hook — zero new processes
([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]],
[[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

**And the narrow-matcher sentence in the section above is the principle such a guard needs**, written
here for the same reason it would be written there: *a guard on every edit becomes a ritual performed
without reading; a guard on rule-bearing paths fires exactly where the recorded divergences happened.*

**What the objection was right about, once narrowed:** the hook receives the tool input including
`file_path`, so it can match and exit immediately and **no scoping is lost**. What is spent is latency on
every `Edit|Write` in the repository, and that number is what the option is taken or dropped on. Not a
closed decision ([[an-objection-priced-against-a-cost-already-paid-dissolves-on-a-page-nobody-opened]]).

## The guard gained a branch, and it is the one the whole `.claude/rules/` design rests on — 2026-08-19

**`.claude/hooks/ask-the-vault.ps1` now has a branch that reads `.claude/rules/`**, matches each
file's `paths:` against the payload and injects the body as `additionalContext`. It has a page of
its own, because it answers a different question from the row in the table above — not *what stands
around a session* but *what re-delivers a rule the context lost*
([[the-guard-branch-lives-inside-a-hook-that-already-runs]]).

**Two facts about this script changed with it.** It now **strips HTML comments outside fenced
blocks**, so that both delivery paths hand out the same text; and it is **last in the chain**, so a
rule scoped where an earlier branch already speaks is shadowed.

**Measured, and it settles the objection this page recorded as open.** The guard branch costs
**17–21 ms** on top of the **177 ms** this repository already pays for the hook, and the count of
rules barely moves it — 15 runs per case, medians, four cases back to back under the same load: as
it ships on a non-matching path **177 ms**; with the branch, one rule and no match **194 ms**, ten
rules and no match **198 ms**, one rule matching and speaking **202 ms**. A bare
`powershell -NoProfile -ExecutionPolicy Bypass -Command 'exit 0'` is **79 ms**, so roughly half of
today's cost is interpreter startup that any PowerShell hook pays and none of it is new
([[an-objection-priced-against-a-cost-already-paid-dissolves-on-a-page-nobody-opened]]).

**The first instrument lied and the measurement stand had to be fixed first**: piped from Git Bash,
`[Console]::In.ReadToEnd()` receives nothing, so a hook reads an empty payload and exits 0 in
silence — the shipping hook does the same, so *"the guard printed nothing"* was a reading of the
harness ([[a-hook-is-measured-from-powershell-or-not-at-all]],
[[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]).

**`scripts/hook-selftest.ps1` is at 54 caught, 0 missed, exit 0**, from 40 at the start of that
session.

## Advisory is now a ruling rather than a description — 2026-08-19

**This page says of the `PreToolUse` guard: *"Advisory: it never blocks and always exits 0"*, with
`basis: code`.** That is what the script does. **What was decided** is
[[advisory-is-the-default-for-a-hook]]: a hook may refuse only where the action is irreversible and
the refusal cannot be wrong, both at once, and no hook here meets both.

**The distinction is load-bearing and was found the hard way.** The guard branch built above chose
advisory with nothing behind the choice, and this page was the only thing to inherit from — a record
of behaviour read as a policy ([[no-rule-reads-a-harness-file]]). **This page keeps describing; the
decision page is where the policy is read from.**

## The `InstructionsLoaded` block is gone from `.claude/settings.json` — 2026-08-19

**Removed**, with `bash scripts/vault-check.sh` at exit 0 and 21 advisories before and after,
byte-identical output. It is a settings key rather than a cited path, so nothing pointed at it.

**`.claude/hooks/instructions-loaded.ps1` is left on disk and is now inert**: two pages name it in
`sources:` and deleting it reddens the gate
([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]). The section above naming both
as *"cleared when the probe is spent"* is half-executed and says so here rather than being edited.

## A fourth hook joined them, and the guard grew a net — 2026-08-20

**`.claude/hooks/check-the-plan.ps1`, on `ExitPlanMode`**, registered for both hook events. It has
its own page — [[the-plan-check-hook]] — because it answers a different question from these: not
*what does a session start and end with*, but *has the plan about to be presented been checked
against the vault*.

**Why a separate process at all**, given this page's rule that a hook on every edit becomes a ritual
performed without reading: **a bare PowerShell spawn on this machine is 133 ms**, and the write path
fires 71 to 108 times in a working session. A rare event pays nothing for a file of its own; a
frequent one would have paid 9 to 14 seconds per session.

**`.claude/hooks/ask-the-vault.ps1` changed shape.** The branch chain no longer prints — it assigns,
and one note is emitted at the end, because two calls to `Write-Note` would have put two JSON
objects on one stdout and nothing downstream reads that
([[the-guard-chain-appends-the-net-rather-than-branching-on-it]]). The pre-task net is **appended
after** the chain has picked, so an earlier branch still wins its path.

**`.claude/hooks/session-brief.ps1` gained a side effect**: it stamps the session identifier,
printing nothing. A script the session runs is handed no `session_id`, and the stamp is what lets
`/pre-task` record itself at all ([[the-pre-task-ledger]]).

**And `.claude/hooks/pre-task-state.ps1` is registered nowhere on purpose** — a dot-sourced library,
which is the third kind of file under `.claude/hooks/` after a registered hook and a shared helper
([[the-pre-task-state-library]]).

**The ledger is also the heartbeat these hooks never had.** A session that edited files and left no
row has hooks that never loaded, which no reading of `.claude/settings.json` can detect
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).

## The `SessionStart` hook gained two more side effects, and still prints nothing while doing them — 2026-08-20

**`.claude/hooks/session-brief.ps1` now does three things besides printing the brief.** It stamped
the session identifier from the day before; it now also **rotates the pre-task ledger** when
`source` is `startup`, and **appends a `session-start:<source>` row** on every one of its four
matchers ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]],
[[the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal]]).

**It is silent throughout.** Every one of these is a write to a git-ignored file, and the rule this
page already states holds: the brief is printed whatever else happens, and each side effect sits
where it cannot cost the reader the thing the hook exists for.

**The `source` field is what makes the four matchers distinguishable at last.** This page has
recorded since 2026-08-14 that `clear` was observed and `startup` was not; the row now names which
one fired, in a file that survives the session ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**`scripts/hook-selftest.ps1` is at 107 caught, 0 missed**, from 94 at the start of that session.
**Thirteen cases were added and the count moved by thirteen** — which is the reading that matters,
not the total: a branch added while the count stands still is the signal
([[a-fixture-must-materialise-what-the-subject-reads]]).

## The `SessionStart` hook resolves a journal in both places it can be — 2026-08-21

**`.claude/hooks/session-brief.ps1` checks that the file named by the brief's `ingested:` line
exists, and it now looks in `raw/handoffs/` and in `archive/*/*/handoffs/`.** `/ingest` archives the
journal it compiled as its last step, so a single-place check would have fired on every session
start ([[the-ingested-line-stays-a-filename-and-the-hook-resolves-it-wherever-the-journal-lives]],
[[vault-archive-sh]]).

**That is the alarm class this file has now removed three times** — a check that fires when nothing
is wrong ([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

## A hook can see which skill was invoked, and it was measured — 2026-08-21

**A probe registered on `PreToolUse` with matcher `Skill|Write` returned a `Skill` row carrying the
skill's name in a structured field.** `Write` was the control, known to fire, so the run could
distinguish *`Skill` is not matchable* from *the hook never loaded*
([[an-argument-can-be-true-of-one-surface-and-silent-about-another]],
[[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]).

**The probe was registered in `.claude/settings.json` and the file was restored with no diff.** A
temporary harness registration is still a harness change and is recorded as one
([[a-replacement-and-a-widening-were-ratified-after-the-fact]]).

**What this surface is not**: it is not a way to tell a `/pre-task` from a `/vault-ask` at the
dispatch, which is a different surface and is unchanged
([[the-ritual-records-itself-rather-than-being-detected]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# Which of these refuses is a test now, and the sentence saying none of them does went false — 2026-08-21

**The section above, *Advisory is now a ruling rather than a description*, ends on the claim that no
hook here meets the blocking test. That went false on 2026-08-20**, when
`.claude/hooks/lock-the-librarian.ps1` landed and refused, and it stood for a day on this page and on
a `decisions/` page at once. **It is marked rather than edited**, and the reason it survived is that
nothing enumerated the set: the claim ranges over every registration and checking it meant opening
every script by hand.

**The enumeration is now cases in `scripts/hook-selftest.ps1`**, on the owner's ruling of that date,
and never prose alone ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**Read from `.claude/settings.json` at the ingest of 2026-08-22:** six registrations across
`SessionStart`, `PreToolUse` and `PostToolUse`; five scripts, one of them registered twice;
**exactly one refuses** — the lock, via `permissionDecision = 'deny'`.

**And the test a refusal is decided by is no longer the one this page's section cites.** The owner
struck the irreversible-and-cannot-be-wrong rule as a rule he never gave, and the test is now a
measured condition, a measurement reliable where the hook stands, and a refusal that says how to
clear it
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

**`scripts/hook-selftest.ps1` is at 114 caught, 0 missed**, from 110 at the start of that session —
**the count moved by exactly the four cases added**, which is the reading that matters rather than
the total ([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`, and from `.claude/settings.json` read at that ingest.)*

# The rule behind *Advisory is now a ruling* was struck, and the section is re-argued rather than edited — 2026-08-22

**The section *Advisory is now a ruling rather than a description* cites
[[advisory-is-the-default-for-a-hook]] for the policy and closes on *"no hook here meets both"*.**
The owner disowned that rule on 2026-08-21, and the page now carries `status: deprecated`,
`superseded_by:` and an address in `archive/`
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]). **The section
stays exactly as written.**

**Its closing clause went false on 2026-08-20**, the day `.claude/hooks/lock-the-librarian.ps1`
landed and refused. **It was marked rather than rewritten at the ingest of 2026-08-21**, in the
section immediately above this one, and nothing here rewrites it either
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]). **What made it uncheckable
was that nothing enumerated the hook set**; the enumeration is now a case per registration in
`scripts/hook-selftest.ps1`, never prose alone
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**The distinction this page states survives the strike unchanged**: this page keeps describing what
each script does, with `basis: code`, and the policy is read from a `decisions/` page — which is now
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]].
**A description of behaviour is still not a policy** ([[no-rule-reads-a-harness-file]]).

**Re-argued for the `PreToolUse` guard in the table at the head of this page**, whose row reads
*"Advisory: it never blocks and always exits 0"*: it stays advisory, and the ground has moved from a
judgement to something checkable. Its write net reads the pre-task ledger, and **a ledger row cannot
be written in plan mode** — the exact moment the ritual is placed — so the measurement is unreliable
where the hook stands ([[the-pre-task-ledger]],
[[the-guard-branch-lives-inside-a-hook-that-already-runs]]). Its rule-delivery branch measures a
`paths:` glob against the payload, which is measured, but has no measurement for the thing a refusal
there would rest on: whether the writer already has the rule in context.

**The lock is the one registration that refuses, and it satisfies all three conditions**
([[the-librarian-lock-hook]]).

# A sixth script joined them, and it is the first that records rather than speaks — 2026-08-22

**`.claude/hooks/record-the-dispatch.ps1`**, on `PostToolUse` with the matcher `Agent|Task`. It
writes one ledger row per **returned** dispatch, `dispatch:<subagent_type>`, and produces no output
at all — it neither refuses nor speaks, which is a third disposition this page's table did not have
a column for ([[the-dispatch-record-hook]]).

**The set is now seven registrations across three events and six scripts**, read from
`.claude/settings.json` on this date, with `check-the-plan.ps1` still the one script registered
twice. **Exactly one still refuses and it is still the lock**
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]], [[the-librarian-lock-hook]]).

**What it repairs is named in the section above this one.** The `PreToolUse` guard's write net reads
the pre-task ledger, and a ledger row could not be written in plan mode — the exact moment the rule
places the ritual — so the measurement was unreliable where that hook stands. **A hook can write
during planning**, which is what this registration turns into a row
([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

**It is not a candidate for the refusal test at all**: `PostToolUse` fires after the act, so nothing
registered there can deny however good its case.

**Owed against a session restart** — that it fires in a live session. It did not fire on the
librarian dispatches of this date, because it was registered after they had begun
([[claude-code-config-loading]]).

# A seventh script joins them on a fourth event, and it is the first that reads what the assistant says — 2026-08-24

**`.claude/hooks/catch-the-feedback.ps1`, on `MessageDisplay`, with no matcher** — the event takes
none. It lifts a fenced `VAULT-FEEDBACK` block out of the assistant's own reply into
`.superpowers/sdd/vault-feedback.md`, so a session never writes that file
([[the-feedback-catcher-hook]], [[the-session-speaks-the-feedback-line-and-a-hook-files-it]]).

**Registered as `speaks`**, and entered in the register at `scripts/hook-selftest.ps1:980-1058`.
**Exactly one registration still refuses and it is still the lock**
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]],
[[the-librarian-lock-hook]]).

**What is new about its input.** Every other hook here reads a tool call, a prompt or a session
event; this one reads the **assistant's own message**, arriving as `delta` and keyed by
`message_id`. The event fires once with the whole message on this host, against its own description
([[message-display-fires-once-with-the-whole-message]]).

**Registering it took effect immediately, with no restart** — which is not true of everything in
this harness ([[claude-code-config-loading]]).

## `session-brief.ps1` changed the same day, in two ways

**It writes the session's `transcript_path`** to `.superpowers/sdd/session-transcript.path` at
`SessionStart`, which is how the dialogue extractor knows which of 37 transcripts is this session
([[the-session-dialogue-extract]]).

**It gained `[Console]::InputEncoding`.** Six of the seven hooks read stdin and five set it; this
one did not, and a field carrying a user profile path was added to it the same day
([[windows-console-encoding]]). **Nothing checks the pair**, and that is the standing gap rather
than the fix.

## And testing this hook by hand has live side effects

**`session-brief.ps1` rotates the pre-task ledger on `source: startup` and restamps the session on
any `session_id`**, so a probe with a made-up id destroys live state. It did, on 2026-08-24, and the
rows were restored by hand ([[testing-a-session-start-hook-with-a-made-up-payload-has-live-side-effects]]).

# The selftest reading rose and its wall clock fell, and the two moved for different reasons — 2026-08-26

**`scripts/hook-selftest.ps1` reads 169 caught, 0 missed, in 42 seconds**, against 148 caught in
2m17s at the previous reading of the same day. **Neither half of that is one change.**

**The fall in wall clock is the green-gate case leaving.** It ran a full `vault-check.sh` against the
real tree inside the suite, so one case carried most of the runtime; it was thrown out rather than
deferred again ([[the-green-gate-selftest-case-is-thrown-out-rather-than-deferred-again]]).

**The rise in cases is twenty-two new ones for the smoke gate**, which is a different subject
entering the same file rather than the existing subjects being tested harder
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

**So the two figures may not be compared as a before and after.** A cheaper suite with more cases
looks like an efficiency and is not one: the expensive case was removed and cheap cases were added,
and nothing here says anything about the cost of the cases that were already there
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]],
[[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]).

**The reading moved twice more the same day: 175, then 180 caught, 0 missed.** Both rises are cases
added for the retro reminder, the smoke recorder's background branch and the handoff gate — **still a
count of cases and still not a coverage figure.** The number is recorded because the suite's own
total is the only thing standing between a case that did not run and a case that passed
([[an-instrument-that-fails-towards-nothing-to-do]]).

**A settings change was measured taking effect without a restart on the same day**, which is the
first hook observation in that direction and is filed on the page that owns the question
([[claude-code-config-loading]]). It bears on this page's own recurring shape — a hook registered and
never observed firing is indistinguishable from one with nothing to say — but it is one observation
and it does not overturn the 2026-08-22 reading that went the other way.

# Three more scripts join them, and one of them is the second that can refuse — 2026-08-26

**The smoke gate is three hooks, built and registered in one session, all of them on events this
page already lists** ([[the-smoke-gate-hooks]]).

| file | event, matcher | narrowed to | what it does |
|---|---|---|---|
| `remind-the-smoke.ps1` | `PostToolUse`, `Skill` | `retro` | demands a foreground `make smoke` and a `VAULT-FEEDBACK` block per turn. Never refuses |
| `record-the-smoke.ps1` | `PostToolUse`, `Bash` | a `make smoke` or `make suite` command | writes `smoke:<exit code>`, reading the printed marker rather than an exit code |
| `gate-the-handoff.ps1` | `PreToolUse`, `Skill` | `handoff` | **refuses** while the session has no green smoke behind it |

**`gate-the-handoff.ps1` is the second script here that can refuse**, after the plan check
([[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]]).

**`check-the-journal.ps1` gained a job it did not have**: it writes a `write:<path>` row before any
of its own narrowing, so the write history the gate reads costs no new registration on `Write|Edit`
([[the-journal-gate-hook]]).

**The `Skill` matcher was proved live rather than inferred.** `remind-the-smoke.ps1`, registered
during the session that wrote it, fired on that same session's `/retro` — which is one observation
against *hooks are read at session start*, a sentence this repository had written into three places
and which is false ([[claude-code-config-loading]]).

**The selftest reading rose again**: `scripts/hook-selftest.ps1` reports **caught 180, missed 0** at
the end of that day, from 175 and before that 169. All of it is cases added, and the last five are
the reminder's two demands plus three for a backgrounded `make smoke`. **It is a case count and never
a coverage figure.**

# `remind-the-feedback.ps1` joined on 2026-08-28

**Registered on `UserPromptSubmit`, which takes no matcher.** It reads the write time of
`.superpowers/sdd/vault-feedback.md`, carries a silence counter, and speaks on the third consecutive
quiet prompt ([[the-feedback-reminder-hook]]).

**It is the first hook here that decides whether to speak.** Every other one either always speaks or
always refuses ([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

**`scripts/hook-selftest.ps1` reads caught 194, missed 0 in 55 s** on 2026-08-28, up from 180 at that
session's start — fourteen new cases, replacing the nine written for the `PostToolUse` version the
owner overturned the same day
([[the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet]]).

**`MessageDisplay` remains registered and unused for this purpose**, and it is where a counter over
the session's own replies would live.

# `serve-the-rule.ps1` joined on 2026-08-30

**Registered on `PreToolUse` with the matcher `Edit|Write`**, beside `ask-the-vault.ps1` rather than
inside it. It hands over the rule pages that govern the file about to be written, says a thing once
per file per session through the ledger, and **never refuses** ([[the-rule-server-hook]],
[[the-rule-server-is-a-hook-of-its-own]]).

**It is the second hook here that decides whether to speak** — the feedback reminder was the first —
and it decides on a different basis: the reminder counts silence, this one asks whether it has already
said this thing about this file.

**It is silent by path rather than by caller.** A write inside `wiki/` or `archive/`, or to any of the
six registers, produces nothing, because that is the librarian working. **Scoping by agent is not
available**: hooks in `settings.json` do reach subagents, proved here on 2026-08-20
([[hooks-in-the-settings-file-apply-inside-subagents]]), and an agent's frontmatter may add hooks and
may not remove them.

**`.claude/hooks/pre-task-state.ps1` gained a `served-rule` event and a `ServedRuleFiles` field** in
the same change, using the same path column as the `write` row, and **never emptied within a session**
— unlike `WritesAfterSmoke`, nothing makes a served rule stale ([[the-pre-task-ledger]]).

**Its cost, measured through a pipe under load: 750–930 ms**, against 941 ms for `ask-the-vault.ps1`
in the same conditions and 359 ms for a bare spawn. **An earlier pair of 99 ms and 141 ms is void** —
taken from a terminal with no stdin, which is a shape no hook here ever runs in
([[a-process-is-measured-with-the-stdin-it-will-have]]).

**`scripts/hook-selftest.ps1` reads caught 224, missed 0** at the end of that day, from 218. **And it
must be given `< /dev/null` unless it is run in the foreground**: backgrounded, it leaves standard
input open and hangs — 330 minutes on a third of a second of CPU
([[backgrounding-a-task-that-reads-standard-input-is-what-hangs-it]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
