---
title: "The librarian writes the vault unattended: detection replaces permission"
type: decision
status: current
authority: librarian-write-permission
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [agents, vault, process]
---

# The librarian writes, and does not ask

**Decided on 2026-08-13.** It creates, updates and retires pages under `wiki/`, and updates
`index.md`, `tags.md` and `log.md`, without approval. Rejected: review before each write — an
approval gate on a maintenance job is a gate nobody passes twice, and the vault would stop being
maintained within a sprint.

**Review is post-hoc**, and three mechanisms are what make it real rather than nominal:

1. **Git is the audit log.** Each ingest is a commit: `git diff` says *what* changed, mechanically,
   and `log.md` says *why*. A self-reported log alone would be testimony of exactly the kind we
   already decided not to trust wholly in the journal. **A disagreement between log and diff is
   itself a finding.**
2. **It never deletes text.** It appends, or it deprecates a page and writes its successor. No fact
   can vanish silently, because there is nowhere for it to go. The dangerous act was never a new
   page — a new page is at worst clutter — **it is an edit that quietly eats a paragraph.** This
   also shrinks the review from "read everything" to "read the deprecations", of which there are
   nought to two per session.
3. **It does not resolve a contradiction.** Two `current` pages claiming the same `authority` get a
   `> [!CAUTION] CONTRADICTION` block on **both**, and the brief raises it. Asking the owner in
   chat is welcome but insufficient: an answer given in chat leaves no artefact. **The marking is
   the artefact.**

**None of the three serialises anything.** "One writer" is a convention about who is *dispatched*,
and a parallel fan-out of librarians breaks it in silence — observed on 2026-08-14 with `tags.md`
as the target: [[parallel-librarians-break-the-one-writer-property]]. Mechanism 1 sees the
surviving text, never the lost write.

## The guard is a reminder, and cannot be more than one

`.claude/hooks/ask-the-vault.ps1` fires before a write into `wiki/` and says that this store has
exactly one writer. **It cannot enforce that**: a `PreToolUse` payload does not say *who* is
writing — the librarian's write and anyone else's are the same JSON ([[session-hooks]]).

So mechanism 1 above is not a fallback, it is the enforcement. `/ingest` now asks its caller for it
by name: `git diff --stat`, `git diff` over `wiki/`, `tail` of `log.md`, then the two scripts.
**The review that replaced asking permission belongs to the caller, not to the party being
reviewed** — every step of an ingest is performed by the librarian, so a self-check is testimony
again.

## The same division applies to sprints

The librarian reports the state and never closes a sprint — see [[a-sprint-closes-on-its-goal]].
Closing a sprint and choosing between two rules are the same kind of act: a judgement about the
project rather than about the store, and the store's keeper is not entitled to it.

What it is, and what its four callers are: [[vault-librarian]],
[[one-librarian-behind-every-caller]].

## The rule was diverged from on 2026-08-17, and the clause it owes

**The main session wrote `wiki/` by hand**, on the owner's order and after the librarian had
returned: thirty-seven pages retitled or given a `quantity:` line, two with `sources:` repointed, and
one retitled again at the retro - counted and recorded as one divergence rather than as a series of
small permissions ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]).

Two properties made it safe and **neither is written into this rule**: no parallel writer, and the
owner reviewing the diff before the commit. As it stands the rule reads as absolute and the guard
hook says so, which makes every such repair an undocumented divergence — while the vault's own
record already assumes an exception, since supersession and deletion belong to the owner's session.

**The clause is owed and is the owner's to write**: who may write `wiki/` when the librarian is not
running, and what makes it safe. The librarian does not write the store's rulebook, so this is
recorded here and raised in the brief.

## The design was tested for the first time on 2026-08-17, and it held

**The librarian found a contradiction, refused to resolve it, marked both halves, and named the choice as
the owner's. He resolved it in the same turn.** That is the whole loop, exercised end to end on the first
occasion that produced a real one: the `governs:` uniqueness of `vault-check.sh` against the migration of
four rules sharing one destination ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**Then it did the harder half.** Once the owner had decided, the librarian went back and annotated **six
pages** that were still claiming the question open — rather than leave the corpus arguing with itself —
appending a dated resolution under each and deleting none of the alarm.

**Both halves are the property, and the second is the one nobody designed for.** Marking a contradiction is
cheap; the cost of the one-writer rule is that somebody has to notice when the marks go stale, and only the
writer can. **A marked contradiction that outlives its resolution is a worse artefact than none**, because
it reads as a live question.

**The librarian also over-reported.** The same session recorded that the marks had been placed in five
places and that all of them were stale within the hour — the alarm and the resolution both being the
librarian's write, not the session's. That is filed as a `lint:` rather than as a miss: the vault supplied
what it had.

# The commit half of this page stopped being a claim and became a step — 2026-08-29

**This page has said since 2026-08-13 that "each ingest is a commit: `git diff` says what changed,
mechanically, and `log.md` says why."** Nothing performed it. For sixteen days the diff was there to be
read and no ritual required anybody to read it.

**owner:** «комитим. И сразу добавляем последний шаг для ingest - комит.»

**`.claude/skills/ingest/SKILL.md` now ends in a commit**, in `After the librarian returns` and outside
the block quoted to the librarian — which keeps this page's own boundary: **the librarian does not
commit.** It writes; the session reads the diff, commits, and the review is the caller's.

**The step requires the owner's reading of `git diff` before the commit, an English message naming what
was compiled, and `git status --short` printing nothing afterwards.** It was typed in without a
`wiki/rules/` page and the debt is recorded rather than paid
([[the-commit-step-is-typed-into-the-skill-and-the-rule-page-debt-is-recorded]]).

**So the mechanism caught up with a claim the corpus had already made**, which is the useful shape
here: the sentence was not wrong, it was unenforced, and nothing distinguished the two by reading.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
