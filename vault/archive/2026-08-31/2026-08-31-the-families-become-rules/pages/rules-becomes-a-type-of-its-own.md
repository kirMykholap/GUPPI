---
title: "`rules` becomes a type of its own, and a script injects each rule where it governs"
type: decision
status: archived
authority: rules-type
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
tags: [vault, process]
---

# Decided 2026-08-16, scheduled for S2

**A rule becomes a page of its own type in the wiki**, beside `decision`, `concept`, `entity`,
`lesson` and `proposal`. Today a rule that must be obeyed before anyone would think to ask is
excluded from the vault by construction — the vault's `CLAUDE.md` says so under *what does not
belong here* — so those rules live only in a `CLAUDE.md`, which is the one place here that goes
stale with nothing noticing ([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**And a script injects each rule into the zone of the project it governs**, the way Claude's own
per-directory `CLAUDE.md` mechanism works: the rule is written once as a page and delivered where
the work happens, instead of being copied into a file that then drifts.

**Scheduled for S2.** Nothing of it exists yet — no type, no folder, no injector — and this page
records the decision, not a state of the store.

## What it obliges

- The type set grows, so `vault-check.sh` rule 4 (folder against `type:`), the selftest fixtures
  and the catalogue all have to learn it. Adding a rule over every page is what makes the selftest
  fragile, and the fix belongs in the harness ([[a-rule-over-every-page-makes-every-test-fragile]]).
- **The four rules in the repository's `CLAUDE.md` are the first migrants**
  ([[the-repository-claude-md-becomes-a-dispatch-table]]). Their defining property is that obeying
  them late is the same as not obeying them at all, so the injector has to put them where they are
  read *before* the work, not where they are found by searching.
- The count of folders and the count of rules in `CLAUDE.md` both change, which is why two of the
  eight non-compliant titles are expected to be rewritten by this same work
  ([[a-title-names-what-is-counted-instead-of-counting-it]]).

## Two of its open questions answered, 2026-08-16 (second session)

**`rules` is a sixth folder in `wiki/`**, not a type inside an existing one — which was the first
of the four questions blocking S2. The design that needs it is
[[the-harness-is-compiled-not-maintained]], and the mechanism that renders a rule into the file it
governs is [[the-harness-is-built-by-a-script-and-guarded-by-a-gate]].

**A rule page carries `governs:`, never `authority:`.** A rule issues an instruction rather than
answering a question, and sharing a slug with the decision behind it would make rule 3 of
`vault-check.sh` print a contradiction on every normal decision-and-rule pair. `asserts:` is
optional beside it — `governs` keeps the harness *saying* what the vault holds, `asserts` keeps the
tree *being* what the rule claims
([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]]).

**The admission test is written down:** a paragraph becomes a rule page **if it is imperative and
not enforced by a test**; where a test holds the rule, the test is the rule.

Still nothing exists — no folder, no type, no injector
([[what-the-harness-build-waits-on]]).

## Built on 2026-08-17, and one correction to the text above

**`wiki/rules/` exists**, rule 1 of `vault-check.sh` requires it, the frontmatter pass reads
`governs:` and refuses `authority:` on a rule page, and `scripts/vault-inject.sh` renders each
current rule into the region it governs ([[the-folder-set-is-closed-and-tasks-is-not-in-it]],
[[a-region-is-a-paired-comment-named-for-a-rule]]). **No rule page has been written yet**; the first
migration is the next session's work, and it is ordered behind the fifth verdict
([[a-region-is-checked-against-its-rules-governs]]).

Two things this page left open are now decided: **what travels is a marked slice and not the body**
([[what-travels-from-a-rule-page-is-a-marked-slice]]), and **`governs:` is a path from the
repository root** ([[governs-is-a-path-from-the-repository-root]]). `asserts:` is still unbuilt, so
the second half of the pair this page describes does not exist.

**Correction, 2026-08-17.** The line above reading *"`vault-check.sh` rule 4 (folder against
`type:`)"* names the wrong rule: the script's **rule 2** compares the folder against `type:`, and
its **rule 4** is the link rule. The sentence is left standing and the numbers are corrected here,
because the corpus cites these rules by number and repointing a citation silently is the failure
that decision was written against ([[a-retired-rule-number-is-never-reused]]). *The catalogue this
line also names no longer exists* ([[the-page-list-is-a-query-not-a-generated-file]]).

> [!CAUTION] CONTRADICTION
> **"The four rules in the repository's `CLAUDE.md` are the first migrants" collides with the
> uniqueness of `governs:`.** The schema and rule 3b of `vault-check.sh` allow one current rule per
> destination ([[a-deprecated-rule-does-not-render]]); those rules share one destination. Three of
> them became pages on 2026-08-17 and the gate now prints *two current rules govern the same
> destination: `CLAUDE.md`*, while `scripts/vault-inject.sh` renders all four into that file
> without complaint — measured. Marked on both pages. Unresolved; the measurement and the two ways
> out are on that page, and the choice is the owner's.

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

## Executed 2026-08-17, and the sentence "no rule page has been written yet" is now false

**Nine rule pages exist and every one of them renders.** The section above reads *"No rule page has been
written yet; the first migration is the next session's work"* — that was true when it was written and
stopped being true the same day, in the session that followed
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).

**The four rules this page named as the first migrants all migrated**, and five more blocks of the same
file followed them: the `## Language` body, the `/pre-task` trigger, the rule about weakening a rule, the
closing ritual, and the feedback line. **The numbered list was never the whole of what that file
instructs**, which is what the second batch established.

**The prediction in *What it obliges* about counts was right and was paid.** The count of folders, the
count of rules in `CLAUDE.md` and the count of scripts all moved, and the heading over the rules stopped
counting altogether rather than being updated
([[a-rule-leaves-the-numbered-list-and-carries-no-ordinal]]).

**The uniqueness that this page's marked contradiction was about is gone from the check**, and the
decision has a page of its own now ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**`asserts:` is still unbuilt**, so the second half of the pair this page describes still does not exist,
and `governs:` is about to widen beyond this folder
([[governs-becomes-a-property-of-any-page]]).
