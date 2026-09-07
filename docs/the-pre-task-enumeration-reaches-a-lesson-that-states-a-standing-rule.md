# The `/pre-task` enumeration reaches a lesson that states a standing rule

**Draft proposal, prepared by the lessons agent on 2026-08-29 from
`raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

This proposes a change to a file that instructs an agent — `.claude/agents/pre-task.md`, line 116 —
and it names that plainly. **It also asks the owner to revisit a ruling of his own**, which a session
may not do by itself, so what follows is the case for asking rather than the change.

## What it would be

**Phase 1 of `/pre-task` stops discarding `wiki/lessons/` by folder name, and discards by what a page
is.** A lesson that records an incident stays out; a lesson that states a standing procedural rule
comes in.

The mechanism is not designed here, and that is deliberate — see *what is open*. What is proposed is
that the exclusion stop being unconditional.

## Why it is raised: the exclusion has now cost a finding four times

The ruling is `wiki/decisions/the-pre-task-enumeration-covers-every-folder-but-lessons`
(`binding: deferral`, decided 2026-08-21, the owner's). Its ground, in its own words: the lessons are
a work list, so *"a plan check reading them would be reading intentions as constraints"*.

**That page already records three runs on which the exclusion cost a finding**, dated where they
stand — 2026-08-25 twice and 2026-08-28 once, the last of them the page carrying the authority for a
plan's second step, reached only by following a wikilink out of an entity page.

**This journal is the fourth.** The requirement that a plan touching the vault's own machinery
enumerate the brief's *what must not be broken* list as items lives at
`wiki/lessons/a-plan-touching-the-vaults-own-machinery-enumerates-what-must-not-be-broken-as-items`,
and the run reached it **only because the caller named its slug**.

**So a rule stated in `lessons/` is invisible to the ritual that is supposed to apply it**, and the
one page in the corpus that says how a plan over vault machinery must be shaped is in the folder the
plan checker is instructed not to look in.

### The arithmetic the ruling rested on has collapsed

**`lessons/` held 121 pages when the exclusion was ruled and holds 18 now**, after the sweep of
2026-08-29. The cost the exclusion was buying — a cheap enumeration — is no longer a cost worth
buying: the folder is now the smallest in `wiki/` bar `rules/`.

**The ruling's stated ground has already gone false once and been dated in place rather than
re-taken.** The page says the lessons are *"to become a queue drained at ingest"*; the drain moved to
a `/vault-lint` dispatch on 2026-08-24 and is not an ingest step. The exclusion survived that
correction untouched, which is correct process and is also how a ruling outlives its reason.

### The queue's own criterion marked both recurring lessons as handled

**Two of this journal's lessons landed on live pages that are already cited from outside
`lessons/`** — `a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep` and
`a-plan-touching-the-vaults-own-machinery-enumerates-what-must-not-be-broken-as-items`, each cited
twice. Under `scripts/lessons-queue.py` both are `CITED`, which is the loop's end state.

**Both recurred anyway, within days of being written.** That is two fresh instances of a defect the
store already recorded and then archived:
`the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach` (2026-08-26,
now in `archive/`). A citation is a trace that somebody read the page; it is not evidence that the
failure stopped happening.

**And the queue's shape is the argument for reading the folder rather than draining it.** Eleven of
the eighteen live lessons are cited by nothing outside `lessons/` at all, so the folder today is
mostly unread by anything, while the two pages that *are* read are the two that recurred.

## What it would take

**One line of `.claude/agents/pre-task.md` and a way to tell the two kinds apart.** Line 116 reads
*"Drop `## lessons` and `## archive`"*, with the ground given inline: *"`lessons/` records what burned
us, which is a different question from what stops this plan"*. The archive half is not touched by
this draft.

Three ways to tell the kinds apart, none chosen:

1. **A field on the lesson page.** Cheapest to read, and it is the shape the vault has already
   refused once: a page declaring itself changes what an instrument sees and nothing checks the
   declaration ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).
2. **The folder splits.** A lesson stating a standing rule is arguably a `rule` already, by the
   folder set's own definition — except that a rule must name a `governs:` destination and render
   text into it, and *"enumerate the constraint list as items"* is addressed to a plan, which is not
   a file in this repository.
3. **Enumerate `lessons/` whole and let the shortlist do the narrowing.** Eighteen rows added to a
   pass that already prints hundreds. This is the option the ruling's own discharge section endorses
   for the other four folders — *"the reading is narrowed by the shortlist rather than by the
   scope"* — and it is the one that needs no new field and no new folder.

**Route 3 is the cheapest today and would not have been in August.** Its whole cost is eighteen more
rows in a catalogue pass measured at about 1.7 s.

## What is open

- **This reverses a ruling of the owner's, and only he can.** The session's part is the four datapoints
  and the changed arithmetic; the decision is his and this draft does not assume it.
- **Whether route 3 reintroduces the harm the ruling named.** A plan checked against a work list reads
  intentions as constraints. Eleven of the eighteen live lessons are incident records and would be
  exactly that noise. Nobody has measured how a shortlist behaves when a sixth of its input is a
  work list.
- **What happens to the exclusion when `lessons/` grows back.** The folder was drained by a sweep, not
  by a policy; if it returns to 121 pages the cost argument returns with it, and a ruling taken on
  today's size would go false without saying so
  ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).
- **Whether the `archive/` half is the same question.** This journal records two consecutive runs in
  which the load-bearing constraints were in `archive/` and unreachable by enumeration, all of them
  recovered by following wikilinks out of live pages. The owner has ruled that `/pre-task` should not
  read `archive/`, and the right question is whether the citing page carries the claim — which is a
  different proposal and is named here so it is not folded into this one.

## What it would oblige

- **A reading on the next run.** The two counts `/pre-task` returns — pages shortlisted, pages opened
  — are the only series that shows whether the wider scope cost anything, and they are already
  recorded per run on `wiki/entities/the-pre-task-agent`.
- **The ruling page is corrected in place, not superseded**, if the exclusion is lifted: the claim
  changes, so this is a supersession and needs a successor page. If it is only narrowed, it is a dated
  section on the existing page. Which of the two it is depends on the owner's answer and this draft
  does not pick.
- **`.claude/agents/pre-task.md` carries a rendered region**, so any edit inside it is a
  `wiki/rules/` write and not a session's. The line at issue sits **outside** the region — the
  entity page records the region as lines 28–102 as of 2026-08-26 — so this is a session edit, and
  that boundary must be re-read against the file before anyone touches it rather than taken from
  here.

## What it would retire

- **`wiki/lessons/a-plan-touching-the-vaults-own-machinery-enumerates-what-must-not-be-broken-as-items`**
  — but only if the exclusion is lifted. That page exists because the ritual could not reach the
  constraint, so the plan had to carry it; a ritual that reaches it makes the page's remedy the
  wrong one, and its content moves onto the ruling.

**If the owner leaves the exclusion standing, this proposal retires nothing** and its whole product
is the fourth datapoint added to the ruling page. That outcome is a legitimate one and is named here
so the draft is not read as assuming its own acceptance.
