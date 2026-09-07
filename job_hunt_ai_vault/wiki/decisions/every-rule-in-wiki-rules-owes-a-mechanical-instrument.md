---
title: "Every rule in `wiki/rules/` owes a mechanical instrument, and the ones that have none are named"
type: decision
status: current
authority: rule-instrument-obligation
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "job_hunt_ai_vault/sprint.md", ".claude/hooks/record-the-dispatch.ps1", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [vault, harness, testing]
---

# The ruling, 2026-08-23

> **owner: Значит все эти 5 правил должны получить свой дом. Механический, так как это правила и
> они должны исполнятся.**

**A rule that nothing can observe is an exhortation**, and this store has already priced that:
knowing a rule has never once been what made it hold here
([[knowing-a-rule-is-not-a-mechanism]]). His sentence gives the ground rather than the mechanism —
*they are rules and they must be executed* — so what shape each instrument takes is open and
**that each one gets one is not.**

**It is acceptance criterion 1 of S3**, and the criterion admits a second way of satisfying it: a
rule gets an instrument **or a page saying why it cannot have one**. The criterion is decided by
`bash scripts/vault-check-selftest.sh` and `pwsh scripts/hook-selftest.ps1` each carrying a case
per new instrument and reporting `missed 0`.

# The five, and what stands in the way of each

| the rule | what observes it today | the obstacle |
|---|---|---|
| [[a-session-ends-with-retro-then-handoff-then-ingest]] | nothing | **no `Stop`, `SessionEnd` or `SubagentStop` hook is registered**, so no event exists at which a session's end can be noticed at all |
| [[ask-before-weakening-or-working-around-a-rule]] | nothing | the condition is an intention — weakening a rule and repairing one look identical in a diff |
| [[write-the-miss-into-vault-feedback-before-the-turn-ends]] | nothing | the party the rule binds is disarmed by plan mode, which is the recorded cause of every breach so far ([[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]) |
| [[dispatch-librarians-in-parallel-only-for-reading]] | nothing | see below — counting dispatches cannot express the rule |
| [[english-in-the-repository-russian-with-the-owner]] | nothing | see below — a red gate would lock out the librarian |

# The parallel-librarian rule cannot be enforced by counting dispatches

**`.claude/hooks/record-the-dispatch.ps1` runs on `PostToolUse` and writes a row per *returned*
dispatch.** There is no in-flight row, so at the moment two librarians are running, the ledger
holds nothing about either of them ([[the-dispatch-record-hook]],
[[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).

**And a counter would enforce the wrong rule even with in-flight rows.** The rule permits a
read fan-out and forbids a write fan-out; a hook cannot tell them apart, because the difference is
in what the agent is asked to do. **A counter would forbid the thing the rule allows**, which is a
worse instrument than none.

# An English-in-the-repository gate is refused, and the refusal is an owner ruling

**Owner, 2026-08-20: the language rule is forward-only and the unit is the file**
([[english-is-the-rule-and-the-russian-past-is-deferred]]). **10,947 Cyrillic lines across 107
files** would turn a corpus-wide gate red on the day it landed, and a red gate locks out the
librarian, which is this project's worst failure mode rather than a nuisance
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**The shape the corpus supports is a `--lint` advisory over new or touched files** — which is the
forward-only rule expressed as an instrument rather than contradicted by one
([[the-tag-density-advisories-move-behind-lint]]).

# What this obliges, and what it does not

- **Each of the five gets an instrument or a page saying why it cannot.** The page is a legal
  answer and is not a defeat: two of the five above already have most of that page written into
  this one.
- **A new instrument gets a selftest case in the same change.** Otherwise the criterion cannot be
  read, and a refusal with no case is removed silently by the next refactor
  ([[a-case-that-passes-before-the-change-tests-nothing]]).
- **Nothing here says the rules are weakened while they wait.** They bind whether or not anything
  watches; what is missing is the watching.

# A sixth rule joins the list, and it closes a way the criterion's decider cannot count — 2026-08-23

**The style rule has no instrument and is not getting one.** Prose style is a judgement no linter
here reads, and the owner made himself its watcher — «сторож - я»
([[write-plainly-name-the-source-and-say-what-is-not-done]],
[[the-style-rules-watcher-is-the-owner-and-it-governs-chat-alone]]).

**So the list this page keeps is six rather than five**, and the sixth member closes in a way the
other five have no precedent for.

## A rule now closes three ways and the decider counts one

| closure | counted by criterion 1's decider |
|---|---|
| an instrument exists, with a selftest case | yes |
| a page says why no instrument is possible | no |
| the owner watches it himself | no |

**The owner ruled that the command is what changes**, not the criterion
([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]). **So this page owes a
record of which closure each of the six took**, or the new command has nothing to read — and that
record is not written here yet.

# One of the six has an instrument, 2026-08-24, and the row that named its obstacle is discharged

**The feedback rule's obstacle was *the party the rule binds is disarmed by plan mode*.** That was
not an obstacle to instrumenting the rule — it was a defect in the rule's mechanism, and the
mechanism changed: a session speaks the line, a hook files it
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]],
[[speak-the-feedback-in-the-turn-and-the-hook-files-it]]).

**`scripts/hook-selftest.ps1` gained fifteen cases for `.claude/hooks/catch-the-feedback.ps1`** —
the fence reader in both directions, accumulation until `final`, deduplication by `message_id`, the
`/handoff` drain skip and the resumption after it, an undeclared kind kept with a note, and exit 0
on a malformed payload. The suite reads **caught 138, missed 0**, against 123
([[the-feedback-catcher-hook]]).

