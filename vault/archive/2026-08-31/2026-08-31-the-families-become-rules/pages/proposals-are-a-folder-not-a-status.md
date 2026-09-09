---
title: "What we planned and never did gets a folder, not a status: wiki/proposals/ is a category of its own"
type: decision
status: archived
authority: proposal-category
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["scripts/vault-check.sh", "scripts/vault-catalogue.sh", "scripts/vault-check-selftest.sh", "CLAUDE.md"]
tags: [vault, process]
---

# The question it was added for, and the shape it was given instead

**Decided by the owner on 2026-08-15.** His reason is a question he wants the store to answer
quickly: **"what did we plan and never do"** — the things that were discussed, designed in passing
and put off, which today survive only in a chat log and are therefore lost the moment the window
closes. The shape he asked for was a **status**, something like «предложено» / «отложено» on a page
in `decisions/`.

**What was built is a folder: `wiki/proposals/`.** The reasoning below is the session's, not his —
he asked for the capability and the shape was chosen here, which is why this page says so rather
than putting the argument in his mouth.

*(The title read "What we planned and never did gets a folder, not a status: wiki/proposals/ is the
fifth category" until 2026-08-18. **That ordinal counted the folder set, which belongs to the world
outside this page and not to it**: `wiki/rules/` arrived on 2026-08-17 and the set is six, so the
title had gone stale without a word of the page changing — the exact shape of
[[a-stated-count-drifts-from-the-list-it-heads]], and the last section below already records the
larger set ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). This page never carried a
`quantity:` line, so the repair is the retitle alone. **The owner ruled ordinals into rule 10's
word list on 2026-08-18** ([[ordinals-count-and-first-does-not]], written 2026-08-19 — the ruling
had until then been carried as prose on this page and three others), and the recorded order is
corpus-before-check precisely so that
tightening the predicate never reddens a page
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]); this lands ahead of the
verdict that will catch it. The title now says what the folder is instead of where it came in the
queue ([[a-title-names-what-is-counted-instead-of-counting-it]]). Not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## Why a folder and not a `status:` value

**A field asks to be read carefully; a folder makes the mistake structurally impossible.** The
mistake in question is not hypothetical here and is not rare:

