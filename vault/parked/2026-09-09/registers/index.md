# Index — map of the vault

Retrieval is **`ripgrep` first, then the wiki links on whatever it found**. You do not need to
find every relevant page, only one, and walk from there. This file exists for what grep cannot
supply, and for why it is shaped this way see [[the-index-is-a-map-not-a-catalogue]].

**The list of every page is `pages.base`** — an Obsidian base, filterable by kind, status, sprint
and tags. It is a query rather than a file of rows, so it cannot fall behind the corpus. An agent,
which has no editor, runs `bash scripts/vault-catalogue.sh` for the same list. This file stays a
map: a hundred new pages do not lengthen it, and it answers *where do I start*, never
*what is there* ([[pages-base]], [[the-page-list-is-a-query-not-a-generated-file]], 2026-08-17).
*(This citation was [[the-catalogue-is-generated-not-maintained]] until 2026-08-17, when the
generated `catalogue.md` it named was replaced by the base.)*

## Categories

| Folder | The question it answers |
|---|---|
| `wiki/decisions/` | what we chose, when, why, what we rejected, what it obliges |
| `wiki/concepts/` | how it is built and why it works that way |
| `wiki/entities/` | what exists and what it is like |
| `wiki/lessons/` | what we learned the hard way |
| `wiki/proposals/` | what was raised or deferred and **never built** — *what did we plan and never do* |
| `wiki/rules/` | a rule the harness **renders** into the file it governs, rather than a reader remembers |

**The sixth row was added on 2026-08-17, on the owner's decision**, and the note below it
stood while the table had five rows. It is kept whole rather than replaced: it carries why the
row was withheld, and it ends *"If the owner would rather have the row, it is one line."* He
asked for the line. **What the reversal does not touch:** S2's criterion 3 still deletes this
table ([[the-index-reads-and-the-schema-writes]]), and the rule that a copy which has drifted
twice is repaired by removing it rather than by correcting it stands unchanged
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]) - what was overridden is its
application to this one row, by the only person who can override it. The folder's first page is
[[the-owner-decides-how-a-slice-is-executed]], which renders into the repository's `CLAUDE.md`.

*What stood here from 2026-08-17 until the row was added, on the same day:*

**`wiki/rules/` is missing from that table on purpose, and the table is what is wrong.** The folder
was built on 2026-08-17 and the set is six: a rule the harness *renders* rather than a reader
remembers, carrying `governs:` and never `authority:`
([[the-folder-set-is-closed-and-tasks-is-not-in-it]], [[rules-becomes-a-type-of-its-own]]). No sixth
row was added because **this table is a copy that S2's criterion 3 deletes**, and a list that keeps
drifting is repaired by removing it rather than by adding the missing row
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]). The authoritative set is in
[`CLAUDE.md`](CLAUDE.md) and in rule 1 of `vault-check.sh`.

**The `proposals/` row is under a ruling it does not yet reflect — 2026-08-22.** A proposal that
has been **built** now stays in that folder with a `built` mark rather than moving to `archive/`, on
the owner's decision, and he said it rewrites the earlier ones
([[a-built-proposal-stays-in-proposals-with-a-built-mark]]). So the row's *never built* is the
question the folder was created for and is no longer a description of what it holds. **The row is
left standing and dated rather than reworded**, because what separates a built page from an unbuilt
one is the mark, the mark does not exist yet, and whether it is a third `status` value or a field of
its own is deferred to the next session in his own words.

**That paragraph is reversed and its last clause is answered — 2026-08-23, and it is left standing
rather than reworded.** A built proposal does **not** stay in the folder: it takes
`status: implemented` and moves to `archive/` once a live page cites it, on the owner's ruling that
the archive is history and the wiki is the source of truth
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]], superseding
[[a-built-proposal-stays-in-proposals-with-a-built-mark]], now in `archive/`). **The shape of the
mark is settled and it is a third `status` value**, not a field of its own
([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]) — so the
clause *"whether it is a third `status` value or a field of its own"* is closed. **So the row's
*never built* is a description of the folder again**, and the row still stands unreworded: a
built-but-unimplemented proposal keeps a `built` mark inside the folder, and that mark waits on
`wiki/tasks/` and S4 ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). A **refused** one also
leaves, with `status: refused`, and that value is not minted either
([[a-refused-proposal-is-archived-and-takes-status-refused]]).

