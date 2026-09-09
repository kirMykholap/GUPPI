---
title: "`wiki/rules/` holds the rules of the repository's `CLAUDE.md`, and from 2026-08-20 one page in it governs `.claude/rules/ast-boundaries.md` instead"
type: entity
status: current
authority: rules-folder-inventory
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md", "scripts/vault-inject.sh"]
tags: [harness, vault]
---

# What is in the folder, measured 2026-08-17 at `814472a`

`ls job_hunt_ai_vault/wiki/rules/` → **nine pages**, all `governs: CLAUDE.md`, all `basis: human`,
all carrying exactly one `<!-- text -->` slice and no `authority:`. The folder went from **zero to
nine in one day**, in two batches — four, then five — neither of them compiled from a journal: the
owner decided each migration in session and the librarian wrote the pages inside it.

**The count is written with its date because it is the world's and not this page's**: every rule
that migrates out of a harness file lands here, and the figure moves without this page being
touched ([[a-stated-count-drifts-from-the-list-it-heads]]).

| Batch | Pages |
|---|---|
| first, at `e81a6e4` and `e478c19` | [[the-owner-decides-how-a-slice-is-executed]], [[the-suite-never-runs-against-the-production-database]], [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]], [[our-javascript-does-not-choose-which-rows-are-on-screen]] |
| second, at `bdab5c9` | [[english-in-the-repository-russian-with-the-owner]], [[a-pre-task-runs-before-anything-non-trivial]], [[ask-before-weakening-or-working-around-a-rule]], [[a-session-ends-with-retro-then-handoff-then-ingest]], [[write-the-miss-into-vault-feedback-before-the-turn-ends]] |

**Nothing of the numbered list survived as a number.** Three rules still stand in the list in that
file and the fourth left it for a block of its own, because a marker has to stand alone at column
zero and an ordinal shipped into the wiki would drift as the remaining rules migrated
([[a-rule-leaves-the-numbered-list-and-carries-no-ordinal]]).

## The property that matters, and what it cost

**Every page in the folder governs the same destination** — true until 2026-08-20, when the AST
rule left for `.claude/rules/ast-boundaries.md` (last section). That is the fact that met
`vault-check.sh` first and lost: the check forbade two current rules from naming one destination,
which stopped the migration at its second page. The rule was removed by the owner rather than the
migration abandoned ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

`harness` selects nine pages inside this folder, which is under the per-folder ceiling of ten, so
no density advisory names it ([[the-folder-is-the-first-narrowing]]).

## What a reader of this folder should not conclude

**Being a page is not being rendered**, and the two are separately checkable: the page is here, the
region is in `CLAUDE.md`, and `scripts/vault-inject.sh` is what makes them equal
([[a-region-is-a-paired-comment-named-for-a-rule]], [[a-check-asks-by-running-the-writer-it-checks]]).
All nine agree with their regions at `814472a` — `bash scripts/vault-inject.sh --check` reports
every rule in step.

**And the folder is not the whole of what instructs an agent.** Twelve of thirteen governed files
carry no region at all ([[a-governed-file-with-no-region-is-an-advisory]]), and two blocks of
`CLAUDE.md` itself are still hand-written prose for reasons that are recorded rather than accidental
([[the-repository-claude-md-after-the-rules-left-it]]).

The decision that this folder exists is [[rules-becomes-a-type-of-its-own]]; what travels off a page
in it is [[what-travels-from-a-rule-page-is-a-marked-slice]]; the admission test a paragraph has to
pass to become one of these pages is on [[the-harness-is-compiled-not-maintained]].

# The title goes false the day the AST rule moves — flagged 2026-08-18, not yet

**This page's title says each of these rules governs *that one file*.** That holds today and stops
holding the moment `an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test` moves to
`.claude/rules/ast-boundaries.md` with a `paths:` scope
([[moving-a-rule-into-claude-rules-with-a-paths-scope]],
[[a-rule-moving-to-conditional-delivery-needs-its-page-first]]).

**When it happens the title is corrected in place, not superseded** — the claim about the folder
changes, the address does not, and nothing is stranded
([[a-title-corrected-in-place-is-not-a-supersession]]).

# The folder is not the only place a rendered record lives, from 2026-08-18

**A page in any folder may carry `governs:`** ([[governs-becomes-a-property-of-any-page]]), and the
first one that does is a `concepts/` page
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]). So *the rules of
`CLAUDE.md`* and *the records rendered into `CLAUDE.md`* stopped being the same set: ten regions,
nine of them rules.

**Every marker in this file's regions is still `rule:`**, and none needed rewriting when the type
word arrived — the singular was already the form in use
([[the-marker-carries-the-records-type]]).

# It happened, and the title is corrected in place — 2026-08-20

