---
title: "The cleanup suspends the rules that would refuse it, and says so in one place"
type: decision
status: current
authority: cleanup-rule-suspension
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: repeal
target: [a-decisions-archival-condition-is-read-off-its-binding, the-decisions-folder-is-censused-before-its-type-system-is-redesigned, what-travels-from-a-rule-page-is-a-marked-slice, every-rule-in-wiki-rules-owes-a-mechanical-instrument]
sources: ["[[a-decisions-archival-condition-is-read-off-its-binding]]", "[[the-decisions-folder-is-censused-before-its-type-system-is-redesigned]]", "[[what-travels-from-a-rule-page-is-a-marked-slice]]", "[[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]", "job_hunt_ai_vault/authority.md"]
tags: [vault, process, record-schema]
---

# Context

**`wiki/decisions/` holds 320 live pages and 282 of them carry `binding: prohibition`.** They are
about this store rather than about the product: of 597 live pages in `wiki/`, forty carry a product
tag. The owner opened the session of 2026-08-30 saying most of the folder is not needed and that
reading the corpus costs the session its budget.

**The mechanism he ruled on that day** is that a prohibition family becomes one page in `wiki/rules/`
carrying the family's `authority:` slug, and a hook serves that page when a file it governs is
touched. The 282 prohibitions sit in **53 of the 63 families `job_hunt_ai_vault/authority.md`
already groups**, every slug registered, the largest family holding fourteen.

**Four live rules refuse that mechanism**, and each was taken by the owner on a ground that reads
correctly where it stands:

- [[a-decisions-archival-condition-is-read-off-its-binding]] — a `prohibition` does not leave
  `wiki/` while it stands, because `/pre-task` does not read `archive/`, so a constraint moved there
  stops reaching the reader it exists for.
- [[the-decisions-folder-is-censused-before-its-type-system-is-redesigned]] — the folder's state is
  established by a census before anything about its type system changes. That census is the second
  mode of the decisions agent and **has never run**.
- [[what-travels-from-a-rule-page-is-a-marked-slice]] — a live rule page with no marked slice is
  red, and, with [[governs-is-a-property-of-wiki-rules-alone]], naming a destination is what makes a
  page a rule at all.
- [[every-rule-in-wiki-rules-owes-a-mechanical-instrument]] — each rule gets an instrument or a page
  saying why it cannot.

**Files this touches:** `job_hunt_ai_vault/wiki/rules/_schema.yaml`,
`job_hunt_ai_vault/wiki/decisions/_schema.yaml`, `scripts/vault-check.sh`,
`scripts/vault-archive.sh`, `.claude/hooks/serve-the-rule.ps1`, `.claude/settings.json`.

# The question

Are the four lifted one at a time, each with its own decision, or once, by this page.

# How it works after

**The four no longer stand, and this page is where a reader learns that.** They stay in `wiki/` as
the carriers of what was decided and why; nothing about them is deleted or superseded, because a
repeal is not a supersession and this store ruled that on 2026-08-30.

**What becomes legal.** A prohibition may leave `wiki/decisions/` for `archive/` once the family
rule carrying its clause exists. A page in `wiki/rules/` may carry `authority:` and no `governs:`
and no marked slice, under `render: authority`, and is delivered by a hook rather than by injection.
The rule pages written for the 53 families are instrumented by that one hook rather than by a
selftest case each. And the folder's type system changes without the census having run.

**What stays exactly as it was.** A decision carrying `target_kind: repeal` never leaves
`wiki/decisions/`, and `scripts/vault-archive.sh` refuses it absolutely — **so this page itself
never leaves.** The thirty-six pages carrying `binding: deferral` are untouched by all of the above
and stay where they are. `decided_by:` stays legal in `wiki/proposals/` and `wiki/rules/` and
nowhere else.

**The target this decision is discharged by** is the harness change itself: the schema and gate
edits that admit `render: authority`, and `.claude/hooks/serve-the-rule.ps1`, which is what replaces
the delivery the first of the four was protecting. Until that hook exists, lifting the first rule
leaves 282 prohibitions with no reader at all — **so the hook is built before any decision is
archived**, and that ordering is part of this ruling rather than advice beside it.

**`target:` is written here as an inline list of plain slugs**, because a repeal cancels four things
and one field naming one of them would be false. No verdict reads it: rule 17 resolves `target:` for
`rule` and `proposal` kinds alone, and the archiver reads only `target_kind:`. Named here so a later
instrument that starts reading it knows what it will find.

# Recommendation

**One decision rather than four.** All four fall to the same argument — a prohibition sent to
`archive/` stopped reaching its reader, and that is now false, because the hook delivers the rule at
the moment a governed file is touched, which `wiki/decisions/` never did for any reader at any time.
One argument is one decision; four pages each citing the same ground would be four copies of it, and
this store repairs a drifting copy by deleting it rather than by keeping it in step.

**Rejected: lifting them one at a time.** It costs four ratifications for one judgement, and three
of the four had already been given in the same conversation. Its only advantage — that a later
reader can find each lift beside the rule it lifts — is answered by `target:` naming all four here.