**One clause of the paragraph above went false on 2026-08-23, later the same day, and it is
corrected here rather than in place.** **`refused` is minted** — `wiki/proposals/_schema.yaml`
declares it beside `implemented`, and the word is red in every other folder. So is `idea`, which
had been decided on 2026-08-17 and unminted for six days. A refused proposal also carries
`decided_by:` naming the decision that refused it, and **no** `superseded_by:`; the requirement is
conditional on the status, so `scripts/vault-archive.sh` enforces it rather than the gate
([[a-refused-proposal-is-archived-and-takes-status-refused]],
[[an-idea-is-a-proposal-with-an-immature-status]],
[[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]]). **`built` is still
not minted** and still waits on `wiki/tasks/` and S4, so that half of the paragraph stands
unchanged. The note is dated the day the text became false
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

Full rules in [`CLAUDE.md`](CLAUDE.md). `proposals/` was added 2026-08-15
([[proposals-are-a-folder-not-a-status]]): a folder rather than a `status:` value, so that an
intention can never be read as a record of something built. It did **not** take deferral away from
`decisions/` — the decision records *that* we said not now, the proposal carries *what* we would
build, and both often exist. `tasks/` is still not one of them:
[[the-folder-set-is-closed-and-tasks-is-not-in-it]]. *(This paragraph cited
[[the-wiki-has-five-folders-and-tasks-is-not-one]] and said "the set is five" until 2026-08-17.)*

## Naming

`kebab-case`, descriptive, no dates in the filename. The filename is part of the search surface.
**No category prefix** — the folder and `type:` already carry the category, and a name should start
with its subject: [[filenames-carry-no-category-prefix]], decided 2026-08-15.

**A title carries no measurable quantity** — unconditionally, decided 2026-08-16. Name what is
counted instead of counting it ([[a-title-names-what-is-counted-instead-of-counting-it]]), and let
the form follow the type: an entity is a noun phrase, a decision states its claim
([[the-titles-form-follows-the-records-type]]).

**And the filename carries none either, decided 2026-08-17** — the rule covers the address as well as
the title ([[the-title-rule-extends-to-filenames]]). **Only the title half is checked**: rule 10 of
`vault-check.sh` reads `title:` by design, so a filename that counts is a violation nothing prints.
The renames are blocked on the rewriter-and-detector pair, because a filename is what every
`[[wikilink]]` resolves to ([[a-rewriter-must-be-paired-with-a-detector]]); at least four filenames
carry a count today and the worst carries 23 inbound links.

**Both clauses of the paragraph above went false on 2026-08-18 and are corrected here rather than
in place.** **The filename half is checked** — rule 10 reads the slug with the predicate it reads
the title with, as an **advisory** where the title half is red, and it printed six names at this
ingest ([[the-title-rule-extends-to-filenames]],
[[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]],
[[the-filename-advisory-prints-one-name-per-line]]). **"At least four" was thirteen** when it was
counted, of which six print today. **The "23 inbound links" does not reproduce**: measured at
`c521a10` over the link set the check reads, the worst of the six carries 20 and the page the figure
was written about carries 14 ([[a-page-rename-is-sed-and-verify]]). And **"blocked on the
rewriter-and-detector pair" was overpriced** — all six renames took 10.1 seconds in a worktree,
including a full gate run; what is genuinely outside the detector is `log.md`
([[log-md-is-outside-the-link-set-the-check-reads]]).

**And the escape hatch is gone — owner, 2026-08-18.** The rule is unconditional in both halves and
the `quantity:` field is rejected; a flagged title is retitled and a flagged filename waits for its
rename. The field still stands on 24 pages and the check still reads it, which is a state and not a
permission ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[the-title-check-asks-and-the-answer-is-a-retitle]]).

**Third correction, 2026-08-19: all three figures above are zero, and this paragraph stops
carrying figures.** The field stands on **no** page — `grep -rc '^quantity:' wiki archive` sums
to 0, against the 24 stated above — and the filename advisory prints nothing:
`bash scripts/vault-check.sh | grep 'filename(s) count'` is empty, against *thirteen, of which
six print*. The corpus stopped counting in its titles on 2026-08-18 and the sixteen renames
landed on 2026-08-19 ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[the-title-rule-extends-to-filenames]], [[a-page-rename-is-sed-and-verify]]). **One clause
above stayed true**: the check still reads the field — rule 10's `awk` short-circuits on a
`quantity:` line — so it is a silencer no page uses rather than one that has been removed.
**And the reading is the command, not this sentence.** That is the repair available to a figure
that has now been corrected three times: name the decider instead of the number, which is what
every acceptance criterion in [`sprint.md`](sprint.md) already does.

**Three corrections on one paragraph is the signal
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]] was written about**, and it is
reported here rather than acted on. That page's repair is deleting the copy, and deleting is not
the librarian's ([[the-librarian-writes-unattended]]); S2's criterion 3 already schedules the
deletion of this whole section — *no categories table, no naming rule, no sprint identifier*
([[the-index-reads-and-the-schema-writes]]). Until it lands the section stands with its
correction on it, which is what that rule prescribes for the interval and what was done with the
categories table above.

