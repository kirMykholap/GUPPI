---
title: "The plan-check hook"
type: entity
status: current
authority: plan-check-hook
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/check-the-plan.ps1", ".claude/settings.json"]
tags: [harness, agents, process]
---

# What it is

`.claude/hooks/check-the-plan.ps1`, registered on **`ExitPlanMode`, on either hook event**
([[exit-plan-mode-is-an-ordinary-tool-and-the-owner-performs-the-transition]]).

| event | what it does |
|---|---|
| `PreToolUse` | if a pre-task is owed for this plan, records an `advised-plan` row and returns an advisory note carrying the rule's text |
| `PostToolUse` | records `scope-approved` — the machine-observable form of the owner approving a plan |

**Advisory, never a deny.** Exiting plan mode is reversible, so the first half of the owner's test
fails and the other half does not rescue it ([[advisory-is-the-default-for-a-hook]]).

**It reads the rule's text from the file the injector generates** and holds **no fallback copy of
the words**: a copy is how a rule starts disagreeing with itself
([[a-pre-task-runs-between-the-plan-and-its-approval]],
[[a-generated-rule-file-with-no-paths-carries-no-frontmatter]]). When that file is missing it says
so loudly instead of going quiet.

# Why it is a file of its own

**Measured: a bare PowerShell spawn on this machine is 133 ms**, and the write path fires 71 to 108
times in a working session — a further process there would cost 9 to 14 seconds per session to guard
an event that fires once or twice. This event is rare, so a file of its own is free. It is the same
reasoning the owner used when he rejected matching everything and filtering inside the script
([[session-hooks]]).

**`scripts/record-pre-task.ps1` is deliberately not under `.claude/hooks/`.** It is a command the
session runs, not a hook, and the registration check would find it owing neither a `settings.json`
entry nor a dot-source ([[the-ritual-records-itself-rather-than-being-detected]]).

# What it inherits from every hook here

**Pure ASCII, and message text in single quotes.** A `.ps1` without a BOM is read in the system ANSI
codepage, and in a double-quoted PowerShell string a backtick is an escape — four shipped instances
of that in consecutive sessions ([[windows-console-encoding]],
[[a-backtick-in-a-double-quoted-powershell-string-is-an-escape]]).

**It parses the payload with `ConvertFrom-Json` rather than a regex**, because the payload carries
arbitrary caller text and a greedy pattern over it can be steered by that text ([[session-hooks]]).

**It re-checks the tool name the matcher already narrows to.** A matcher naming the wrong string
produces a hook that never fires, which looks identical to a hook with nothing to say; the selftest
pins the registration and this line keeps the script honest under a wider matcher.

# It has been observed firing

**On a live edit inside the session that built it**, on the net branch and on the loud failure when
the rule text cannot be delivered, with no offender planted
([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).

# Why it speaks was re-argued when the rule behind it was struck — 2026-08-22

**The paragraph above grounds *Advisory, never a deny* in reversibility**, which was the leading
half of the struck test. The owner disowned that rule on 2026-08-21 and the page is now retired
([[advisory-is-the-default-for-a-hook]],
[[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]). **It is kept as
written**, because it records the ground this hook was actually built on.

**Re-argued against the test that replaces it, this hook still speaks — and it fails on the middle
condition rather than the leading one**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]):

| the condition | this hook |
|---|---|
| the condition is measured rather than judged | **satisfied.** *Is a pre-task owed for this plan* is a ledger read, not an opinion ([[the-pre-task-ledger]]) |
| the measurement is reliable where the hook stands | **not satisfied.** A ledger row cannot be written in plan mode, and `ExitPlanMode` fires at exactly that moment, so a ritual that did happen can leave the ledger silent |
| the refusal says how to clear it | it could — the advisory it already returns carries the rule's own text |

**Where it cannot measure, it allows and says so aloud**, which is exactly the advisory note this
hook returns. **The disposition is the new rule's own consequence, not a default it falls back to.**

**Same answer, different ground, and the ground is checkable.** *Exiting plan mode is reversible*
was a judgement about the act; *the ledger cannot be read at this moment* is a property of where the
hook stands, and anyone can check it ([[the-pre-task-ledger]]).

# It advised a session that had performed the ritual, and the advisory disposition is what made that cheap — 2026-08-22

**Observed on this session's `ExitPlanMode`: the hook asked for a `/pre-task` that had already been
run in full, both phases.** Two `advised-plan` rows, 17:15:47 and 17:42:56, both in plan mode.

**Why, exactly, and it is not a defect in this file.** `Read-LedgerState` discharges the ritual on a
`dispatch:pre-task` row and on nothing else — *any other agent type is a dispatch and not the
ritual*, which is a stated property with a selftest case behind it
([[the-dispatch-record-hook]], [[the-pre-task-ledger]]). The ritual of this session was performed by
a `vault-librarian` dispatch at 17:10:18, because **the `pre-task` agent did not exist when the plan
was checked**; it was written later in the same session
([[claude-code-config-loading]], [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**It was predicted before it was observed**, which is what makes it evidence rather than an
anecdote: the recorder's own page says the type is read literally, and the consequence for a ritual
performed under another type follows from that in one step
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**What it costs at this disposition is one advisory line, and that is the whole point.** Under a
blocking gate the same reading would have refused a session that obeyed the rule exactly — the
condition being measured is *is a `dispatch:pre-task` row present*, and it was measurable and
answered **no** about a session that had done the work. **A reliable measurement of the wrong
question is not the middle condition satisfied**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[a-refusal-is-conditional-or-absolute-and-nothing-else]]).

**It is self-clearing and does not recur.** The condition was that the agent did not exist; it does
now, and a ritual performed by dispatching it writes the row the gate reads. **Nothing is changed in
this file on account of it**, and it is recorded because an alarm that fires when nothing is wrong is
one a reader learns not to read, and the first instance is the one to write down
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).