# Ratification

**owner, 2026-08-30: «хорошо, ратифицирую все эти 4 пункта одним решением».** Given against the
session's own list of the four, put to him in prose in chat, after he had ruled on each of the
mechanism's parts separately over the preceding exchanges.

# Four things this page did not carry, added at the ingest — 2026-08-30

**The four lifted pages now name this one, and none of them did.** A reader who greps
`binding: prohibition` and lands on any of the four learned nothing about the lift, because the link
ran one way only. Each now carries a dated section naming this decision, the date and the scope, and
each stays `current` — a repeal is not a supersession and none of them is `deprecated` or
`superseded_by:` anything.

**The title says *suspends* and the body says the four "no longer stand", and nothing states an end.**
No expiry, no restoration condition, and *What becomes legal* reads as permanent. **That difference is
left standing rather than resolved here**, because whether the lift is for the duration of the cleanup
or for good is the owner's word and he gave one sentence covering both readings. It is raised in the
brief.

**Its own precondition is not met.** This page rules that *"the hook is built before any decision is
archived"*, because lifting the first of the four leaves 282 prohibitions with no reader at all. The
hook exists and **the delivery does not**: `.claude/hooks/serve-the-rule.ps1` has no `authority:`
matching branch, and its path silence excludes every file under `wiki/`
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]],
[[the-rule-server-hook]]). **So nothing may be archived under this ruling yet, on the ruling's own
terms.**

**One of the four is an acceptance criterion of an open sprint.**
[[every-rule-in-wiki-rules-owes-a-mechanical-instrument]] is S3's criterion 1, and suspending it
changes what that criterion is decided by while S3 is open. Neither this page nor `sprint.md` said so;
both now do, and **whether the criterion is met is still the owner's to read**.

**And a fifth rule was checked and does not need lifting.**
[[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]] refuses a page carrying *two* text
slices; a family rule carries none, which that verdict does not object to. Named here so its absence
from the list of four reads as a check rather than as an omission.

# The lift ends four different ways, and this is the end the page above said it did not state — 2026-08-31

**The section above says the difference between *suspends* and *no longer stand* is "left standing
rather than resolved here, because whether the lift is for the duration of the cleanup or for good is
the owner's word". He gave it.** The four are not one thing and they do not end together.

**owner selected, 2026-08-31: «окей, согласен».** Put to him as four separate recommendations, one per
rule, rather than as a single verdict on the set.

| the lifted rule | what became of it |
|---|---|
| [[what-travels-from-a-rule-page-is-a-marked-slice]] | **narrowed permanently** |
| [[a-decisions-archival-condition-is-read-off-its-binding]] | **narrowed permanently** |
| [[every-rule-in-wiki-rules-owes-a-mechanical-instrument]] | **lifted until S3 closes** |
| [[the-decisions-folder-is-censused-before-its-type-system-is-redesigned]] | **discharged, not deleted** |

**The two narrowings are permanent because the thing each protected stopped existing in that case.** A
`render: authority` rule carries no slice **by construction** — it renders into no file, so there is
nothing to mark and no drift to detect. And a prohibition discharged into a rule now leaves by the
ordinary path, because the reader it was being kept in `wiki/` for is now served by the hook at the
moment a page carrying its slug is read. Neither narrowing releases anything else: outside those two
cases both rules stand exactly as written.

**The instrument obligation stays lifted until S3 closes, and reading criterion 1 is his.** It is that
sprint's first acceptance criterion and this page's suspension of it changes what the criterion is
decided by while the sprint is open. Nothing here reads it.

**The census is discharged rather than deleted, and he offered to delete it.** «может просто уберем
ее?» — and he took the recommendation against, because that page is the only record of why the cleanup
table was built at all. What discharges it: the table is the reading it asked for, and
`docs/vault-cleanup-verdicts.md` supplies the half the table lacked — which member of a group is in
force.

## Two paragraphs above this line went false on the day the sweep ran, and they are dated rather than struck

**"They stay in `wiki/` as the carriers of what was decided and why"** — three of the four are now in
`archive/2026-08-31/2026-08-31-the-families-become-rules/pages/`. Only
[[every-rule-in-wiki-rules-owes-a-mechanical-instrument]] is still in `wiki/decisions/`. Their claims
survive as clauses on the family rules and their reasoning is one wikilink deeper, which is the
arrangement rather than a loss ([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]).

**"Nothing may be archived under this ruling yet, on the ruling's own terms"** — that precondition was
met on 2026-08-31. `.claude/hooks/serve-the-rule.ps1` gained the `authority:` branch, was registered on
`Read`, and delivers; 129 decisions moved after it did, and not before
([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]]).

## What a reader of the two narrowed rules is told, and where

**Both narrowings have to be written onto the clauses that carry them**, because the decisions
themselves have left. [[a-rule-page-and-the-slice-that-travels]] carries the marked-slice clause and
[[draining-a-folder-into-the-archive]] carries the archival-condition clause, and both were written
unnarrowed. Each now says what the narrowing is, on the same line as the clause.

*(Added at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