## Current sprint

**S3 — every claim the vault makes about itself is decided by a command**, opened 2026-08-23, the
same day S2 closed. New pages carry `sprint: S3` until it closes. The goal, its acceptance criteria
and the command that decides each one are in [`sprint.md`](sprint.md), which is the only place they
live. *(This section read "S2 — the vault is used, not maintained" until 2026-08-23, "S1 — the vault
checked whole" until 2026-08-17, and "none declared, `sprint:` is `S0`" until 2026-08-14. It also
counted S2's acceptance criteria until 2026-08-23; the count is gone rather than corrected, for the
reason the paragraph above gives — name the decider, not the number.)*

## Hub pages

Entry points into the large subjects. Grep first; if you do not know where to start, start here
and walk the links.

| Subject | Start at |
|---|---|
| collecting vacancies | [[collection-runs-in-a-thread]] |
| judging what disappeared | [[deactivation-cycle]], and [[why-deactivation-is-profile-scoped]] for the reasoning under it |
| the vacancy list and its filters | [[vacancy-list-invariants]] |
| the two pages and the shell around them | [[one-shell-the-vacancies-and-collection-pages-and-one-poller-on-each]] |
| the web stack, and what would change it | [[the-stack-stays-htmx]] |
| layering and what holds it | [[architectural-boundaries]] |
| the database schema, its migrations, and what keeps them in step | [[migrations-do-not-drift-from-the-models]] |
| how a slice is run | [[how-a-slice-is-executed]] |
| what a test is worth | [[a-test-green-under-any-implementation]] |
| the environment | [[docker-desktop]], [[app-restart-required]] |
| this vault, and who maintains it | [[journal-vault-brief-each-artefact-has-one-owner]], and [[vault-librarian]] for the agent that writes it |
| what the owner asked this vault to be, and what was built instead | [[the-owners-instructions-note-and-what-was-built-from-it]], and [[the-owners-method-note-and-what-was-built-from-it]] for the method under it — the two disagree with each other |
| why the store is compiled at all, rather than searched | [[the-vault-is-compiled-not-retrieved]] |
| the harness — the files that instruct an agent, and why they are becoming a build | [[the-harness-is-compiled-not-maintained]], and [[no-rule-reads-a-harness-file]] for the failure class it answers |
| a rule that is rendered rather than read, and the regions it lands in | [[a-region-is-a-paired-comment-named-for-a-rule]], and [[what-travels-from-a-rule-page-is-a-marked-slice]] for what a rule page ships |
| a record that renders from outside `wiki/rules/`, and what a slice may not carry | [[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]], and [[a-marker-with-its-type-is-a-complete-address]] for the address the marker became |
| how the renderer and the gate divide the work, and what neither of them sees | [[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]], and [[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]] for the case that fell between them |
| the repository's `CLAUDE.md` as a file — what is in it and what is knowingly wrong in it | [[the-repository-claude-md-after-the-rules-left-it]], and [[wiki-rules-holds-the-rules-of-the-repository-claude-md]] for the folder its rules live in |
| how a session ends, and what each step of it is for | [[the-end-of-a-session-is-a-retrospective]], and [[the-retro-step]] for the step that was added |
| a rule of the repository's `CLAUDE.md`, now that each of them is a page | [[the-owner-decides-how-a-slice-is-executed]], [[the-suite-never-runs-against-the-production-database]], [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]], [[our-javascript-does-not-choose-which-rows-are-on-screen]] |
| a rule of that file from outside its numbered list — language, the librarian, the closing ritual | [[english-in-the-repository-russian-with-the-owner]], [[a-pre-task-runs-before-anything-non-trivial]], [[ask-before-weakening-or-working-around-a-rule]], [[a-session-ends-with-retro-then-handoff-then-ingest]], [[write-the-miss-into-vault-feedback-before-the-turn-ends]] — **retired 2026-08-24, and the live one is [[speak-the-feedback-in-the-turn-and-the-hook-files-it]]** |
| a rule delivered on a matching path instead of to every session | [[the-generated-ast-boundaries-rule-file]], and [[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]] for what triggers a delivery and what does not |
| the pre-task ritual — when it runs, what records it, and what plan mode does around it | [[a-pre-task-runs-between-the-plan-and-its-approval]], and [[the-plan-check-hook]] for the hook that delivers it |
| the agent that performs the pre-task, and what it is told to read | [[the-pre-task-agent]], and [[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]] for the discipline it shares with the librarian |
| a measurement written into this store — where the number goes and who writes it | [[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]], and [[vault-measure-py]] for the script that is the only writer of a gauge's number |
| who reads this vault and who writes it — the agents the librarian dispatches | [[who-reads-the-vault-and-who-writes-it]], and [[the-verdict-and-the-pen-are-held-by-different-parties]] for the sentence the whole arrangement turns on |

