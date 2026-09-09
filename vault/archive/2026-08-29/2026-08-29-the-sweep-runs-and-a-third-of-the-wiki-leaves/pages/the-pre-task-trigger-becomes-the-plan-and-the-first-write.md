---
title: "The `/pre-task` trigger becomes the plan and the first write, and `non-trivial` is gone"
type: decision
status: archived
authority: pre-task-trigger
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/check-the-plan.ps1", "CLAUDE.md"]
tags: [harness, agents, process]
---

# The ruling, 2026-08-20

> **owner:** «убираем, окей.»

**Chosen:** `/pre-task` runs between a plan and its approval, and before the first write of a
session if no plan was presented. The rule's text is
[[a-pre-task-runs-between-the-plan-and-its-approval]].

**Rejected:** keeping a judgement about the work, made by the party that wants to start it.

**What decided it was the record, not an argument.** Three skips, three causes, and **in none of
them did the session believe it was starting implementation**
([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]]). A trigger
that asks *is this non-trivial* is answered by the party least able to answer it, and the answer is
invisible afterwards. Presenting a plan is a fact about the session; so is writing a file.

# What it obliges

**A plan presented without a pre-task is now a fact a hook can see.** `ExitPlanMode` is the one
event in this harness where a finished plan exists and no source has been touched
([[the-plan-check-hook]]), and the write path is a net for sessions that never present a plan at all.

**The ritual has to record itself**, because a `/pre-task` and a `/vault-ask` are the same dispatch
and differ only in wording ([[the-ritual-records-itself-rather-than-being-detected]],
[[the-pre-task-ledger]]).

# The half that was deliberately not carried over

> **owner:** «я предлагаю не возращать половину триггера про нетронутую область. Проверим как это
> работает.»

**That is a narrowing of a written rule, taken knowingly and on the record.** *An area you have not
touched this session* was the half of the old trigger that was **not** a judgement — a fact about
the session, firing precisely where *non-trivial* would have said no — and the measured lesson
recommends it in its own words
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

**What is no longer covered by anything:** work entering an untouched area **inside an
already-approved scope**. The plan path fires once per approved scope
([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]) and the write net fires
only where no gate was passed at all, so a session that plans once and then wanders into an
untouched area is asked nothing.

**It is a trial, in the owner's words** — *«проверим как это работает»* — so the question of whether
the narrowing costs anything is open and is answered by the next skip that this trigger would not
have caught.
