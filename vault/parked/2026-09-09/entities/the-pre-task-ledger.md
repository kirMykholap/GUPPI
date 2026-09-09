---
title: "The pre-task ledger and the session stamp"
type: entity
status: current
authority: pre-task-ledger
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1", "scripts/record-pre-task.ps1"]
tags: [harness, agents, process]
---

# What it is

**`.superpowers/sdd/pre-task-ledger.tsv`** — git-ignored, append-only, and the artefact the rule page
used to say did not exist.

| column | what it holds |
|---|---|
| `ts` | the timestamp, fixed-width so lexical order is chronological order |
| `session_id` | the key everything else is asked per session |
| `event` | which gate the row came from |
| `permission_mode` | the mode observed in the payload, which is not always what the settings say |
| `pre_task` | whether a pre-task stood behind this row |
| path | the file the row was occasioned by, where there is one |

**The session stamp is the same path plus `.session`.** It exists because a hook is handed a
`session_id` and **a script the session runs is handed nothing**, so `scripts/record-pre-task.ps1`
would otherwise have no key to write under. Adding it widened an approved scope and is recorded as a
divergence ([[an-approved-scope-was-widened-by-a-step-that-was-forced-rather-than-chosen]]).

# What is read out of it

**A skipped ritual, a heartbeat proving the hooks loaded, and the mode the session started in**
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]) — and the state machine that
asks them is [[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]].

**A column a human reads must mean what it says.** `pre_task` records whether a pre-task stood
behind the row and **not** whether anything was owed; the difference appears on the later writes of
a session that skipped the ritual
([[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

**Rows are appended with `AppendAllText` and a `UTF8Encoding` constructed as false**, because
`Add-Content -Encoding UTF8` writes a BOM in Windows PowerShell 5.1 and it lands in front of the
first field of the first row — which here is the timestamp the plan path compares
([[add-content-utf8-writes-a-bom-in-front-of-the-first-field]]).

# Who drains it, and what is open

**`/handoff` drains it, not `/retro`.** The plan said `/retro`, and
[[the-retro-writes-its-own-transit-file]] rejects exactly that operation for a reason that applies
here unchanged: its rows are raw machine observations with no verdict on them, and the retro's
output holds only resolved lines.

**It grows without bound and is read whole on every `Edit|Write`.** A few lines per session today.
**Nothing prunes it and nobody has decided when it should be pruned** — named here rather than
answered, because inventing a retention rule is a decision about the project
([[a-queue-only-one-party-can-drain-is-unbounded]]).

# It is the only rule-usage counter this project has

**The rows record invocations and skips of one rule**, and the pipe from them — ledger, `/handoff`,
journal, `/ingest`, corpus — is already closed. Whether that generalises into an axis of
`/vault-lint` is raised and deliberately not built ([[a-rule-usage-axis-for-vault-lint]]).

# It changed shape the same day, and two sentences above went false — 2026-08-20

**It holds one session.** At `SessionStart` with `source` = `startup` the whole file is moved into
`.superpowers/sdd/ledger/` and a fresh one opens with a `#`-prefixed pointer row ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]],
[[the-ledger-archive-directory]], [[rotation-is-a-whole-file-move-and-never-a-read-modify-write]]).
**So *"it grows without bound"* above is a reading of the morning of 2026-08-20**, and the retention
question it named as unanswered has been answered — the growth moved rather than ended.

**The `pre_task` column has a third value, `-`**, for a row that asserts nothing about the ritual
([[the-pre-task-column-gains-a-state-for-asserting-nothing]]). The table above lists two.

**A new row type: `session-start:<source>`**, appended by `.claude/hooks/session-brief.ps1`. It is
the instrument for whether a `/clear` keeps the session identifier, the reset that drops what a
session accumulated before a `clear`, and the signal that tells the rotation this is a new session
([[the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal]]).

**Measured when that work began: 7 rows and 404 bytes across two sessions** — three at `mode=auto`
and four at `plan`, `plan`, `unknown` and `acceptEdits`.

# The drain this page asserts does not exist — reported 2026-08-20

**The section above says *"`/handoff` drains it, not `/retro`"*, and that is the ruling rather than
the state of the tree.** Verified by grep in the fourth session of 2026-08-20: neither
`.claude/skills/handoff/SKILL.md`, nor `/retro`, nor `.claude/templates/handoff.md` mentions the
ledger. **The first of this file's three stated jobs is unbuilt**, and
[[the-retro-writes-its-own-transit-file]] asserts the same drain in the same words.

**It matters more after rotation than before.** A session that ends without the closing ritual now
has its rows filed into `.superpowers/sdd/ledger/` by the next `startup`, where a drain would not
look even once it exists. **Not built that night**: it is a change to a closing-ritual skill and was
outside the approved scope. The work item names its file — `.claude/skills/handoff/SKILL.md`.

# Nothing drains it, and that is the ruling — 2026-08-21

**The section *Who drains it, and what is open* above says *"`/handoff` drains it, not `/retro`"*.
There is no drain and there will not be one.** The owner, at the retro of 2026-08-21:
«Слив ledger не строим.» The question had been put to him three times across that session before it
was answered.