**A row was added on 2026-08-20, in the third session of that day, and two rows above it went
stale.** The ritual acquired a moment, an artefact and a hook, and the knowledge is spread over a
trigger decision, a rule page, a hook, a ledger, a state machine and half a dozen facts about plan
mode that this corpus did not hold at all — no single page is the entry point, which is what a hub
row is for ([[the-index-is-a-map-not-a-catalogue]]).

**What went stale, reported rather than repaired in place:** the row naming the rules of that file
*from outside its numbered list* still lists [[a-pre-task-runs-before-anything-non-trivial]], which
is **retired to `archive/`** and superseded by [[a-pre-task-runs-between-the-plan-and-its-approval]]
— and that successor governs a hook message rather than `CLAUDE.md`, so the row is true about where
to start and stale about what the file holds. **The same row is now short by one**:
[[dispatch-librarians-in-parallel-only-for-reading]] entered `CLAUDE.md` on the same day, on the
other half of the same criterion
([[a-rule-applied-in-opposite-directions-on-one-day-is-not-a-reversal]],
[[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]).

**The row above it was added on 2026-08-17, in the same day's second migration.** The numbered list
was never the whole of what that file instructs: the `## Language` section, the `/pre-task` trigger,
the rule about weakening a rule, the closing ritual and the feedback line are all imperative, none of
them is held by a test, and each is now a page rendered into a region rather than prose typed into a
file ([[rules-becomes-a-type-of-its-own]]).

**What is still prose in that file, and why**, so that a reader does not take the two rows as the
set: the by-hand `rg` recipe cannot render yet — a fenced code block inside a `<!-- text -->` slice is
dropped by the injector — and the paragraph defining what *retrospective* means is a definition
rather than an imperative, which fails the folder's admission test and waits on an owner decision
about whether a non-rule record may render at all.

**The last row is dated 2026-08-17 and it is a state, not a set.** The rules that could not wait for
a question have all left that file's numbered list for `wiki/rules/`, one on the migration that
built the fifth verdict and the other three the same day. **Being a page is not the same as being
rendered**: a region is marked in the destination and `scripts/vault-inject.sh` writes the text into
it, and until a rule's region exists the gate says so ([[a-region-is-a-paired-comment-named-for-a-rule]],
[[a-governed-file-with-no-region-is-an-advisory]]). If a rule is ever added to that file, it is a
page from the start — the migration is what is finished here, not the folder.

**Both of those paragraphs are dated 2026-08-17 and both have moved since, later the same day.** The
migration is finished **and rendered**: nine rules of that file are pages, each region is marked, and
`bash scripts/vault-inject.sh --check` reports every one of them in step
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]). Region coverage is `1 of 13`, so the
*"until a rule's region exists"* clause above no longer applies to any of them.

**What is still prose in that file now has pages behind the reasons, which it did not before.** The
`rg` recipe still cannot render — the injector drops a fenced block inside a slice, measured
([[the-injector-drops-a-fenced-block-inside-a-slice]]); the project description **stays** on the
owner's ruling that a *sourced* assertion is legitimate there
([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]); the map is designed and unbuilt
([[the-map-in-claude-md-and-its-admission-test]]); and `## Commands` is drifting, at `~2 s` stated
against `4.9 s` measured ([[the-command-list-moves-into-a-makefile]]). `## Where things are` is
**deleted** ([[where-things-are-is-deleted-now-and-generated-later]]).

**Two clauses of the paragraph above went false on 2026-08-18, and it is left standing.** **The map
is built**: it is a page in `concepts/`, it carries `governs: CLAUDE.md`, and its region is the first
one in this project rendered from outside `wiki/rules/`
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[governs-becomes-a-property-of-any-page]]). It holds the vault, its librarian and the sprint —
**and not the sprint's contents**, which is what stops the region becoming the next
`## Where things are`; the routes stay hand-written prose on the owner's decision of the same day.
**And the `rg` recipe's mechanical excuse is gone**: a fenced block inside a slice survives into the
destination from `e83ce28`, so [[the-injector-drops-a-fenced-block-inside-a-slice]] describes code
that has changed and is owed a correction by this session's ingest. The recipe stays prose anyway,
on the reason the owner gave — it is the one part of that file which has never gone stale.

