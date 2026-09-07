---
title: "`make` is the entry point, and every check has a target, a trigger and an obligation"
type: proposal
status: current
authority: check-system-arrangement
basis: human
sprint: S3
created: 2026-08-26
decided_by: [[a-proposal-page-settles-who-runs-which-check-and-when]]
sources: ["scripts/vault-check.sh", "scripts/vault-check-selftest.sh", "scripts/hook-selftest.ps1", "scripts/session-dialogue-selftest.py", "scripts/vault-measure-selftest.py", ".claude/settings.json", ".superpowers/sdd/pre-task-ledger.tsv", "CLAUDE.md"]
tags: [testing, harness, process]
---

# What this page is

**The arrangement of the whole check system**: which check exists, what each one costs, who fires
it, at which moment, and what a red result from it obliges. It is the page the owner ordered on
2026-08-26 — «формируем конкретную страницу proposal для того, чтобы разобраться с тестами»
([[a-proposal-page-settles-who-runs-which-check-and-when]]) — and everything below was settled by
him in conversation that day, unless a clause says otherwise.

**Nothing here is built.** There is no `Makefile` in this repository today, no
`.claude/hooks/gate-the-handoff.ps1`, and no registration of the hooks named below. That is what
makes this a proposal rather than a record.

# The targets

Six, and the name of each is the word the vault already uses for the thing it runs
([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]]).

| target | what it runs | cost |
|---|---|---|
| `gate` | `bash scripts/vault-check.sh` alone, against the **live corpus** | 21.5 s at 682 files |
| `smoke` | `gate`, then `style`, then the three cheap selftests whole, then `scripts/vault-check-selftest.sh --only <pattern>` | about three minutes |
| `suite` | all four selftests whole, so `smoke` is literally a subset of it | the long one |
| `test` | `uv run pytest -q` — the product, 550 test functions | about 75 s on an idle machine |
| `style` | `uv run ruff check src tests` and `uv run ruff format --check src tests` | seconds |
| `help` | prints the list above | free |

**`gate` is unchanged.** It reads the live corpus, builds no sandbox, breaks nothing, and the
21.5 s figure is the one measured at 682 files on 2026-08-26.

**The three cheap selftests are `scripts/hook-selftest.ps1`, `scripts/session-dialogue-selftest.py`
and `scripts/vault-measure-selftest.py`.** They run whole inside `smoke` because none of them
copies the corpus. Only `scripts/vault-check-selftest.sh` does, which is the whole reason it is
narrowed rather than run ([[the-selftest-is-a-mutation-test-of-the-gate]]).

**The narrowing is `--only <pattern>`, which exists on the script already**, and the make variable
carrying it is `ONLY=`, so a session runs `make smoke ONLY=<pattern>`. The pattern is **named by
the session**, never inferred from a diff — an inferred selection fails towards a green run, which
is the clause [[the-smoke-runner-is-built-first-thing-next-session]] settled and which survives
here untouched.

**`suite` settles what the naming page left as "the full sweep"**. It is the four selftests whole,
and the containment is the point: a green `suite` implies every case `smoke` would have run.

**`help` is typed by hand and not generated.** Generating it from the targets is carried, not
built. A generator is a second reader of the same list, and this project has paid for two readers
of one condition before; it is simply not worth building today.

## Why the style target is called `style` and not `lint`

**`lint` is taken twice over in this repository** — `/vault-lint` is a skill, and
`bash scripts/vault-check.sh --lint` is a mode of the gate. A third `lint` meaning *ruff over
`src` and `tests`* is exactly the collision the naming decision of the same day was taken against,
and the precedent it cites is *retrospective*, which meant two things for three days and put two
live, contradictory answers in the vault
([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]]).

## The composition of `smoke` is wider than the page that designed it, and the widening is his

**[[the-smoke-runner-is-built-first-thing-next-session]] named the three cheap selftests plus the
narrowed suite. The owner added `gate` and `style` on 2026-08-26**, so that one command covers the
whole repository cheaply — the vault, the harness and the Python style in a single run.

