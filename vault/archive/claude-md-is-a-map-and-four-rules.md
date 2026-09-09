---
title: "CLAUDE.md is a map plus the rules that cannot wait; everything else moved into the vault, and no wikilink survived"
type: decision
status: deprecated
authority: claude-md-scope
basis: human
sprint: S0
decided: 2026-08-14
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", "CLAUDE.md"]
tags: [process, vault]
superseded_by: [[the-repository-claude-md-after-the-rules-left-it]]
---

# The rule file is a map, and the vault holds the rest

**Decided by the owner on 2026-08-14**, after an acceptance run made under honest conditions
showed the corpus answering the questions the file was carrying. `CLAUDE.md` went from **218 lines
to 112** — measured on disk after the ingest: **110 lines**, and the journal's own figure of "about
110" is the one to trust over the round number.

**What left, wholesale:** the JavaScript section, the boundary table, the swap-target-invariant
paragraph, all twelve "rules that bite silently", the six bullets of how a slice is executed, most
of the tests section, and the whole environment section.

**Rejected: keeping any of it as a summary alongside the vault.** Nothing is duplicated, and **a
rule that survives the cut has to stand without a footnote**. Two copies of a rule diverge, which
is the failure the vault exists to prevent; a summary is a copy that has already started.

**Obliges:** every removal was checked against the vault before it was made — all nineteen cited
pages existed — and the ingest that follows owes the same comparison in the other direction, block
by block, page by page. The previous shrink (231 lines to 190) dropped the only statement of where
our own JavaScript lives, and the whole-branch review restored it as a **Critical**
([[javascript-policy]], [[handoff-retires-only-when-every-unit-has-a-verdict]]). That is why the
check is a condition of the cut and not a courtesy.

## The test that chose the four rules that stayed

**Obeying them late is the same as not obeying them at all.** That is the whole criterion, and it
explains a list that otherwise looks arbitrary:

| Rule | Why it cannot wait for a question |
|---|---|
| the test database comes from `TEST_DATABASE_URL`; never run the suite against production | the fixture drops and rebuilds schema — there is no second chance ([[the-test-database-is-built-and-truncated-by-its-fixtures]]) |
| an AST boundary test fails: fix the cause, never the test | by the time you ask, the test is already edited ([[architectural-boundaries]]) |
| our own JavaScript may not decide which rows are on screen | asked afterwards, the code is written and the review is a rewrite ([[javascript-policy]]) |
| how a slice is executed is the owner's decision and overrides any skill | **a skill will confidently say otherwise**, so a reader who does not know this never forms the question ([[how-a-slice-is-executed]]) |

The fourth is the sharpest of them: the others are rules you might break in ignorance, that one is
a rule another document will actively argue you out of.

**A fifth item stayed for a different reason** — the test database rule is in the file *because
nothing in the vault described it* when the cut was made. It is now written down, so that entry no
longer depends on the gap.

## No wikilinks in `CLAUDE.md`, on purpose

`[[page]]` is Obsidian syntax. It resolves inside the vault and is **inert outside it**: in
`CLAUDE.md` it reads as a citation the reader cannot follow, and a subagent handed the file has no
way to expand it.

**Obliges: the three routes into the vault must stay in the file** — `/vault-ask`, `/pre-task`, and
the by-hand `rg` recipe over `tags.md` then `wiki/`. They are the replacement for nineteen dead
citations, and removing one of them would leave the shortened file pointing nowhere.

`scripts/vault-check.sh` keeps a rule for the links that used to be there (rule 15: the repository's
`CLAUDE.md` may not name a page that does not exist). With no links left it now passes vacuously —
correct, and worth knowing before someone reads its green as evidence that the pointers are sound
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## One block was not carried, and the check is why we know

**The language section's second paragraph was dropped and no page held it** — *the rule applies to
new work; what predates 2026-08-05 stays Russian; do not mass-translate; do not rename existing
tests*. It had been filed `elsewhere:CLAUDE.md` by the migration of 2026-08-13, so it was accounted
for and homeless at the same time. Recovered into
[[the-language-rule-applies-only-to-new-work]] by the ingest of the same day.

