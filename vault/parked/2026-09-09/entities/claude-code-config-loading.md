---
title: "What a session start reloads for agents, skills and hooks, and what it does not"
type: entity
status: current
authority: config-reload
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["docs/superpowers/plans/2026-08-13-second-brain.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md"]
tags: [process, agents]
---

> [!NOTE] THE TITLE WAS CORRECTED IN PLACE ON 2026-08-22, AND THIS PAGE IS NOT SUPERSEDED
> **It used to read *"Agents, skills and hooks are loaded when a session starts, so a new one needs
> a restart"*, and it said that from 2026-08-13 until the owner's ruling of 2026-08-22.** Its agent
> half stopped being true on 2026-08-22, when `.claude/agents/pre-task.md` was written mid-session
> and `subagent_type: "pre-task"` was dispatched and ran in that same session - the measurement is
> at the foot of this page. Its skill half had been contradicted by this page's own body since the
> day the title was written: a skill was observed registering without a restart on 2026-08-13, in
> the paragraph directly below.
>
> **The new title names the question and answers none of it**, which is what the owner chose. The
> answer is now known to differ by kind and is measured for only some of the kinds, so a replacement
> blanket claim - *skills and agents load without a restart, hooks do not* - would be a fresh
> assertion resting on a single observation, which is the move the measurement below already warns
> against ([[an-unsourced-number-is-dropped-not-chosen]]).
>
> **Nothing new is claimed about hooks.** They were not measured on 2026-08-22, and what this page
> holds about them is what it held before.
>
> **The address did not move and no page was retired.** The filename is the identity here and is
> what every wikilink resolves to, so a title corrected in place strands nothing and
> `supersedes:`/`superseded_by:` do not apply
> ([[a-title-corrected-in-place-is-not-a-supersession]]). The callout below judges the struck title,
> quoted above, and is left exactly as it was written.

> [!NOTE] THE TITLE IS FALSE IN ITS AGENT HALF, MEASURED 2026-08-22
> **A new agent was created and dispatched in the same session**, so *"a new one needs a restart"*
> does not hold for an agent. The heading below is dated where it stands and the measurement is at
> the foot of this page. **The claim is not reversed for hooks and skills**, which this observation
> says nothing about.

# A new agent needs a fresh session; a new skill does not

**The two do not behave the same way, and the difference was measured rather than assumed.**

Both were written on 2026-08-13, minutes apart, in the same session:

- **`.claude/agents/vault-librarian/AGENT.md` — not registered.** Dispatching
  `subagent_type: "vault-librarian"` failed with *"Agent type not found. Available agents: claude,
  claude-code-guide, Explore, general-purpose, Plan, statusline-setup"*.
- **`.claude/skills/vault-ask/SKILL.md` — registered on its own**, appearing in the available-skills
  list later in the same session without any restart.

So a plan step that says "write the agent, then use it" cannot be satisfied in one session, while
the same step for a skill can. Hooks in `.claude/settings.json` were not tested here; assume they
follow the agent rule until measured.

**Fully measured on 2026-08-14: both hooks have been observed firing**, the `SessionStart` one on
the `clear` matcher, in a session that asked for nothing ([[session-hooks]]). A hook therefore
follows the agent rule — read when a session starts — and the brief arrives without a dispatch.

**Half measured on 2026-08-13.** The `PreToolUse` guard **was observed firing** in the session that
wrote it — on every write into `wiki/` — so a `PreToolUse` hook does not need a restart. The
`SessionStart` hook has never been observed at all, which is consistent with the agent rule and
proves nothing either way, because the session it would serve is by definition a later one. See
[[session-hooks]]; that item answers itself the first time a brief arrives unasked.

## A subagent's `CLAUDE.md` is the one that existed when the *parent* session started

Measured 2026-08-13, twice. The harness injects the repository's `CLAUDE.md` into a subagent as it
stood at the parent session's start, not as it stands on disk — a librarian dispatched after
`d30b317` was still handed the 231-line file while the tree held the shortened one.

**Any test of what an entry point supplies has this confound**, and the acceptance re-run of the
shortened `CLAUDE.md` fell straight into it: the agent had the long version for free and said so
itself. To test whether a document is sufficient, the session asking must have started **after** it
was cut ([[vault-librarian]]).

