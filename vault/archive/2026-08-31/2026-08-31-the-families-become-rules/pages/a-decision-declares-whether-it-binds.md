---
title: "A decision declares whether it binds, and `binding:` is required in `decisions/`"
type: decision
status: archived
authority: decision-binding
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["wiki/decisions/_schema.yaml", "scripts/vault-authority.sh", "scripts/vault-check.sh", "CLAUDE.md"]
tags: [vault, process, retrieval]
binding: prohibition
---

# The folder held three different things and answered as one

**Measured 2026-08-21 across the 189 pages then in `decisions/`:** six carry a `DIVERGENCE:` title
and record how a rule was already broken; about thirty record a deferral; the rest forbid
something. Nothing in the frontmatter separated them, so nothing reading the folder could.

**The cost is paid by `/pre-task`, which is the folder's heaviest reader.** A plan checked against
`decisions/` came back with a list of *relevant* pages where it needed a list of what *stops* it,
and the difference is the whole use of the answer. A deferral tells a plan "this is already
designed, do not invent it again"; a divergence teaches and forbids nothing; only a prohibition is
a constraint the plan can violate. Read as one kind, all three arrive as advice.

So `binding:` is required in `decisions/`, with three values:

| value | what it means | how a plan check reads it |
|---|---|---|
| `prohibition` | it may not be done; lifting it is a conversation with the owner, never a session's call | a hard constraint, enumerated in full |
| `deferral` | not now — doing it later is what was intended | context: this is already designed, do not invent it again |
| `divergence` | how a rule was already broken | context; it teaches and forbids nothing |

**It is `optional` in `wiki/decisions/_schema.yaml` for exactly as long as the back-fill runs, and
that is an ordering fact rather than a doubt about the field.** A key in neither schema block is
rejected outright, so the field has to be legal before any page may carry it; and `required` before
the corpus carries it turns the gate red, which the librarian lock reads as a refusal to dispatch
the writer that would clear it ([[the-librarian-lock-hook]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). Promoted as the last step of the same
session that fills it. Decided in the same ruling as
[[occams-razor-is-the-ground-rule-for-the-vault]] and
[[authority-becomes-the-index-and-is-required-outside-rules]].

# An absent value reads as `prohibition`

**The field is required, so this is not a default the schema permits.** It is what a reader assumes
about a page that has not been marked up yet, during the window in which the corpus is being
marked up — and it is the safe direction. **A deferral misread as a prohibition costs a question. A
prohibition misread as a deferral costs the constraint.**

**It is the same kind of choice as [[the-pre-task-column-gains-a-state-for-asserting-nothing]]**,
where the question was what an unwritten value asserts to the human who reads the column. There the
answer was a third state, because `no` on a row that owed nothing asserts a skipped ritual; here
there is no third state to add, so the reading is fixed at the strict end instead. Both are the
same discipline: what absence *says* is chosen deliberately rather than inherited from whatever a
type happens to coerce to.

# Rejected: split `decisions/` into separate folders

**This is the stronger alternative and it was argued as one.** A folder cannot lie: a page sitting
in `prohibitions/` is a prohibition, with no self-declaration to trust and nothing to drift.

**It was refused on a named ground.** The folder set is closed
([[the-folder-set-is-closed-and-tasks-is-not-in-it]]), and it is closed against exactly this — a
category added in passing because it would be convenient. More concretely, moving 189 pages into
three folders rewrites 189 addresses, and in this store the filename is the identity: it is the
search surface and it is what every wikilink resolves to. A move of that size is the operation this
project requires the rewriter-and-detector pair for
([[a-rewriter-must-be-paired-with-a-detector]]).

**A field is reversible; a rename is not.** `binding:` can be withdrawn the way `quantity:` was, in
a day, by deleting a line from every page that carries it. A folder split that turns out wrong is
undone by a second sweep of 189 renames.

# The risk the field carries, named rather than hidden

**It is a self-declaration, and this store has already been burned by one.** `quantity:` was minted
on 2026-08-17 and withdrawn on 2026-08-18 for a reason that applies here word for word: *"a
declaration silences the one instrument that would have caught it drifting"*. **Two of its
twenty-four declarations were false while they stood**, and neither was found by anything
mechanical, because nothing mechanical was left looking
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**The mitigation is partial, and it is stated as partial rather than sold as a fix.**

- **`divergence` is mechanically verifiable**: the title begins with `DIVERGENCE:`, so the
  declaration and the page's own first string can be compared. `bash scripts/vault-authority.sh
  --binding` does exactly that, in both directions — a page declaring `divergence` without the
  title, and a `DIVERGENCE:` title declaring something else.
- **`prohibition` and `deferral` are judgements** and no script can separate them. `--binding`
  counts them and prints the counts for a human to compare against what he expects, which is a
  detector for a drifting *distribution* and not for a wrong page.

**That asymmetry is why the reader's default is the strict one.** The two values nothing can check
are the two a mistake would be silent in, so the unmarked and the unverifiable both resolve towards
the constraint rather than away from it. It does not make the field safe; it makes its failures
expensive in the cheaper direction ([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

# What it does not change

**It does not re-sort the folder and it moves no page.** Every decision stays where it is, under
the same address, with one line added.

**It says nothing about the other folders.** `concepts/`, `lessons/`, `entities/` and `proposals/`
forbid nothing by construction, so the field would carry one value across each of them and have no
discriminating power — the objection that kept `render:` out of the schema for two days
([[render-was-not-introduced]]) and the same test a field has to pass here
([[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]).

# It got its first reader the next day — 2026-08-21

**Carried by 193 of 193 pages in `decisions/`, and read by nothing until `/pre-task` split into two
phases.** Phase 1 keeps `prohibition` — **168 pages** — and drops `deferral` (19) and `divergence`
(6), which forbid nothing ([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**That is the reading the vault's own `CLAUDE.md` tabulates for the field**, applied by the consumer
it was designed for: a plan check needs a list of what *stops* it, not a list of what is *relevant*.

**The field's worth is now measurable rather than argued.** The filter takes the titles a plan is
matched against from 193 to 168 lines — small in bytes, and the whole difference between a
constraint and a piece of context ([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# Two decision shapes recur and fit none of the three values — 2026-08-29

**A RATIFICATION signs off something already being practised.** The ask-before-weakening rule and the
style rule were both ratified on 2026-08-23; neither creates a constraint, both confirm one that was
already running. Under the three values a ratification reads as a `prohibition` indistinguishable from
a new one, which loses the fact that nothing changed.

**A REPEAL's product is the deletion of a rule rather than its creation.** The `authority.md` step of
2026-08-29 is one; **the shape occurred twice in nine days.** A repeal marked `prohibition` reads to
`/pre-task` as a constraint, which is the opposite of what it is
([[a-rules-page-leaves-only-on-a-decision-and-a-deprecated-mark]]).

**Neither is proposed as a new value here.** The census is the thing that would say whether two more
values earn their place, and it comes before the type system is redesigned
([[the-decisions-folder-is-censused-before-its-type-system-is-redesigned]]).

**And a repeal has a window in which every check is green on a false page** — between the ruling and
the librarian performing the supersession, the repealed page is `current`, the gate asks for a
successor only on `deprecated`, and the archiver's refusal fires only at move time. **That window was
open for hours on 2026-08-29.**

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
