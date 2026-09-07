---
title: "The `/pre-task` enumeration covers every folder but `lessons/`, and the ritual was not changed"
type: decision
status: current
authority: pre-task-enumeration-scope
binding: deferral
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md", ".claude/agents/pre-task.md", ".claude/agents/vault-librarian.md"]
tags: [process, retrieval, agents]
---

# The owner ruled the current scope wrong, 2026-08-21

**`/pre-task` guarantees a full enumeration over `decisions/` and nothing else.** Its skill says
*"List every `decisions/` page"*, and the librarian's own definition repeats it
([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]],
[[one-librarian-behind-every-caller]]).

**He raised it explicitly and said it is wrong.** The enumeration must cover `concepts/`,
`entities/`, `proposals/` and `rules/` as well — **`lessons/` alone stays out**, and it stays out for
a reason rather than by omission: the lessons are to become a queue drained at ingest, so a plan
check reading them would be reading a work list rather than a constraint
([[lessons-become-a-queue-drained-into-proposals]]).

**What falls outside the guarantee today: 121 `lessons/`, 102 `concepts/`, 33 `entities/` and 24
`proposals/`.** Only `decisions/` is enumerated, so the promise that a plan is checked against
everything already decided is false as stated.

# It was not built, and that is the deferral

**The session built the index those folders are searched by and did not touch the ritual that would
use it** ([[authority-becomes-the-index-and-is-required-outside-rules]]). This is `binding: deferral`
and not a prohibition: doing it is what was intended, and it is the first item on the sprint's next
list.

**The work item names its files:** `.claude/skills/pre-task/SKILL.md` and
`.claude/agents/vault-librarian.md`. Both are the session's to write, not the librarian's
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

# The cost is not hypothetical: it was paid in the session that named it

**`proposals/a-generated-harness-map` held a finished design, was not found, and was nearly written
again from scratch** ([[a-generated-harness-map]]). A `/pre-task` covering `proposals/` would have
returned it.

**And the shape was on the record before that.** The one error a wider reading would have caught in
an earlier session sat in `concepts/`, which the ritual as written does not read
([[breadth-was-what-was-missing-and-pre-task-is-one-way-to-buy-it]]). **The finding is now a ruling
rather than an observation.**

# What it does not decide

**It does not say how the wider enumeration is paid for.** A frontmatter sweep over the whole corpus
is one pass and is already built ([[vault-scripts]]); whether the ritual reads it, and what the
ten-page opening ceiling means once four more folders are in scope, is the funnel question and is
open ([[the-reading-funnel-is-delivered-as-a-procedure]], [[the-folder-is-the-first-narrowing]]).

**It does not reopen the ceiling.** Enumerating is not opening, and the distinction is the whole
reason the wider scope is affordable at all.

# The deferral is discharged, and it was built the next day — 2026-08-21

**`.claude/skills/pre-task/SKILL.md` now enumerates `concepts/`, `entities/`, `proposals/` and
`rules/` whole, and `decisions/` filtered to `binding: prohibition`** — about **342 rows** against
the 193 this page measured, with `lessons/` out by the ruling above
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

