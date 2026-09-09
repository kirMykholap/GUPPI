---
title: "A `/pre-task` agent, and a `PostToolUse` hook that writes its ledger row"
type: proposal
status: current
authority: pre-task-agent-design
basis: human
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", ".claude/agents/vault-librarian.md", "scripts/vault-inject.sh"]
decided_by: [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]
tags: [agents, harness, retrieval]
---

# The design, as the owner asked for it and as it was agreed

> **owner: нужно оформить то, что мы обсуждали как полноценный proposal и обязательно обсудить на
> следующей сессии.**

**None of it is built.** It is written down because the largest thing the session of 2026-08-21
produced was this design, and a design that survives only in the chat that produced it is the
failure this folder exists to prevent ([[chat-is-not-a-channel-that-survives-the-session]]).

The four steps, **in this order**:

1. **The shared reading discipline is extracted into a `wiki/rules/` page** and rendered into every
   reading agent rather than copied into each. The mechanism exists and already runs on this exact
   file — `.claude/agents/vault-librarian.md` carries a rendered region
   ([[a-region-is-a-paired-comment-named-for-a-rule]],
   [[what-travels-from-a-rule-page-is-a-marked-slice]]).
2. **`/pre-task` becomes its own agent**, doing the whole ritual and reading pages itself. No nested
   dispatch is needed, which was the objection that killed the earlier shape. It reports what
   contradicts the plan, what is already built and must not be repeated, and what to take into
   account ([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]).
3. **A `PostToolUse` hook on `Agent` writes the ledger row from `subagent_type`**
   ([[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]], [[the-pre-task-ledger]]).
4. **Only then does the write gate become blocking**
   ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

# Why `PostToolUse` and not `PreToolUse`