**This is a widening of that page's composition clause and not an overturn of the page.** Its other
two clauses stand exactly as written: *a floor always runs*, and *the selection is named by the
session rather than guessed*. Both are restated above because this page is the one a reader will
open.

# `make` is the answer, and that closes the open clause

**[[the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate]] left one thing open** —
"whether `make` is the answer, as against a shell script or a skill" — because the owner reopened
the question rather than settling it. **This page is the clause it was waiting for.** He settled it
on 2026-08-26 by approving the plan this arrangement was written into: it is `make`.

**GNU Make 4.4.1, at `/c/ProgramData/chocolatey/bin/make`, measured present on 2026-08-26.**

**Rejected: a shell script.** **Rejected: a skill.** Both were live candidates in the same
conversation and neither was chosen.

# Who runs what, and when

| check | fired by |
|---|---|
| `gate` | `.claude/hooks/check-the-journal.ps1` on a write into `raw/handoffs/`; once at `/ingest` step 10; and again inside `smoke` |
| `smoke` | the agent, reminded by a hook at the start of `/retro`, and again as the **last action before** `/handoff` |
| `suite` | at a sprint's close, or in a rare case somebody names |
| `test` | the session |
| `style` | the session, before every commit |

**The `suite` cadence is unchanged** from [[the-suite-stops-running-every-session]]; this page
inherits it rather than deciding it again.

**`smoke` runs twice per session by design.** The run at the start of `/retro` is a reading — it
tells the retro what is broken while there is still a conversation to fix it in. The run before
`/handoff` is the one that matters, because it is the last thing that happens before the journal
leaves the session.

# What a red result obliges

| check | red means |
|---|---|
| `gate` | loud, does not block. Unchanged |
| `smoke` | **blocks `/handoff`, with no bypass** |
| `suite` | blocks a sprint's close |
| `test` | blocks a commit |
| `style` | blocks a commit |

**The ground for blocking at `/handoff` is the owner's own**: `/handoff` hands the journal to the
librarian and is the point of no return, so the check belongs immediately before it. A session that
goes red returns to the retro, fixes what broke, and runs `smoke` again.

**There is no bypass and none is designed.** A flag that skips it would be used at the end of a
long session, which is the only moment it matters.

**What enforces a red `suite` at a sprint's close is deliberately not built and is carried.**
Closing a sprint is a topic of its own and this page does not open it.

# The hole this leaves, stated rather than hidden

**`test` is deliberately outside `smoke` and outside the block.** A session that edited `src/` can
therefore hand its journal to the librarian with the product untested.

**It is a known hole and it costs nothing while product work may not interleave into a vault
sprint.** The day those two kinds of work share a session is the day this clause has to be
reopened. It is recorded here so that reopening it is a decision somebody takes rather than a
defect somebody discovers.

# The hooks

Three, all writing to and reading from the ledger that already exists,
`.superpowers/sdd/pre-task-ledger.tsv` ([[the-pre-task-ledger]]).

| hook | event and matcher | narrowed to | what it does |
|---|---|---|---|
| the retro reminder | `PostToolUse`, matcher `Skill` | `retro` | reminds the agent to run `smoke`. **Never refuses** |
| the smoke recorder | `PostToolUse`, matcher `Bash` | a command containing `make smoke` | writes the row `smoke:<exit code>` |
| the handoff gate | `PreToolUse`, matcher `Skill` | `handoff` | **refuses while the path is closed** |

**The smoke recorder is `PostToolUse` and not `PreToolUse`, by the ledger's own rule**: a returned
result is evidence that work happened, and an intention to run something is not. It is the same
reasoning that put `check-the-journal.ps1` on `PostToolUse` — the condition being recorded does not
exist until the command has returned ([[the-journal-gate-hook]]).

**There is no fourth registration on `Write|Edit`.** The row `write:<path>` is written by
`.claude/hooks/check-the-journal.ps1`, which is already registered on that matcher and already runs
on every write. A further PowerShell spawn on the write path is the cost the harness measured and
refused once already ([[the-plan-check-hook]]).

