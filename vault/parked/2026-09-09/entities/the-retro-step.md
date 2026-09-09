---
title: "The retro step: its skill, its form, and the transit file it writes"
type: entity
status: current
authority: retro-step
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/skills/retro/SKILL.md", ".claude/templates/retro.md"]
tags: [harness, process]
---

# What exists, as of 2026-08-17

The end of a session runs **retro, then `/handoff`, then `/ingest`**
([[the-end-of-a-session-is-a-retrospective]]). The retro is the new step and it owns three files:

| Part | Path |
|---|---|
| the skill | `.claude/skills/retro/SKILL.md` |
| the form | `.claude/templates/retro.md`, in [[claude-templates-directory]] |
| the transit file | `.superpowers/sdd/retro.md`, git-ignored ([[the-retro-writes-its-own-transit-file]]) |

**It interrogates; `/handoff` routes** — [[retro-interrogates-and-handoff-routes]]. Its sections
are named after failure shapes rather than after folders: *open questions*, *could not close*,
*diverged*, *fell out silently*, *went wrong*, *left fragile*, *contradicted itself*, *worth
keeping*. Each carries a `→ handoff:` line naming the journal section it feeds, which is the first
of the mapping's two hops.

**`Open questions` is a gate rather than a payload.** The retro does not end while a line there
carries no verdict, and the list is built whether or not the owner takes the conversation —
[[the-open-questions-list-is-built-whether-or-not-it-is-discussed]]. There is no queue behind it:
every action item routes into an address that already exists
([[the-retro-has-no-action-queue]]).

## What it produced on its first run, which is the evidence rather than the claim

Three things reached the journal of 2026-08-17 **only because the interrogation ran before it**:

- the count of `wiki/` pages edited by hand, which read as routine one permission at a time and as
  a divergence in one line ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]);
- three claims asserted from prose or from intention rather than from the file, two of them already
  repeated to the owner ([[a-claim-asserted-from-prose-rather-than-from-the-file]]);
- the gap in S2's acceptance criteria, which surfaced under *what fell out without a decision* and
  became the sixth criterion.

None would have been in a journal written straight after the work. What the step still cannot
reach is what the closing ritual itself produces after the journal is written —
[[the-closing-ritual-produces-what-the-journal-cannot-hold]].

## Not to be confused with `docs/retro.md`

**`docs/retro.md` was never ours.** The owner dropped a reference from another project into `docs/`
on 2026-08-17 to show the shape of a retrospective, and removed it the same day. It is named here
because a foreign skill file sitting in `docs/` reads as this project's own to a session that finds
it later.

## Its second run, measured — 2026-08-17

**The retro list ran to 26 lines: 17 answered, 9 deferred, 0 could-not-close.** Fourteen were
routed without the owner; **eight were put to him and all eight came back.**

**The split was itself the owner's choice**, on the argument that most lines needed a *destination*
rather than an argument — which is what [[retro-interrogates-and-handoff-routes]] claims the step is
for, now with a number behind it. A zero in *could not close* is the column worth watching: it is
the one that says whether the gate on `Open questions` is real
([[the-open-questions-list-is-built-whether-or-not-it-is-discussed]]).

**Eight of eight returned** is the measurement that decides whether putting a line to the owner is
expensive. On this run it was not.

## It ran on 2026-08-17 and the owner could not tell — recorded 2026-08-17

**The skill was invoked, its body was loaded, and nothing was said out loud.** The owner's report is that
he could not tell `/retro` had run at all. The instruction it skipped is explicit and is the skill's own:
say which skill is being used and for what, then follow its checklist out loud.

**A ritual nobody can see running is a ritual nobody can tell was skipped**, which is the whole finding
([[a-ritual-that-runs-unannounced-cannot-be-told-from-improvisation]]).

**The step's output was not the problem.** That run produced eleven owner decisions and twenty-four feedback
lines. What was missing was the evidence, at the time, that the steps were being taken — and this step
exists precisely because it produces what the journal cannot hold
([[the-closing-ritual-produces-what-the-journal-cannot-hold]]).

**It also lost a file to the shell, twice**, while writing its own transit file
([[the-retro-writes-its-own-transit-file]], [[prose-does-not-survive-a-shell-command-string]]).

# It gained a ratification step, and the steps after it moved down — 2026-08-21

**`.claude/skills/retro/SKILL.md` now carries *Ratify every word about to be put in his mouth* as
step 5**, between the gate and the writing of the retro file; writing the file became step 6 and
`/handoff` step 7.

