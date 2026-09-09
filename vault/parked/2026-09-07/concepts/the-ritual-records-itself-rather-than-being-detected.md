---
title: "The ritual records itself rather than being detected"
type: concept
status: current
authority: ritual-self-recording
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "scripts/record-pre-task.ps1"]
tags: [harness, agents, process]
---

# Why a hook cannot detect a `/pre-task`

**A `/pre-task` and a `/vault-ask` are the same dispatch to the same agent** and differ only in the
wording of the prompt ([[one-librarian-behind-every-caller]], [[vault-librarian]]). A hook watching
the dispatch tool would therefore have to match on wording — which is **asserting the sentence
rather than the condition**, the failure this repository has already recorded in its own selftest
([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

**So the ritual writes its own row.** `scripts/record-pre-task.ps1` is what `/pre-task` runs to
record itself, and the ledger holds the row ([[the-pre-task-ledger]]).

# The failure direction is the safe one

**A recording that does not happen produces a spurious advisory, never a silent skip.** The session
is asked to run a ritual it has already run; it says so, or runs it again, and the cost is one
message. The opposite arrangement — inferring that the ritual ran — fails by staying quiet in
exactly the case the mechanism exists for.

# What it costs

**The record is only as honest as the party writing it.** Nothing stops a session from recording a
pre-task it did not run, and nothing is meant to: the ledger is a record, not an assertion
([[a-pre-task-runs-between-the-plan-and-its-approval]]), and the enforcement this project uses for
that class is a diff and a log rather than a lock ([[the-librarian-writes-unattended]]).

# What this page is about is the dispatch surface, and there is now a second one — 2026-08-21

**The argument above is true and it ranges over the *dispatch*.** A `/pre-task` and a `/vault-ask`
are the same dispatch to the same agent, so a hook watching the dispatch tool would have to match on
prompt wording. That has not changed.

**It never considered the *skill* surface, because at the time the ritual's observable act was the
dispatch.** Phase 1 of `/pre-task` is now a skill invocation
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]), and a hook **can** see
which skill, by name, in a structured field. Measured with a `Skill|Write` matcher where `Write` is
a control known to fire:

```
tool=Write | event=PreToolUse | skill=       | input_keys=content,file_path
tool=Skill | event=PreToolUse | skill=sprint | input_keys=args,skill
```

**This page is not wrong; it is answering about somewhere else**, and the general form of that is
[[an-argument-can-be-true-of-one-surface-and-silent-about-another]].

**Its second argument survives intact, and it is the one that decided the design.** Inferring that a
ritual ran fails by staying silent in exactly the case the mechanism exists for. **So the design
that was about to be built — a hook on the `Skill` tool — would have bought zero seconds at the cost
of the one property the mechanism exists for**, and it was reversed before a line of it was written
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]],
[[an-instrument-that-fails-towards-nothing-to-do]]).

**Where the recording is going instead**: a `PostToolUse` hook on `Agent`, reading `subagent_type`
— evidence of work rather than of intent
([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*