**The confound was removed once, on 2026-08-14, and the instrument expired with the session.** The
acceptance run was made in a session that had *started* with the shortened file, and four agents
reported the file they were holding independently — two by counting a transcription, two by
matching heading order and sampled phrases — all four finding the 210-line post-`d30b317` version,
which is what the parent session had begun with. **That is the only condition under which such a
run proves what it claims** ([[the-acceptance-questions]]). It cannot be repeated for the same
file: the next session's agents will hold whatever is on disk when it starts.

**The workaround, which is not the same test:** dispatch `general-purpose` and instruct it to read
the definition file and follow it. That exercises the instructions and the corpus. It does **not**
exercise registration, so a plan step that says "run the acceptance questions" cannot be fully
satisfied in the session that wrote the agent.

This is the same shape as [[app-restart-required]] — a change that is on disk and not yet in the
running process — and it has the same remedy: restart before disbelieving the change.

## A definition file can also move mid-session, and the registry re-read it — 2026-08-20

**Both layouts resolve.** The owner moved `.claude/agents/vault-librarian/AGENT.md` back out to
`.claude/agents/vault-librarian.md` in the middle of a session, and **the first dispatch after the
move was accepted and ran** ([[vault-librarian]]). So the registry re-reads rather than caching the
session's opening state, at least for a definition that already existed under another layout.

**That does not weaken the heading above.** A *new* agent still needs a fresh session; what this
measures is a *move* of one already registered, which is a different question and had never been
asked.

**The answer was unavailable while the gate was red**, because the librarian lock denies at
`PreToolUse`, before the agent type is looked up — two denied dispatches proved the hook and said
nothing about the registry ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**The line above naming `.claude/agents/vault-librarian/AGENT.md` as *not registered* is left exactly
as it is.** It is a claim about where the file was at a time, and repointing it would make the
sentence assert the opposite of what it meant while the gate stayed green
([[a-rewriter-must-be-paired-with-a-detector]], [[fidelity-to-a-source-and-fidelity-to-the-tree]]).

## A workspace setting that the VS Code extension does not read — 2026-08-20

**`permissions.defaultMode` in this repository's `.claude/settings.json` does not reach a VS Code
session.** The extension reads its starting permission mode from `claudeCode.initialPermissionMode`
in **user** settings and ignores workspace values entirely
([[the-vs-code-extension-reads-its-starting-mode-from-user-settings]]).

**Both are set here**, and neither covers the other: the repository half governs terminal sessions,
the user half governs the editor.