**[[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]] now carries
`governs: .claude/rules/ast-boundaries.md`, `render: whole` and a `paths:` scope of
`tests/unit/*boundar*.py`.** The flag above is spent: a page in this folder governs a file that is
not `CLAUDE.md`, and the move went ahead on the owner's ground with the guard in front of it
([[the-ast-rule-moves-to-prove-the-mechanism]],
[[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]).

**This page's `title:` read *"...holds every rule of the repository's `CLAUDE.md`, and each of them
governs that one file"* until this date.** It now names the page that governs elsewhere. **Corrected
in place and not superseded**, exactly as the flag promised: the claim about the folder changed, the
address did not, and nothing is stranded ([[a-title-corrected-in-place-is-not-a-supersession]]). The
filename underneath is left as it was — a rename moves every inbound link and is a scheduled sweep,
not something a session does inside another change
([[a-title-names-what-is-counted-instead-of-counting-it]]).

**What in the body is dated rather than false.** The table and the folder reading are both taken at
`814472a` and stand as the reading of that day
([[a-stated-count-drifts-from-the-list-it-heads]]). The claim that met `vault-check.sh` is annotated
where it sits rather than removed, because the paragraph it supports — that destination uniqueness
was taken out of the check instead of the migration being abandoned — is unaffected by the move and
is the reason there was nothing to fight today
([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**And the destination is not this page's to assert.** `.claude/rules/ast-boundaries.md` is generated
whole by `scripts/vault-inject.sh` from the rule page's slice and its `paths:`, and it is the
session's to run in the same change as the removal of the region from `CLAUDE.md`
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
[[paths-lives-on-the-vault-page-and-is-written-widest]]). **Being a page is still not being
rendered**, which is what the section above says and what the gate reports while the halves are
apart.

# The destination exists now — 2026-08-20

**The last section says the destination is not this page's to assert and is the session's to
generate. It was generated.** `.claude/rules/ast-boundaries.md` stands on disk, written whole by
`scripts/vault-inject.sh` from the rule page's slice and its `paths:`, and the region left
`CLAUDE.md` in the same change ([[the-generated-ast-boundaries-rule-file]],
[[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]]).

**So *being a page is not being rendered* is satisfied on both halves for all nine.**
`bash scripts/vault-inject.sh --check` reports every rule in step, and `bash scripts/vault-check.sh`
exits 0.

**What this changes about the folder as a whole:** eight of its pages render into `CLAUDE.md` and one
generates a file of its own, so the folder now holds two delivery modes and the field that
distinguishes them is required on every page in it
([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]],
[[the-whole-mode-owns-a-file-end-to-end]]).

# The folder gained a rule and lost one, on the same day — 2026-08-20, third session

**Its size and its shape both moved**, and the paragraph above about *eight render into `CLAUDE.md`
and one generates a file of its own* is a reading of that morning:

- **[[a-pre-task-runs-before-anything-non-trivial]] is retired to `archive/`**, superseded by
  [[a-pre-task-runs-between-the-plan-and-its-approval]], which governs
  `.claude/hooks/messages/pre-task.md` under `render: whole`. **So `whole` is no longer a synonym
  for `.claude/rules/`**: it is a file the injector owns end to end, wherever that file lives, and
  the `paths:` requirement keys on the destination rather than on the mode
  ([[paths-is-required-where-it-is-read-and-nowhere-else]]).
- **[[dispatch-librarians-in-parallel-only-for-reading]] joined**, `governs: CLAUDE.md`,
  `render: region`, carrying a sentence that had existed on a `lessons/` page since 2026-08-14 and
  was delivered nowhere ([[parallel-librarians-break-the-one-writer-property]]).

**A rule leaving that file and another entering it on one day is one criterion applied twice**, and
the record says so rather than leaving the coincidence to be interpreted
([[a-rule-applied-in-opposite-directions-on-one-day-is-not-a-reversal]],
[[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]).

**The count is not patched anywhere else on this page.** A figure that drifts is dated where it
stands ([[the-region-coverage-figure-is-dated-where-it-stands]]); what is read off the tree is
`bash scripts/vault-check.sh` and `bash scripts/vault-inject.sh --check`, both of which were green
at the ingest that wrote this section.

# The folder is the only place a rendered record lives again — 2026-08-21

**The section headed *The folder is not the only place a rendered record lives* is false from this
date, and it is left standing as the state between 2026-08-18 and 2026-08-21.** Its opening
sentence — *"A page in any folder may carry `governs:`"* — was the ruling of 2026-08-17, and the
owner overturned it at the retro of 2026-08-21: `governs:` is a property of `wiki/rules/` alone,
because a page that renders its text into another file **is** a rule
([[governs-is-a-property-of-wiki-rules-alone]]).

**So *the rules of `CLAUDE.md`* and *the records rendered into `CLAUDE.md`* are one set again**, and
the clause *"ten regions, nine of them rules"* is spent along with the sentence above it. The two
pages that were the exception moved into this folder the same day, `type: concept` becoming
`type: rule` and nothing else in their frontmatter changing
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]).

