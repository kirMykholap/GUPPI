---
title: "The dispatch-record hook, and the ledger row a returned dispatch writes"
type: entity
status: current
authority: dispatch-record-hook
basis: code
sprint: S2
created: 2026-08-22
sources: [".claude/hooks/record-the-dispatch.ps1", ".claude/settings.json", ".claude/hooks/pre-task-state.ps1", "scripts/hook-selftest.ps1"]
tags: [agents, harness, process]
---

# What it is

**`.claude/hooks/record-the-dispatch.ps1`, registered on `PostToolUse` with the matcher `Agent|Task`.**
It writes one ledger row per **returned** dispatch, with `dispatch:<subagent_type>` in the event
column, and says nothing to anybody. It exits 0 on every path, including every failure of its own —
a recorder that broke a dispatch would cost more than the record is worth.

It is step 3 of the pre-task chain, built on 2026-08-22
([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

# What it repairs, and the hole was in the rule's own moment

**`/pre-task` records itself by a script the *session* runs** — `scripts/record-pre-task.ps1`
([[the-pre-task-ledger]]). **That is a write, plan mode forbids the session to write, and the rule
places the ritual inside plan mode**, between the plan and its approval
([[a-pre-task-runs-between-the-plan-and-its-approval]]).

**So the ritual performed exactly right left no row, and the guard beside it then asked for it
again.** It happened four times in one session on 2026-08-21 and once more on 2026-08-22, in the
session that built this file
([[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).

**A hook can write during planning, and the proof was already in the ledger**: rows carrying `plan`
in their permission-mode column ([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
[[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]). That measurement is what
dissolved the design deadlock rather than answering it
([[a-blocker-can-be-dissolved-instead-of-answered]]).

# `PostToolUse` rather than `PreToolUse`, and the column is the reason

**A returned result is evidence of work; a requested dispatch is evidence only of intent.** A
dispatch that failed or was cancelled would still leave a `PreToolUse` row saying the ritual ran, and
a column a human reads at a retro must mean what it says
([[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

**The precedent is in the tree**: `check-the-plan.ps1` is registered on both events for the same
distinction ([[the-plan-check-hook]]).

# The event column stays an observation and the conclusion lives elsewhere

**The hook writes `dispatch:<type>` — what happened.** `Read-LedgerState` in
`.claude/hooks/pre-task-state.ps1` is what decides that a returned `dispatch:pre-task` discharges the
ritual. **A hook that wrote `pre-task` directly would be asserting a conclusion in a column**, and a
later reader could not tell an inference from an observation
([[a-column-a-human-reads-is-not-the-column-a-branch-reads]], [[the-pre-task-ledger]]).

**Any other agent type is a dispatch and not the ritual**, and a selftest case asserts exactly that.

# What its details are, and each of them was already paid for once

- **The matcher names both `Agent` and `Task`.** The dispatch tool was renamed in 2.1.63 and the old
  name still resolves as an alias, so a matcher naming one of them is a recorder that silently does
  not exist on some version ([[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]]).
- **Both spellings of the type are read** — `subagent_type` on the tool's input and `agent_type` on
  the subagent lifecycle events — for the reason the lock beside it accepts both
  ([[the-librarian-lock-hook]]).
- **A dispatch with no type is still recorded**, as `dispatch:default`. Dropping those rows would
  make the ledger say that a session which dispatched ten agents dispatched none, which is an
  instrument failing towards *nothing happened here*
  ([[an-instrument-that-fails-towards-nothing-to-do]]).
- **The row carries `-` in the pre-task column rather than `no`.** `no` is a claim about the world;
  a dispatch row asserts nothing either way about the ritual
  ([[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).
- **The payload is parsed as JSON and never matched with a regular expression**, and the file is pure
  ASCII because Windows PowerShell reads a `.ps1` in the system codepage without a BOM
  ([[a-hook-is-measured-from-powershell-or-not-at-all]]).

# It cannot refuse, and it is not a candidate for the refusal test

**`PostToolUse` fires after the act**, so an exit code from it changes nothing that has not already
happened. This file could not block if it wanted to, and the three-condition test does not range over
it ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]],
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

**Exactly one hook here still refuses, and it is not this one.**

# What it makes legal, and what is still owed

**The blocking write gate stays gated.** Under the ratified refusal test a blocking gate failed the
second condition — the measurement was unreliable where the hook stood, because the row could not be
written at the moment the rule names. This hook makes that measurement reliable, **and the gate
becomes legal only once this hook has run for real**, not once it exists
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**Owed against a session restart: that it fires in a live session.** Hooks are loaded when a session
starts ([[claude-code-config-loading]]), and it did not fire on the librarian dispatches of
2026-08-22 because it was registered after they had begun. **Until that is observed, everything above
is read off the script and the selftest and not off a live run.**

# The owed observation is taken: it fires in a live session, and it writes during planning — 2026-08-22

**The section above says *"owed against a session restart: that it fires in a live session"*. It is
discharged.** In the session that began at 16:40:11 on this date — the first to start with this hook
already registered — it wrote a row for every dispatch, unprompted. **The ledger carries five of
them for this session; these are the two that carry the argument:**

```
17:10:18  dispatch:vault-librarian  plan  -
18:35:23  dispatch:pre-task         auto  -
```

**The `plan` in the first row's mode column is the load-bearing half.** It is this hook's own row,
written while the session was in plan mode, so *a hook can write during planning* is no longer
inferred from rows other hooks wrote — it is a property of **this** recorder, observed at the exact
moment the rule places the ritual ([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
[[a-pre-task-runs-between-the-plan-and-its-approval]],
[[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).

**That is the refusal test's middle condition, met on the tree rather than on paper.** *The
measurement is reliable where the gate stands* was the condition a blocking write gate failed, and
the reason it failed was that the row could not be written at the moment the rule names. It can
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[a-refusal-is-conditional-or-absolute-and-nothing-else]]).

**And the row that discharges the ritual exists.** `dispatch:pre-task` is on the record, written by
this hook from a real dispatch, so `Read-LedgerState` discharges the ritual by exactly the path the
design named rather than by a case nobody had run
([[the-pre-task-ledger]], [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**The event column behaved as designed on both rows.** The hook wrote `dispatch:<type>` — an
observation — and the conclusion that one of those types is the ritual was drawn by
`Read-LedgerState` and not by this file ([[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

**So *"everything above is read off the script and the selftest and not off a live run"* is dated
here rather than rewritten** ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**What this does not clear.** The blocking write gate has a second gate that nothing here touches:
the deadlock risk of removing the `Advised` and `ScopeAt` short-circuits while the librarian writes
about fifty pages per ingest, verifiable only by a real ingest
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
[[the-vault-is-excluded-from-the-pre-task-net]]).

## Both rows are real and neither is the row the write gate needs — 2026-08-22, at the ingest

**Everything in the section above is true row by row, and the conclusion drawn from the pair is
not.** The two rows are `dispatch:vault-librarian` at `plan` and `dispatch:pre-task` at `auto`. **A
blocking write gate needs `dispatch:pre-task` written in plan mode, and no such row exists**
([[a-chain-proved-in-halves-is-not-proved]]).

**What this hook has proved of itself stands unchanged**: it fires in a live session, it writes one
row per returned dispatch, and it can write during planning. **What is not proved is a property of
the ritual's own path**, and this file's selftest already asserts the thing that forbids substituting
one row for the other — *any other agent type is a dispatch and not the ritual*.

**The owner read sprint item 14 as NOT MET on that ground and put its closure on his confirmation**
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).