*(**That file is deleted as of 2026-08-22** and the `now` above means 2026-08-21. What it enumerates
is at `.claude/agents/pre-task.md`, which the closing section of this page records; the sentence is
dated where it stands and not rewritten —
[[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
[[the-date-of-a-correction-note-is-the-date-the-text-became-false]].)*

**The funnel question this page left open is answered by the same change.** The wider enumeration is
paid for by `bash scripts/vault-catalogue.sh` — one pass, 1.66 s — and the ten-page opening ceiling
is untouched, because the reading is narrowed by the shortlist rather than by the scope
([[vault-scripts]], [[the-folder-is-the-first-narrowing]]).

**`binding:` got its first reader here**, which is what the field was designed for
([[a-decision-declares-whether-it-binds]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# The citation is repointed, and the enumeration this page ruled on is at the new address — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`.**
The skill was deleted on this date ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]),
and rule 5 of the gate requires every repository path in `sources:` to resolve — a citation to a file
that is not there reads as provenance and is not ([[vault-scripts]]). **The address moves and the
history stays readable**: the two sections above name the skill in prose, on the day it was the file
the work item pointed at, and neither is rewritten.

**What this page ruled survived the move whole.** `.claude/agents/pre-task.md` drops `lessons/` and
`archive/`, keeps `concepts/`, `entities/`, `proposals/` and `rules/` whole, and reduces `decisions/`
to `binding: prohibition` — the scope of the ruling, now in the file that performs it rather than in
the file a caller read.

**Two things the discharge section above names are not carried at the new address**, and neither is a
retraction: the row counts — **342 against 193** — and the `1.66 s` reading of the catalogue pass are
the skill's figures. The agent gives no totals and says *about 1.7 s*. They stand here as a
measurement of 2026-08-21 ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**The work item's second file also moved.** It named `.claude/agents/vault-librarian.md` as the other
place the enumeration lived; the librarian is no longer part of this ritual at all
([[one-librarian-behind-every-caller]]).

# The exclusion survives and its stated ground does not — 2026-08-24

**This page says `lessons/` stays out because the lessons are "to become a queue drained at
ingest".** The drain moved: it is a `/vault-lint` dispatch that reads the whole queue at once, and
it is not an ingest step ([[lessons-become-a-queue-drained-into-proposals]],
[[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]]).

**The ruling itself is untouched.** `lessons/` is still a work list rather than a set of
constraints, and a plan check reading it would still be reading intentions as constraints. **What
went false is the sentence explaining where the draining happens**, and it is dated here rather than
rewritten ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**The reason the ground had to move is on the collector's page**: an ingest stands inside one
session's context, where the seventh instance of a family looks exactly like the first, so a drain
performed there could never see a family at all.

**The counts in this page are the tree of 2026-08-21.** `lessons/` holds 140 pages on 2026-08-24,
not 121, and the figure above stands as a measurement of its own date
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# Measured 2026-08-25 — both halves of the filter cost a finding in one run

**Phase 1 drops `lessons/` and it drops `binding: deferral`.** On the run of 2026-08-25 each omission
cost a finding.

**The page forbidding the plan's extra `governs:` address is in `lessons/`**, and its title says
nothing about `governs:` — so neither the folder filter nor a title scan could reach it
([[a-rule-may-not-govern-a-file-the-ritual-empties]],
[[the-feedback-rules-extra-destination-is-withdrawn]]).

**The ratification of the three harness defects is a `deferral` page**, dropped by the binding filter
([[the-harness-defects-found-this-session-enter-the-sprint-one-line-each]]).

**Four of the five load-bearing pages for that plan were outside the filter.** The narrow dispatch
found them by reading; the enumeration did not offer them
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

# Measured 2026-08-28 — the decisive page for the plan was in `lessons/`

**Phase 1 drops `lessons/` whole — 178 pages — and the page carrying the authority for the plan's
second step was in it**:
`the-integration-suite-hangs-rather-than-failing-when-docker-is-down`. It was reached only by a
wikilink from `wiki/entities/the-test-database-guard.md`.

**That is the third recorded run where the folder filter cost a finding**, and on this one the narrow
dispatch recovered it by following a link rather than by being offered the page
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]],
[[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

**The ruling is untouched.** What the readings accumulate is evidence about the cheap phase's
discard rate, which is what they were written down for.

# The fourth run on which the exclusion cost a finding — 2026-08-29

**The requirement that a plan touching the vault's own machinery enumerate the brief's *what must not
be broken* list as items lives in `wiki/lessons/`**, at
[[a-plan-touching-the-vaults-own-machinery-enumerates-what-must-not-be-broken-as-items]]. **Phase 1
discards that folder by instruction, and the agent reached the page only because the caller named its
slug.**

**So a lesson stating a standing procedural rule is invisible to the ritual that is supposed to apply
it** — a sharper statement than the three readings above, which were about incidents this pass did not
reach. This one is about a rule.

**And the arithmetic the ruling rested on has moved.** `lessons/` held 121 pages when this was decided
and holds **18** after the sweep of 2026-08-29 — the smallest folder in `wiki/` bar `rules/`. The cost
the exclusion was buying is most of the way gone.

**The case for revisiting it is written out and is not taken here**:
[[the-pre-task-enumeration-reaches-a-lesson-that-states-a-standing-rule]]. **This is his ruling and only
he lifts it**; the ruling stands unchanged until he does.

**One correction to the ground stated above.** `.claude/agents/pre-task.md:130` keeps `concepts/`,
`entities/`, `proposals/` and `rules/` **whole** and filters only `decisions/`, on
`binding: prohibition` or `deferral`, at line 118. So *"`/pre-task` reads decisions instead of the other
folders"* is false; what only `decisions/` carries is `binding:`, the answer to what stops a plan.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