**And the file's first sentence stops being wrong when the map renders.** It says the file *"is a map
and a handful of rules for how to work"*, and it was left deliberately wrong as a marker of exactly
this gap ([[the-repository-claude-md-after-the-rules-left-it]]). **Whether it is then reworded is the
owner's**, and so is the disposition of the design page, which was built today and deliberately not
retired ([[the-map-in-claude-md-and-its-admission-test]], [[marked-regions-and-the-prose-outside-them]]).

**The correction owed above was made at the ingest of 2026-08-18, and the design page's disposition
is settled.** [[the-injector-drops-a-fenced-block-inside-a-slice]] is retired to `archive/`; the
behaviour as it stands is [[a-fenced-block-inside-a-slice-survives-into-the-destination]]. Both
built proposals are retired under one policy of the owner's
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]),
[[marked-regions-and-the-prose-outside-them]] **stays `current`** on his ruling, and
[[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]] is retired too — the field is read
on any page now ([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]). **The `1 of 13`
above is not patched**: a drifting count is dated where it stands or deleted, never renumbered in
eight places ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**The clause about the definition of *retrospective* is settled, and the count of regions has
moved.** This file says above that the paragraph defining that word *"waits on an owner decision
about whether a non-rule record may render at all"* — it was licensed on 2026-08-18 and **it
rendered the same day**, at `46b7c76`, as the eleventh region and the second from outside
`wiki/rules/` ([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]],
[[a-definition-may-render-into-the-repository-claude-md]]). **The question that record left open is
now closed too**: `authority:` beside `governs:` is forbidden on any page
([[authority-beside-governs-is-forbidden-on-any-page]]). **The `1 of 13` above is still not
patched** and is now `1 of 14`, because `.claude/rules/` exists and holds a probe file
([[the-conditional-delivery-probe]], [[the-region-coverage-figure-is-dated-where-it-stands]]).

**A row was added on 2026-08-20, and it is a subject rather than a file.** Conditional delivery is
now a mechanism with a built half and an unbuilt half, spread over a hook branch, a delivery mode, a
generated file, a deletion rule and a movability criterion — and no single page is the entry point,
which is what a hub row is for ([[the-index-is-a-map-not-a-catalogue]]). The row above it, naming
the rules of the repository's `CLAUDE.md`, **still lists [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]]
and that page no longer governs that file**: it is a `wiki/rules/` page like the others and is
reached the same way, so the row is true about where to start and stale about what the file holds
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]],
[[the-repository-claude-md-after-the-rules-left-it]]).

**`governs:` went back to `wiki/rules/` alone on 2026-08-21, and two pages changed folder.** The
owner overturned his own ruling of 2026-08-17 at the retro: a page that renders its text into
another file **is** a rule, so the field is a property of that folder and of no other
([[governs-is-a-property-of-wiki-rules-alone]], superseding
[[governs-becomes-a-property-of-any-page]], now in `archive/`). The map and the definition of
*retrospective* moved from `concepts/` into `wiki/rules/` with `type: rule`
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]). **It is a folder move and not a
rename** — a `[[wikilink]]` resolves by filename anywhere under `wiki/` or `archive/`, so no address
moved and no inbound link was rewritten.

**So two things this file says above are now dated rather than current.** The paragraph about the
map calls it *"a page in `concepts/`"* whose region is *"the first one rendered from outside
`wiki/rules/`"*, and the paragraph about the definition of *retrospective* calls its region *"the
second from outside `wiki/rules/`"*. Both were true when written and neither is patched in place: a
statement about a day is dated where it stands ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**The hub row reading *a record that renders from outside `wiki/rules/`* is stale in its subject and
true about where to start.** There is no such record now; the two pages it was written for are in
that folder. What its entry points still answer is what the field means and what a slice may not
carry ([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]],
[[a-marker-with-its-type-is-a-complete-address]]) — which is a hub row's job, so the row stays.

**Owed at the destination, and not the librarian's to write:** the two regions in the repository's
`CLAUDE.md` are marked `<!-- concept: … -->` and the injector now derives `rule:` from the folder,
so both marker pairs are the session's to rewrite in the same change
([[the-marker-carries-the-records-type]], [[a-check-asks-by-running-the-writer-it-checks]]).

**The markers that paragraph says are owed were written, in the same session.** Both regions in the
repository's `CLAUDE.md` now read `<!-- rule: … -->`, `bash scripts/vault-inject.sh` exits 0, and
region coverage stands at `5 of 15` with the unmarked files unchanged. Recorded here rather than by
striking the paragraph out, which is how a statement about a day is kept
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**A hub row was added on 2026-08-21: how a claim is looked up before a page is written.** The
subject arrived whole in one session and is spread across a ground rule, a rendered imperative, a
required field, a register and a script — no single page is its entry point, which is what a hub row
is for ([[the-index-is-a-map-not-a-catalogue]]).

