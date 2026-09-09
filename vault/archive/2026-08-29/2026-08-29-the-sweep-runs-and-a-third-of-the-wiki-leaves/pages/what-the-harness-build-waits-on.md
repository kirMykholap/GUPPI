---
title: "What the harness build waits on, each row with what waiting costs"
type: decision
status: archived
authority: harness-deferrals
binding: deferral
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [harness, process, vault]
---

# Deferred 2026-08-16, with the consequence written beside each

A whole session designed the harness as a build ([[the-harness-is-compiled-not-maintained]]) and
**built none of it**. Everything below was raised and put off at one sitting; it is one page because
it is one decision — *not now, and here is what that costs*. The same shape, for the earlier session
of the same day, is [[structure-work-agreed-and-not-executed]].

| Not doing now | What waiting costs |
|---|---|
| **The `asserts:` predicate set** — four sketched, the full set and the rule for growing it not agreed | **nothing downstream can be written**, including the entity pages about the application ([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]], [[entities-describe-the-application-once-the-detector-exists]]) |
| **The `authority` register** — agreed in principle, undesigned: where it lives, who writes it, whether it is generated, what the librarian owes before minting one | the field goes on behaving as a per-page invention ([[an-authority-register-on-the-model-of-the-tag-dictionary]], [[a-field-with-no-register-produces-unique-values-by-default]]) |
| **The handoff template written to disk** — designed, not written | `/ingest` keeps cutting on numbers, and both skills keep their own copies ([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]) |
| **The marked regions themselves** — which regions exist in which files | the harness keeps saying what nothing checks; the markup is gradual and starts with `.claude/skills/ingest/SKILL.md` and the repository's `CLAUDE.md`, **both of which have recorded divergences already** ([[marked-regions-and-the-prose-outside-them]]) |
| **Mechanising the title rule** — S2's criterion 2, open since the rule was written | eight titles carry a measurable quantity and nothing checks it ([[a-title-names-what-is-counted-instead-of-counting-it]]) |
| **A home for ideas** — S2's second blocking question, untouched | an idea is pre-design and `proposals/` holds designs, so an idea still has nowhere to go ([[proposals-are-a-folder-not-a-status]]) |
| **The gates at session start** — parked by the owner as not a priority | routing stays manual ([[session-hooks]]) |
| **Naming the steward** — trivial and open | nothing; it is named here so it is not forgotten ([[the-steward-is-scripts-that-run-after-the-librarian]]) |
| **The proposal status defect** — recorded, not fixed | `deprecated` cannot tell *built* from *refused* ([[the-proposal-status-cannot-tell-built-from-refused]]) |

## The three that block construction, and the order of work

**Three items block building anything**: the template's final form on disk, the `asserts:` predicate
set, and the marked-region rules including which files may be exempt from *no region means red*.

**The agreed order is template first, then the marked-region rules, then the predicates** — because
`/ingest`, the end-of-session ritual and the harness section all depend on the template, and a
number that moves is what made the coupling expensive in the first place.

## Re-read at the end of 2026-08-17: one row discharged, and the register grew

**The template row is done.** `.claude/templates/handoff.md` exists, `/ingest` cuts by heading text,
and both skills read the mapping from the template rather than holding a copy
([[claude-templates-directory]], [[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]).
**Two of the three items that block construction remain, in the agreed order: the marked-region
rules, then the `asserts:` predicate set.** The consequence is unchanged — the harness goes on
saying what nothing checks, and the entity pages about the application cannot be written
([[entities-describe-the-application-once-the-detector-exists]]).

**The title row is done too**: mechanising the title rule was S2's criterion 2 and rule 10 exists
([[the-title-check-asks-and-does-not-judge]]).

**A home for ideas is decided and not built** — `proposals/` with `status: idea`
([[an-idea-is-a-proposal-with-an-immature-status]]). The row's consequence stands until the schema
and rule 2 carry the value.

**Three items joined the register on 2026-08-17**, each deferred with its consequence stated:

| Not doing now | What waiting costs |
|---|---|
| **A `PreToolUse` lock on the librarian dispatch** — designed, blocked on one fact: the exact matcher string for the agent-dispatch tool | the expensive irreversible step can still be spent on a broken input ([[a-lock-on-the-librarian-dispatch]]) |
| **A gate that refuses work without an open sprint** — designed; `SessionStart` cannot do it | nothing stopped a session working a whole day outside a sprint, and nothing would stop the next ([[a-gate-that-refuses-work-without-an-open-sprint]]) |
| **Moving `raw/` into the dated archive** — a slice of its own, re-measured | the cost grows with the corpus: **150 of 165 pages** name `raw/handoffs`, **23 of them in prose** where the detector is blind ([[moving-raw-into-a-dated-archive]]) |

**The whole of this register is vault work, and no product slice interleaves with it**
([[product-work-does-not-interleave-into-the-vault-sprint]]).

## Re-read at the end of 2026-08-17, second session: two rows discharged, three joined

**The marked-region row is done, and the row it named as blocking is dissolved rather than
answered.** Rule 11 and rule 12 exist, `scripts/vault-inject.sh` renders, and `wiki/rules/` is a
folder ([[a-region-is-a-paired-comment-named-for-a-rule]],
[[a-check-asks-by-running-the-writer-it-checks]]). *Which files may be exempt from "no region means
red"* is not on this register any more, because the verdict became an advisory and the question
stopped existing ([[a-governed-file-with-no-region-is-an-advisory]],
[[a-blocker-can-be-dissolved-instead-of-answered]]).

**What is left of that row is its substance**: no file carries a region, and the coverage advisory
reads **`0 of 13`**. The consequence is unchanged and is the whole reason the mechanism was built —
**the harness goes on saying what nothing checks.**

**One of the three items that block construction remains: the `asserts:` predicate set**
([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]]). The entity pages about the application
still cannot be written ([[entities-describe-the-application-once-the-detector-exists]]).