- **This project has twice compiled intent as though it were a record of something built** — both
  of the owner's notes of 2026-08-13, which are specifications written in the present tense about a
  store that did not exist ([[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]).
- **The second time it was caught by a human reading, not by any check.** Nothing in the toolchain
  can see it: `vault-check.sh` reads structure and a page's claim is outside its vocabulary
  entirely, and a coverage verdict of `page:X` asserts that X exists, never that X is true.

A page in `decisions/` carrying `status: proposed` is one field away, at every future reading, from
being quoted as settled. A page whose **path** is `wiki/proposals/` cannot be: the folder is in
every grep hit, every wikilink resolution, every catalogue row, and in `type: proposal`, which rule
2 of `vault-check.sh` enforces against the folder name. The rule needed no new list to say so —
`want` is the folder minus its trailing `s` — so the category cost one word in rule 1 and nothing
in rule 2.

**`status` therefore stays two-valued.** A proposal is `current` while it stands, and `deprecated`
with `superseded_by:` once it is built or refused — so **the page's own frontmatter answers what
became of it**, by the same mechanism as every other retirement in this vault, and the question
"what did we plan and never do" is answered by `rg -l "^status: current" wiki/proposals`. A third
status value would have been a second vocabulary to keep in step with the first.

## The boundary with `decisions/`, which was not taken over

**Deferring something is still a decision** and keeps its page in `decisions/`: a date, a reason,
and a rejected alternative — the rejected alternative being *do it now*. **The proposal carries the
design**: what would be built, what it would take, what is open. The two are different pages and
**both often exist**; the vault's own `CLAUDE.md` now states this in the same words.

- A **deferral with nothing designed behind it needs no proposal page.**
  [[collection-features-deferred]] is that shape: four features not built, each with a one-clause
  reason, none of them designed far enough that a second page would carry anything the decision
  does not already say.
- A **design that would otherwise survive only in a chat log does** need one, and that is exactly
  the loss the owner named.

The first two pages in the folder show both halves working:
[[dynamic-tag-classification-by-a-skill]] is a design with no decision behind it yet, and
[[migrating-the-repository-to-english]] is a design whose decision half is
[[english-is-the-rule-and-the-russian-past-is-deferred]].

## Rejected

- **`status: proposed` / `status: deferred` on a `decisions/` page** — the owner's asked-for shape,
  and the reason against it is the whole section above.
- **A `tasks/` folder, again.** It was not on the table and this is not a back door to it: a
  proposal is compiled by the librarian from a source in `raw/`, like every other page here, and a
  task list is not compiled from anything. That argument is on
  [[the-wiki-has-five-folders-and-tasks-is-not-one]], because it is the folder set's question and
  not this one's.

## What it obliges

A category is a change to the map, and this one was made in a single pass across five places:
**rule 1 of `vault-check.sh`; the section loop of `vault-catalogue.sh`, which gives the folder its
own section and its own count; the vault's `CLAUDE.md`, which carries the category and the boundary
above; `index.md`; and the selftest**, which now runs a proposal in its own folder, one mistyped as
a decision, and the folder removed.

**`/ingest` step 1b files an intention there.** That is the load-bearing half: a folder nothing
writes to is the failure this vault already refuses on
[[the-wiki-has-five-folders-and-tasks-is-not-one]], so the category exists only because the ingest
loop now has a step that produces its pages.

## Both citations above point at a page retired on 2026-08-17

[[the-wiki-has-five-folders-and-tasks-is-not-one]] is in `archive/`; the folder set is six and its
page is [[the-folder-set-is-closed-and-tasks-is-not-in-it]]. **Both arguments this page borrows from
it survive verbatim** — `tasks/` is refused on the same two grounds, and the boundary against
`proposals/` is carried into the successor and extended to `rules/`.

**The five-place cost recorded above was paid again**, minus `index.md` and plus the frontmatter
pass, when `wiki/rules/` was added ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# One clause of this page was rewritten by the owner — 2026-08-22

**The clause is *"A proposal is `current` while it stands, and `deprecated` with `superseded_by:`
once it is built **or** refused."* It is left standing and it is false in its **built** half from
this date** ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**A built proposal now stays in `wiki/proposals/` with a `built` mark**, on the owner's ruling, and
he said in the same sentence that the ruling rewrites the earlier ones
([[a-built-proposal-stays-in-proposals-with-a-built-mark]]). **The refused half is untouched**: a
refusal has a successor asserting the same claim the other way, and that is what supersession is for.

**The argument this page makes against a third `status` value is now argued at the owner**, and it is
his to answer: *"a third status value would have been a second vocabulary to keep in step with the
first."* Whether the `built` mark is that third value or a field of its own is deferred to the next
session in his own words. **Nothing here prejudges it** — the sentence is named because he is the one
choosing, and it is the only argument on the record against one of his two options.

**What the ruling costs this page's own reason for existing, stated rather than left to be found.**
The section above answers *what did we plan and never do* with
`rg -l "^status: current" wiki/proposals`. **A built proposal staying `current` puts a built thing in
that answer**, so the mark is what has to carry the distinction until the query is rewritten around
it. The query over-reports in the meantime, which is the safe direction and is still wrong.

**The two-valued `status` field is not otherwise touched.** Every other folder is unaffected, and so
is the boundary with `decisions/` below.

# The section above is overtaken on its own date — 2026-08-23

**The owner reversed the ruling of 2026-08-22 the following day, and the argument this page makes
against a third `status` value lost.** An implemented proposal does move to `archive/`; `archive/`
is history rather than a verdict about truth; and the mark is a third value in `status` rather than
a field of its own ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]],
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**Two clauses of the section above are therefore false from this date**
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]): that a built proposal *stays*
in `wiki/proposals/`, and that the shape of the mark is deferred. **The rest of that section stands
as written**, including the refused half and the cost to this page's own query.

**The clause this page originally carried is partly true again.** *"A proposal is `current` while it
stands, and `deprecated` with `superseded_by:` once it is built **or** refused"* was declared false
in its built half on 2026-08-22, and the correction survives: an implemented proposal moves to
`archive/` **without** being deprecated and **without** a `superseded_by:`, because there is no
successor asserting the same claim differently. What carries it instead is `status: implemented` and
a citation from the live page that records what was built.

**And the query this page exists for is answerable again.** `rg -l "^status: current" wiki/proposals`
stops over-reporting once an implemented proposal has left the folder — which is the reversal's own
argument for itself.