**The row in the table above is left as written.** It records the obstacle as it stood on
2026-08-23, and the retired rule it names is in `archive/`; the successor is a different page with a
different claim ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

## What this does and does not do to criterion 1

**It moves the criterion by one member of six and closes nothing.** The other five stand: two of
them have most of their *why not* written into this page, one is watched by the owner himself, and
none has a case in either suite.

**The record this page owes is still not written** — which closure each of the six took — and the
decider still counts only the first of three ways
([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]).

# Two closures were decided on 2026-08-25, and one obstacle in the table was read wrongly

**`ask-before-weakening-or-working-around-a-rule` closes by a mechanism rather than by a page saying
none is possible.** The owner ruled that the rule guarding every other rule cannot be closed that way,
and named the delivery himself: a `.claude/rules/` file scoped to the rule pages, with his own watch as
the observing half ([[the-ask-before-weakening-rule-gets-a-claude-rules-file-and-the-owner-as-its-watcher]]).

**`dispatch-librarians-in-parallel-only-for-reading` closes by a page**, on his ruling, and the page
carries the argument that a dispatch counter cannot express the rule
([[the-parallel-dispatch-rule-closes-by-a-page]], [[a-dispatch-counter-cannot-express-the-parallel-rule]]).

**And the obstacle recorded here for the session-end rule was inherited without being tested.** It
reads that no event exists at which a session's end can be noticed, and a session proposed registering
a hook for that event. **A hook can do nothing there** — by the time it fires the ritual is missed and
there is nobody to ask — **and the ritual leaves artefacts in the tree, so the question needs no event
at all** ([[the-session-end-rule-is-instrumented-by-asking-the-tree]]).

**None of this is built**, and no register records which rule closed how
([[the-rule-closure-register-is-deferred-and-its-design-is-complete]]).

# The seventeenth rule, 2026-08-30, and it names its instrument before it is built

**[[the-reply-is-a-report-answers-and-one-case]]** landed with an instrument named:
a `MessageDisplay` hook checking that the reply **opens with the frontier line**
([[the-reply-format-rule-gets-a-hook-that-checks-the-form-and-not-the-fact]]). **Not built**, and named
rather than left implicit, which is what this rule asks for.

**It is instrumentable where the rule it supersedes was not, and the difference is worth stating.**
`every-question-to-the-owner-carries-its-context` had **no** instrument and could have none: whether a
question carries its four parts is a judgement about prose. The successor obliges a **visible
artefact** — a numbered list at the top of every message — and an artefact is checkable.

**The general form this instance suggests**: a rule that obliges an artefact can be instrumented; a
rule that obliges a quality cannot. Rewriting the second kind as the first is not always possible, and
where it is, it is worth doing for exactly this reason.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*

# This page is suspended for the cleanup — 2026-08-30, and it is not deprecated

**[[the-cleanup-suspends-the-rules-that-would-refuse-it]] lifts this page for the cleanup**, with
three others, on one ratification.

**What is lifted is one instrument per rule.** The 53 family rules are instrumented by **one hook**
between them — the same hook serves every one of them, so a selftest case per rule would be
fifty-three cases exercising one mechanism ([[the-rule-server-hook]]).

**The instrument is unfinished, and that is the honest reading of the trade.** The hook has no
`authority:` matching branch and exits silently for every path under `wiki/`, so a rule delivered by
lookup reaches nobody as it stands
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]). **A lift taken
against an instrument that does not deliver is a lift against nothing yet.**

**It is acceptance criterion 1 of S3 and neither the repeal nor `sprint.md` says so.** The criterion
reads *"the five rules that no instrument checks have one — or a page saying why they cannot"*, and
suspending this page changes what the criterion is decided by while S3 is open. **Whether the
criterion is affected is the owner's reading and nothing here does it**
([[a-sprint-closes-on-its-goal]]).

**This page stays `current`, is not `deprecated` and carries no `superseded_by:`.** A repeal is not a
supersession, ruled 2026-08-30. **The suspension has no stated end.**

# The suspension now has an end, and the instrument it was waiting for delivers — 2026-08-31

**Lifted until S3 closes, and no further.** The owner ruled on each of the four lifted rules separately
and this one alone got a term rather than a narrowing
([[the-cleanup-suspends-the-rules-that-would-refuse-it]]). **owner selected, 2026-08-31: «окей,
согласен».** The sentence above — *"the suspension has no stated end"* — is what that answers, and it
stands as written because it was true for a day.

**Reading acceptance criterion 1 of S3 is his.** This page is that criterion, and nothing here, in
`sprint.md` or in the brief decides whether it is met. That was already this page's position and the
term does not change it.

**The paragraph above saying the instrument is unfinished has gone false.**
`.claude/hooks/serve-the-rule.ps1` gained its `authority:` matching branch on 2026-08-31, was
registered on `Read`, and its silence is now scoped by mode so the half serving vault pages has an
occasion to fire. **A lift taken against an instrument that does not deliver is no longer what this is**
([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]],
[[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).

**What the instrument covers and what it does not.** Nineteen rule pages are instrumented by that one
hook rather than by a selftest case each, which is the trade this suspension bought. **Five of the
nineteen are served to nobody** — no live page of their family carries their slug — so the instrument
exists and its coverage does not, and that gap closes by the convergence pass rather than by another
hook ([[the-convergence-pass-over-the-live-non-decision-pages]]).

*(Added at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