**The first rule migration was agreed and not done.** **owner:** yes to migrating, and then the
closing ritual was chosen over it when both were on the table, on the ground that **code is
recoverable from a record and reasons are not**
([[the-closing-ritual-produces-what-the-journal-cannot-hold]]). A ratified deferral rather than a
thing that slipped.

**Three rows joined the register on 2026-08-17, in the second session:**

| Not doing now | What waiting costs |
|---|---|
| **The fifth verdict of rule 12** — compare each region against its own rule's `governs:` | a region carrying a rule's slug in the wrong governed file is untouched and unremarked; **the first migration is exactly when that can happen**, so this one is ordered *before* it rather than merely queued ([[a-region-is-checked-against-its-rules-governs]]) |
| **The `whole` delivery mode** | `settings.json` and the four `.ps1` hooks stay outside the region mechanism entirely, because neither syntax admits an HTML comment ([[the-governed-set-is-swept-and-markdown-by-property]], [[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]) |
| **Retiring the selftest case «the vault is renamed»** | it is green today and goes red the first time a rule governs a file inside the vault; **it will look like a bug to whoever meets it** ([[governs-is-a-path-from-the-repository-root]]) |

**Also standing, decided and not built:** `render:` is not a field, so the delivery-mode design has
no writer ([[render-was-not-introduced]]).

## Re-read at the end of 2026-08-17, third session: three rows discharged, nine joined

**The fifth verdict is built**, and the row above that names it as *"the fifth verdict of rule 12"* was
wrong about where it would live: rule 12 holds no logic of its own, and the verdict is about a region's
address, so it went into rule 11 ([[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]],
[[a-proposal-can-be-wrong-about-the-hole-it-describes]]).

**The first rule migration is done, and then eight more.** Every rule of the repository's `CLAUDE.md` is
a page in `wiki/rules/` and renders into a marked region
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]). **What is left of that row is the
coverage number**: `1 of 13`, up from `0 of 13`, and the owner's verdict on S2's criterion 6 is
unchanged at **NOT MET** — the criterion asks about files.

**`governs:` uniqueness is off the register in the other direction**: it was not deferred, it was
**removed** ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**One of the three items that block construction still remains: the `asserts:` predicate set**
([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]]).

**Nine rows joined the register on 2026-08-17, in the third session:**

| Not doing now | What waiting costs |
|---|---|
| **The mechanism change** — `governs:` read as a field, `[type]:` markers, a verdict for a type that disagrees with its page, a verdict for a slice with no `governs:` | **three records have nowhere to live** — the project description, the definition of *retrospective*, and the map ([[the-marker-carries-a-type-and-governs-is-read-as-a-field]], [[governs-becomes-a-property-of-any-page]]) |
| **The injector's fenced-block defect** | the by-hand `rg` recipe cannot become a rule and stands as unsourced prose in a section that is otherwise rendered ([[the-injector-drops-a-fenced-block-inside-a-slice]]) |
| **`make`, the map, and a generated `Where things are`** — one generator that fills a region from the tree | `## Commands` is drifting **now**: it says `vault-check.sh` takes `~2 s` and the measured figure is `4.9 s` ([[a-generator-fills-a-marked-region-from-the-tree]], [[a-makefile-holds-the-projects-pipelines]], [[the-map-in-claude-md-and-its-admission-test]]) |
| **The rule forbidding a hand-edit inside a marked region** | **nothing anywhere says it.** The mechanism is protected by two people remembering it ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]) |
| **The questions document for an empty repository** — `proposals/`, `status: idea`, one line per question that cannot be closed without the owner | **four such questions today**, and they live only in this session's journal ([[the-open-questions-list-is-built-whether-or-not-it-is-discussed]], [[an-idea-is-a-proposal-with-an-immature-status]]) |
| **The catalogue's `governs` column** — five lines for the agent half | the Obsidian half exists as a named view, so **the reader who most needs *which rules render into this file* is the one who cannot get it** ([[the-page-list-is-a-query-not-a-generated-file]], [[pages-base]]) |
| **The detector for `current` pages citing archived ones** — deferred by the owner **twice** this session | fifteen pages now argue from a page archived today, and nothing lists them ([[a-live-page-can-argue-from-a-deprecated-one]], [[a-rewriter-must-be-paired-with-a-detector]]) |
| **The filename renames** under the extended title rule | the worst offender carries **23 inbound links**, and a filename is what every `[[wikilink]]` resolves to ([[the-title-rule-extends-to-filenames]]) |
| **The selftest's cost** — one `awk` pass over all rule pages instead of two processes each | **8m04s today**, and roughly fifteen seconds per further migrated rule; marking up the remaining twelve files takes it past fifteen minutes ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]) |

