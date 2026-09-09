---
title: "A deprecated rule does not render, or its successor's file would carry the retired text"
type: concept
status: current
authority: deprecated-rule-rendering
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-inject.sh"]
tags: [harness, vault]
---

# The invariant

`scripts/vault-inject.sh` renders **current** rule pages only. A page with `status: deprecated` is
skipped, and rule 11 requires no region for it.

## Why it is not merely tidiness

A rule is retired by being **superseded**: the successor is written, it takes the same subject, and
in the normal case it governs the same file. If a deprecated rule went on rendering, the injector
would write the **retired text back into the file its successor governs**, and it would do so on
every run, quietly, with the gate green.

Two rules rendering into one region is already one of the conditions rule 11 exists for
([[a-region-is-a-paired-comment-named-for-a-rule]]). A deprecated rule is the version of that
failure where one of the two is invisible, because nobody looks in `archive/` for the cause of a
wrong harness file — the blindness this store has already recorded from the other direction
([[a-live-page-can-argue-from-a-deprecated-one]]).

## The consequence for `governs:`

`governs:` is required to be **unique across current rules** and is not compared against archived
ones. A retired rule keeps its `governs:` line, because that line is part of the record of what it
once governed, and it collides with nothing precisely because it renders nothing
([[governs-is-a-path-from-the-repository-root]]).

> [!CAUTION] CONTRADICTION
> **The uniqueness stated just above and the migration decided on
> [[rules-becomes-a-type-of-its-own]] cannot both hold.** That page says the rules of the
> repository's `CLAUDE.md` are the first migrants; they all govern that one file, so `governs:`
> cannot be unique across them. Marked on both pages. Unresolved — the choice is the owner's.

## The collision, measured 2026-08-17

Three further rule pages were written on the owner's decision, each carrying `governs: CLAUDE.md`
([[the-suite-never-runs-against-the-production-database]],
[[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]],
[[our-javascript-does-not-choose-which-rows-are-on-screen]]), joining
[[the-owner-decides-how-a-slice-is-executed]]. The gate now prints

```
VAULT-CHECK: two current rules govern the same destination: CLAUDE.md
```

**and `scripts/vault-inject.sh` renders all of them without complaint.** Measured in a sandbox copy
of the injector against a destination carrying one region per slug: each rule's text landed in its
own region and the run ended `4 region(s) rewritten, 0 problem(s)`.

**The two ends of the mechanism disagree about what `governs:` names.** The injector keys on the
pair *(file, slug)* and never on the file alone, and rule 11 keys its duplicate verdict the same
way — *one slug marking two regions in one file*
([[a-region-is-a-paired-comment-named-for-a-rule]]). Only the frontmatter check keys on the path.
Its own comment reads *"a region carries the text of exactly one rule, so two rules claiming one
destination is a question with two answers"*: the premise is true and the conclusion does not
follow, because a file carries as many regions as it has rules.

So either `governs:` names a **region**, and the uniqueness belongs on the pair rather than on the
path — or it names a **file that may carry one rule only**, and the migration of the repository's
`CLAUDE.md` rules cannot be done the way it was decided.

**Not resolved here.** `scripts/vault-check.sh` and the vault's schema line are not the librarian's
to write ([[the-steward-is-scripts-that-run-after-the-librarian]], [[the-librarian-writes-unattended]]),
and choosing between two rules is a judgement about the project rather than about the store. The
gate stays red on this line until the owner picks one.

> [!NOTE] RESOLVED BY THE OWNER, 2026-08-17
> **The uniqueness went out of the check, and the migration stands.** At `e478c19` the owner removed
> `governs:` uniqueness from `scripts/vault-check.sh`, on the first day it met a real tree: it was
> stricter than the schema it guarded, which says a rule names the one destination *its own* text
> goes to and says nothing about a destination taking one rule. What it appeared to protect is held
> by verdicts that read the tree instead — one slug marking two regions in one file, and a region
> sitting in a file its rule does not govern — and its selftest case **flipped rather than
> disappearing**: two rules on one file with two regions is now asserted green. The gate no longer
> prints that line. The block above is left standing as the record of the alarm that produced the
> decision, which is the point of marking rather than choosing
> ([[ask-before-weakening-or-working-around-a-rule]]).

## The uniqueness half of this page is retired, and it has a decision of its own — 2026-08-17

**The `governs:` destination-uniqueness verdict no longer exists.** The measurement and the two ways out
that this page carried are now the record of how the decision was reached, and the decision itself is
[[governs-uniqueness-is-removed-and-the-pair-carries-it]]: **removed by the owner, the migration stands,
and uniqueness moved onto the pair of file and slug.**

**What this page states and keeps stating is untouched: a deprecated rule renders nothing.** The address
verdict added the same day depends on it — a region naming a deprecated rule is left alone on purpose, and
widening the join to archived pages would re-open the question closed here
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

## Not rendering is not removing, and under `region` the retired text stays exactly where it is — measured 2026-08-26

**The injector deletes a retired `whole`-mode file and leaves a retired `region`-mode region
standing.** Its own comment states the ground: under `region` the successor rewrites the same region
and the retired text is overwritten, so skipping the page is enough. **That holds only while a
successor renders into the same region**, and it does not hold when a rule is retired into a page
that renders nothing at all.

**Measured on the retirement of [[our-javascript-does-not-choose-which-rows-are-on-screen]] into
[[javascript-policy]].** The page was deprecated, lost `governs:` and `render:`, and moved to
`archive/`. `bash scripts/vault-inject.sh` then reported *0 region(s) rewritten, 0 file(s)
generated, 0 removed, 0 problem(s)* and the paired comment was still at `CLAUDE.md:102`. It could
not have been otherwise: the injector's sweep greps for `^governs:`, so a page that has lost the
field is never walked, and the `whole`-mode removal branch is the only one that deletes anything.

**What catches the leftover is rule 11 of the gate, not the injector.** It reddens with *the region
resolves to `job_hunt_ai_vault/wiki/rules/our-javascript-does-not-choose-which-rows-are-on-screen.md`,
which does not exist — a region with no page behind it renders nothing*
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]). So the failure is loud rather
than silent, which is the difference from the `whole`-mode case this page was written about.

**The repair is a hand edit and it belongs to the session**, because the marker pair and the prose
between it are not something the injector owns once no page governs the file under that slug. The
librarian was ordered to leave `CLAUDE.md` untouched on this retirement and did, and the gate is red
on that one line until the session removes it.

**The region was cut by hand later the same day and the gate is clean of it.** **What would remove it
mechanically is designed and not built**, in three shapes with their costs
([[the-injector-removes-a-region-whose-rule-folded-into-another-page]]). It waits because the failure
is loud: rule 11 names the file, the line and the slug that did not resolve.