**The handoff gate's refusal is argued on its own page**, because a hook is advisory unless its
page argues all three conditions
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]]).

# The staleness rule

**The path to `/handoff` opens only when the latest `smoke:` row is zero AND newer than the last
`write:` row on a path git does not ignore.**

**Both halves are load-bearing.**

- *Latest*, not *any*. The fix loop produces several `smoke` runs in a session, so a green row
  early in the day would otherwise license every write after it.
- *Newer than the last write*. A green run taken before the last edit is evidence about a tree that
  no longer exists ([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]]).

**`.superpowers/sdd/` is git-ignored in full** — `.superpowers/sdd/.gitignore` holds `*` — so
`/retro`'s own transit files do not close the path. Without that clause the ritual's own writing
would invalidate its own green run every time, and the rule would be unusable on the day it landed.

# No CI exists, and none can

**This repository has no git remote and no CI configuration.** Every check above runs on the
owner's machine, fired by an agent or typed by him. That is stated rather than left to be
discovered, because "why is this not just in CI" is the first question a reader has, and the answer
is not *we did not get to it*.

# Rejected

**Rejected: a shell script as the entry point**, and **rejected: a skill.** `make` was chosen
against both on 2026-08-26.

**Rejected: generating `help` from the target list.** Carried instead.

**Rejected: a bypass on the `/handoff` block.** The moment a bypass is wanted is the moment the
block is doing its job.

**Rejected: putting `test` inside `smoke`.** It would make the cheapest check in the session cost
the product suite, and the hole it leaves is named above instead.

# The build landed while this page was being written — 2026-08-26

**"Nothing here is built" above went false within the hour, and it is marked here rather than
edited** ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]). The session that
ordered this page was implementing the arrangement in parallel with the librarian writing it, so
**the tree is the authority on what exists and this list is a reading taken at one moment**, not a
register.

**What was on disk when this note was written**: `Makefile` with all six targets;
`.claude/hooks/remind-the-smoke.ps1`; `.claude/hooks/record-the-smoke.ps1`, whose ledger row is
`smoke:<exit code>` as designed; and the `smoke:` branch in `.claude/hooks/pre-task-state.ps1`.
**Not on disk**: `.claude/hooks/gate-the-handoff.ps1`. **Not in `.claude/settings.json`**: any
registration whose matcher is `Skill` — the string does not occur in that file.

**Two things the built `Makefile` settles that this page left open, and both are its own reasoning
rather than a change of decision:**

- **`smoke` does not use `make` prerequisites.** `smoke: gate style` aborts the target on the first
  failure, which would hide whether the selftests passed. Each step is invoked separately, its
  failure caught, and the accumulated code is what the target exits with — a run taken before
  handing work over reports every verdict it has.
- **`ONLY=` is optional and its absence is a legal run**, not a degraded one. With no pattern the
  floor still runs, which is the floor clause of
  [[the-smoke-runner-is-built-first-thing-next-session]] holding.

**And one place where what landed does not match the clause above, flagged rather than resolved:
`help` is generated.** This page records the owner's ruling that it is typed and that generation is
carried; the `Makefile` sweeps `$(MAKEFILE_LIST)` with `awk` for `## ` comments, so the target list
is derived while each description is typed beside its target. Whether that is the generation he
ruled out, or the typing he asked for with the list swept, is a judgement about the project and not
about the store — it is his.

# A backgrounded `make smoke` is recorded by nothing, and the recorder now says so — measured 2026-08-26

**The row is written from the `SMOKE-EXIT:` line the run prints at its end, and a backgrounded call
does not print it.** `PostToolUse` is documented to fire for background tasks; **what the
documentation does not say is WHEN**, and the observed payload settles the question in one direction:
it carries `run_in_background`, a task id and an output path, **and no verdict** — which is
consistent with firing at launch and inconsistent with firing at completion.

**So the recorder failed safe: no verdict visible, no row.** That is the correct behaviour and it was
the dangerous one, because the session then meets the consequence at `/handoff`, which refuses with
no green row and no clue why.