**And one thing was deliberately not patched rather than deferred**: the first sentence of the
repository's `CLAUDE.md`, which still calls the file *"a map and a handful of rules"* after the map was
deleted and nine rules began rendering. Patching it would have been another sentence of unsourced prose
from the same author ([[the-repository-claude-md-after-the-rules-left-it]]).

## Re-read at the end of 2026-08-18: three rows discharged, five joined

**The mechanism change is built** — `governs:` is a field on any page, markers carry the record's
type, and both new verdicts landed, one of them replaced by a reachable one
([[governs-becomes-a-property-of-any-page]], [[the-marker-carries-the-records-type]],
[[the-unreachable-verdict-is-dropped-and-replaced]]). **Of the three records that had nowhere to
live, one is built**: the map ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]).

**The injector's fenced-block defect is fixed**
([[a-fenced-block-inside-a-slice-survives-into-the-destination]]). What that row said it blocked —
the `rg` recipe becoming a rule — is now a *decision* rather than an obstacle: the routes stay
prose, on the owner's ruling, because they are the one part of that file which has never gone stale.

**The `make`/map/`Where things are` row keeps two of its three consumers.** The map came out of it
correctly, as a page rather than a generator's output; `## Commands` is still drifting at `~2 s`
stated against `4.9 s` measured, and the layout block is still deleted
([[a-generator-fills-a-marked-region-from-the-tree]], [[the-command-list-moves-into-a-makefile]]).

**The `awk` row is revised rather than discharged**, and the revision is the useful part: it was
filed as the precondition for the wider injector walk and it was not one. The wider walk is
**faster** than the narrow one, and the quantity to count is processes per page
([[measure-before-optimising-and-count-processes-not-pages]]).

**The hand-edit row's priority is raised by the owner** — see below.

**One of the three items that block construction still remains: the `asserts:` predicate set**
([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]]).

**Five rows joined the register on 2026-08-18:**

| Not doing now | What waiting costs |
|---|---|
| **The separator's outcome, unverified** — whether the paragraph break survives the stripping and reaches the model | a mechanism believed to work with no evidence, on the one thing the change was for. **One minute closes it**, and the owner has booked it for next session ([[the-injector-writes-the-separator-inside-the-region]], [[block-comments-are-stripped-before-claude-md-reaches-the-model]]) |
| **The definition of *retrospective*** — decided as a `concepts/` page, unbuilt | the word that already put two contradictory answers into this corpus still has no page rendering into the file that uses it ([[a-definition-may-render-into-the-repository-claude-md]], [[the-end-of-a-session-is-a-retrospective]]) |
| **The project description**, and **its blocker is narrower than this register recorded** | [[entities-describe-the-application-once-the-detector-exists]] gates *one page per package* behind `asserts:`; **a one-paragraph description of what the tool is is not that**. Not writing the narrowing down costs the next session reading the blocker widely and deferring again. Folder to be decided when it is built |
| **The filename half of rule 10** | **11 filenames of 259 carry a quantity**, measured 2026-08-18; the filename half of the corpus's own naming rule is unenforced ([[knowing-a-rule-is-not-a-mechanism]], [[the-title-rule-extends-to-filenames]]) |
| **Moving a rule to conditional delivery** — designed, blocked on one measurement | the `InstructionsLoaded` hook has to say whether a `paths:`-scoped rule reaches a subagent, and every task here is reviewed by one ([[moving-a-rule-into-claude-rules-with-a-paths-scope]], [[a-rule-moving-to-conditional-delivery-needs-its-page-first]]) |

**The hand-edit row is no longer a deferral for lack of importance.** **owner: priority raised.** It
sat here as *"the mechanism is protected by two people remembering it"*; this session measured that
**the gate did not catch one form of it either** — a blank line hand-added inside any region passed
byte equality that was not byte equality
([[a-command-substitution-strips-the-newline-a-gate-compares]],
[[hand-edits-of-the-wiki-are-a-recorded-divergence]]). It is a hole with evidence.

**Two rows left this register in the other direction, by being retired rather than done.** Both
built proposals are in `archive/` on the owner's one-policy call
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