**It was found by a ledger column rather than by reading the file** — the session reported `auto`
while the settings said otherwise ([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).
That is this page's recurring shape: a configuration file that is correct on disk and inert in the
running session is invisible to every reading of that file.

## A new agent was created and dispatched in the same session, and no restart was involved — 2026-08-22

**The measurement, and it is a single observation reported as one.** In session
`e96de950-62a3-4617-881a-caaaaf0b53a5`, which began at 16:40:11:

- **`.claude/agents/pre-task.md` did not exist when the session started.** It is untracked at
  `c9f4637` and was written mid-session.
- **`subagent_type: "pre-task"` was dispatched and ran**, returning findings. The harness announced
  the new type mid-session rather than refusing it.
- **The ledger carries the row**: `18:35:23 dispatch:pre-task auto -`, in the same session id as the
  `session-start:startup` row above it ([[the-pre-task-ledger]],
  [[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).

**So *"a plan step that says 'write the agent, then use it' cannot be satisfied in one session'"* is
false as a general claim.** It was satisfied in one session on this date.

### What this does NOT measure, and the page is deliberately not blanket-corrected in the other direction

**Skills are untouched.** They were measured registering without a restart on 2026-08-13 and nothing
here changes that.

**Hooks are untouched, and the one observation available is consistent with the old claim.**
`.claude/hooks/record-the-dispatch.ps1` was registered in an earlier session of 2026-08-22 and did
**not** fire on the dispatches already under way in that session; it fires normally in this one,
which started after it was registered ([[the-dispatch-record-hook]]). That is what *loaded when the
session starts* predicts.

**And the 2026-08-13 observation is not withdrawn.** `.claude/agents/vault-librarian/AGENT.md` was
genuinely refused with *"Agent type not found"* that day. **Two readings survive both facts and this
page picks neither**: the harness changed between 2026-08-13 and 2026-08-22, or the two files differ
in layout — a nested `<name>/AGENT.md` against a flat `<name>.md`, which is the same distinction the
2026-08-20 note above is about. **The second is an inference and is marked as one**; it would be
settled by creating a nested agent mid-session and dispatching it, and nobody has
([[a-question-asked-is-not-a-question-answered]]).

**One observation is not a rate and is not converted into one** ([[an-unsourced-number-is-dropped-not-chosen]]).
What it does settle is that the general claim in this page's title cannot be relied on for an agent.

### What the stale claim cost on the day it was found

**This session's plan recorded the new agent's acceptance as *owed against a restart*, on this
page's authority, and deferred it.** The basis was false and the item was already discharged when it
was written down — an entity page consulted correctly, answering with a measurement that had gone
stale, which is the failure mode `basis: measurement` has no defence against
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]],
[[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

**It is the same shape as everything else on this page**, met from the far side: a configuration
fact that is correct on disk, wrong in the running session, and invisible to every reading of the
file — except that here it was the *store* that was stale and the session that was right.

## The hook half is now measured too, and it goes the same way as the agent half — 2026-08-26

**A hook registered mid-session fired in that same session.** `.claude/hooks/remind-the-smoke.ps1`
and its registration — `PostToolUse`, matcher `Skill` — were written during the session of
2026-08-26, and the hook **fired on that session's own `/retro`.** The acceptance that had been
recorded as owed against a restart passed live instead.

**So *"a settings change needs a restart"* does not hold for a hook on this machine, on one
observation.** That is the same status the agent half has carried since 2026-08-22: a single
observation, reported as one, not converted into a rate
([[an-unsourced-number-is-dropped-not-chosen]]).

**And it does not blanket-correct the page in the other direction either.** The 2026-08-22 reading
recorded here — `record-the-dispatch.ps1` registered in an earlier session of that day and **not**
firing on the dispatches already under way — is untouched and is still what *loaded at session start*
predicts. **Two observations of hooks now disagree**, and the difference has not been isolated: a
`PostToolUse` matcher against a `PreToolUse` one, a new matcher string against a new script, and two
different days of the harness are all still confounded ([[a-question-asked-is-not-a-question-answered]]).

**What the sentence cost while it stood.** *"Hooks are read at session start, so registering does not
arm it this session"* was written into two harness files and a commit message, and used as the ground
for deferring an acceptance that could have been taken on the spot
([[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]]). **The files are corrected
and the commit message stands** — a commit message is not editable and a wrong record is evidence
about the process that produced it ([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

**This page's own title is what protects it here**: it names the question and answers none of it. The
title corrected in 2026-08-22 would otherwise have needed a third correction today.

# An agent definition's registration is DELAYED, not deferred to the next session — 2026-08-29

**Measured twice in one session, and the first reading was wrong.** Dispatching `decisions-agent`
immediately after writing `.claude/agents/decisions-agent.md` returned *"Agent type 'decisions-agent'
not found"* with the file present and its `name:` field matching. **The session wrote "agent definitions
are read at session start."**

**That was falsified inside the same session.** Both new agents became dispatchable a few turns later,
**with no restart**. The correct reading is that registration is **delayed**, and *how long* is
unmeasured — nobody has taken the interval, and neither reading generalises to the other events.

**It also contradicted this page**, which has said since 2026-08-22 that a new agent was created and
dispatched within one session. **The first measurement disagreed with a live page nobody consulted, and
then disagreed with itself.**

**It is the opposite of the `PostToolUse` hook registration measured on 2026-08-29**, which took effect
mid-session with no restart at all. **Two events, two behaviours, and neither generalises** — which is
the whole point of this page.

**The cost of the delay was real.** The live proof of the `contradicts` verdict was named in the
approved plan as the check that must happen before an ingest; it was due while the agents were
unavailable and became possible only after the commit, so **both agents shipped unexercised**
([[the-decisions-agent]], [[the-lessons-agent]]).

**And nesting has a documented bound.** A subagent may dispatch its own subagents to a default depth of
**3 levels**, configurable by `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; the tool is named `Agent` in an
agent definition's `tools:` line.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