**What changed is that it says so out loud.** `.claude/hooks/record-the-smoke.ps1` carries a branch
that fires on `run_in_background` with a `make smoke` or `make suite` command and returns a note
naming the cause and the fix — *run it again in the foreground* — and the reminder hook's text now
demands the foreground as well. **Three selftest cases hold it**: that no row is written, that the
note names both `BACKGROUND` and `foreground`, and that the hook still exits 0, because `PostToolUse`
cannot refuse.

**The general shape is one this store already has a page for**: an instrument whose failure looks
like nothing to do ([[an-instrument-that-fails-towards-nothing-to-do]]). **The repair was not to make
the instrument cleverer but to make its silence audible**, which is the cheap half and is the half
that was missing.

**What is not established**: whether `PostToolUse` fires a **second** time when a background task
completes. Nobody has looked, and if it does, a recorder reading the output file would be a real
option rather than a guess.

# The readings taken against this arrangement — 2026-08-26

| what | reading |
|---|---|
| `make smoke`, no `ONLY=` | exit 0 in **66–69 s** |
| `powershell -NoProfile -File scripts/hook-selftest.ps1` | **caught 180, missed 0** |
| `bash scripts/vault-check.sh` | exit 0, region coverage **8 of 15** |

**What they do not mean.** `make smoke` is not the suite — `scripts/vault-check-selftest.sh` runs in
it only under `ONLY=` and ran under none of these readings. The hook selftest's 180 is a case count
and not a coverage figure; it rose from 175 the same day because cases were added, not because
anything was measured better. And `8 of 15` is the advisory's own count of harness files carrying a
region, which is a state of the tree and never a reading of criterion 4
([[a-sprint-closes-on-its-goal]]).

**Conditions:** one reading each, on an otherwise idle machine, against a tree that moved between
them ([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

# The arrangement is built end to end, and where each half now lives — 2026-08-26

**Everything on this page above the obligations table exists on disk and ran live**, by the close of
the session that ordered the page. The tree is the authority; this section says where the live record
of it is, because a proposal is not a record of something that exists.

| what exists | the page that records it |
|---|---|
| the `Makefile`, its targets and its four load-bearing properties | [[the-makefile]] |
| the three hooks, their narrowing and what each cannot do | [[the-smoke-gate-hooks]] |
| the observation-and-inference split behind the staleness rule | [[the-smoke-gate-records-observations-and-the-reader-derives-the-refusal]] |
| why the recorder reads a printed marker | [[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]] |
| the rows the ledger gained | [[the-pre-task-ledger]], [[the-pre-task-state-library]] |

**The chain ran live and `/handoff` PASSED the gate** on a green row newer than the last write. **A
refusal has still never been observed on a real `/handoff`** — every red state is held by selftest
cases alone.

**Two clauses of this page are deliberately not built and are carried:** what enforces a red `suite`
at a sprint's close, which is S3's item 29 and belongs to the conversation about closing a sprint; and
`help` as a generated list, which the owner ruled acceptable in its swept form in the meantime.

**`test` was never run.** Docker was not answering, so the fixture could not build the test database
and every test errored at setup — the cause is inferred from the missing service and not read
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]). It is S3's item 30.

**This page is left `status: current` rather than marked `implemented`, and that is a state report
rather than a judgement.** Two of its clauses are unbuilt by design and one of its checks has never
run; whether that is an implemented arrangement with carried work or an arrangement still landing is
the owner's reading, not the librarian's
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

## The final readings of the day, which supersede the table above as the latest

| what | reading |
|---|---|
| `make smoke`, no `ONLY=`, after the retro's edits | `SMOKE-EXIT: 0` in **70 s** |
| `bash scripts/vault-check.sh` inside it | exit 0, region coverage **9 of 15** |
| the three cheap selftests inside it | **180**, **52** and **59** cases, all `missed 0` |

**This is the run that stands behind that session's `/handoff`.** It includes no suite slice. The
`8 of 15` in the table above was true earlier the same day and moved when a rule page rendered into
`.claude/skills/retro/SKILL.md`; the denominator did not grow
([[every-turn-of-a-retro-files-a-feedback-block]]).