**The move changes the type word in each region's marker, which is derived from the folder**: the
two pairs in the repository's `CLAUDE.md` are `<!-- concept: … -->` until the session rewrites them
as `<!-- rule: … -->` ([[the-marker-carries-the-records-type]],
[[a-marker-with-its-type-is-a-complete-address]]). Until then the injector reports that `CLAUDE.md`
carries no region for either page ([[a-check-asks-by-running-the-writer-it-checks]]).

**What this page's title still says is still true**, and that is worth stating rather than assuming:
the folder holds the rules of the repository's `CLAUDE.md`, and one page in it governs
`.claude/rules/ast-boundaries.md` instead. Two more pages governing `CLAUDE.md` does not falsify
either half. **What the title does not say, and now under-describes, is the folder's contents**: it
holds an imperative, a definition and a map, admitted on delivery rather than on grammatical mood.

**No count on this page is patched.** The readings above are each dated where they stand, and what
is read off the tree is `bash scripts/vault-check.sh` and `bash scripts/vault-inject.sh --check`
([[the-region-coverage-figure-is-dated-where-it-stands]]).

# One sentence here is not a dated reading but a live claim, and it is false — 2026-08-26

**The section headed *The property that matters* ends with:** *"`harness` selects nine pages inside
this folder, which is under the per-folder ceiling of ten, so no density advisory names it."* **That
is a claim about what the gate prints, not a reading of a past day, and it stopped holding.**

**Measured 2026-08-26 over `wiki/rules/`: sixteen pages, and `harness` is on fifteen of them.** The
per-folder tag ceiling is ten, so the advisory does name this folder — the one consequence the
sentence asserted would not happen ([[the-folder-is-the-first-narrowing]],
[[the-tag-density-advisories-move-behind-lint]]).

**The rest of the same reading has moved with it, and none of it is patched above.** `governs:` now
takes three values that are not `CLAUDE.md` — `.claude/rules/ast-boundaries.md`,
`.claude/hooks/messages/pre-task.md` and `.claude/agents/vault-librarian.md` — and three pages carry
a **list** rather than a single destination, which the field's own syntax page allows
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]). `render:` reads
fourteen `region` and two `whole`.

**The title still holds and still under-describes.** *One page governs `.claude/rules/ast-boundaries.md`
instead* is true and is no longer the only departure; the title names the first one because it was
the first, and correcting it in place would be a third rewrite of the same sentence rather than an
answer ([[a-title-corrected-in-place-is-not-a-supersession]]).

**And the folder is decided to lose a page that has not left.**
[[our-javascript-does-not-choose-which-rows-are-on-screen]] becomes a `decisions/` page with
`binding: prohibition`, losing `governs:` and `render:` and minting an `authority:`; the move is an
open sprint line ([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]]). **Until it
happens the table above is right about where that page lives.**

# The folder is about to change shape, and what it holds today is the last reading of the old one — 2026-08-30

**The addresses, read whole: seventeen live rules render into eleven files, and eleven of the
seventeen render into the repository's `CLAUDE.md`.** That is the complete list of places a rule's
text can arrive today, and **every one of the eleven files is markdown while `CLAUDE.md` has no
frontmatter at all** — which is why a lookup keyed on a page's `authority:` could never address the
file eleven rules go to, and why the rule server needs a matcher by path as well
([[the-rule-server-hook]]).

**`render:` reads `region` on fifteen and `whole` on two.** A session had told the owner it carried one
value; that was wrong and is corrected here.

**Sixteen of the seventeen name a decision in `decided_by:` that is now in `archive/`** — the sweep of
2026-08-29 took it. One names a live decision and was created on 2026-08-30. **That does not say
archiving decisions is safe in general; it says it has already been done to 66 of them, the rules
still render, and the gate is green.**

**What arrives next is up to 53 more pages, under a mode this folder has never held.** A rule under
`render: authority` carries a slug and no `governs:`, is written into no file, and is found by a
lookup ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]],
[[the-prohibition-families-become-rule-pages-served-by-a-hook]]). **Their `authority.md` rows land in
the same pass or the gate locks out the only party who may write them**
([[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]]).

**The estimate is an upper bound and is recorded as one**: `rules/` 17 → up to 70, `decisions/` 321 →
about ten, the corpus down by roughly 250. It assumes every family produces a rule, which the
dead-family verdict is exactly what does not assume.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