**A `PreToolUse` row records intent rather than work.** A dispatch that failed or was cancelled
would still leave a row saying the ritual ran — and a column a human reads must mean what it says
([[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

**A returned result is evidence of work where a requested dispatch is only evidence of intent**, and
the precedent is in the tree: `check-the-plan.ps1` is registered on both events
([[the-plan-check-hook]]).

# What it needs no exemption for, and what it cannot do

**It needs no plan-mode exemption.** Plan mode blocks edits and not a dispatch, and hooks write the
ledger during planning already — the rows prove it, carrying `plan` in their permission-mode column
([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
[[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]). **That measurement is what
dissolved the design deadlock**: the problem was never that the ledger is unwritable during
planning, only that `scripts/record-pre-task.ps1` is launched by the session rather than by an event
([[a-blocker-can-be-dissolved-instead-of-answered]]).

**A pre-task agent will find misses in plan mode and cannot record them there**, because recording
is a write. The store already says this about the librarian answering during planning, so it is
known before it is built rather than after
([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
[[write-the-miss-into-vault-feedback-before-the-turn-ends]]).

**A new agent needs a session restart**, so it cannot be tested in the session that writes it. Its
acceptance test is owed against a restart ([[claude-code-config-loading]]).

# The measurement that sizes step 1

**Of the librarian's 151 lines of instruction, about 100 are shared by any reader of the vault** —
finding the vault and reading its `CLAUDE.md`, grep-then-links, `tags.md` as the bridge between the
two languages, `index.md` as a map and not a catalogue, narrowing before opening, the folder as the
first narrowing, and the two closing sections of an answer. **Only `## Writing`, about 34 lines, is
the librarian's alone** ([[one-librarian-behind-every-caller]], [[vault-librarian]]).

**So a second reading agent duplicates two thirds of a file before it does anything else**, which is
the arithmetic behind extracting the shared part rather than copying it.

# What is open

**`governs:` takes one address.** It is read with `head -1` in `scripts/vault-inject.sh`, so step 1
cannot render into a second agent until the field takes a list — **conditional on that second agent
existing** and owed no earlier ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**Whether an agent may hold `authority:` at all is not this page's question**, but the rules folder
forbids it beside `governs:` and step 1's page is a rule
([[authority-beside-governs-is-forbidden-on-any-page]]).

**What the blocking gate does to the librarian is unverifiable except by running one**, and that is
step 4's whole risk rather than a detail of it.

Retired with `superseded_by:` the day it is built or refused, after the librarian has checked that
nothing on it lives only here
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# The order was ratified, one step is built, and one of the steps changed its ground — 2026-08-21

**The owner ratified the four steps in the order this page states them.** Nothing was reordered.

**Step 1's blocker is cleared.** `governs:` takes a bare path or an inline list, in the injector, in
the gate and in the rules schema, so a rule page can render the shared reading discipline into more
than one agent. **The section *What is open* above is false in its first clause from that date**
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
[[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]]).

**Phase 1 moves inside the agent, which reverses the owner's own lifting of the main-context
clause.** That clause was lifted for the **skill** shape and does not survive the **agent** shape: if
phase 1 stays outside, the empty case leaves no dispatch, so the hook writes no row and the gate
cannot tell *checked and found nothing* from *did not check* — and the empty case is exactly what a
skipper would claim. **Recorded as a reversal under a new ground rather than as an oversight**
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]],
[[a-rule-applied-in-opposite-directions-on-one-day-is-not-a-reversal]]).

**Step 3 is the condition of step 4's legality, not a convenience before it.** Under the ratified
refusal test a blocking gate fails the second condition today: the ledger row cannot be written in
plan mode, which is the exact moment the rule places the ritual, so the gate would refuse sessions
that performed it. Once a hook writes the row, the measurement becomes reliable where the hook
stands. **This page states the same order for a weaker reason — deadlock risk — which is real and
additional**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).

**Still nothing is built of steps 2, 3 and 4.** Checked at the ingest of 2026-08-22:
`.claude/agents/` holds `vault-librarian.md` alone, and `.claude/settings.json` carries no
`PostToolUse` registration on `Agent` ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**The owner put the quote-is-Cyrillic rule ahead of this chain** for the next session
([[a-quote-is-cyrillic-rule-with-an-advisory-verdict]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# Step 3 is built, and step 4 is still gated — 2026-08-22

**The section above says *"Still nothing is built of steps 2, 3 and 4"*. Step 3 landed on this
date** and the sentence stands as written, dated where it is
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**`.claude/hooks/record-the-dispatch.ps1` is registered on `PostToolUse` for `Agent|Task`** and
writes one row per returned dispatch, `dispatch:<subagent_type>`. **This page's argument for
`PostToolUse` over `PreToolUse` is what was built** — a returned result is evidence of work where a
requested dispatch is evidence only of intent ([[the-dispatch-record-hook]]).

**The conclusion did not travel into the event column.** The row says what happened;
`Read-LedgerState` is what decides that `dispatch:pre-task` discharges the ritual. That split is not
tidiness — a hook writing `pre-task` directly would put an inference in a column a human reads as an
observation ([[a-column-a-human-reads-is-not-the-column-a-branch-reads]]).

**Step 4 stays gated, exactly as this page ordered it.** *Only then does the write gate become
blocking* — and *then* is now read as **once step 3 has run for real**, not once it exists. What made
the blocking gate illegal was the second condition of the refusal test: the ledger row could not be
written in plan mode, which is the moment the rule places the ritual, so the gate would have refused
sessions that performed it. **This hook makes that measurement reliable where the hook stands, and
the observation that it does is still owed**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**Owed against a session restart**: that the new hook fires in a live session. It did not fire on the
librarian dispatches of this date, because it was registered after they had begun
([[claude-code-config-loading]]).

**Steps 2 and 4 are unbuilt and step 1 is unbuilt for this chain.** `.claude/agents/` still holds
`vault-librarian.md` alone. **The `governs:` list did gain its first real customer today**, though on
a different rule: [[a-block-attributed-to-the-owner-is-written-in-his-own-russian]] names two skills,
which is the mechanism step 1 waits on, proved on a page other than step 1's
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

**This proposal is therefore not retirable**: three of its four steps are open
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# Steps 1 and 2 were not owed on 2026-08-22, ratified retrospectively — and step 2's price rose

**The option the owner selected named six items, and neither the shared reading discipline nor the
`/pre-task` agent was among them.** The plan carrying their removal was written before that answer
arrived, so the narrowing was announced and then approved rather than the other way round
([[narrowing-a-scope-notifies-and-widening-it-asks]],
[[a-replacement-and-a-widening-were-ratified-after-the-fact]]).

**Two reasons the order held anyway.** Step 2 cannot be tested in the session that writes it — a new
agent needs a restart ([[claude-code-config-loading]]) — and **step 1 renders into two reading agents
of which the second *is* step 2**, so building it first renders into a file that does not exist.

**And step 2's price rose on the same day it was postponed.** Once `/pre-task` always dispatches its
second phase, the agent stops being a convenience and becomes **how the ritual is performed**
([[the-pre-task-always-dispatches-its-narrow-phase]]). **It goes first next session**, at that higher
price.

**Step 4 is unchanged and still waits on step 3 firing in a live session**, which is owed against a
restart. Consequence, stated: the pre-task ledger's plan-mode hole is repaired in principle and
unproved in fact ([[the-dispatch-record-hook]]).

# Steps 1 and 2 landed on 2026-08-22, and step 1 shipped smaller than this page sized it

**`.claude/agents/pre-task.md` exists** — 115 lines, `name: pre-task`, `tools: Read, Grep, Glob,
Bash`, both phases inside it and no dispatch out of it, which is step 2 as this page designed it.
**`.claude/skills/pre-task/` is deleted.** The ritual is now performed by dispatching
`subagent_type: "pre-task"`, and the rule that states *when* it runs gained a sentence saying *how*
([[a-pre-task-runs-between-the-plan-and-its-approval]],
[[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**Step 1 is a `wiki/rules/` page rendering into both agents**
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]), on the mechanism
this page said it was waiting for and which cleared on 2026-08-21
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

**The owner ruled on the slice's extent, and it is narrower than *The measurement that sizes step 1*
above.** That section counts *the two closing sections of an answer* among the shared hundred lines.
**They are not in the slice.** He selected one rule page carrying the librarian's
`## Start here, every time` and `## How to search` and **not** `## Answering a topic query`.

**The ground is this page's own argument turned against its arithmetic.** The ten-page ceiling and
the stop-and-report discipline are written about *topic* queries, and `/pre-task` asks the opposite
question — a ranked partial answer is the dangerous one when the decision a plan violates may be
twelfth of eight returned ([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]],
[[one-librarian-behind-every-caller]]). Rendering that section into the pre-task agent would deliver
it a discipline it must not follow.

**Also rejected: two rule pages**, the second carrying the topic answer. It would render into exactly
one file, which is a mechanism with no second addressee — and the injector exists because a rule in
two places diverges ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**The consequence the ruling accepts, recorded rather than repaired:** Sources and Not in the vault
are stated twice, in the librarian's words and in the pre-task agent's own. The section above counted
them as shared and they are duplicated instead. **It is a few lines, and it is named on the rule page
so that a later reader does not repair it as an oversight.**

**Step 3 is built and step 4 is still gated**, unchanged by any of this: it waits on the dispatch
hook firing in a live session ([[the-dispatch-record-hook]],
[[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]).

**Owed against a session restart, and it is now two things**: that `pre-task` resolves as a dispatch
target at all, and that the hook writes `dispatch:pre-task` when it returns
([[claude-code-config-loading]]). **Neither can be observed by the session that built them.**

**This proposal is still not retirable**: step 4 is open, and the acceptance runs above are owed
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# Steps 1 and 2 are built, and one of this page's own reasons was measured false — 2026-08-22

**Step 1 is the rule page, step 2 is the agent, and both exist.** The shared reading discipline
renders into two agent definitions from one page, and `.claude/agents/pre-task.md` has run once
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]],
[[the-pre-task-agent]]).

**The sentence above at *"Two reasons the order held anyway"* is false in its first reason and is
left standing.** *A new agent needs a restart* was given as a **live** constraint, and it was
measured false on this date: the agent was created, resolved as a dispatch target and dispatched
inside one session. **The page it cites is corrected; that sentence is not**
([[claude-code-config-loading]], [[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**The second reason held.** Step 1 renders into two reading agents of which the second *is* step 2,
so building it first would have rendered into a file that did not exist — and that is the reason the
order was actually executed on.

**Step 4 is still not built and its second gate is untouched**: that a real ingest does not deadlock
behind a blocking write gate, once the `Advised` and `ScopeAt` short-circuits are removed while the
librarian writes about fifty pages. **It has already deadlocked here once**
([[the-librarian-lock-hook]], [[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**And step 3's chain is not proved.** The ledger holds the right agent at the wrong moment and the
right moment with the wrong agent; sprint item 14 is NOT MET and closes on the owner's confirmation
([[a-chain-proved-in-halves-is-not-proved]],
[[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

## What retiring this page means changed under the ruling of 2026-08-22

**The closing line above cites [[a-built-proposal-retires-once-nothing-on-it-lives-only-there]],
which is `deprecated` in `archive/` from this date.** A built proposal now stays in
`wiki/proposals/` with a `built` mark ([[a-built-proposal-stays-in-proposals-with-a-built-mark]]), so
**the question this page faces when its steps land is no longer *does anything live only here*** —
it is what the mark is, and the mark does not exist yet.

**Nothing about this page's disposition changes today**: it is `current` because it is not built, not
because it is waiting for a move.