**Corrected on 2026-08-15 by the owner: that paragraph was deleted deliberately.** He said so while withdrawing the clause itself — the new-work boundary was his, added because he did not want to deal with the rest at the time, and it had gone stale ([[english-is-the-rule-and-the-russian-past-is-deferred]], which replaces the page named above). The recovery was still worth making, and the store was still homeless for a day; what is no longer true is reading this instance as an *accident* of the cut. The other instance, the JavaScript one, is untouched by the correction.

**That is the second time a shrink of this file has dropped exactly one thing**, and both were
found by reading the removed text beside the page meant to carry it rather than by any check that
runs. The first cost a Critical at whole-branch review ([[javascript-policy]]); this one cost a
day, and only because the check was made a condition of the cut.

## What the file is now

A description of the project, the language rule, the commands, the four rules, and a map of where
things are — plus the loop: a session ends with `/handoff` then `/ingest`
([[journal-vault-brief-each-artefact-has-one-owner]]), and a wrong answer from the vault is written down in the turn
it is noticed ([[feedback-is-recorded-in-the-turn-it-is-noticed]]).

The corpus's own count of the boundary tests was **right where the file was wrong**, which is the
direction this project had never checked: [[a-stated-count-drifts-from-the-list-it-heads]].

## The owner decided on 2026-08-16 what this file becomes next

**A dispatch table**: *need to know what is decided → call this skill; need to start a slice → call
this agent* ([[the-repository-claude-md-becomes-a-dispatch-table]]). The four rules leave for the
`rules` type ([[rules-becomes-a-type-of-its-own]]), and "where things are" is dropped or generated.

**Nothing of that is done, and this page is not superseded by it.** It describes the file as it
stands on disk; that one describes what it becomes. **Re-admitting wikilinks was rejected** in the
same breath — the owner does not want them there, and a pointer at a skill is checkable exactly as
a pointer at a page is.

# Retired 2026-08-17, by the session that performed the change

**The retirement was owed to *"the session that performs the change"*** and that session was
2026-08-17 ([[the-repository-claude-md-becomes-a-dispatch-table]]). Three of the five things the
section above calls *what the file is now* are no longer true:

| What this page says the file holds | 2026-08-17 |
|---|---|
| the four rules, in a numbered list | **nine rules, rendered from `wiki/rules/`** into nine marked regions ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]) |
| a map of where things are | **deleted**, not corrected ([[where-things-are-is-deleted-now-and-generated-later]]) |
| the language rule | **one rendered region, one page** ([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]) |
| the project description, and the commands | unchanged, and both still hand-written prose |

**The successor is [[the-repository-claude-md-after-the-rules-left-it]]**, which describes the file as
it now stands and carries `authority: claude-md-scope`.

## What is on this page and nowhere else, and is why nothing here was deleted

- **The test that chose which rules belong in that file at all** — *obeying them late is the same as
  not obeying them at all* — with the four-row table saying why each one qualifies. That test is what
  the rule-page admission test was later built on top of, and it is the reason those rules are the ones
  that migrated ([[the-slice-execution-rule-migrates-first]]).
- **Why the file refuses `[[wikilinks]]`**: they resolve inside Obsidian and are inert outside it, so
  in that file they read as a citation nobody can follow.
- **The 218-to-110-line cut, and the two blocks it dropped that no page held.** That is the evidence
  behind S1's criterion 4 and behind [[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]].

**Sixteen `current` pages in `wiki/` cite this one**, counted with `rg -l` immediately after the move and including its own successor and six of the nine rule pages, and none of those
citations is broken — they argue from a page that is now history, which is legitimate and recorded
([[a-live-page-can-argue-from-a-deprecated-one]]). The detector that would list them is still unbuilt
([[a-rewriter-must-be-paired-with-a-detector]]).
