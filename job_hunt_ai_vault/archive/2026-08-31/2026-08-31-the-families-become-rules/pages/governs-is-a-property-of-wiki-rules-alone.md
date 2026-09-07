---
title: "`governs:` is a property of `wiki/rules/` alone, and a page that renders is a rule"
type: decision
status: archived
authority: governs-scope
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["wiki/rules/_schema.yaml", "wiki/concepts/_schema.yaml", "scripts/vault-inject.sh", "CLAUDE.md"]
tags: [harness, record-schema, vault]
supersedes: [[governs-becomes-a-property-of-any-page]]
---

# Decided by the owner on 2026-08-21, at the retro, and it overturns his own ruling of 2026-08-17

> **owner:** *"Странная формулировка governs у concepts. Если у концепта появляется governs — Он
> становится правилом. Поэтому authority = required в concepts. А governs из concepts уходит."*

**`governs:` may be carried by a page in `wiki/rules/` and by no other page.** The field names the
file a page's marked slice is rendered into, and naming one is what makes a page a rule. The folder
is not a filing preference that a renderable record may opt out of.

**The argument is the folder set's own definition, read the other way round.** `wiki/rules/` is
*the one category whose text is written to be rendered somewhere else* — every other category is
read by a reader who came looking, while a rule reaches the file it governs whether anyone came
looking or not. A page that renders therefore satisfies the definition of the folder by carrying
the field, and a concept carrying `governs:` was a rule filed under the wrong kind
([[rules-becomes-a-type-of-its-own]], [[what-travels-from-a-rule-page-is-a-marked-slice]]).

**It closes the shape by removing the field rather than by ruling on it.** The question *may a page
outside `wiki/rules/` own a question and also render* has been answered three times from three
sides — unruled, then forbidden, then required-unless
([[authority-beside-governs-is-forbidden-on-any-page]],
[[authority-becomes-the-index-and-is-required-outside-rules]]). With `governs:` confined to one
folder the condition has nothing left to range over: `authority:` is required everywhere outside
`wiki/rules/` and forbidden inside it, with no third case.

# What the overturned decision was right about, and what it was wrong about

**It was taken to solve a real problem and it solved it.** On 2026-08-17 the owner had just ruled
that a *sourced* assertion may render into the repository's `CLAUDE.md`
([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]), and a **definition** joined it
on 2026-08-18 ([[a-definition-may-render-into-the-repository-claude-md]]). Neither is an imperative,
and under the mechanism of that week neither had anywhere to render from. Two alternatives were
weighed and both were refused on tests the project already had: a seventh folder, against the closed
folder set ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]), and admitting a description to
`wiki/rules/`, against that folder's admission test as it was then stated — *imperative and not
enforced by a test* ([[the-harness-is-compiled-not-maintained]]).

**Its mechanical half is untouched and is what makes the correction cheap.** The injector still
walks `wiki/*/*.md` pre-filtered on `^governs:`, still takes the destination from the field, and the
marker still carries the record's type rather than the word `rule`
([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]],
[[the-marker-carries-the-records-type]]). None of that is reversed here. What is reversed is **who
is allowed to carry the field**, which was never a property the code enforced.

**What it was wrong about is the admission test it argued from.** It read `wiki/rules/` as the
folder of imperatives and concluded that a non-imperative admitted there would empty the test. The
owner's ruling replaces the test with one about delivery rather than mood: a page that renders is a
rule. Under the old test the folder's meaning was protected and the *type word* went wrong; under
the new one the type word is right and the folder holds three moods.

**Its own consequence is what the owner is correcting.** The decision produced exactly two pages
outside `wiki/rules/` that carried `governs:`, and both were rules in everything but their folder —
each with one `<!-- text -->` slice, each governing `CLAUDE.md`, each declining `authority:` because
it would have collided with the decision it stated, and each arguing at length on its own page for
why it was not a rule ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]). A category that needs a section of
prose per member explaining why the member is not what it looks like is the wrong category.

# What it obliges

- **The two `concepts/` pages carrying `governs:` move into `wiki/rules/` and change `type:` to
  `rule`.** Done on 2026-08-21. It is a folder move and not a rename: link resolution is by
  filename anywhere under `wiki/` or `archive/`, so no inbound link moves and the rewriter-and-detector
  pair a rename needs is not in play ([[a-title-corrected-in-place-is-not-a-supersession]]).
- **The marker type word in each region changes with the folder.** `scripts/vault-inject.sh` derives
  it from the folder the page sits in, so `<!-- concept: … -->` in the repository's `CLAUDE.md`
  becomes `<!-- rule: … -->` for both pages. Until that is written the injector reports that
  `CLAUDE.md` carries no region for them and rule 12 is red — the expected state of a half-finished
  move, not a defect in the pages ([[a-check-asks-by-running-the-writer-it-checks]]). **The region
  is the session's to mark and the injector's to fill; the librarian writes `wiki/`**
  ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).
- **`concepts/_schema.yaml` drops `governs:` and `render:` and promotes `authority:` to required.**
  The session's to write, in the same change. With that edit the confinement is mechanical rather
  than remembered: `governs` appears in neither block of the other four folders' schemas already, so
  the gate rejects it there and would then reject it in `concepts/` too
  ([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]], [[the-per-folder-frontmatter-schema]]).
- **`render:` follows `governs:` out of `concepts/`.** It was admitted there only to serve a page
  that renders, and it is meaningless on one that does not
  ([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]],
  [[an-absent-render-is-red-on-a-page-that-renders]], [[the-legal-value-list-lives-in-each-folders-schema]]).
- **Two pages in the corpus assert the opposite and are corrected in place**, not superseded:
  [[wiki-rules-holds-the-rules-of-the-repository-claude-md]] and
  [[the-per-folder-frontmatter-schema]]. The claim about the tree changed; neither address moved.

# What it does not decide

**It does not say what a rule is *for*.** `wiki/rules/` now holds an imperative, a definition and a
map, and the three ruled-renderable shapes are unchanged — the folder admits by delivery, and what
may be delivered into the repository's `CLAUDE.md` is still the owner's list of 2026-08-17 and
2026-08-18 ([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]],
[[a-definition-may-render-into-the-repository-claude-md]]).

**It does not touch the prose of the repository's `CLAUDE.md` outside the regions.** The routes and
the pointers stay hand-written there on the owner's decision
([[the-repository-claude-md-becomes-a-dispatch-table]],
[[the-repository-claude-md-after-the-rules-left-it]]).

**It does not rule on whether the `ruleclaim` verdict is now redundant.** That verdict was widened
in 2026-08-18 to catch `authority:` beside `governs:` on any page, and confining `governs:` to one
folder makes the wide half unreachable rather than wrong
([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]). Whether an unreachable
branch is removed is a question about the check and is not asked here.

**And it does not decide the filenames.** Both moved pages keep the names they had, including the
one whose title still argues from `concepts/`; a rename moves every inbound link and is a scheduled
sweep rather than something done inside another change.