| Subject | Start at |
|---|---|
| whether a claim already has a page, and what a new page has to earn | [[occams-razor-is-the-ground-rule-for-the-vault]], and [[authority-becomes-the-index-and-is-required-outside-rules]] for the index the lookup reads |

**A hub row was added on 2026-08-22: whose words a sentence is, and what may be reasoned from it.**
The subject arrived as a defect on 2026-08-21 — a rule the owner never gave, standing for three days
as a quotation stamped `basis: human` — and it is now spread across a failure chain, a ruling on the
verdict's severity, a rendered rule, a gate advisory and a ratification step. No single page is its
entry point, which is what a hub row is for ([[the-index-is-a-map-not-a-catalogue]]).

| Subject | Start at |
|---|---|
| whether a sentence is the owner's own, and what a paraphrase may be worth | [[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]], and [[a-block-attributed-to-the-owner-is-written-in-his-own-russian]] for the rule that reaches the session writing the line |

**The pre-task hub row is true about where to start and its subject changed on 2026-08-22.** The
ritual is no longer a skill: `.claude/skills/pre-task/` is deleted and `/pre-task` is performed by
dispatching `subagent_type: "pre-task"`, an agent of its own
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]). Its rule page still names *when* it
runs and now also *how*, so the row's entry point is unchanged
([[a-pre-task-runs-between-the-plan-and-its-approval]]). **The row is not rewritten**: a hub row
names where to start, and it still does ([[the-index-is-a-map-not-a-catalogue]]).