**This is a correction and not a retirement, and the distinction is the point.** The reasoning that
assigned the drain to `/handoff` rather than `/retro` is still sound and is left standing above —
raw machine observations do not belong in a document whose contract is a verdict per line
([[the-retro-writes-its-own-transit-file]]). What changed is that there is **no drain to assign**.
The alarm that stood from 2026-08-20 is closed by cancelling the work rather than by doing it, and
the work item that named `.claude/skills/handoff/SKILL.md` is withdrawn.

**The rows are not lost.** Rotation files each session into `.superpowers/sdd/ledger/`, which is read
by a human at a retro and by nothing else, and the owner ruled the same day that the archive is not
pruned ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]],
[[the-ledger-archive-directory]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# A second kind of row rides the columns that exist — 2026-08-21

**`scripts/record-pre-task.ps1` gained `-Kind`, which is `pre-task` or `vault-ask`, and it rides the
`event` column rather than a new one.** The ledger is a fixed six-column TSV and **a seventh column
breaks the split for every reader** — the state library, the plan hook and the write gate all parse
by position ([[the-pre-task-state-library]],
[[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**`-Candidates` and `-Opened` ride the `path` column**, which is free text the hooks never parse.

**A `vault-ask` row matches no case in `Read-LedgerState`'s switch**, so it is visible in the record
and decides nothing, and its `pre_task` column reads `-` rather than `no`
([[the-pre-task-column-gains-a-state-for-asserting-nothing]]). **Verified live**: after writing one,
`PreTaskAt` still pointed at the real pre-task row.

**So `/vault-ask` leaves a trace at last.** It was one of the mechanisms found built and wired to
nothing — dispatching the same agent as every other caller, and recording nothing about it
([[one-librarian-behind-every-caller]], [[an-admission-test-for-mechanisms]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# It recorded a whole design argument without being asked to — 2026-08-21

**Read as the session left it:**

```
23:00:16  session-start:startup  unknown      -
23:52:14  first-write            plan         no
23:52:14  advised-write          plan         no
23:52:29  advised-plan           plan         no
23:57:02  scope-approved         acceptEdits  no
23:58:03  pre-task               unknown      yes
```

**Two advisories fired, both correct by their own data, and both were wrong**: phase 1 had run.
**They could not know, because recording is a write and plan mode forbids writes** — the `pre-task`
row landed six minutes later, once the mode changed.

**An advisory that cannot stop anything, over a measurement that is blind precisely where the rule
places the ritual.** That is the case for putting a `PostToolUse` hook that writes the row ahead of
any blocking gate, and the ledger produced it by itself
([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]],
[[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]],
[[the-pre-task-ran-at-half-strength-and-the-permission-to-dispatch-arrived-after-the-plan-was-approved]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# A third and fourth kind of row ride the same columns — 2026-08-26

**The smoke gate writes into this file rather than into one of its own**, and it added two event
values, both in the column that already carried `dispatch` and `feedback`:

| event | written by | what it observes |
|---|---|---|
| `smoke:<exit code>` | `.claude/hooks/record-the-smoke.ps1` | a `make smoke` or `make suite` that RETURNED, with what it returned |
| `write:<path>` | `.claude/hooks/check-the-journal.ps1` | any file written, before that hook's own narrowing |

**Both are observations and neither is a conclusion.** Whether the path to `/handoff` is open is
derived from the rows by `Get-HandoffRefusal`, not stored in them — the same split this file has run
on since it began ([[the-smoke-gate-records-observations-and-the-reader-derives-the-refusal]],
[[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

**`write:` rides an existing hook on purpose.** A registration of its own on `Write|Edit` would put a
second PowerShell spawn on every write in the repository to serve one event at the end of a session
([[the-plan-check-hook]]).

**The rows are read at `PreToolUse` on `/handoff` and are there by then**, which is the reliability
half of the refusal test: unlike the plan check, plan mode is not in play at `/handoff`, so nothing
prevents the writes that produce the rows
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

# A `served-rule` event and a `ServedRuleFiles` field — 2026-08-30

**`.claude/hooks/serve-the-rule.ps1` appends a `served-rule` row when it hands over a rule**, and
`pre-task-state.ps1` accumulates the paths into a `ServedRuleFiles` field. **It uses the same path
column the `write` row does**, so no column was added for it.

**It is never emptied within a session, and that is the difference from `WritesAfterSmoke`.** A write
goes stale the moment the suite runs again; **nothing makes a served rule stale** — the reader has
been told, and telling him again is noise rather than safety.

**The field is what makes the hook say a thing once per file per session.** Without it the note fires
on every edit of `CLAUDE.md` in a session that edits it eleven times, and a reminder that fires every
time becomes furniture
([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

**The hook scans `wiki/rules/` before it opens the ledger, and that order was measured.** Deriving the
ledger state costs more than reading the head of seventeen files and would be paid on every write,
including the great majority that govern nothing; scanning first means an ungoverned path never
touches the ledger at all. **If the ledger cannot be read the note is said again**, which is the safe
direction: a repeated note costs a paragraph and a silenced one costs the rule. Both choices were
closed by the session and ratified afterwards
([[the-forks-the-session-closed-without-asking-are-ratified]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