**What it does:** lists every line the session is about to attribute to the owner — typically five
to fifteen — and puts the list to him. He answers each with yes, no, or a correction. A line he does
not answer is `could-not-close:`, never a silent promotion to his word
([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]]).

**Where it sits is load-bearing.** `/handoff` builds the journal from this file and `/ingest` builds
pages from the journal, so an unratified attribution is a page tomorrow. Running before the file is
written is the last point at which a wrong sentence costs a question rather than a supersession
([[the-closing-ritual-produces-what-the-journal-cannot-hold]]).

**Its first run found a hole in itself and it is left as one**: a ruling the owner made by choosing
among options the session authored fits neither row of its table
([[a-ratification-row-for-a-ruling-the-owner-chose-and-the-session-worded]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# The hole it found in itself is closed, and the step narrowed — 2026-08-22

**The table has a third shape.** A ruling taken from a rendered menu is written as `owner selected:`,
carrying the option's label verbatim plus what it was chosen against — his decision, the session's
words, and never quotation marks
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]). **The
proposal that reported the hole is retired**
([[a-ratification-row-for-a-ruling-the-owner-chose-and-the-session-worded]]).

**And step 5 stops ratifying remarks that settle nothing.** Only decisions are brought for signature;
a list padded with a session-opening question is read less carefully than a list of rulings.

# What one run of it measured, 2026-08-22

**It ran as `grill-me`, the agent asking** — three rounds, plus one the owner opened himself
([[grill-me-skill]], [[interviewing-in-rounds-asks-only-what-is-unblocked]]).

**Nineteen questions were put to him**, and **three more were closed by reading the repository rather
than by spending his attention** ([[a-file-this-session-did-not-touch-is-a-vault-question-before-an-owner-question]]).

**The lines it produced: 22 opened, 18 answered, 4 deferred, none that could not be closed.** Against
the same session's own attribution measurement — ten owner utterances, two of them his own words —
that is what the third shape was created for.

# It gained a step 0 on 2026-08-24, and its list stops being written from memory

**Step 0 runs `scripts/session-dialogue.py`** and the skill builds its list of open questions from
`.superpowers/sdd/session-dialogue.md` rather than from what the session remembers
([[the-session-dialogue-extract]],
[[the-floor-under-a-session-is-read-because-the-record-already-existed]]).

**Step 1 gained a four-item attention checklist**, measured from what had actually gone missing in
past retros rather than composed. **Step 5 assembles the ratification list from `decision:` marks**
instead of from recall
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**Both steps must report how many items came from the marks and how many were found by reading.**
On the first run: **four of fifteen open questions came from the marks; eleven were found by
reading.** That ratio is the only measurement this channel will ever have of what the marks miss,
and it says they miss two thirds — **a number to watch across sessions rather than to act on once.**

**What it bought immediately** is an attribution question answered in seconds: the owner asked
whether «порог не назначаем» had been his words, and it was turn 38, verbatim
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

# How its list is worked changed — 2026-08-29

**The session sets a verdict on every line alone and brings the whole list as one block**, and the
owner accepts or refuses with a correction
([[the-retro-verdicts-are-set-by-the-session-and-brought-as-one-block]]).

**The step that calls for `AskUserQuestion` was diverged from again**, and the session used no menu at
all — 18 owner turns, 88 replies, zero menus
([[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]).

**And how a question reaches him at all was ruled on the same day**: context, how it works today, what
would be built, and a recommendation
([[every-question-put-to-the-owner-carries-context-and-a-recommendation]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# DIVERGENCE: the menu step was answered in prose for the third recorded time — 2026-08-29

**Step 2 of the skill calls for `AskUserQuestion`. It was not used.** The record it was taken against:
two interruptions of that menu on 2026-08-24, an existing divergence page, the same divergence taken on
2026-08-29, and the owner's ruling of 2026-08-29 that the session sets its own verdicts and brings them
as one block. **Rejected alternative: obey the skill.**

**The prohibition it is measured against is
[[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]**, and the two now disagree
about which is the rule: the skill says menu, the decision says prose, and the practice has taken prose
three times running.

**`scripts/session-dialogue.py` reports zero menus for the session**, second consecutive session at
zero — thirteen owner turns, thirty-three replies, and every ruling in his own words except five he
selected from options framed in prose ([[the-session-dialogue-extract]]).

**Recorded as a divergence rather than taken silently.** It is filed here rather than as a new page
because `binding: divergence` selects nothing in `wiki/decisions/` today — the sweep of 2026-08-29 took
all 22 — so a new divergence page would be taken by the archiver on sight
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