**And a rule renders into an agent definition rather than into `CLAUDE.md`, for the first time into
two of them.** The reading discipline every reader of this store needs — find the vault, read its
`CLAUDE.md`, grep then follow links, `tags.md` across the two languages, narrow before opening, the
folder first, the tag inside it, and the ceilings with their `/pre-task` carve-out — is one page
rendered into both agents rather than copied into the second
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]],
[[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

| Subject | Start at |
|---|---|
| how an agent is told to read this store, and why that text lives in one place | [[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]], and [[the-folder-is-the-first-narrowing]] for the measurements under it |

**The row naming the rules of the repository's `CLAUDE.md` gained no member and one of them
shrank.** `plans` was struck from the English list of
[[english-in-the-repository-russian-with-the-owner]] and the plan the owner reads in order to
approve it is named on the Russian side
([[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]). The rendered region in that file
moves with the page, by the injector, so nothing here has to be kept in step by hand
([[a-check-asks-by-running-the-writer-it-checks]]).


**A row was added on 2026-08-22, at the ingest of the session that rebuilt the ritual.** `/pre-task`
became an agent and the skill was deleted, so *how the ritual is performed* stopped being a command
anyone could type and became a dispatch — and the file that performs it now shares its reading
discipline with the librarian by rendering rather than by copying. **The row above it is unchanged
and still answers *when* it runs**; this one answers *what runs*
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**A hub row was added on 2026-08-23: what became of a proposal, and where it lives now.** The
subject moved twice in two days and in opposite directions, and it is now spread over a
disposition ruling, a status-value ruling, a refusal ruling, a script precondition and a concept
about how a mark is read — no single page is its entry point, which is what a hub row is for
([[the-index-is-a-map-not-a-catalogue]]). **The `proposals/` paragraph above is the same subject
seen from the folder's side** and is not a substitute for the row: it says what the folder holds,
and the row says where to start reading.

| Subject | Start at |
|---|---|
| what became of a proposal, and where it lives now | [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]], and [[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]] for how the mark is read |

## The feedback rule in the hub table above is the first rule row to name a retired page — 2026-08-24

**The rule telling a session to write `.superpowers/sdd/vault-feedback.md` was superseded**, and the
successor is named beside it in the row rather than replacing it: a session speaks the line in a
fenced `VAULT-FEEDBACK` block and a hook files it
([[speak-the-feedback-in-the-turn-and-the-hook-files-it]],
[[the-session-speaks-the-feedback-line-and-a-hook-files-it]]).

**Both links resolve and only one renders**, which is the property that makes leaving the old one
safe: a deprecated rule renders nothing, so the row records where the text used to come from without
sending a reader to text that is no longer in any file
([[a-deprecated-rule-does-not-render]]).

**It is also the first rule here to govern more than one file** — `CLAUDE.md`, `/vault-ask` and
`/handoff` — so the region coverage advisory moved from `7 of 15` to `8 of 15` on the day it landed,
and `.claude/skills/vault-ask/SKILL.md` carries its first region
([[a-governed-file-with-no-region-is-an-advisory]],
[[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

## A hub row was added on 2026-08-26: how a measurement is written into this store

**The subject acquired a script, a spelling and a gate rule in one session**, and no single page was
the entry point — which is what a hub row is for ([[the-index-is-a-map-not-a-catalogue]]). The
family in `authority.md` stands at eleven slugs, and the knowledge is spread over a role split, a
grammar decision, a byte-level spelling, a writer script and a delegated gate rule
([[vault-measure-py]], [[the-measure-regions-spelling-fences-the-command-in-backticks]],
[[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]).

**Nothing else in this file changed at that ingest.** The categories, the naming rule and the
current sprint are all as they were.

## A hub row was added on 2026-08-29: who reads this vault, and one older row went stale

**The subject arrived whole in one day.** Two reading agents were written, the librarian gained the
tool to dispatch them, and the design naming all five actors was ratified — so the knowledge is spread
over a proposal, a concept, two entity pages and a decision, and **no single page is the entry point**,
which is what a hub row is for ([[the-index-is-a-map-not-a-catalogue]]).

**What went stale, reported rather than repaired in place:** the row naming *the harness — the files
that instruct an agent* starts at [[the-harness-is-compiled-not-maintained]], which the sweep of
2026-08-29 moved to `archive/`. **The link resolves and the page is frozen**, so the row is true about
where to start reading and stale about whether that page is still the live statement — and a live one
does not exist ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]],
[[the-commit-step-is-typed-into-the-skill-and-the-rule-page-debt-is-recorded]]).

**The categories, the naming rule and the current sprint are unchanged.** S3 is still open.

## Two hub rows were added on 2026-08-30: a decision's lifecycle, and the form of a reply

**The lifecycle arrived as twenty decisions in one day and no single page is its entry point** — it is
spread over a proposal container, six ratifications, six unbuilt work items, two schema entities and a
gate. The proposal is the only page that lists them together, which is what makes it the start
([[the-index-is-a-map-not-a-catalogue]]).

**The reply-format subject has the same shape for a different reason**: the rule renders into
`CLAUDE.md`, its decision explains what was absorbed, and a concept explains why the landing takes two
sessions. A reader arriving at any one of the three needs the other two.

| Subject | Start at |
|---|---|
| what a decision declares, and what closes it | [[the-decision-lifecycle]], and [[a-decision-declares-its-target-and-the-handshake-closes-it]] for the mechanism |
| how a reply to the owner is built, and the frontier it opens with | [[the-reply-is-a-report-answers-and-one-case]], and [[a-decision-with-a-rule-target-cannot-close-inside-a-single-ingest]] for why a rule lands late |

**A row went stale on 2026-08-30 and is repaired here rather than left**: the feedback row's
`every-question-to-the-owner-carries-its-context` was superseded and archived this ingest, and the
live statement is now the first row above.

**The categories, the naming rule and the current sprint are still unchanged.** S3 is open.

## A hub row was added later on 2026-08-30: how a rule reaches whoever it governs

**A rule gained a delivery that renders into no file**, and the subject is now spread over a mode, a
hook, a decision about the mechanism and the design that would apply it to 282 prohibitions. **No one
page is the entry point**, which is what makes a hub row the right answer
([[the-index-is-a-map-not-a-catalogue]]).

| Subject | Start at |
|---|---|
| how a rule reaches whoever it governs, and what changed on 2026-08-30 | [[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]], and [[the-rule-server-hook]] for the hook that is supposed to deliver it |
| what the cleanup of `wiki/decisions/` is and what it stands on | [[the-prohibition-families-become-rule-pages-served-by-a-hook]], and [[the-cleanup-suspends-the-rules-that-would-refuse-it]] for the four rules it lifts |

**Two statements above this line went false on 2026-08-30 and are corrected here rather than
reworded**, because a claim struck in place leaves nothing saying it was ever made.

**`wiki/rules/` no longer carries `governs:` and never `authority:`.** The paragraph under
*Categories* says so, and it was true from 2026-08-21 until this day. **`authority:` is now legal in
that folder** — optional there, and the only way a rule delivered by lookup can be addressed at all,
because such a page has no destination to name
([[authority-uniqueness-becomes-a-per-type-question]]).

**And the `wiki/rules/` row of the categories table is now narrower than the folder.** It reads *"a
rule the harness **renders** into the file it governs"*; under `render: authority` a rule is rendered
nowhere and is fetched instead. **The row is left standing and dated**, on the same ground the
`proposals/` row above it was.

**A third claim about this store went false in a file the librarian may not edit**, and it is recorded
here because a reader arrives at both: `job_hunt_ai_vault/CLAUDE.md:199-200` and `:347` say two
`current` pages sharing an `authority:` are a contradiction, with no qualification by type. **From
2026-08-30 that is true only within a type**, and two pages of different types sharing a slug is
legal and expected. That file is what the gate reads as its own input and is the session's to write
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

## The rules delivered by lookup rather than by injection — 2026-08-31

**These are the rule pages that are written into no file.** A rule rendered into a destination is
reached through the file it governs; these are reached by `.claude/hooks/serve-the-rule.ps1` matching
their `authority:` slug against the slug of whatever vault page is being read. Nothing in the tree
points at them, so without this list every one of them is an orphan — which is why a flat list of
pages sits in a file that otherwise holds only hub pages. **The owner ratified the exception on
2026-08-30**, narrowing the standing prohibition on listing pages here: «Да, можно»
([[the-index-is-a-map-not-a-catalogue]]).

**Read the slug as the address, not as a summary.** Each was compiled from one family of
`authority.md` and carries the slug that a live `concepts/` or `entities/` page of that family also
carries, so the rule arrives when that page is opened
([[a-rule-page-carries-a-family-slug-and-the-decision-that-caused-it]]). Five of them found no such
page and keep the slug of the decision that caused them; those are served by nothing until a concept
or an entity takes the slug, and they are marked below.

| Rule page | `authority:` |
|---|---|
| [[a-rule-page-carries-a-family-slug-and-the-decision-that-caused-it]] | `rule-about-rules-delivery` — no live carrier yet |
| [[the-tag-dictionary-and-the-question-asked-in-one-language-of-a-corpus-written-in-another]] | `alias-purpose` |
| [[what-the-owner-said-and-what-was-put-in-his-mouth]] | `retro-ratification` — no live carrier yet |
| [[a-rule-page-and-the-slice-that-travels]] | `rules-folder-inventory` |
| [[where-a-rules-text-is-sent]] | `rule-delivery-modes` |
| [[the-region-a-rule-renders-into]] | `region-form` |
| [[a-copy-of-a-list-drifts]] | `derived-register-proof` |
| [[a-number-this-project-quotes]] | `coverage-denominator-source` |
| [[the-per-folder-schema]] | `per-folder-frontmatter-schema` |
| [[admitting-a-frontmatter-field]] | `field-admission-test` |
| [[the-no-quantity-rule]] | `title-check-mechanism` |
| [[what-a-page-is-called-and-what-kind-it-is]] | `page-naming` — no live carrier yet |
| [[renaming-a-page]] | `rename-cost` |
| [[retiring-a-page]] | `archive-script` |
| [[draining-a-folder-into-the-archive]] | `sweep-mode-inheritance` |
| [[what-the-vault-is-and-what-its-answers-are-worth]] | `vault-artefacts` |
| [[how-a-measurement-is-written-down]] | `measure-region-spelling` |
| [[a-deferral-with-a-proposal-behind-it-and-the-decision-nobody-compiled]] | `missing-decision-compilation` — no live carrier yet |
| [[a-decisions-own-lifecycle-what-it-declares-and-what-closes-it]] | `repealed-status-mint` — no live carrier yet |

**The categories, the naming rule and the current sprint are unchanged.** S3 is open.

## Two claims above this line were repaired, and the delivery they were about now works — 2026-08-31

**"A third claim about this store went false in a file the librarian may not edit" is discharged.**
`job_hunt_ai_vault/CLAUDE.md` now reads *"the sole answer to **within its own type**"* and *"If two
`current` pages **of the same type** claim the same `authority`"*. The session wrote it, which is whose
it was, and the note above stands as the record of the day the file and the corpus disagreed
([[authority-uniqueness-becomes-a-per-type-question]]).

**And the hub row for how a rule reaches whoever it governs was pointing at a delivery that did not
exist.** It does now: `.claude/hooks/serve-the-rule.ps1` matches a `render: authority` page on the
touched file's own slug — **exactly, resolving nothing** — and is registered on `Read` as well as on
`Edit|Write` ([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]]). The row
itself is unchanged; both pages it names are still the entry points.

**What the list above is worth is a separate number from its length.** Fourteen of the nineteen carry a
slug a live concept or entity also carries, so the hook serves them; five are served to nobody until a
page takes their slug, and the pass that does that is
[[the-convergence-pass-over-the-live-non-decision-pages]]. **The five marked "no live carrier yet" in
the table above are those five**, and the marking is current.

**No hub row was added and no category changed.** S3 is open.
