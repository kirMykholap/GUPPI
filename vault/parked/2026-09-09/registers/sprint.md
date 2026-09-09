# Current sprint

**S3 is open**, declared by the owner on 2026-08-23, the same day S2 closed. Its goal and its four
acceptance criteria were written by this session and approved by him in the plan he read that day.

New pages carry `sprint: S3` from here until it is closed. `sprint:` is **origin, not membership**,
so a page compiled from a session that ran inside S2 goes on carrying `sprint: S2`. Nothing is
re-stamped.

A sprint is declared explicitly, never inferred from a branch or a merge, and it is closed on
its goal rather than on an empty backlog. How to open and close one: the `/sprint` skill.

<!-- Shape when one is open:

## S1 — <short name>
Opened: YYYY-MM-DD
Goal: <a checkable statement, not a theme>
Acceptance criteria:
1. <observable>
2. <observable>
Milestones: <list>
Closed: —

### Changes to the goal
- YYYY-MM-DD: <what changed and why>
-->

## S3 — Every claim the vault makes about itself is decided by a command

Opened: 2026-08-23
Closed: —

**Goal:** every claim the vault makes about itself is decided by a command.

**Attribution, stated at the opening because it is the part that goes wrong later.** The goal above
and the four criteria below were **written by this session**; the owner **approved them by approving
a plan**, on 2026-08-23. That is a decision and not an utterance — the ruling is his, the wording is
the session's, and none of it is a quotation or is signed as his words
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]). He also
said what he wants of the sprint's execution: a concrete and detailed plan, because he can already
feel the two of you diverging in places. His words are quoted whole in the closing reading of S2,
below.

**Acceptance criteria, each naming the command that decides it** — the pattern S1 and S2 were both
written in, and the one thing here that removes the need to read a document in order to trust it:

1. **The five rules that no instrument checks have one — or a page saying why they cannot.**
   *Decided by:* `bash scripts/vault-check-selftest.sh` and `pwsh scripts/hook-selftest.ps1` each
   carry a case per new instrument and report `missed 0`.
   *Caveat, recorded at the opening rather than discovered at the close:* one selftest case prints
   `MISSED` on a red tree, so `missed 0` is unreachable while the gate is red
   ([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]).
   *The caveat is answered rather than standing — 2026-08-26.* The owner threw the case out, on
   exactly this reading: it makes the criterion unreadable when the criterion is needed
   ([[the-green-gate-selftest-case-is-thrown-out-rather-than-deferred-again]]). **The removal has not
   landed**, so `caught 148, missed 0` still includes the case and the caveat still applies to any
   run taken before the edit.
2. **A proposal does not reach `archive/` without a live page citing it.**
   *Decided by:* `bash scripts/vault-archive.sh` refuses with exit 2, and the selftest carries the
   case ([[vault-archive-sh]]).
3. **`decided_by:` is legal in every schema and the count of pages lacking it prints under
   `--lint`.**
   *Decided by:* `bash scripts/vault-check.sh --lint` prints the count;
   `bash scripts/vault-check.sh` exits 0.
4. **The two deciders carried from S2 exist, and region coverage reaches 15 of 15.**
   *Decided by:* a rule reads `index.md` content; rule 5b covers a second kind of target; the
   advisory prints `15 of 15` ([[the-index-reads-and-the-schema-writes]],
   [[the-repository-claude-md-becomes-a-dispatch-table]],
   [[a-governed-file-with-no-region-is-an-advisory]],
   [[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

### What entered S3 on 2026-08-24, on the owner's decision, and what landed that day

**Three harness defects go onto the sprint, one line each** — the `PreToolUse:Edit` hook excepted
for `wiki/*/_schema.yaml`, this file's own `CLAUDE.md` losing its obligation to regenerate a
deleted `catalogue.md`, and `scripts/session-dialogue.py` gaining a third menu state
([[the-harness-defects-found-this-session-enter-the-sprint-one-line-each]]).

**Beads moves to Sprint 4**, and he had answered that once already
([[beads-is-carried-to-the-sprint-after-this-one]]).

**Carried to the next session:** the instruments the five rules of `wiki/rules/` still owe and the
first run of the lessons collector
([[the-instrument-work-and-the-first-lessons-collector-run-move-to-the-next-session]]); the
librarian printing each criterion's decider output into the brief, for a third consecutive session
([[the-librarian-prints-each-criterions-decider-output-into-the-brief]]); the flag that would skip
rules 12 and 13, with the prohibition still standing
([[the-injector-is-cheapened-instead-of-adding-a-flag-and-the-prohibition-is-not-lifted]]); the
grammar and build of the `measure:` section
([[the-measure-section-is-a-marked-region-legal-in-any-folder-and-required-nowhere]]); and the
entity split for the gate and its suite, with the owner's plan recorded on [[vault-scripts]].

**What landed on 2026-08-24, as the state of the tree and not as a verdict.** Criterion 3's decider
prints a shortfall of seven pages where it printed thirty-three; the narrowed `idea` verdict is
built and proved in both directions
([[the-idea-and-decided-by-verdict-is-built-narrowed-to-a-non-deferral-cause]]); the gate and its
suite each gained a printed register
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]]). **No criterion is read off
this list — reading one is the owner's** ([[a-sprint-closes-on-its-goal]]).

### What this sprint is scoped against

**Two live prohibitions are to be overturned inside S3, by the owner's decision — and the overturns
are work items rather than done deals.** Both pages are `current` today and stay `current` until a
session writes the page that overturns them. **Nothing here overturns either of them, no page
overturning them exists, and stating the overturn is the owner's** — writing it is the next
session's work.

- **A built proposal stays in `wiki/proposals/` rather than moving to `archive/`**
  ([[a-built-proposal-stays-in-proposals-with-a-built-mark]]). Scoped in as work for S3.
- **The folder set is closed and `wiki/tasks/` is not in it**
  ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). Scoped in, and **deferred to S4**, with the
  category itself; the two move together or not at all.

**Corrected 2026-08-23, later the same day, and the paragraph above is left as it was written.**
One clause of it is false from this date — a page overturning the first of the two now exists. The
rest of it stands, including that stating an overturn is the owner's
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

- **The first is overturned, and that work item is done.**
  [[a-built-proposal-stays-in-proposals-with-a-built-mark]] is `deprecated`, carries
  `superseded_by:`, and has left `wiki/` for
  `archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-a-proposal-gets-an-implemented-mark/pages/`.
  Its successor is
  [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]], and the mark it
  needed is decided on
  [[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]. Both
  rulings are the owner's, taken 2026-08-23.
  - **The path above is stale from the ingest of that day's journal, and the line is left as it was
    written.** The session folder was named from a guess, because the librarian that wrote it had no
    handoff and therefore no fixed slug, and its own `log.md` entry said the folder is what has to
    move if the handoff lands under a different name. It did:
    `archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/pages/` is
    where the page is now. **The old path is not rewritten here** — a path in prose has no detector
    and a record of what was done is supposed to name the address it used
    ([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]],
    [[the-date-of-a-correction-note-is-the-date-the-text-became-false]]). No `sources:` line
    anywhere cited it, so nothing mechanical had to be rewritten with the move.
- **The second is untouched and stays scoped in.**
  [[the-folder-set-is-closed-and-tasks-is-not-in-it]] is still `current`, no page overturns it, and
  `wiki/tasks/` is still deferred to S4 with the category itself. **Two further live prohibitions of
  the same substance are still standing, and the session that writes that overturn must answer
  them**: [[the-brief-has-no-active-tasks-section]] and [[the-retro-has-no-action-queue]]. Naming
  them here is not an argument against the overturn — it is the list it owes an answer to.

### What has landed inside S3, and it is the state of the tree rather than a verdict

**Recorded 2026-08-23.** Each criterion above names the command that decides it, and **no criterion
is read off this list** — reading one is the owner's.

- **The legal `status` values left `scripts/vault-check.sh` for the six `wiki/*/_schema.yaml`
  files.** Five carry `[current, deprecated]`; `proposals/` carries `implemented` as well. The
  hardcoded pair and its message are gone from the gate
  ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
  **`built` is not minted** — it waits on `wiki/tasks/`, deferred to S4 below.
- **The gate gained a verdict, `realised`.** A page carrying `status: implemented` while still in
  `wiki/` is red, and the message says it is not `deprecated` on the way and carries no
  `superseded_by:`.
  - **Corrected 2026-08-23, found later the same day: no such verdict exists, and the line above is
    left as it was written.** It was written and removed on the same day, 2026-08-23, on the
    owner's correction that `implemented` **opens a state rather than naming a place** — a page takes the mark and
    stays in `wiki/` while it is tested for having someone who points at it
    ([[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]],
    [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]). **Read off
    the tree on 2026-08-23 rather than off a memory:** `scripts/vault-check.sh:473-496` carries only
    a comment recording the removal — *"`implemented` DOES NOT, and a verdict saying it did was
    written here on 2026-08-23 and removed the same day when the owner corrected it… So nothing here
    judges `implemented`"* — and `rg -n "realis" scripts/vault-check.sh scripts/vault-check-selftest.sh`
    returns nothing. The vault's own `CLAUDE.md` carries the correction and this register did not.
    **The note is dated the day the text became false**, which is the day this line was written
    about a verdict already removed; the finding, in a later session of that same day, is not what
    dates it
    ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]). What does the testing is
    `scripts/vault-archive.sh`, which refuses the move while no live page names the slug.
- **`scripts/vault-inject.sh` refuses a status it does not know**, rather than reading it as
  not-current. Before this, a rule page with a mistyped status silently stopped rendering.
- **`scripts/vault-archive.sh` gained a precondition.** For `kind = pages` it refuses with exit 2
  unless a live page under `wiki/` names the slug ([[vault-archive-sh]]). It matches the slug as a
  string, so a `[[wikilink]]` and a bare mention both count — **a wider test than the script's own
  `pages_citing`**, which matches a `sources:` path and printed `cited by 0 page(s)` today about a
  page five live pages name.
- **`job_hunt_ai_vault/CLAUDE.md` now states the three values**, which two of them oblige a page to
  leave `wiki/`, and that an implemented proposal is not a supersession.
- **All three refusals were verified by planting offenders in the real tree, in both directions.** A
  sweep of all 530 slugs found exactly one page the archive precondition would refuse — the
  corpus's single orphan — so it produces no false refusal today.

**owner selected: an implemented proposal moves with `status: implemented` and a citation from the
live successor, carrying neither `deprecated` nor `superseded_by:`** — 2026-08-23. A selection
rather than an utterance: the session put the librarian's reading to him and he affirmed it, so the
label stands verbatim and none of it is signed as his own words
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

### What S3 owes, read on 2026-08-23

- **No selftest case exists for any of the three refusals above.**
  `scripts/vault-check-selftest.sh` and `scripts/hook-selftest.ps1` do not know about `realised`,
  the injector's refusal, or the archive precondition. **Criteria 1 and 2 are decided by those two
  suites, so neither is decidable today.** This is the first thing the next session owes.
  - **Corrected 2026-08-23, found later the same day: `realised` is not one of the three**, for the
    reason given under the landed list above — the verdict does not exist. The two suites still know nothing of the
    injector's refusal or the archive precondition, and that half of the line stands.
- **The 29 pages in `wiki/proposals/` are unmarked** — every one of them `status: current`. Which of
  them are implemented is the owner's reading and not a sweep's, and **at least three carry a
  recorded reason not to move**, already noted in the carried items below.
- **Phases A, C, D, E, F, G and H of the plan the owner approved at the opening are not started.**

### Deferred to S4, explicitly

- **the `wiki/tasks/` category, and the tick-who-writes question** with it
  ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]);
- **the `built` mark, which depends on tasks** — whether it is a third `status` value or a field of
  its own is still his ([[a-built-proposal-stays-in-proposals-with-a-built-mark]],
  [[proposals-are-a-folder-not-a-status]]);
- **a mechanism proving `basis: human`**;
- **the back-fill of `decided_by:`, 314 pages.** Criterion 3 asks only that the field be legal and
  that the shortfall be counted; filling it in is not this sprint's work.
  - **Corrected later the same day: the population this figure counts is now two folders, and the
    figure itself does not survive being checked.** The item is left exactly as written, because a
    count is written with its date or not written at all. `314` was written earlier on 2026-08-23 as
    the six-folder count of pages lacking the field; **it is not derivable from anything in this
    store, and it did not agree with the tree it was written against** — the corpus stood at about
    530 pages then, no page carried `decided_by:` then and none does now, so the six-folder count was
    the whole of `wiki/`.
    **Counted later the same day:** 543 pages in `wiki/`, of which 0 carry the field. **Under the
    narrowing the population is 46** — 31 in `wiki/proposals/` and 15 in `wiki/rules/` — and the
    back-fill stays deferred to S4 over that population
    ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**Corrected 2026-08-23: the shape of the mark is settled, and only the minting is still deferred.**
The second item asks whether the mark is a third `status` value or a field of its own; the rulings
of that day make it a value — `implemented` is one, legal in `wiki/proposals/` alone
([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]],
[[proposals-are-a-folder-not-a-status]]). What stays deferred to S4 is `built` itself, whose test is
a task list and therefore waits on `wiki/tasks/`. The rest of this list is untouched.

### What landed in the second session of 2026-08-23, and it is the state of the tree rather than a verdict

**Recorded at the ingest of that session. Each criterion above names the command that decides it,
and no criterion is read off this list — reading one is the owner's.**

- **`decided_by:` exists.** Declared `optional` in `wiki/proposals/_schema.yaml` and `required` in
  `wiki/rules/_schema.yaml`, promoted only after every rule page carried it. `scripts/vault-check.sh`
  reddens a target whose `type:` is not `decision`, and `--lint` counts the shortfall over those two
  folders ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).
- **`refused` and `idea` are minted in `wiki/proposals/`**, and both are red in every other folder
  ([[a-refused-proposal-is-archived-and-takes-status-refused]],
  [[an-idea-is-a-proposal-with-an-immature-status]]).
- **`Links:` is legal in all six schemas and no script writes it**, deliberately: the writer was
  ruled to be a script rather than an agent
  ([[links-is-filled-by-a-script-from-the-bodys-wikilinks]]).
- **`scripts/vault-archive.sh` gained a second precondition** — a proposal carrying
  `status: refused` is not released without `decided_by:` — and had its `--include` operand
  repaired, which had been running the `pages` precondition with no file filter at all
  ([[vault-archive-sh]],
  [[an-option-after-a-double-dash-is-an-operand-and-the-search-runs-unfiltered]]).
- **The link sweep now excludes the four RAW archive kinds**, which is the repair that unblocked the
  archive step of the previous ingest
  ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).
- **The style rule is written and renders into `CLAUDE.md`.** Its watcher is the owner, and it
  governs what a session writes for him rather than what goes into `wiki/`
  ([[write-plainly-name-the-source-and-say-what-is-not-done]],
  [[the-style-rules-watcher-is-the-owner-and-it-governs-chat-alone]]).
- **`ask-before-weakening-or-working-around-a-rule` is ratified**, nine days after it began being
  enforced with no decision behind it
  ([[the-ask-before-weakening-rule-is-ratified-after-being-enforced-without-a-decision]]).
- **The vault's own `CLAUDE.md` was corrected in four places**, one of which strikes the
  `concepts`/`lessons` bullet whole
  ([[the-clause-that-concepts-describes-the-product-is-struck]]).

**Readings taken at the ingest, each from its own invocation**
([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]): `bash scripts/vault-check.sh`
exits 0 with the standing advisory at `7 of 15`; `bash scripts/vault-check.sh --lint` exits 0 and
now prints a `decided_by:` line naming every page in `wiki/proposals/` that lacks the field;
`bash scripts/vault-authority.sh --check` exits 0. **The two suites criterion 1 names were not
re-run at this ingest** — the journal's readings are `caught 168, missed 0` and
`caught 123, missed 0`, both exit 0.

### What this sprint gained as work, in the second session of 2026-08-23

- **The librarian prints each criterion's decider output at every ingest, into the brief** — the
  owner's design, not built. Files to change: `.claude/agents/vault-librarian.md` and whatever
  generates `brief.md` ([[the-librarian-prints-each-criterions-decider-output-into-the-brief]]).
- **Criterion 1's decider must count all three ways a rule closes**, not selftest cases alone. The
  owner ruled the command is what changes, never the criterion
  ([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]).
- **A verdict pairing `status: idea` with `decided_by:` is ordered built**, and the ordering is part
  of the item: the back-fill of `wiki/proposals/` comes first, or the verdict reddens every page in
  the folder and locks the librarian out of the fill
  ([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]],
  [[a-verdict-pairing-the-idea-status-with-a-named-decision]]).
- **A script that fills `Links:` from the bodys wikilinks**, added to the sprint on his own words
  ([[links-is-filled-by-a-script-from-the-bodys-wikilinks]]).
- **The suite is made cheaper, measurement first** — exclude the sandbox path from the virus
  scanner, read the result, and only then narrow the gate
  ([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).
- **`plant_rule_page` is decoupled from a real page slug**, which forty-three selftest cases now
  stand on ([[a-fixture-helper-that-hardcodes-a-page-slug-couples-every-case-built-on-it]]).

### What that session deferred, with the consequence of each

- **The ratification sweep — 27 blocks across 22 pages — for a third consecutive session**, and the
  first time with the list in front of him. Two of the 27 sit on pages the session's own work rests
  on ([[the-ratification-sweep-waits-for-a-session-of-its-own]]).
- **The `decided_by:` back-fill in `wiki/proposals/`.** It blocks the `idea` pair he ordered built,
  and it is the next session's first item.
- **The hook that writes `- miss:` in plan mode**, with his instruction to raise it again next
  session. The feedback rule has now been broken eight times for the same reason
  ([[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).
- **Region coverage, criterion 4, at `7 of 15`.** The eight unmarked files are unchanged, and this
  is never to be reported as coverage improving
  ([[the-region-coverage-figure-is-dated-where-it-stands]]).
- **The ratification hook — phase 7 of the approved plan — cut whole rather than half-built**
  ([[the-ratification-hook-is-cut-whole-and-what-does-not-fit-moves-to-the-next-session]]).
- **Beads — a question for the owner and not an item.** The session does not know what the word
  means here, which is the whole of the problem, and it has been named twice without ever being put
  back to him. **It is carried as a question rather than as work**, because nothing can be scoped
  until it is answered.
- **Whether the style rule also governs `wiki/`** — answered *no for now*, so the question is closed
  rather than carried ([[the-style-rules-watcher-is-the-owner-and-it-governs-chat-alone]]).
- **The Obsidian CLI**, recorded as a proposal on his instruction and not started
  ([[the-obsidian-cli-as-a-reading-surface-for-this-store]]).

### Carried from S2

**Nothing was dropped when S2 closed**, so no `decisions/` page for a dropped item is owed
([[a-sprint-closes-on-its-goal]]).

**Four of S2's seven criteria carry: 1, 3, 4 and 6.** Criterion 2 was met before S2 opened;
criteria 5 and 7 are met on the owner's own verdicts. The readings are in the S2 block below and
are not restated here.

**And every item of S2's *next* lists carries** — **owner, 2026-08-23:** «Все, что в нем осталось -
переносим на s3», which reaches them. They are reproduced below **with their S2 numbers kept**, so
that no renumbering hides one and no two are merged. **Whether an answered item leaves the list is
item 24, and item 24 has never been put to him**, so the answered ones are carried with their state
rather than struck out.

**The two sentences above went false on 2026-08-26, and the correction is dated that day**: item 24
was answered, an answered item is struck in place, and the struck items below carry the markup and a
line naming the page that holds the answer
([[an-answered-item-leaves-the-next-list-by-being-struck-in-place]]). The markup was applied on
2026-08-27; nothing on this list is deleted, renumbered or merged.

1. ~~**`/pre-task` must cover `concepts/`, `entities/`, `proposals/` and `rules/`, not `decisions/`
   alone**~~ — **struck 2026-08-27: answered on
   [[the-pre-task-enumeration-covers-every-folder-but-lessons]]**, and the artefact is
   `.claude/agents/pre-task.md:130`, which keeps `concepts`, `entities`, `proposals` and `rules`
   whole ([[a-generated-harness-map]]);
2. ~~**the reading funnel is not delivered as a procedure** — no skill names
   `scripts/vault-catalogue.sh` or `authority.md`~~ — **struck 2026-08-27: answered on
   [[the-reading-funnel-is-delivered-as-a-procedure]]**, and the artefacts are
   `.claude/agents/pre-task.md:108`, which runs `bash scripts/vault-catalogue.sh`, with
   `.claude/skills/vault-lint/SKILL.md:124` and `.claude/agents/vault-librarian.md:135`, which name
   `--near` ([[the-folder-is-the-first-narrowing]]);
3. **`lessons/` becomes a queue drained into `proposals/` at the ingest** — his design, not built
   ([[lessons-become-a-queue-drained-into-proposals]]);
4. **a real data format for `tags.md` and `authority.md`** — half-answered on 2026-08-22: PyYAML is
   a declared `dev` dependency, and the format question is untouched
   ([[a-machine-readable-format-for-the-registers]],
   [[pyyaml-is-declared-rather-than-added-and-the-dependency-rule-is-not-opened]]);
5. **an admission test for mechanisms** — its verdict of 2026-08-22 was narrow: not an acceptance
   criterion of S2, with the proposal neither built nor refused
   ([[an-admission-test-for-mechanisms]],
   [[the-harness-versus-product-split-is-recorded-and-not-acted-on]]);
6. ~~**the `authority.md` families standing over the ceiling of about ten**, rebalancing being a
   judgement about the corpus~~ — **struck 2026-08-26: the ceiling was deleted from the register
   rather than satisfied**, so there is no over-the-ceiling family left to name
   ([[the-authority-registers-family-ceiling-is-deleted]]);
7. ~~**[[an-authority-register-on-the-model-of-the-tag-dictionary]] is retirable** — **and the page
   that said how is itself retired.**
   [[a-built-proposal-retires-once-nothing-on-it-lives-only-there]] was superseded on 2026-08-22 by
   [[a-built-proposal-stays-in-proposals-with-a-built-mark]], which is one of the two prohibitions
   scoped in above, so **how this proposal retires is bound to an overturn that has not happened.**
   Reported here, not resolved~~;
   - **Corrected 2026-08-23: that overturn happened, on the same day this list was written.** An
     implemented proposal now leaves for `archive/` carrying `status: implemented`, so **how** this
     proposal retires is answered; **whether** it is implemented is a reading nobody has given
     ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]);
   - **Struck 2026-08-27: answered on
     [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]**, and the
     artefact is the page itself, now sitting in
     `archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/pages/`
     with `status: implemented`;
8. **the four owed readings**, now carried for an eighth session — whether the `core` criterion
   still sorts `CLAUDE.md` without a remainder; the JavaScript rule page whose ground was
   `/pre-task` arriving unconditionally; which reading the conditional-delivery gate carries; what
   `permissions.defaultMode: "plan"` should mean for a `claude -p` run
   ([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]],
   [[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]],
   [[a-rule-moving-to-conditional-delivery-needs-its-page-first]],
   [[the-vs-code-extension-reads-its-starting-mode-from-user-settings]]);
9. **whether a hook should refuse rather than advise** — the first half was settled on 2026-08-22,
   and **the five mechanisms built and wired to nothing, plus the wider conversation he asked for,
   are still owed** ([[the-dispatch-record-hook]],
   [[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]], [[vault-archive-sh]]);
10. ~~**the recorded objection that proposals should carry no `authority`**, standing unresolved and
    marked on its page ([[an-authority-register-on-the-model-of-the-tag-dictionary]])~~ — **struck
    2026-08-27: answered on [[authority-becomes-the-index-and-is-required-outside-rules]]**, and the
    artefact is lines 207-210 of that page, where the objection was put and refused on 2026-08-26;
11. ~~**the ratification sweep of the owner-attributed blocks**, its own session, headed by
    [[a-refusal-is-conditional-or-absolute-and-nothing-else]]; the list is
    `bash scripts/vault-check.sh --lint` and is not copied here
    ([[the-ratification-sweep-waits-for-a-session-of-its-own]])~~ — **struck 2026-08-27: answered on
    [[a-sweep-may-run-inside-a-session-when-the-list-is-assembled-in-advance-and-shown-whole]]**,
    which carries `supersedes: [[the-ratification-sweep-waits-for-a-session-of-its-own]]` and names
    the sweep that met the replacement condition. **The condition this item names — a session of its
    own — was retired by the owner on 2026-08-24 rather than met**, and a session of 2026-08-27 read
    it as live until `/pre-task` corrected it;
12. ~~**whether a paraphrase that survives ratification is demoted to `basis: inference`** — offered
    and neither taken nor refused, and the one claim keeping
    [[a-quote-is-cyrillic-rule-with-an-advisory-verdict]] alive
    ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]])~~ — **struck
    2026-08-27: answered on [[a-paraphrase-that-survived-ratification-keeps-basis-human]]**, and the
    artefact is line 19 of that page: it keeps `basis: human`, whatever voice it is written in;
13. ~~**`/pre-task` becomes an agent** — **read MET by the owner on 2026-08-22**
    ([[the-pre-task-agent]]). Carried rather than struck out, because item 24 is unanswered.~~ —
    **struck 2026-08-27: answered on [[the-pre-task-agent]]**, and the artefact is
    `.claude/agents/pre-task.md`, landed in commit `35163c9`; the declaration of 2026-08-26 below
    struck this line and this carries the markup;
14. **the blocking write gate waits on `record-the-dispatch.ps1` firing in a live session** —
    **read NOT MET by the owner on 2026-08-22, and it does not close on a reading**: he ruled that
    it closes when he is satisfied the mechanism works and gives his confirmation
    ([[a-chain-proved-in-halves-is-not-proved]],
    [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]);
15. **the count of readers of `governs:` becomes a selftest case**
    ([[the-count-of-a-fields-readers-lives-nowhere]],
    [[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]);
16. **the session slug is written to a file and `/handoff` reads it**
    ([[the-session-slug-is-written-to-a-file-and-the-handoff-reads-it]]);
17. ~~**item 6 above is eleven slugs in one family**, and rebalancing went to `/vault-lint` on his
    ruling rather than being done in passing~~ — **struck 2026-08-26 with item 6: the ceiling the
    count was measured against is deleted**, and the rebalancing-is-`/vault-lint`-work clause it
    cites is unaffected ([[the-authority-registers-family-ceiling-is-deleted]],
    [[authority-becomes-the-index-and-is-required-outside-rules]]);
18. **step 4, the blocking write gate** — both of its gates must clear and only one is close; the
    second is that a real ingest does not deadlock behind it, verifiable only by building it and
    running one ([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]],
    [[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]);
19. **whether the `built` mark is a third `status` value or a field of its own** — his own words,
    and **deferred to S4** above, because it depends on tasks. Until it exists the corpus disagrees
    with its own ruling ([[a-built-proposal-stays-in-proposals-with-a-built-mark]],
    [[proposals-are-a-folder-not-a-status]]);
    - **Corrected 2026-08-23: the shape is answered and the disagreement named here is a
      different one now.** The mark is a `status` value rather than a field of its own, and the
      ruling this item measured the corpus against was overturned the same day
      ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]],
      [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]). The mark
      the live ruling needs exists; what carries is `built`, with `wiki/tasks/`, and the 29
      unmarked pages in `wiki/proposals/` recorded above;
20. ~~**whether phase 1 of the ritual keeps dropping `deferral` and `divergence`**
    ([[the-pre-task-agent]],
    [[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]])~~ — **struck 2026-08-27:
    answered on [[the-pre-task-keeps-deferral-in-phase-one-and-drops-divergence-alone]]**, and the
    artefact is `.claude/agents/pre-task.md:118-122`, landed in commit `6a22ffc`;
21. ~~**whether `scripts/vault-catalogue.sh` gains a `binding:` column**
    ([[the-page-list-is-a-query-not-a-generated-file]])~~ — **struck 2026-08-27: answered on
    [[the-catalogue-gains-no-binding-column-and-the-question-is-withdrawn]]**, and the artefact is
    lines 20-22 of that page, where the owner withdrew the question rather than deferring it;
22. ~~**`bash scripts/vault-authority.sh --near` is named by no skill and no agent as a reading
    step**~~ — **struck 2026-08-27: answered on
    [[the-reading-funnel-is-delivered-as-a-procedure]]**, and the artefacts are
    `.claude/skills/vault-lint/SKILL.md:124` and `.claude/agents/vault-librarian.md:135`, each of
    which names `--near`; the declaration of 2026-08-26 below struck it as stale and this carries the
    markup;
23. ~~**eight vault `.md` files are CRLF on disk** against `.gitattributes`; git normalises on commit
    and nothing measures it — `/vault-lint`~~ — **struck 2026-08-27: answered on
    [[the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them]]**, and the artefact is
    the reading `grep -rlU $'\r' job_hunt_ai_vault --include=*.md | wc -l` → 0; the instrument is
    `.claude/skills/vault-lint/SKILL.md:45`;
24. ~~**whether an answered item leaves this list.** Never put to the owner, and it carries
    unanswered like the rest.~~ — **struck 2026-08-27: answered on
    [[an-answered-item-leaves-the-next-list-by-being-struck-in-place]]**, and the artefact is line 21
    of that page: an answered item is struck where it stands, with one line naming the page holding
    the answer.

**Two further lists carry as well and are not restated here**, for the same reason S2 did not
restate them: the *next* list of 2026-08-20 with its sixteen items, and the unnumbered *carried
unchanged* paragraph beneath the list of 2026-08-22. Both are read in the S2 block below, which is
where they stand ([[the-deferrals-of-this-session-go-onto-the-sprint]]).

### What landed in the session of 2026-08-24, and it is the state of the tree rather than a verdict

**The feedback channel stopped requiring a session to write a file.** A session prints a fenced
`VAULT-FEEDBACK` block and `.claude/hooks/catch-the-feedback.ps1` files it
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]], [[the-feedback-catcher-hook]]).

**Which criterion each phase feeds, named rather than implied:**

| what landed | the criterion it touches | what it does to it |
|---|---|---|
| the catcher, with fifteen cases in `scripts/hook-selftest.ps1` | **criterion 1** | one of the six rules owing an instrument now has one; **five do not**, so the criterion moves and does not close ([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]) |
| the successor rule page, governing three files | **criterion 4** | region coverage read `7 of 15` before the ingest and `8 of 15` after it — `.claude/skills/vault-ask/SKILL.md` carries its first region ([[a-governed-file-with-no-region-is-an-advisory]]) |
| `scripts/session-dialogue.py` and `/retro` step 0 | none | it is harness work the sprint did not name, and it is recorded as such rather than counted against a criterion |
| `/vault-lint` gains a lessons-queue dispatch | none | the collector has never been run ([[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]]) |

**Readings taken by that session, each from its own invocation**: `session-dialogue-selftest.py`
caught 32, missed 0; `hook-selftest.ps1` caught 138, missed 0, up from 123;
`vault-check-selftest.sh` caught 168, missed 0 in 34m8s; `vault-check.sh` exit 0;
`vault-inject.sh` 0/0/0/0.

**What that session did not do**, and none of it is a shortfall: the suite is not narrowed, the
lessons collector has not been run, and the `idea`/`decided_by:` verdict and back-fill were decided
and not built.

### Two figures in the text above are corrected here rather than in place — 2026-08-24

**The `decided_by:` population.** The passage in *Deferred to S4* reads *"under the narrowing the
population is 46 — 31 in `wiki/proposals/` and 15 in `wiki/rules/`"*, measured 2026-08-23.
**Measured 2026-08-24: 50 pages, of which 17 carry the field and 33 do not.** `wiki/rules/` is
**full at 16 of 16**, so the entire shortfall is in `wiki/proposals/`, which stands at **1 of 34**.
The old figures stand where they are, dated to the day they were taken
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**The claim that the verdict "reddens every page in the folder".** It holds under only one of three
readings of the pairing, and under the other two nothing reddens. **The ordering the item protects
does not depend on which reading is right** — back-fill first, verdict second — so the item stands
and its justification is narrower than it says
([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]],
[[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

### Two lines of this sprint are struck rather than corrected — 2026-08-25

**A drifting list is repaired by deleting the line, not by extending it**
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]). Both lines below stay legible
where they stand and are struck here.

**Struck: the item obliging the vault's `CLAUDE.md` to lose its `catalogue.md` obligation.** It is
already done. That file no longer obliges regenerating a catalogue and states the opposite; live
mentions survive only in `.superpowers/sdd/` transcripts and one design spec under `docs/`. The item
sits in *What entered S3 on 2026-08-24* and was work for a day after it had been completed
([[the-harness-defects-found-this-session-enter-the-sprint-one-line-each]], [[pages-base]]).

**Struck: the entry listing [[a-refusal-is-conditional-or-absolute-and-nothing-else]] as pending in
the ratification sweep**, item 11 of *Carried from S2*. **That page was ratified in the owner's own
Russian on 2026-08-22 and says so in a section of its own.** A `/pre-task` reported it as a page the
sweep's instrument cannot reach — and it is unreachable **because it is already correct**. The sweep
itself is a live item and is not struck by this
([[the-owner-signature-is-removed-where-the-words-are-not-his]]).

### What the session of 2026-08-25 put into S3, and it is the state of the tree rather than a verdict

**Nothing was built.** The session decided twelve items, wrote a plan, had it checked by `/pre-task`,
revised it against the findings, and committed it
([[the-plan-is-committed-and-the-execution-moves-to-a-session-of-its-own]]). **No criterion is read
met or unmet here, and closing this sprint is the owner's.**

**What became work, each with a page:** the overturn of the gate's alphabet test, in the order the
sweep forces ([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]],
[[the-owner-signature-is-removed-where-the-words-are-not-his]]); the schema-file exception delivered
by a flag of its own ([[the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own]]);
`scripts/session-dialogue.py` with four menu states rather than three
([[the-harness-defects-found-this-session-enter-the-sprint-one-line-each]]); the measure section's
grammar and its writer script ([[the-measure-section-grammar-is-one-line-per-number]],
[[a-gauge-is-written-by-a-script-that-runs-the-command]]); the archive sweep's reporting shape
([[the-archive-sweep-reports-a-refusal-and-the-gate-stays-silent-about-placement]]); the lessons
collector as a reading dispatch
([[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]); the
`.claude/rules/` file that closes the meta-rule
([[the-ask-before-weakening-rule-gets-a-claude-rules-file-and-the-owner-as-its-watcher]]); and the
repository's `CLAUDE.md` joining the owner-block rule's destinations
([[the-owner-block-rule-gains-the-repository-claude-md-as-a-destination]]).

**What landed at the ingest rather than in the session:** the style rule's slice, amended on his
ruling and rendered into `CLAUDE.md`
([[the-style-rules-slice-is-amended-rather-than-superseded]]).

**Two deferrals now owe the sprint they happen in, or a refusal**, by the rule agreed the same day
([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]]): the flag that would skip the
gate's delegated rules ([[the-gate-flag-fork-is-recorded-and-nothing-is-built]]), and the librarian
printing each criterion's decider output into the brief
([[the-librarian-prints-each-criterions-decider-output-into-the-brief]]).

**Beside criterion 4, read off the tree on 2026-08-25 and not judged here.** **No rule in
`scripts/vault-check.sh` reads the content of `index.md`** — rule 1 checks its existence alone. **And
rule 5b is vacuous**: the repository's `CLAUDE.md` holds zero `[[wikilinks]]`, so the rule can never
print, while the file names four skills whose existence nothing verifies. **So the criterion has three
clauses and only the third has ever been read** ([[the-index-reads-and-the-schema-writes]],
[[the-repository-claude-md-becomes-a-dispatch-table]], [[a-governed-file-with-no-region-is-an-advisory]]).

**And one finding he named belongs here rather than to any page**: a dozen items taken to the
discussion stage with nothing built is a shape that costs more attention than it returns. **One item
carried through discussion, decision, build and verification** is the shape he asked for at the end
of the session.

### What the session of 2026-08-26 built, and it is the state of the tree rather than a verdict

**The plan's harness half is built and verified; its librarian half was not started.** Built, each
with cases: **A1** (a flag of its own for the per-folder schemas,
[[the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own]]); **A3** (four menu states,
[[a-menu-resolves-to-a-state-and-an-interrupt-counts-as-an-answer]]); **B3** (the catcher's note on an
unquoted attribution, [[the-feedback-catcher-hook]]); **E1** ([[vault-measure-py]]); **E2** (gate
rule 15, [[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]);
**E3** (rule 11 recognises a measure marker); **E6** (a case per refusal); **G** (the librarian's
channel, [[the-librarian-writes-its-log-and-the-brief-carries-what-it-hands-back]]). **A2 required
nothing** — the ingest of 2026-08-25 had already struck both lines.

**Nothing was committed.** The whole session stands uncommitted in the working tree at `9950dbd`.

**No criterion is read off this list — reading one is the owner's** ([[a-sprint-closes-on-its-goal]]).

### What entered S3 on 2026-08-26, one line per item

**The plan's unbuilt half, line by line rather than into a second plan document** (owner selected it,
[[the-deferrals-of-this-session-go-onto-the-sprint]]):

1. **B1** — the context obligation for a quoted line, **addressed to the wrong rule page.** It
   belongs to [[speak-the-feedback-in-the-turn-and-the-hook-files-it]], which already governs
   `CLAUDE.md` and `/vault-ask`; the owner-block slice delivers it to `/ingest`, which writes no
   feedback blocks. Not doing it delivers the requirement to the party that cannot use it
   ([[a-quote-written-for-the-librarian-carries-its-context]]).
2. **B4** — the remaining dated notes of the owner-block sweep.
3. ~~**C1** — a dated note owed to
   [[a-sweep-may-run-inside-a-session-when-the-list-is-assembled-in-advance-and-shown-whole]], whose
   own sentence — *the list is read from the run, never from a page* — is broader than the reason
   under it. **Not doing it leaves the next `/pre-task` reading a live breach.**~~ — **struck
   2026-08-27: answered on
   [[a-sweep-may-run-inside-a-session-when-the-list-is-assembled-in-advance-and-shown-whole]]**, and
   the artefact is line 54 of that page, a heading dated 2026-08-26 that says the clause is wider
   than the reason under it.
4. **C2 and C3** — the rest of the sweep of 27 owner-attributed blocks, which is unstarted and keeps
   rule 14 live ([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]]).
5. ~~**D** — the stated-count deletion. **Discharged differently at the ingest of 2026-08-26**: the
   eighteen-condition list moved into a dated history section on [[vault-scripts]] rather than being
   deleted, on the owner's ruling, and the one live citation of the number survives the move~~ —
   **struck 2026-08-27: answered on
   [[the-vault-scripts-page-stays-a-hub-and-the-gate-and-its-suite-get-subject-pages]]**, and the
   artefact is `job_hunt_ai_vault/wiki/entities/vault-scripts.md:41`, the dated history heading the
   eighteen-condition list moved under.
6. **E4 and E5** — the remaining measure-region work.
7. **`vault-measure.py --refresh` run against the corpus**, which has never written a number outside
   a fixture because no measure region exists yet ([[vault-measure-py]]).

**Two repeated deferrals now name S3, which discharges the obligation that a repeated deferral names
its sprint or is refused** — owner, «Да, называем обеим S3»
([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]]):

8. **the gate's flag fork** ([[the-gate-flag-fork-is-recorded-and-nothing-is-built]]);
9. **the librarian printing each criterion's decider output into the brief**, now for a fourth
   consecutive session ([[the-librarian-prints-each-criterions-decider-output-into-the-brief]]).

**And three items the session's own work created:**

10. ~~**`scripts/lessons-queue.py`'s counter**, which reads *cited by a rule or a proposal* as
    *handled*. **Fixed after the drafts are filed, not before**, and the queue's fall from 104 is an
    artefact rather than progress
    ([[the-lessons-queue-counter-is-fixed-after-the-drafts-are-filed]],
    [[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]]).~~ —
    **struck 2026-08-27: answered on [[the-lessons-queue-counter-prints-cited-and-landed-apart]]**,
    and the artefact is `scripts/lessons-queue.py:95-96`, where `cited` and `landed` are computed
    and printed apart.
11. **The archiver the owner described does not exist** — the sweep over `lessons/`, the sweep that
    finds `deprecated`/`superseded_by:` pages and checks their successor is live, and the mechanical
    `status: archived` write with its schema value
    ([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]],
    [[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]]).
12. **A `wiki/rules/` page for "file content is written with Write or Edit and never through a
    shell"**, with its region, because a governed file with no region is a shortfall against
    criterion 4 ([[file-content-is-written-with-the-tool-and-never-through-a-shell]]).

**One topic rather than an item:**

13. **Archiving policy for every page type in the wiki** — a named topic for the next session, on his
    own words, and **no design is written before the conversation**
    ([[archiving-policy-for-every-page-type-is-a-named-topic-for-the-next-session]]).

**Two harness items decided the same day and not built:**

14. ~~**`/retro` gains a mandatory `VAULT-FEEDBACK` instruction** — his words, after a retro that filed
    none through eight exchanges
    ([[divergence-the-retro-filed-no-feedback-block-while-it-ran]]).~~ — **struck 2026-08-26: done in
    two shapes, and it took a third silence to get there.** The instruction is a rendered rule
    ([[every-turn-of-a-retro-files-a-feedback-block]]) and a demand at the head of
    `.claude/hooks/remind-the-smoke.ps1`, with a selftest case asserting the hook says it. **Struck
    with a warning rather than as closed**: neither shape fires per turn, which is the cadence the
    rule is about, and the retro that ordered the strike had itself run nine replies with zero blocks
    before the owner caught it.
15. ~~**`/retro` gains a step-0 launch of the full selftest suite in the background**, permanently
    ([[the-selftest-suite-runs-in-the-background-while-the-retro-proceeds]]).~~ — **struck 2026-08-26
    by the declaration below, and the markup was added 2026-08-27**, so this item now carries its
    strike where every other struck item of this file carries one
    ([[an-answered-item-leaves-the-next-list-by-being-struck-in-place]]).

**And one correction owed to every skill and plan naming `pwsh`:** there is no `pwsh` on this
machine. Windows PowerShell 5.1 is the only shell present, and the working command is
`powershell -NoProfile -File scripts/hook-selftest.ps1`.

### What two later sessions of 2026-08-26 built, and it is the state of the tree rather than a verdict

**Built by hand, all outside `wiki/`, nothing committed at the time the journals were written**
(HEAD `f5817c4`):

- **`.claude/agents/pre-task.md`** — phase 1 keeps `binding: deferral` and drops `divergence` alone;
  the override paragraph is deleted
  ([[the-pre-task-keeps-deferral-in-phase-one-and-drops-divergence-alone]]).
- **`scripts/lessons-queue.py`** — `decisions/` is read as a citer and the answer prints as `CITED`
  beside `LANDED`; the queue fell from 100 to 37
  ([[the-lessons-queue-counter-prints-cited-and-landed-apart]]).
- **`scripts/vault-check.sh`** — rule 15's interpreter probe no longer runs the Microsoft Store stub;
  the gate had hung for an hour ([[python3-on-this-machine-is-the-microsoft-store-stub]]).
- **`.claude/agents/vault-librarian.md`** — the gate instruction now matches the ritual
  ([[divergence-the-librarians-gate-instruction-described-something-nobody-has-ever-done]]).

**Item 10 of the list above is discharged** by the second of those.

**Readings:** gate 20.45–21.5 s, exit 0, region coverage `8 of 15`. `hook-selftest.ps1` caught 148,
missed 0. **`vault-check-selftest.sh` has no reading from either session** — one run was launched and
never returned, the other was killed unfinished at 56 minutes
([[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]]).

**No criterion is read off this list — reading one is the owner's** ([[a-sprint-closes-on-its-goal]]).

### What entered S3 later on 2026-08-26, one line per item

**The plan's third phase, deferred whole by the owner and ordered as the next session's first work
after the check-system items** ([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]).
**The slug deletions come first**, because a retirement's slug leaves `authority.md` before the page
moves ([[retiring-a-page-removes-its-slug-from-the-authority-register]]):

16. ~~**Delete `prose-path-detector` and `authority-register-design` from `authority.md`**, then move
    [[a-path-detector-for-prose-references]] (`status: refused`, set at this ingest) and
    [[an-authority-register-on-the-model-of-the-tag-dictionary]] (`status: implemented`, set at this
    ingest) into `archive/` with `bash scripts/vault-archive.sh … pages`.~~ — **struck 2026-08-26:
    done.** Both slugs are out of `authority.md`, both pages are in
    `archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/pages/`,
    and the register agrees with the tree in both directions
    ([[retiring-a-page-removes-its-slug-from-the-authority-register]]).
17. ~~**The green-gate selftest case is removed from `scripts/hook-selftest.ps1`**~~ — **struck
    2026-08-27: answered on
    [[the-green-gate-selftest-case-is-thrown-out-rather-than-deferred-again]]**, and the artefact is
    `scripts/hook-selftest.ps1:496-501`, where the comment recording the removal stands in the place
    the case held.
18. ~~**The `authority.md` family ceiling and its three over-the-ceiling notes are deleted.** They are
    marked false in place at this ingest~~ — **struck 2026-08-26: done earlier the same day.** The
    word *ceiling* survives in `authority.md` only inside the slug `authority-family-ceiling`
    ([[the-authority-registers-family-ceiling-is-deleted]]).
19. ~~**The five CRLF files in the vault are renormalised**, four under `wiki/` and one under
    `raw/handoffs/`, which is immutable and stays~~ — **struck 2026-08-26: done earlier the same
    day.** No file under `job_hunt_ai_vault/wiki` or `job_hunt_ai_vault/raw` carries a carriage
    return today ([[the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them]]).
20. ~~**`/vault-lint` gains a CRLF count step**, and the count is not `grep -c $'\r'`.~~ — **struck
    2026-08-27: answered on
    [[the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them]]**, and the artefact is
    `.claude/skills/vault-lint/SKILL.md:45-54`, where the step counts with `tr -dc '\r' | wc -c`.
21. ~~**`scripts/lessons-queue.py`'s docstring title and the `/vault-lint` collector brief are
    rewritten** — both describe a population the script no longer measures.~~ — **struck 2026-08-27:
    answered on
    [[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]]**, and the
    artefacts are `scripts/lessons-queue.py:2-9` and `.claude/skills/vault-lint/SKILL.md:89-93`,
    neither of which carries a figure now.
22. ~~**[[our-javascript-does-not-choose-which-rows-are-on-screen]] moves to `decisions/`** with
    `binding: prohibition`, minting an `authority:` and losing `governs:` and `render:`; the region
    leaves `CLAUDE.md` in the same change~~ — **struck 2026-08-26: done in another shape, and one
    half of it is owed.** The rule folded into [[javascript-policy]] rather than becoming a page of
    its own, so nothing was minted and the register is untouched; **the region is still in
    `CLAUDE.md`**, because the injector cannot remove a region no successor renders into, and that
    edit is the session's ([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]],
    [[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]).

**The check system, ordered by the owner as the first work of the next session:**

23. ~~**A `proposals/` page settling who runs which check and when** — *"это первым делом"*~~ —
    **struck 2026-08-27: answered on [[a-proposal-page-settles-who-runs-which-check-and-when]]**,
    and the artefact is
    `job_hunt_ai_vault/wiki/proposals/make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation.md`.
24. ~~**A smoke runner**, with a floor that always runs and a selection the session names~~
    ([[the-smoke-runner-is-built-first-thing-next-session]]). ~~**It is blocked on a narrowing flag on
    `scripts/vault-check-selftest.sh` that does not exist**~~
    ([[the-suite-gets-a-subset-mode-that-issues-no-verdict]]) — **the blocker clause is struck
    2026-08-26: the flag exists and was never missing.** `--only <pattern>` is parsed at
    `scripts/vault-check-selftest.sh:31`, landed in the session of 2026-08-24 and was used twice on
    2026-08-26. **Only the clause is struck, not the item**: whether the runner itself is done is a
    reading of the tree that belongs to whoever takes it, and `make smoke` was measured green at
    66-69 s the same day
    ([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).
    **The item itself is struck 2026-08-27: answered on
    [[the-smoke-runner-is-built-first-thing-next-session]]**, and the artefact is `Makefile:70-85`,
    where the five-step floor runs unconditionally and `ONLY=` adds the slice.
25. ~~**A single entry point for both `smoke` and `suite`**, `make` being the revived candidate and
    present on this machine~~ — **struck 2026-08-27: answered on
    [[the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate]]**, and the artefact is
    `Makefile:52`, whose `.PHONY` line declares six targets.
26. ~~**A selftest case for the hanging-interpreter defect**, which landed without one~~ —
    **struck 2026-08-27: answered on
    [[a-defect-one-day-old-outlived-the-selftest-that-shipped-with-it]]**, and the artefact is
    `scripts/vault-check-selftest.sh:2398`, whose fixture `plant_store_stub()` stands at line 1409
    of the same file.

**And one harness item with a test surface behind it:**

27. **The attention-list grouping defect in `scripts/session-dialogue.py`**, whose repair moves with
    a 52-case selftest ([[the-grouping-defect-in-the-dialogue-extract-is-an-s3-harness-line]]).

**Three lines of this sprint are struck rather than corrected — 2026-08-26**

- **Item 15 above is struck.** `/retro` does **not** gain a step-0 launch of the full suite: the
  suite came out of the session loop the same day and runs at a sprint's close
  ([[the-suite-stops-running-every-session]]).
- **The `/pre-task`-becomes-an-agent line carried from S2 is struck**, read MET by the owner on
  2026-08-22 and standing only because a neighbouring item was open.
- **The `--near` item carried from S2 is struck as stale**, not as done: it is named by a rendered
  rule region in `.claude/agents/vault-librarian.md` and by `.claude/skills/vault-lint/SKILL.md`.

**An answered item is struck in place from here on, on one line naming the page that holds the
answer** ([[an-answered-item-leaves-the-next-list-by-being-struck-in-place]]).

### What the retro of 2026-08-26 put onto this sprint, each with the destination the owner named

**Each line names where it goes, because two of the four are not this sprint's to work** — a line
filed here with no destination is a line the next reader has to place.

28. **The product's exposure at `/handoff`** — `uv run pytest` stays outside `smoke` and outside the
    block, so a session that edited `src/` can hand its journal to the librarian with the product
    untested. **Addressed to the first product sprint**, not to S3. The hole is already named on the
    arrangement page and this line is the address rather than the finding
    ([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).
29. **What enforces a red `suite` blocking a sprint's close** — nothing does today; the obligation is
    written and unbuilt. **Addressed to the conversation about closing a sprint**, which the owner
    called a topic of its own. Not an S3 build item, and no design is written before that
    conversation ([[a-sprint-closes-on-its-goal]]).
30. ~~**`make test` was not run in the session of 2026-08-26, and it is the next session's first work.**
    The database was not up, docker did not answer, every test errored at setup, and the run was
    killed before pytest printed its `ERRORS` block — **so the cause is inferred and not read.**
    Re-running it is what turns the inference into a reading~~ — **struck 2026-08-27: answered on
    [[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]**, and the reading is
    `make test` against the renormalised working copy with the database up → **614 passed, exit 0,
    133 s**; nothing was skipped, nothing errored, and nothing failed to collect, so there is no
    unrun remainder for that page's second half to name.
31. ~~**A rule page for the retro's feedback obligation**~~ — **struck the day it was added: it is
    item 14 above and it landed 2026-08-26** ([[every-turn-of-a-retro-files-a-feedback-block]]).
    Recorded here so that the sprint's own list says where item 14 was discharged, and struck in
    place rather than omitted ([[an-answered-item-leaves-the-next-list-by-being-struck-in-place]]).

**The numbering continues the list above and does not restart.** Two of these four are addressed
outside S3 and stay on this page anyway: a line moved to a sprint that does not exist yet is a line
in no file at all.

### The conversations named for the next session, as the journal of 2026-08-26 listed them

Archiving policy per page type; the wide half of the per-type schema; whether a hook refuses rather
than advises, with the five mechanisms wired to nothing; a machine-readable format for the registers;
the `built` mark in detail; the fog finding; the admission test for mechanisms and the
harness/product split; **the reading funnel, raised by the owner himself that day**
([[the-reading-funnel-is-delivered-as-a-procedure]]); and **optimisation**, holding the suite's
34-minute runtime, the ~26k-token cost of reading the extract whole, and the dispatch costs
([[optimisation-becomes-a-conversation-topic-of-its-own]]).

**No count is written here.** The journal calls the list *ten conversations … now one longer* and
enumerates nine, and three counts of that session's own decisions circulated before one was checked
— 24 in the plan, 25 in conversation, 28 in the file. The list is the answer; a number beside it is
a second thing to keep true
([[a-stated-count-drifts-from-the-list-it-heads]], [[a-title-names-what-is-counted-instead-of-counting-it]]).

**Added by the ingest of 2026-08-26, from the journal that named it: the librarian's own work and
its dispatch.** **owner:** «Отметь плиз на следующую сессию - обязательно поднять вопрос работы
библиотекаря и его диспатча. Обсудим там.» **It carries no sprint line by the journal's own
account** — the dispatch that wrote that session's sprint lines had already returned when he named
it — so it is filed here, with the conversations, and not among the work items. What stands behind
it: seven dispatches at 1,224,158 tokens and about 103 minutes, more than half that session's wall
clock, with no split between corpus reading, gate runs and page writing
([[agent-round-trip-cost]]).

### What entered S3 on 2026-08-28, one line per item

**The frontier the owner ruled is written down rather than carried in a conversation** — *«оставшийся
фронтир не теряется и записывается»*
([[the-output-side-is-finished-today-and-does-not-close-the-corpuss-growth]]).

**And the scope of the next session is all of it.** At ratification he corrected the session's
attribution: *"take the first three of six"* described the frame of that day and was never a decision
about how much work follows — **the next session takes all of the optimisation, archiving and process
items** ([[the-archiving-sweep-and-the-dead-link-advisory-move-to-the-next-session]]).

32. **The archiving sweep inside `scripts/vault-archive.sh`** — walks a folder, applies its criterion,
    writes `status: archived`, moves the page, and continues past a refusal, collecting refusals and
    exiting non-zero on the list. Design decided and written; no code
    ([[the-archive-sweep-that-walks-each-folder-and-collects-its-refusals]],
    [[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]).
33. **The gate advisory on a live link into a deprecated page** — keyed on the target's `status:`, an
    advisory and never a red. Design decided and written; no code. It would report 424 link
    occurrences across 210 live pages naming 42 slugs
    ([[the-gate-advisory-naming-a-live-link-into-a-deprecated-page]]).
34. ~~**The decisions agent**, reading only, returning a verdict per page, dispatched at every ingest.
    Three measured inputs: 269 unprocessed decisions, 120 prose-only mentions, 424 links into
    deprecated pages ([[the-decisions-agent-that-reads-the-folder-and-returns-a-verdict-per-decision]]).~~
    — **struck 2026-08-29: answered on [[the-decisions-agent]]**. *(Its cadence changed in the
    building: the folder-wide walk is mode 2, on demand, and mode 1 reads only what a handoff carries.
    Mode 2 has never run, so item 39 stands.)*
35. ~~**The lessons agent**, reading only, writing a proposal draft into `docs/`. Not run for a second
    consecutive session ([[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]).~~
    — **struck 2026-08-29: answered on [[the-lessons-agent]]**.
36. ~~**The rewiring of `/ingest`** to the scheme where the session dispatches and the librarian writes
    what comes back ([[the-ingest-rewired-so-the-session-dispatches-and-the-librarian-writes]]).~~
    — **struck 2026-08-29: answered on [[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]]**.
    *(The scheme this line describes was reversed before it was built: the **librarian** dispatches and
    returns once.)*
37. **The admission side**, with the lead nobody has measured: the ingest of 2026-08-26 produced 10
    new pages against 24 dated sections on existing ones, and the share of the ten that could have
    been a section is unknown ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).
38. **An archival criterion for `entities/` and `concepts/`** — 169 pages of 737 with no exit
    criterion at all, deferred explicitly on 2026-08-28
    ([[entities-and-concepts-get-no-archival-criterion-today]]).
39. **The yield of the decisions agent is unmeasured, and the first run is the measurement.** The
    corridor *between 150 and 269 will remain* is the price of not having measured it.
40. **One `VAULT-FEEDBACK` requirement is written in two hook files** — the head of
    `remind-the-smoke.ps1` for `/retro` and the whole of `remind-the-feedback.ps1` for every prompt.
    Removing the duplication is one hook owning the requirement and naming the rituals, which is an
    edit to both files rather than an addition to one ([[the-feedback-reminder-hook]]).
41. **The strike form used on 2026-08-28 is wider than the rule that governs it** — it names both the
    answering page and the artefact in the tree, where
    [[an-answered-item-leaves-the-next-list-by-being-struck-in-place]] asks for the page. Twenty-three
    lines already carry the wider form. Ratify the widening or narrow the lines.
42. **`--only` on `scripts/vault-check-selftest.sh` is fixed or documented as a defect.** Today it is a
    substring glob, a pattern with alternation matches nothing, and the inline cases bypass the filter
    — so an empty run prints `caught 1, missed 0 - FILTERED` and reads as a pass
    ([[a-narrow-suite-run-that-matches-no-case-still-prints-a-catch]]).
43. **A turn counter on `MessageDisplay` for the session's own silence.** The point is registered and
    fires on every assistant reply; `UserPromptSubmit` covers the owner's rulings and does not cover a
    session that goes quiet in its own replies
    ([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

### What the session of 2026-08-29 built, and it is the state of the tree rather than a verdict

**Five commits, `d6a488b..b3ebc52`**, and the working copy is clean afterwards.

- **Items 34, 35 and 36 landed as `b3ebc52`.** `.claude/agents/vault-librarian.md` carries `Agent` and
  a table of the two subagents; `.claude/agents/decisions-agent.md` and
  `.claude/agents/lessons-agent.md` are new; `/ingest` gained step 2b — dispatch both readers before
  any write — and step 3b, `processed` set in the same act as `decided_by:`.
- **`/ingest` ends in a commit**, as `167830b`, in `After the librarian returns` and outside the block
  quoted to the librarian ([[the-commit-step-is-typed-into-the-skill-and-the-rule-page-debt-is-recorded]]).
- **The archive folder was repaired before that commit** — 239 pages moved out of a folder naming no
  session, one `sources:` citation rewritten
  ([[the-archive-gains-a-folder-per-session-inside-the-date]]).
- **Both agents shipped unexercised.** A new agent definition is not dispatchable at once; the live
  proof of the `contradicts` verdict was due while they were unavailable and did not run. **Their
  first real dispatch was the ingest of the same evening**, which is where their measurements come
  from.
- **Two of the owner's four agenda blocks did not happen.** Block 4, the policy on numbers, was never
  opened — both contradiction pairs and the four-disagreeing-counts `CAUTION` block stand, and item 41
  is inside it ([[the-strike-form-item-is-parked-and-the-count-leaves-the-governing-pages-prose]]).
  Block 3 was worked partly.
- **Item 27 was ordered repaired — «чиним» — and was not built.**
- **Checks:** `vault-check.sh` exit 0 at 19.4 s, advisory `9 of 15` before the agents and `9 of 17`
  after; `make style` clean at 88 files; `make smoke` **SMOKE-EXIT: 0** in the foreground. The gate's
  selftest was not run, deliberately: no schema, verdict or script changed. `make test` was not run
  and no Python changed.

**Nothing here closes anything.** Whether a criterion is met is the owner's to read.

### Changes to the goal

- **2026-08-23, at the opening: criterion 4 folds two of S2's criteria into one, deliberately.** S2
  carried `index.md` and the repository's `CLAUDE.md` as separate criteria, and each named a decider
  that turned out not to fully exist. S3 names both deciders in one criterion alongside region
  coverage, because the three are one statement — **a claim the vault makes about itself is checked
  by something that runs.** The S2 readings are untouched and are below
  ([[a-sprint-closes-on-its-goal]]).
- **2026-08-23, later the same day: criterion 3 narrows its first clause to two folders, and the
  criterion is left readable above rather than rewritten in place.** As written it reads *"`decided_by:` is legal in
  every schema and the count of pages lacking it prints under `--lint`"*. **From this date the first
  clause is: legal in `wiki/proposals/` and `wiki/rules/` and in no other folder**, required in
  `wiki/rules/` and optional in `wiki/proposals/`; and the `--lint` count is the count of pages **in
  those two folders** lacking it. The owner took the narrowing by approving a plan he read in
  Russian — a decision and not an utterance, the same attribution the criteria themselves carry —
  on the ground that a decision produces a proposal or a rule and nothing else, everything further
  down naming what it descends from in `sources:`
  ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).
  - **The second clause is unchanged and is still owed.** Read off the tree on 2026-08-23:
    `bash scripts/vault-check.sh --lint` exits 0 and prints tag density per folder, region coverage
    at `7 of 15`, and 27 owner-attributed blocks carrying no Cyrillic — **and no `decided_by:`
    line.** No `_schema.yaml` declares the key and no page carries it. That is the state of the
    tree; **reading the criterion met or unmet is the owner's** and nothing here does it.
  - **The narrowing is mechanically safe and the argument the wider set rested on was false.** The
    all-six obligation was grounded in the gate iterating what a folder declares — true of a
    `values:` block, false of a key: `scripts/vault-check.sh:382` makes a page carrying an
    undeclared key **red**, so a folder left out fails towards refusing rather than towards passing
    ([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]],
    [[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]]). The `Links:` field is
    unaffected by the narrowing and still enters all six declarations, because it is legal
    everywhere ([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]]).
  - **And the `314 pages` figure in *Deferred to S4* moves with this**, where it is corrected beside
    itself rather than renumbered here.
- **2026-08-24: the owner put three items into S3 that its criteria do not name, and none of them
  changes a criterion.**
  - **The suite's runtime is to be reduced** — «стоит все таки уменьшить время его работы», about
    `scripts/vault-check-selftest.sh`, which now costs **34m8s at 562 files** against 27m15s at 543.
    It is the second step of a live proposal rather than a new one, and he **raised it for discussion
    in the next session** ([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).
  - **The `decided_by:` back-fill has a method**: read off each page's `sources:`, never swept, with
    `status: idea` set only where no decision exists. 34 pages to read, of which only 4 mention
    `decisions/` at all ([[the-decided-by-back-fill-is-read-off-each-page-and-never-swept]]).
  - **The `idea` / `decided_by:` verdict is ordered built**, with the standing objection resolved in
    his own terms rather than overruled
    ([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]]).
  - **Criterion 1 gained its first closure and did not close.** The instrument is the catcher's
    fifteen selftest cases; five of the six rules still owe one, and the decider still counts only
    the first of the three ways a rule closes
    ([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]).
  - **Nothing here closes anything, and the readings above are the state of the tree.** Whether a
    criterion is met is the owner's to read ([[a-sprint-closes-on-its-goal]]).

### The session of 2026-08-30 that made a rule findable by lookup ran OUTSIDE this sprint

**The owner ruled it a forced session with no sprint in it** — «Чистка - это отедльная вынужденная
сессия. Спринт тут не учавствует» ([[the-cleanup-is-a-forced-session-outside-any-sprint]]). **So
nothing below is offered against an S3 criterion**, and it is recorded here because this file is the
frontier between sessions and nothing else carries what the day left open.

**Two readings of "outside any sprint" survive and the difference matters here.** S3 is open —
`Closed: —` above — so *"not counted to S3"* and *"governed by no sprint at all"* give opposite
answers about whether the standing rule was suspended for a day. **The owner's sentence supports
either and neither is chosen.**

**What it built, and it is the state of the tree rather than a verdict.** One commit, `2be376b`, 23
files, and the working copy clean afterwards apart from the journal.

- **`scripts/vault-catalogue.sh` stopped printing the `## archive` section** — 201,927 → 131,604
  bytes, about 17,500 tokens off every dispatch ([[vault-scripts]]).
- **`Links:` left all six `wiki/*/_schema.yaml`** and the proposal behind it is `status: refused`
  ([[the-links-field-and-the-script-that-would-fill-it-are-refused]]).
- **`authority:` became legal in `wiki/rules/` and gate rule 3 compares slugs within a type**
  ([[authority-uniqueness-becomes-a-per-type-question]]).
- **`render:` gained `authority` as a third value**, `governs:` moved to `optional:` and became
  conditional in the gate, and two verdicts came with it
  ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).
- **`.claude/hooks/serve-the-rule.ps1` is new**, registered on `PreToolUse` `Edit|Write`
  ([[the-rule-server-hook]]).
- **`.claude/skills/vault-ask/SKILL.md` is `context: fork`** and no longer dispatches the librarian
  ([[the-vault-ask-skill]]).
- **`docs/vault-cleanup-families.md` is the review table**, 1,819 lines, verdict columns empty.
- **Checks on `2be376b`, each from its own invocation:** `vault-check.sh` exit 0 with an empty
  stderr; `vault-check-selftest.sh` caught 212, missed 0; `hook-selftest.ps1` caught 224, missed 0;
  `make style` clean at 88 files; `make smoke` SMOKE-EXIT: 0 in the foreground. `make test` not run,
  no Python changed. **Three earlier suite runs were thrown away**, having run against a gate that
  had silently stopped checking ([[the-gate-can-stop-checking-and-go-on-exiting-zero]]).

**One acceptance criterion of this sprint was suspended by that session's own ruling, and it is named
here rather than left in the decision.** [[every-rule-in-wiki-rules-owes-a-mechanical-instrument]] is
**criterion 1**, and it is one of four rules lifted for the cleanup by
[[the-cleanup-suspends-the-rules-that-would-refuse-it]]. **Whether that changes what criterion 1 is
decided by is the owner's to read**; nothing here does it, and the rule page stays `current` because a
repeal is not a supersession.

### What the session of 2026-08-30 deferred, each with the consequence of not doing it

**Everything on its frontier but the cleanup moved, and none of it names a sprint**
([[everything-on-the-frontier-but-the-cleanup-is-deferred-and-none-of-it-names-a-sprint]]). **The
count of deferrals in this store that name no sprint went sixteen to twenty-four**, against
[[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]] — and the ruling that the
cleanup belongs to no sprint removed the destination that rule asks for. **Both pages carry a
`RAISED, NOT RESOLVED` mark and neither is narrowed.**

44. **The sweep and the 53 family rules.** They stand on **99 verdicts the owner has not given** — 53
    prohibition families and 46 concept/entity groups — in `docs/vault-cleanup-families.md`, whose
    verdict columns are empty. *Consequence:* the corpus grew today rather than shrank, and the next
    sweep runs over a larger `wiki/` ([[the-prohibition-families-become-rule-pages-served-by-a-hook]]).
45. **The 53 `authority.md` rows land in the same pass as the 53 rule pages.**
    `scripts/vault-authority.sh:244` builds its tree side from every page carrying `authority:` with
    no folder filter, so the pages alone redden gate rule 13. *Consequence:* the 2026-08-29 deadlock
    at fifty-three times the size of the one that happened on one page that day, and the exception
    granted was for one line ([[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]]).
46. **The taxonomy is written in no schema.** `concepts/` non-functional, `entities/` functional,
    ratified in his own words and present in neither `_schema.yaml`. **The schema half is the
    session's to write, not the librarian's.** *Consequence:* the sweep walks by a rule that exists
    on one page and in a chat log ([[concepts-are-non-functional-requirements-and-entities-are-functional]]).
47. **The `required` half of paired `authority:`.** Twenty-two families hold concepts with no entity —
    54 pages — so requiring the pair now reddens them on the first run
    ([[the-required-half-of-paired-authority-waits-on-the-taxonomy]]).
48. **The `authority:` matching branch on `serve-the-rule.ps1`, and the `Read` matcher after it.**
    The branch does not exist and the hook's path silence excludes every file under `wiki/`.
    *Consequence:* a rule under `render: authority` reaches nobody, so the delivery the repeal traded
    the first lifted rule for is not there
    ([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).
49. **The awk program moves into a file and is called with `awk -f`.** Ratified and deferred the same
    day. *Consequence:* every comment inside those quotes spends a headroom under four kilobytes that
    nothing measures ([[the-awk-program-moves-into-a-file-of-its-own]]).
50. **The rule about rules**, born with the family rules and written nowhere yet. Its decision exists
    and the gate on conditional delivery is satisfied by it
    ([[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]]).
51. **The dividend of the forked `vault-ask` is unmeasured.** He asked directly and the mechanism was
    built without answering. The measurement is named: the first real fork run against a librarian
    dispatch on the same question ([[the-dividend-of-the-forked-vault-ask-is-unmeasured]]).
52. **The catalogue's own future is an open question rather than a deferral.** He asked why the script
    still exists; if `/pre-task` phase 1 goes when `decisions/` empties, the catalogue goes with it,
    and **nothing decides that** — there is no design behind it and no page claims one.
53. **`docs/who-reads-the-vault.md` is still false** where it says `decided_by:` becomes legal in
    `entities/` and `concepts/`. **Third session owed**, and the file is outside the librarian's reach
    ([[who-reads-the-vault-and-who-writes-it]]).

**Nothing here closes anything, and the readings above are the state of the tree.** Whether a
criterion is met is the owner's to read ([[a-sprint-closes-on-its-goal]]).

## Closed sprints

### S1 — The vault checked whole

Opened: 2026-08-14

**Goal:** every source in `raw/` is compiled, the corpus has been through `/vault-lint` once —
it never has — and no finding of that run is left without an outcome.

Each criterion below names **the command that decides it**. That is deliberate: the owner cannot
check a 96-page corpus by reading it, so acceptance has to be a terminal reading rather than a
report from whoever did the work. The fourth criterion has no command and says so, which is the
honest shape for one that cannot be mechanised.

**Acceptance criteria:**

1. `/vault-lint` has run over the whole corpus, and **every finding it reports carries an
   outcome** — fixed by the librarian, or a `decisions/` page saying why it stands.
   *Decided by:* the `lint:` entry that run appends to `log.md`, read whole. A finding listed
   there without an outcome is this criterion not met. Note that `lint:` entries already exist
   from ingest fix waves, so the one that counts is the one dated in this sprint.
2. **Every source in `raw/` reports `INGEST COMPLETE`** — six of them, including the owner's two
   notes of 2026-08-13, which are cited by the corpus and have never been compiled.
   *Decided by:*
   `for f in job_hunt_ai_vault/raw/*/*.md; do bash scripts/vault-coverage.sh "$f"; done`
   — skipping `TEMPLATE.md`, which is a form and not a source.
3. **The three tag advisories are closed by a decision** — `process` 33, `vault` 31 and
   `testing` 24 pages, all over the split threshold. Split them, or raise the threshold, with the
   reason written down.
   *Decided by:* `bash scripts/vault-check.sh | grep advisory` prints nothing, or every line it
   still prints is named by a `decisions/` page. An advisory that stands forever stops being read,
   which is worse than not having it.
4. **There is a working answer to the shrinking-`CLAUDE.md` problem:** two successive cuts of that
   file each dropped exactly one thing no page held, and both times it was found by a human
   reading the removed text beside the page meant to carry it. Either a check that fires, or a
   written decision that there will be no check.
   *Decided by:* **nothing** — no command decides this one. It is the owner's call on a mechanism
   that does not exist yet, and this sprint does not pretend otherwise.

**Milestones:** the unfinished ingests first — every later check is run against an incomplete
corpus until they are done — then the audit, then the advisories, then the fourth.

Closed: 2026-08-17

### Changes to the goal

- **2026-08-16 — criterion 3, partly met and partly retired.** The owner read it off the run: its
  **intent is met**, since every printed advisory is named by a `decisions/` page, while **its own
  wording describes a check that no longer exists** — it names three tags at 33, 31 and 24 pages
  against a corpus-wide split threshold, and `2036d98` replaced that with a per-folder count against
  ten. The pages and the threshold the criterion names are both gone. Wording retired, intent met.
- **2026-08-17 — criterion 1, met by its own wording.** It asks that every finding carry **an
  outcome**: *fixed by the librarian, or a `decisions/` page saying why it stands*. Of the six
  findings of the 2026-08-15 audit, #2, #4 and #6 are fixed and #5 is discharged; **#1 and #3 are
  not executed, and both are covered by [[the-audits-findings-are-owed-to-the-owner]]**, which
  is that `decisions/` page — a date, a reason per item, and a rejected alternative. The owner's
  reading is that an accounted finding is an outcome and an unexecuted one is not a gap. The
  stricter reading — that a finding must be *executed* — was available and was not taken.
- **2026-08-17 — criterion 4, declared NOT met, and the sprint closed anyway.** It asked for
  *either a check that fires or a written decision that there will be no check*. What exists is a
  third thing: **a design, and nothing built**
  ([[the-harness-is-compiled-not-maintained]], [[marked-regions-and-the-prose-outside-them]]).
  Calling a design a working answer would have closed the sprint on something other than its goal,
  so it is written unmet instead. **The work is carried into S2, not dropped** — the build order is
  already agreed on [[what-the-harness-build-waits-on]]: the template, then the marked-region rules,
  then the `asserts:` predicates.

### The reading it was closed on, 2026-08-17

**The goal was:** every source in `raw/` compiled, the corpus through `/vault-lint` once, and no
finding of that run left without an outcome. **All three hold.** Nine of nine sources report
`INGEST COMPLETE`, the audit ran on 2026-08-15 over a corpus that had never had one, and every
finding it made carries an outcome in `log.md`.

**Three of the four criteria are met and the fourth is written unmet.** A sprint closes on its goal
([[a-sprint-closes-on-its-goal]]), and the goal never mentioned the shrinking-`CLAUDE.md` problem —
criterion 4 was the one criterion added beyond the goal, and the one with no command behind it. It
is the honest place for this sprint to end rather than the place it fails.

**Two things landed in the closing session that the criteria did not ask for**, both recorded here
because a sprint's record is where its work is read off: the `/ingest` cadence contradiction was
resolved by supersession, and **S2's criterion 2 was met ahead of S2** — see below.

### S2 — The vault is used, not maintained

Opened: 2026-08-17
Closed: 2026-08-23

Drafted 2026-08-16 and opened a day later, once every blocking question below had an answer. The
draft was written down because it was designed in conversation and the conversation was the only
place it existed; what follows is that draft with the answers filled in and nothing else changed.

**Goal:** the vault becomes a tool that can be used rather than maintained — every record
type has a schema saying *what it asserts and what expires it*, `CLAUDE.md` and `index.md` stop
holding copies of each other, and rules live in the wiki and are injected into the zones they
govern.

**Acceptance criteria**, each naming the command that decides it — the one pattern in this
project that removes the need to read a document in order to trust it:

1. **Every record type has a template, and every template passes the check.**
   *Decided by:* the selftest runs each template through `vault-check.sh` and reports
   `caught N, missed 0`. A template nothing tests becomes the next stale `CLAUDE.md`.
   *(**Part-built, reported by the librarian 2026-08-19; no verdict is read off here.** Each
   `wiki/` folder now carries a `_schema.yaml` naming the frontmatter keys a page there must and
   may hold, and `vault-check.sh` reads it rather than restating it — three verdicts, and the
   selftest reports `caught 120, missed 0`
   ([[the-per-folder-frontmatter-schema]],
   [[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]], [[vault-scripts]]). **That is the
   field half.** The wide reading this criterion is written against — what a record of each type
   *asserts* and what *expires* it — is **deferred on the owner's ruling that it is a conversation
   about each type, not a task**
   ([[the-wide-half-of-the-per-type-schema-is-a-conversation-not-a-task]],
   [[a-schema-per-type-says-what-a-record-asserts]]). **The criterion is read on its decider**, and
   the decider names a template rather than a key set; whether a schema the gate reads satisfies it
   is the owner's ([[a-sprint-closes-on-its-goal]]).)*
2. **No title carries a measurable quantity.** — **MET on 2026-08-17, before S2 opened.**
   *Decided by:* rule 10 of `vault-check.sh`, with six cases in the selftest. The pattern was
   written down as the work required: digits, number words, and three exemptions that are not
   counts — a code span, an ISO date, and a digit glued to a letter. **The word *one* was measured
   out of the rule** rather than argued out: all 14 titles using it used it as a pronoun or an
   invariant. The check **asks and does not judge**, because no lexical predicate separates
   *"Two staleness checks, at two different times"* (a violation; there are three) from
   *"...are two different properties"* (not one; a third would make the page wrong, not stale) —
   so a flagged page answers once in `quantity:`. Measured over the corpus: **37 of 165 titles
   carried a quantity, of which 18 were retitled and 19 answered.** The estimate this criterion
   was written against — eight — was low by a factor of four, and the reason is on the record: the
   rule had no written boundary, so nobody could count against it
   ([[a-title-names-what-is-counted-instead-of-counting-it]]).
3. **`index.md` holds no copy of what `CLAUDE.md` or `sprint.md` own.**
   *Decided by:* a rule in the check — `index.md` carries no categories table, no naming rule and
   no sprint identifier ([[the-index-reads-and-the-schema-writes]]).
4. **The repository's `CLAUDE.md` is pointers, and every skill or agent it names exists.**
   *Decided by:* rule 5b extended to a second kind of target, printing nothing
   ([[the-repository-claude-md-becomes-a-dispatch-table]]).
5. **`rules` exists as a type and a script injects each rule where it governs.** — **MET on
   2026-08-17, owner's verdict.**
   *Decided by:* rule 1 of the check names the folder set including it, and the injector has a
   selftest ([[rules-becomes-a-type-of-its-own]]). Both hold: rule 1 names `wiki/rules/`
   ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]) and `scripts/vault-inject.sh` is covered
   by the selftest, which caught 97 and missed 0. **The criterion is read on its own decider**, not
   on whether any rule page has been written — none has, and the first migration is next
   session's work.
   *(**The last clause stopped being true at `e81a6e4`, later the same day**, and is left standing
   because it is what was read when the verdict was given. Reported by the librarian, 2026-08-17:
   **nine rule pages exist, all of them render, and the selftest now catches 99 and misses 0** —
   [[wiki-rules-holds-the-rules-of-the-repository-claude-md]]. The verdict above is unchanged and is
   the owner's; nothing in this note revises it, because the criterion is read on its decider and
   both halves of that decider still hold.)*
6. **Every file the harness governs carries a marked region or is fully generated, and no rule
   lives outside one.** — **NOT MET on 2026-08-17, owner's verdict.**
   *(**Reworded 2026-08-20, on the owner's ruling, and the wording is the librarian's to write.**
   It read *"Every file the harness governs carries a marked region, and no rule lives outside
   one."* until this date. The occasion is `.claude/rules/ast-boundaries.md`, a governed file the
   injector owns end to end and which **can never acquire a region** — a region protects an insert
   into a file that has other content around it, and a generated file has none. The criterion had
   acquired a member for which it was unsatisfiable by construction.
   **The owner's wording beat the one the session offered**: the session proposed dropping
   marker-carrying files from the denominator, which hides the file; he counts one as satisfied,
   which is honest — the file is governed and is handled, by the other mechanism
   ([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]],
   [[hiding-a-file-from-a-denominator-is-weaker-than-counting-it-as-handled]]).
   **The verdict above is untouched**, and reading this criterion again is the owner's
   ([[a-sprint-closes-on-its-goal]]).)*
   *Decided by:* a rule in the check that names the governed set and reports a file carrying no
   region ([[marked-regions-and-the-prose-outside-them]]). **Added at opening**, 2026-08-17, for
   the reason below. **The rule exists and reports `0 of 13`**
   ([[a-governed-file-with-no-region-is-an-advisory]]). The owner's instruction was explicit: write
   it **as not met**, rather than as *the decider is built* — the criterion asks about the files,
   and no file carries a region.
   *(**Restated by the librarian, 2026-08-17, third session, and the verdict is unchanged.** The
   owner read it again at the end of that session and again on the files: **NOT MET.** What moved is
   the number — region coverage is **`1 of 13`**, and nine rules of the repository's `CLAUDE.md`
   render into it ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]). **The criterion asks
   about files**, and one file of thirteen carries a region. This is the second time he has read this
   criterion on the files rather than on the mechanism being built; the first was on the day it was
   written. The twelve that carry none are named by the advisory in every run.)*
   *(**The denominator may move, and this criterion does not move with it — owner, 2026-08-18.** The
   governed set is swept rather than listed ([[the-governed-set-is-swept-and-markdown-by-property]]),
   so it grows for reasons other than a skill being added: `.claude/rules/` landing would add files
   by construction ([[moving-a-rule-into-claude-rules-with-a-paths-scope]]). **The number is reported
   as *the twelve unmarked files are unchanged*, never as *coverage improved*** — he has twice read
   this criterion as a file count, and a moved denominator reads as progress in a numerator that did
   not move ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]). **No
   verdict is restated here**: the reading of 2026-08-17 stands untouched, and reading it again is
   the owner's.)*
   *(**The denominator moved, exactly as that note predicted — reported 2026-08-19.** Region
   coverage is **`1 of 14`**: `.claude/rules/` landed with the probe file in `f552abd`, which is
   the *by construction* growth the note above named ([[the-conditional-delivery-probe]]). So
   *"one file of thirteen"* above is a reading of 2026-08-17 and stays as written. **The
   unmarked files are unchanged and there is one more of them** — thirteen carry no region,
   twelve of them the same twelve, and the numerator has not moved since the day it became one.
   Read from `bash scripts/vault-check.sh | grep 'marked regions'`. **No verdict is read off
   here**, and coverage did not improve
   ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).)*
   *(**Reported by the librarian at the third ingest of 2026-08-20; no verdict is read off here.**
   The reading is **`a region or whole generation covers 3 of 15`**, from
   `bash scripts/vault-check.sh`. The file that arrived is `.claude/hooks/messages/pre-task.md`,
   generated whole from [[a-pre-task-runs-between-the-plan-and-its-approval]] and marked from the
   moment it exists — **so the numerator and the denominator moved together**, which is the
   *by construction* growth this criterion was told to expect
   ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).
   **The unmarked files are unchanged**, and that is the required phrasing — never
   *coverage improved*. **How many of them there are is where the record disagrees with itself,
   and it is left as a disagreement**: the advisory names **twelve** and lists them, the journal
   of this session says to report **thirteen**, and the same journal reads the previous state as
   `2 of 14` where the corpus records `2 of 15`. **The reading is the command, not any of those
   sentences.** Reading the criterion is the owner's ([[a-sprint-closes-on-its-goal]]).)*

7. **`authority:` is on every page outside `wiki/rules/`, and the register agrees with the tree in
   both directions.**
   *Decided by:* `bash scripts/vault-authority.sh --check --binding`.
   *(**Added 2026-08-22, on the owner's decision, and it is the seventh criterion this sprint has
   carried.** The work of 2026-08-21 earned one: `authority:` stopped being a label and became the
   index a claim is looked up in before a page is written, the field became required outside
   `wiki/rules/`, and `authority.md` joined the registers
   ([[authority-becomes-the-index-and-is-required-outside-rules]],
   [[no-new-entity-where-an-existing-one-can-carry-the-claim]]).
   **Two candidates were rejected in favour of this one.** The admission rule itself — the most
   important of the three — **is decided by no command**, and that is the ground it was rejected on;
   what a criterion nothing decides has cost here before is on the criteria above and is not
   restated. The `binding:` field was the other; it is checked by the same invocation, which is why
   the flag is in the line above rather than in a criterion of its own
   ([[a-decision-declares-whether-it-binds]]).
   **No verdict is read off here**, on this criterion or on any other; reading one is the owner's
   ([[a-sprint-closes-on-its-goal]]).)*

**The questions that blocked it, all answered before opening:**

1. ~~Is `rules` a sixth folder, or a type inside an existing one?~~ **Answered 2026-08-16: a sixth
   folder** ([[rules-becomes-a-type-of-its-own]]). Rule 1 and the selftest can now be written.
2. ~~Do ideas get a home?~~ **Answered 2026-08-17: `proposals/` with `status: idea`**, under the
   rule **the folder is the KIND of a record and the status is its MATURITY**. The owner first
   proposed `concepts/` with that status; that was argued down on the record, because
   [[proposals-are-a-folder-not-a-status]] made intent structurally impossible to file as a record
   of something built, after that failure had happened twice. A status is the right mechanism for
   *half-thought against designed*; the folder still has to be the one that carries the guarantee.
   **Not built:** the schema knows two statuses and rule 2 of the check enforces them, so `idea`
   has to be added in both, with a selftest case.
3. ~~Does moving `raw/` into a dated `archive/` belong in S2 or later?~~ **Answered 2026-08-16 in
   the half that was blocking: the archive is designed whole**
   ([[archive-is-dated-by-session-and-holds-what-left-the-working-set]]), so the question is no
   longer *what would it look like*. What is left is scheduling rather than design, and the cost
   stands as measured — 115 of 124 pages cite `raw/` in `sources:`
   ([[moving-raw-into-a-dated-archive]]), which needs the rewriter-and-detector pair before it is
   attempted ([[a-rewriter-must-be-paired-with-a-detector]]).
4. ~~Does product work interleave into S2?~~ **Answered 2026-08-17: it does not.** The vault
   continues alone until the owner decides to test it on the product. The stated default held, and
   the product has not moved since 2026-08-12 — which is now a decision rather than drift, which
   is the whole reason the question was written down instead of assumed.

**Milestones**, from the order already agreed rather than invented here
([[what-the-harness-build-waits-on]]): the handoff template first — **done 2026-08-17** — then the
marked-region rules — **done 2026-08-17, in the second session of that day** — then the `asserts:`
predicate set, which is the one item still blocking construction. The `idea` status is small and
independent and can go at any point.

**The eleven filename renames are the first customer of the rewriter-and-detector pair**, recorded
here on 2026-08-18 rather than in a brief — it has arrived in two consecutive briefs and a brief is
not a destination ([[the-growth-signal-is-the-brief]]). Measured that day: **11 filenames of 259
carry a quantity**; nine predate the rule, two were created 2026-08-17, none was minted on
2026-08-18. **The check half is separated from the renames and goes first**, because only
address-moving waits on the pair ([[the-title-rule-extends-to-filenames]],
[[a-rewriter-must-be-paired-with-a-detector]], [[knowing-a-rule-is-not-a-mechanism]]).

**The check half landed on 2026-08-18 and the renames were priced — reported by the librarian, no
verdict restated.** Rule 10 reads the filename as an **advisory**, six names print
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]). **The renames are not
blocked on a rewriter**: all six took 10.1 seconds in a worktree including a full gate run, and the
detector is complete for the link set — what is outside it is `log.md`
([[a-page-rename-is-sed-and-verify]], [[log-md-is-outside-the-link-set-the-check-reads]]). **And
criterion 2's rule was hardened rather than moved**: the owner rejected the `quantity:` field, so
the corpus clean-up — 24 pages, then the filenames, then the schema, then the check — is the next
session's first work and is ordered as a dependency
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). **No criterion is read off
here**; that is the owner's.

**The renames landed on 2026-08-19, and both claims of *the eleven filename renames are the first
customer of the rewriter-and-detector pair* are dead.**
**Sixteen files were renamed, not eleven** — `git status --porcelain | grep -cE '^R'` returns
16. Thirteen of them are the names rule 10 printed at `1520164`, measured in a worktree at that
commit; the other three are built on the ordinals *second*, *fourth* and *fifth*, which the
check cannot see, because rule 10's word list holds no ordinals while the owner's ruling of
2026-08-18 covers them. **That gap is reported and not closed here** — it is a change to the
check ([[the-title-rule-extends-to-filenames]], [[knowing-a-rule-is-not-a-mechanism]]).
**And there was no rewriter-and-detector pair for them to be the first customer of**: none was
built. The sweep was `git mv`, one `sed -f` over every reference in `wiki/`, `archive/`,
`index.md`, `tags.md` and `sprint.md`, and a verification pass; `log.md` was swept by hand,
because rules 4 and 5 do not read it ([[a-page-rename-is-sed-and-verify]],
[[log-md-is-outside-the-link-set-the-check-reads]], [[a-rewriter-must-be-paired-with-a-detector]]).
**The 2026-08-18 measurement has moved in both of its numbers**: eleven filenames of 259
carried a quantity that day and thirteen did at `1520164`, while **none does today** —
`bash scripts/vault-check.sh | grep -c 'filename(s) count'` returns 0 over the **306** pages
`find wiki -name '*.md' | wc -l` now counts. Measured after the sweep:
`bash scripts/vault-check.sh` exits 0 with **19 advisories**, one fewer than the twenty of
2026-08-18, and the filename line prints nothing. **No criterion is read off here**; that is the
owner's.

**Next, and in this order:** the fifth verdict of rule 12
([[a-region-is-checked-against-its-rules-governs]]), then the first rule migration. The ordering is
the owner's and it is not a preference — the migration is exactly when a region can land in the
wrong file.

**Read again at the ingest of 2026-08-19, second session — no verdict is restated and two things
moved.**

**Criterion 1's decider was reporting a number that was already dead.** This criterion is decided by
*"the selftest runs each template through `vault-check.sh` and reports `caught N, missed 0`"*, and the
`caught 120, missed 0` quoted above was measured **before the page carrying the new `_schema.yaml`
citations was compiled in the same ingest**. Those citations are what the suite's sandbox then
materialised into a decoy vault. **Measured on the tree that now exists: the suite was found at
`caught 24, missed 96`, diagnosed and repaired to `caught 119, missed 1`** — the remaining one being
`the vault is renamed`, which is a corpus finding rather than a suite defect
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]],
[[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]],
[[the-renamed-vault-case-is-graded-on-the-question-it-asks]],
[[the-corpus-names-the-vault-directory-and-a-rename-is-a-rewrite]]).
**`basis` moved from `optional:` to `required:` in all six `_schema.yaml` on the owner's ruling**
([[the-frontmatter-core-is-fixed-and-updated-joins-it]]), which is the field half moving again; the
wide reading stays deferred. **The criterion is read on its decider and reading it is the owner's**
([[a-sprint-closes-on-its-goal]]).

**Criterion 6 is unmoved: `1 of 14`, thirteen files carrying no region**, and the numerator has not
moved since the day it became one. The probe file is still one of the fourteen; deleting the probe
scaffolding is unblocked by this ingest and returns the denominator to thirteen
([[the-conditional-delivery-probe]],
[[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

**Next, and in this order — restated 2026-08-19 with one blocker replaced and two items added:**

1. **the guard**, as a branch in `.claude/hooks/ask-the-vault.ps1` reading `.claude/rules/`
   ([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]);
2. **then the AST rule's move, which waits on it.** **The blocker changed and the schedule did not**:
   it was the compaction probe, the probe ran on 2026-08-19 and answered **against** the move — after
   a `/compact` the Edit proceeds with no re-read and the scoped rule is gone — so what the move waits
   on is now the guard ([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]],
   [[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]],
   [[the-compaction-probe-runs-after-the-ingest-and-the-ast-move-waits-on-it]]);
3. **then the `record-schema` sweep and the three trim candidates at `/vault-lint`.** **Ratified as a
   deferral by the owner at the retro of 2026-08-19**, and written here rather than left in a brief:
   they fell out of that session silently because the brief's *next* list was the only place they
   lived, and a second brief was about to carry them the same way
   ([[the-record-schema-sweep-and-the-trim-candidates-go-onto-the-sprint]],
   [[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**The fifth verdict of rule 12 and the first rule migration**, named in the paragraph above this one,
are both done — nine rules render and the address verdict landed on 2026-08-18. That paragraph is left
standing as what was written then ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**Read again at the ingest of 2026-08-20 — no verdict is restated, and the *next* list is emptied
from the top.**

**Both of the items at the head of the ordered list below are done.** The guard is a branch in
`.claude/hooks/ask-the-vault.ps1` ([[the-guard-branch-lives-inside-a-hook-that-already-runs]]),
and the AST rule's move went ahead behind it — `CLAUDE.md` went 145 lines to 139, the rules rendering
into it went from nine to eight, and `.claude/rules/ast-boundaries.md` is generated
([[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]],
[[the-generated-ast-boundaries-rule-file]]). **The blocker that page recorded is discharged**, and
the page recording it is retired.

**The third item did not move for a further day.** The `record-schema` sweep and the three
`/vault-lint` trim candidates are untouched, and the owner puts them first for the next session
([[the-record-schema-sweep-and-the-trim-candidates-go-onto-the-sprint]]).

**Criterion 6's reading, stated the way its own decider requires and not as progress**:
`a region or whole generation covers 2 of 15`. **The numerator moved because the criterion was
reworded, not because any file gained a region** — the thirteen files carrying none that morning
still carry none, and it was proved both ways in the real tree, the marker stripped giving `1 of 15`
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

**Criterion 1's decider reports `caught 130, missed 0`**, from `caught 119, missed 1` at the previous
reading. Of the two old misses, *the vault is renamed* now passes and *the generator lists a new
page* was never a real miss but a SIGPIPE flake in the suite's own plumbing, sitting in nine places
and one of them failing towards green
([[a-quiet-grep-at-the-end-of-a-pipe-reports-a-match-as-a-failure]]). **The wall clock is owed a
real reading**: a run exceeded a 600-second timeout against a record of *roughly five minutes*
([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

**The `raw/` migration gained an order, a mechanism and a design, and is still unbuilt**:
`raw/` gains its internal structure first ([[raw-gains-its-internal-structure-before-the-move]]),
the archive is `archive/<date>/<session>/` ([[the-archive-gains-a-folder-per-session-inside-the-date]]),
and the mechanical half is a script the ingest calls
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]],
[[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]). **`probe/RUNBOOK.md` is its
first cargo**, and it cannot move until twelve `sources:` lines are rewritten
([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]).

**No criterion is read off here**; that is the owner's ([[a-sprint-closes-on-its-goal]]).

**Read again at the ingest of 2026-08-20, second session — no verdict is restated, and the third
item of the *next* list is finally done.**

**The `record-schema` sweep resolved into a channel split rather than a tag split.** The tag-density
advisories now print only behind `bash scripts/vault-check.sh --lint`, and a bare run went from
**twenty-one advisories to one** — the region-coverage line, which is the only one that was ever
about the run in front of you ([[the-tag-density-advisories-move-behind-lint]],
[[a-governed-file-with-no-region-is-an-advisory]]). **`record-schema` was dropped from the two live
trim candidates**, sixteen pages to fourteen in `decisions/`, **and the advisory still prints at
fourteen**, which is what makes it a trim on the merits
([[record-schema-is-dropped-from-the-trim-candidates]]). The third candidate needed nothing: it is
already retired, and a tag on a frozen page classifies nothing.

**Criterion 1's decider reports `caught 133, missed 0`**, from `caught 130, missed 0` at the previous
reading — the old single density case replaced by two that pin the flag in both directions, plus two
parity cases. **And its wall clock now has a real end-to-end reading**: `1093 s` serial, against the
*roughly five minutes* the store carried, with the gate itself at **8512 ms** on a 379-page corpus.
**The suite was then parallelised to 368 s**, byte-identical output, and the parallel floor measured
at 63 s ([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]],
[[the-selftest-was-serial-because-every-case-wrote-into-one-directory]],
[[the-parallel-floor-bounds-any-further-speedup]]).

**The `raw/` migration moved two of its three steps.** `raw/plans/` and `raw/specs/` exist with
`.gitkeep`, and `raw/notes/` gained the one it lacked ([[raw-gains-its-internal-structure-before-the-move]]);
`scripts/vault-archive.sh` is built and has run on its first cargo, the probe scaffolding
([[vault-archive-sh]], [[the-probe-scaffolding-is-archived-whole-into-specs]]). **The reach of a path
rewrite is ruled in both directions**: `archive/` is rewritten, `log.md` never is
([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]). **Step 3, emptying `raw/` itself, has
a hazard nobody had recorded** — two selftest cases depend on `raw/handoffs/` being non-empty and
fail loudly with the wrong diagnosis when it is not; the repair is ruled and built
([[failing-loudly-with-the-wrong-diagnosis]],
[[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

**Next, restated 2026-08-20 with the previous list emptied and this session's unstarted work added.**
The ordering below is the order the items were named in, and **it is the owner's to change**
([[the-deferrals-of-this-session-go-onto-the-sprint]]):

1. **the `render:` default removal** — three moves in one order, one of them code, and doing part of
   it is worse than doing none ([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]);
2. **the prose-path detector** — three `wiki/` pages still name a file that moved five days ago and
   nothing reports it ([[a-path-detector-for-prose-references]]);
3. **the English translation of `tests/integration/test_migrations.py`** — 206 Cyrillic lines of 951,
   the file mixed-language by this session's hand
   ([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]);
4. **two acceptance tests owed after a restart** — that the librarian lock fires at all
   ([[the-librarian-lock-hook]]), and whether `ask-the-vault.ps1` reaches a subagent's writes
   ([[hooks-in-the-settings-file-apply-inside-subagents]]). Each is one move and neither can be run
   inside the session that made it necessary.

**Raised and explicitly not built:** per-session rotation of `log.md`
([[log-md-rotates-per-session-into-the-dated-archive]]), and read-only scouts ahead of the librarian,
which now has its measurement and is short of one figure
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]).

**Next, restated again 2026-08-20 after the second session of that day.** Items 1, 3 and 4 of the
list above are closed; item 2 is untouched and stays. **The ordering is the order the items were
named in and it is the owner's to change** ([[the-deferrals-of-this-session-go-onto-the-sprint]]).

1. **the prose-path detector** — carried unchanged from the list above, and now measured on a live
   rename: of nine wiki pages naming a moved path the gate saw four and was blind to five, of which
   four were correct as written ([[a-path-detector-for-prose-references]]);
2. **the run of the 14 migration tests**, owed **against a condition rather than a date** — re-check
   when Docker is next up ([[a-deferred-check-must-be-run-when-its-condition-arrives]],
   [[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]);
3. **the green-gate selftest case**, which prints `MISSED` on a red tree and has no known repair
   shape ([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]);
4. **whether the `values:` copy becomes a rule**, so the next field admitted to a second folder does
   not rediscover it ([[the-legal-value-list-lives-in-each-folders-schema]]);
5. **whether [[product-work-does-not-interleave-into-the-vault-sprint]] needs a clarifying line**,
   after the owner read it as contradicting a vault task
   ([[a-librarian-answer-that-stops-at-the-agent-boundary-is-not-an-answer-the-owner-has]]);
6. **whether the scouts proposal is re-priced** on the dispatch measurements taken this session
   ([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]);
7. **migration warning language**, unsettled and already answered one way by the newest migration
   ([[the-language-of-a-migration-warning-is-unsettled]]).

**What closed:** the `render:` default removal, all three moves
([[an-absent-render-is-red-on-a-page-that-renders]]); the English translation, with Cyrillic left in
it on the owner's ruling ([[the-migration-test-translation-stands-with-its-remaining-cyrillic]]); and
both acceptance tests, which passed ([[the-librarian-lock-hook]],
[[hooks-in-the-settings-file-apply-inside-subagents]],
[[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).

**Two more divergences are on the record from the second session of 2026-08-20**, and neither is a
criterion: the session wrote `wiki/` by hand while the lock held its only writer out
([[the-session-wrote-wiki-by-hand-while-the-lock-held-its-only-writer-out]]), and `/pre-task` was
skipped again ([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]]).

**Two divergences are on the record from this session** and neither is a criterion: `/pre-task` was
not run before the first four items ([[pre-task-was-not-run-before-the-first-items-of-this-session]]),
and a working file was changed outside the stated scope
([[do-not-change-a-working-file-mid-work]]).

**Read again at the ingest of 2026-08-20, fourth session — no verdict is restated, and the *next*
list gains this session's deferrals under the owner's own ordering rule.**

**Criterion 6's reading, stated the way its decider requires:** `a region or whole generation covers
3 of 15`, **measured twice on the same tree** — once by the session and once independently at this
ingest. **The unmarked files are unchanged and there are twelve of them**, named in the advisory.
**The disagreement the previous ingest left standing is settled on the count**: the journal of the
third session said to report thirteen, and twelve is what the advisory has named since the numerator
became two; the thirteen came from an older brief describing `1 of 14`. **Nothing is patched** —
both figures are dated where they stand ([[the-region-coverage-figure-is-dated-where-it-stands]]).
**And the denominator moves in both directions**, which the page written for its growth now says:
it fell to 14 and rose to 15 for unrelated reasons between the two previous ingests, and the
record skipped the trip
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).
**Reading the criterion is the owner's**, and it was named among the deferrals of this session as
not taken.

**Criterion 1's decider was not re-run this session**, and the figure standing above is the one from
the previous reading. What *was* run is a different suite: `scripts/hook-selftest.ps1` at
**`caught 107, missed 0`**, from 94, with thirteen cases added and the count moved by thirteen
([[session-hooks]]).

**Three harness debts from the brief's alarms were built and committed in `abd2a53`**: `/ingest`
selects its source by sidecar absence ([[the-ingest-chooses-its-source-by-the-sidecar]],
[[the-sidecar-is-the-single-definition-of-compiled]]); the `SessionStart` hook writes a
`session-start:<source>` row and a `clear` resets the pre-task state
([[the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal]]); and the pre-task
ledger holds one session, rotated at `startup`
([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]], [[the-ledger-archive-directory]]).

**The largest finding of that session is not a criterion and is not built**: the owner cannot see
the harness in any of the four directions it was offered in, and he chose to record it rather than
act on it ([[the-harness-is-no-longer-visible-to-its-owner]],
[[the-fog-finding-is-recorded-and-not-acted-on]], [[a-generated-harness-map]]). **It bears on this
sprint's own goal** — the owner's review is the only control this project has. **Whether it earns a
criterion is his.**

**Two divergences are on the record from this session and neither is a criterion**: an approved
scope widened by a helper extraction that was chosen rather than forced
([[an-approved-scope-was-widened-by-a-helper-extraction-that-was-chosen]]), and a question shaped
like a proposal executed as a ratified design
([[a-question-shaped-like-a-proposal-was-executed-as-a-ratified-design]]).

**Next, restated 2026-08-20 after the fourth session. The ordering is the order the items were
named in and it is the owner's to change** ([[the-deferrals-of-this-session-go-onto-the-sprint]]).

1. **the prose-path detector** — carried unchanged and untouched for a third day
   ([[a-path-detector-for-prose-references]]);
2. **the run of the 14 migration tests**, owed against Docker being up rather than against a date.
   **Measured at the fourth session: Docker is not running**
   ([[a-deferred-check-must-be-run-when-its-condition-arrives]],
   [[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]);
3. **the green-gate selftest case**, unchanged
   ([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]);
4. **whether the `values:` copy becomes a rule**, unchanged
   ([[the-legal-value-list-lives-in-each-folders-schema]]);
5. **whether [[product-work-does-not-interleave-into-the-vault-sprint]] needs a clarifying line**,
   unchanged ([[a-librarian-answer-that-stops-at-the-agent-boundary-is-not-an-answer-the-owner-has]]);
6. **whether the scouts proposal is re-priced**, unchanged
   ([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]);
7. **migration warning language**, unchanged ([[the-language-of-a-migration-warning-is-unsettled]]);
8. **whether the rotation trigger stays at `startup`** — he approved a plan containing it and never
   gave a yes or no on the change itself
   ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]]);
9. **whether the helper extraction was acceptable**
   ([[an-approved-scope-was-widened-by-a-helper-extraction-that-was-chosen]]);
10. **whether `.superpowers/sdd/ledger/` needs a bound of its own** — the growth moved rather than
    ended, at roughly a kilobyte per session into a folder nobody reads
    ([[the-ledger-archive-directory]]);
11. **the fog finding**, the largest item and named above ([[the-fog-finding-is-recorded-and-not-acted-on]]);
12. **whether the `core` criterion still sorts `CLAUDE.md` without a remainder** — third session
    carrying it ([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]);
13. **the re-reading of the JavaScript rule page**, whose whole ground is `/pre-task` arriving
    unconditionally ([[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]);
14. **which reading the conditional-delivery gate carries**, after a second move
    ([[a-rule-moving-to-conditional-delivery-needs-its-page-first]]);
15. **what `permissions.defaultMode: "plan"` should mean for a `claude -p` run**
    ([[the-vs-code-extension-reads-its-starting-mode-from-user-settings]]);
16. **criterion 6's reading**, above — the command was run and the record's disagreement is settled;
    reading it is the owner's.

**Withdrawn rather than deferred: the `/clear` measurement.** **owner:** «нет. снимаем, как убираем.
Не делаем.» It was offered at the retro and he took it off the list, and
[[the-approved-scope-survives-a-compact-and-not-a-clear]] stays `basis: inference` and unmeasured.
**The branch built that night is correct either way**, which is why withdrawing it costs nothing.
Recorded here so it is not re-offered as owed.

**Raised and explicitly not built:** the `/handoff` drain of the pre-task ledger, which two `current`
pages assert and no skill implements ([[the-pre-task-ledger]],
[[the-retro-writes-its-own-transit-file]]).

**S2 stays open.** **owner, 2026-08-21:** «мы не закрываем S2. Еще есть много вопросов.» **Whether
the work of that session — the admission rule, the `authority` index and the `binding:` field —
becomes a seventh criterion is deferred to the next session**, in his words: «обсудим на следующей
сессии». Nothing is read off it here, and no criterion is added
([[occams-razor-is-the-ground-rule-for-the-vault]],
[[authority-becomes-the-index-and-is-required-outside-rules]],
[[a-decision-declares-whether-it-binds]]).

**Next, restated 2026-08-21 after the fifth session. The ordering is the order the journal named
the items in, headed by `/pre-task`'s coverage, and it is the owner's to change**
([[the-deferrals-of-this-session-go-onto-the-sprint]]).

1. **`/pre-task` must cover `concepts/`, `entities/`, `proposals/` and `rules/`, not `decisions/`
   alone** — the owner raised it explicitly; the session built the index those folders are searched
   by and did not touch the ritual that would use it. **The cost was paid in that same session**:
   `proposals/a-generated-harness-map` held a finished design, was not found, and was nearly written
   again ([[the-pre-task-enumeration-covers-every-folder-but-lessons]], [[a-generated-harness-map]]);
2. **the reading funnel is not delivered as a procedure** — stages one and two are built and no
   skill names `scripts/vault-catalogue.sh` or `authority.md`
   ([[the-reading-funnel-is-delivered-as-a-procedure]], [[the-folder-is-the-first-narrowing]]);
3. **`lessons/` becomes a queue drained into `proposals/` at the ingest** — his design, not built,
   with the folder at 121 pages ([[lessons-become-a-queue-drained-into-proposals]]);
4. **a real data format for `tags.md` and `authority.md`** — **owner:** «Правило про лишние
   зависимости - окей. Но это то, что нам нужно… Запиши, обсудим на следующей сессии.» Five scripts
   hand-parse YAML and PyYAML is installed but undeclared
   ([[a-machine-readable-format-for-the-registers]]);
5. **an admission test for mechanisms, mirroring the one built for pages** — raised by the session
   after he asked how the work moves onto what matters, with the figure in front of him: 119 commits
   since 2026-08-12, 95 touching the harness or the vault, none touching `src/`. **No verdict was
   given** ([[an-admission-test-for-mechanisms]]);
6. **eight `authority.md` families hold eleven slugs against a ceiling of about ten** — twenty were
   at the ceiling before this work, so the overflow is arithmetic; **rebalancing is a judgement about
   the corpus** ([[authority-becomes-the-index-and-is-required-outside-rules]]);
7. **[[an-authority-register-on-the-model-of-the-tag-dictionary]] is now retirable** — both claims
   that lived only there were landed, and retiring it is the owner's
   ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]);
8. **the four owed readings, carried for a fourth session** — whether the `core` criterion still
   sorts `CLAUDE.md` without a remainder; the JavaScript rule page whose ground was `/pre-task`
   arriving unconditionally; which reading the conditional-delivery gate carries; what
   `permissions.defaultMode: "plan"` should mean for a `claude -p` run
   ([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]],
   [[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]],
   [[a-rule-moving-to-conditional-delivery-needs-its-page-first]],
   [[the-vs-code-extension-reads-its-starting-mode-from-user-settings]]);
9. **whether a hook should refuse rather than advise, and the five mechanisms built and wired to
   nothing** — **owner:** «важно будет обсудить на следующей сессии это и остальные механизмы работы
   всей системы» ([[advisory-is-the-default-for-a-hook]], [[vault-archive-sh]]);
10. **the recorded objection that proposals should carry no `authority`** stands unresolved and
    marked on its page; its first test found **no competing pair among 24 proposals**, and in three
    of the four near-pairs the pages say so themselves
    ([[an-authority-register-on-the-model-of-the-tag-dictionary]]).

**Three items of the list above moved on 2026-08-22, reported and not struck out.**

- **Item 4 is half-answered.** PyYAML is a declared `dev` dependency in `pyproject.toml`, on the
  owner's ruling, and the no-new-dependencies rule is not opened by it
  ([[pyyaml-is-declared-rather-than-added-and-the-dependency-rule-is-not-opened]]). **The format
  question is untouched** and every point that page calls open is still open
  ([[a-machine-readable-format-for-the-registers]]).
- **Item 5 has its verdict, and it is narrow.** The admission test for mechanisms is **not** an
  acceptance criterion of this sprint; the split it was raised on is recorded and not acted on, and
  the proposal itself is neither built nor refused
  ([[the-harness-versus-product-split-is-recorded-and-not-acted-on]],
  [[an-admission-test-for-mechanisms]]).
- **Item 9's first half is settled and the second is unchanged.** The rule that made *advisory* the
  default was struck by the owner and its page is retired; a hook refuses on the three ratified
  conditions and on nothing else, and the hook built on 2026-08-22 cannot refuse at all because
  `PostToolUse` fires after the act ([[the-dispatch-record-hook]],
  [[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
  [[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]). **The five mechanisms
  and the wider conversation he asked for are still owed.**

**Whether an answered item leaves the list is the owner's**, unchanged, and so is the ordering of the
two lists against each other.

**Next, added 2026-08-22 at the ingest of the strike, and the ordering is the order the journal named
them in** ([[the-deferrals-of-this-session-go-onto-the-sprint]]).

11. **the ratification sweep of the owner-attributed blocks**, its own session, each block brought
    with its text and acted on only where he disowns it — headed by
    [[a-refusal-is-conditional-or-absolute-and-nothing-else]], a `prohibition` whose ruling is absent
    from the source it cites. The list is `bash scripts/vault-check.sh --lint` and is not copied here
    ([[the-ratification-sweep-waits-for-a-session-of-its-own]]);
12. **whether a paraphrase that survives ratification is demoted to `basis: inference`** — offered at
    the retro of 2026-08-21 and neither taken nor refused, and it is the one claim keeping
    [[a-quote-is-cyrillic-rule-with-an-advisory-verdict]] alive. It is about the *rank* of a
    paraphrase rather than about the alphabet verdict, which is why it is a conversation of its own
    ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]);
13. **`/pre-task` becomes an agent**, first next session and at a higher price than it had on
    2026-08-22 — once the ritual always dispatches its narrow phase, the agent stops being a
    convenience and becomes how the ritual is performed
    ([[the-pre-task-always-dispatches-its-narrow-phase]],
    [[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]);
14. **the blocking write gate waits on `record-the-dispatch.ps1` firing in a live session**, which is
    owed against a restart. Consequence, stated: the pre-task ledger's plan-mode hole is repaired in
    principle and unproved in fact ([[the-dispatch-record-hook]],
    [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]);
15. **the count of readers of `governs:` becomes a selftest case**, on the owner's ruling of
    2026-08-22 and on the shape ratified for the hook register the week before
    ([[the-count-of-a-fields-readers-lives-nowhere]],
    [[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]);
16. **the session slug is written to a file and `/handoff` reads it**, closing the ordering hole the
    dated archive opened; today it is a promise the session has to remember
    ([[the-session-slug-is-written-to-a-file-and-the-handoff-reads-it]]);
17. **item 6 of the list above is now eleven slugs in one family**, and rebalancing went to
    `/vault-lint` on the owner's ruling rather than being done in passing
    ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**The seventh criterion was set on 2026-08-22 and its decider was unrunnable as written for the first
minute of its life.** `bash scripts/vault-authority.sh --check --binding` ran the check and dropped
`--binding` without a word; the repair landed the same minute and the criterion stands as written
([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]]).

**Twenty-two retro lines were opened in the session of 2026-08-22: eighteen answered, four deferred,
and none could not be closed.** **No criterion is read off here**
([[a-sprint-closes-on-its-goal]]).

**The list of 2026-08-20 stands beneath this one and is not restated**, with two items answered by
the session of 2026-08-21: **whether `.superpowers/sdd/ledger/` needs a bound of its own** — it does
not, «Слив ledger не строим» and the archive is not pruned
([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]], [[the-ledger-archive-directory]])
— and **the `/handoff` drain raised above, which is cancelled rather than built**
([[the-pre-task-ledger]], [[the-retro-writes-its-own-transit-file]]). **Whether the answered items
leave the list is the owner's**, and so is the ordering of the two lists against each other.

**Twenty-two retro lines were opened in that session: eleven answered, eleven deferred, and none
could not be closed.**

**No criterion is read off here**; that is the owner's ([[a-sprint-closes-on-its-goal]]).

**Read off by the owner on 2026-08-22, in the session that rebuilt `/pre-task` as an agent.** These
are his readings and not the librarian's:

- **Criterion 6 — NOT MET**, on the files, as every prior reading of it has been. Region coverage
  moved to `a region or whole generation covers 7 of 15` with eight files carrying neither, and the
  denominator left and returned in the same change — the skill out, the agent in
  ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).
- **Criterion 7 — MET.** The first reading since it was set the day before;
  `bash scripts/vault-authority.sh --check --binding` exits 0 over 509 slugs.
- **Sprint item 13 — MET.** `/pre-task` is an agent, the skill is deleted, and the ritual is
  performed by dispatching `subagent_type: "pre-task"` ([[the-pre-task-agent]]).
- **Sprint item 14 — NOT MET, and it does not close on a reading.** He ruled that it closes when he
  is satisfied the mechanism works and gives his confirmation. The ledger holds
  `dispatch:vault-librarian` in plan mode and `dispatch:pre-task` at `auto`; the row the blocking
  gate needs is neither of them ([[a-chain-proved-in-halves-is-not-proved]],
  [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**Next, added 2026-08-22 at the ingest of the pre-task agent**, continuing the numbering of the list
above and in the order the journal named them
([[the-deferrals-of-this-session-go-onto-the-sprint]]).

18. **step 4, the blocking write gate** — both of its gates must clear and only one is even close.
    The second is that a real ingest does not deadlock behind it once the `Advised` and `ScopeAt`
    short-circuits are removed while the librarian writes about fifty pages, **verifiable only by
    building it and running one**, and it has already deadlocked here once
    ([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]],
    [[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]);
19. **whether the `built` mark is a third `status` value or a field of its own** — his own words,
    «built статус обсудим подробно на следующей сессии». Until it exists the corpus disagrees with
    its own ruling: the schema does not know the mark, rule 2 of the check does not admit it, and
    the folder's founding query over-reports
    ([[a-built-proposal-stays-in-proposals-with-a-built-mark]],
    [[proposals-are-a-folder-not-a-status]]);
20. **whether phase 1 of the ritual keeps dropping `deferral` and `divergence`**, with the two
    measurements of 2026-08-22 beside it — the corpus argues for the filter in three places and
    against it nowhere, and a plan whose subject is a ratified deferral is blind to exactly what it
    drops ([[the-pre-task-agent]], [[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]);
21. **whether `scripts/vault-catalogue.sh` gains a `binding:` column** — one script call or about
    five lines of `awk`, and **the identical deferral for the neighbouring field already stands**, so
    extending it is the repair rather than a new page
    ([[the-page-list-is-a-query-not-a-generated-file]]);
22. **`bash scripts/vault-authority.sh --near` is named by no skill and no agent as a reading step**
    — it reaches a reader only when that reader is about to write, which is why
    [[the-reading-funnel-is-delivered-as-a-procedure]] does not retire;
23. **eight vault `.md` files are CRLF on disk** against `.gitattributes`; git normalises on commit
    and nothing measures it — `/vault-lint`;
24. **whether an answered item leaves this list.** Not put to the owner in that session either, and
    nothing blocks on it.

**Carried unchanged from the list above**, each named rather than restated: the ratification sweep,
with 27 blocks unmoved and one confirmed ([[the-ratification-sweep-waits-for-a-session-of-its-own]]);
rule 14's blindness to the `owner selected:` shape; four `authority.md` families over the ceiling;
the four owed readings, now a seventh session; the machine-readable register format; the fourteen
migration tests against Docker; whether a paraphrase surviving ratification drops to
`basis: inference` — **2026-08-22 produced the first ratification that could test it**
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]); and the thirty flat
pages in `archive/`.

### Changes to the goal

- **2026-08-20, third session: the *next* list is untouched and was ratified twice.** All seven of
  its items stand, the owner having allowed the pre-task block to take that session at its start
  and again at its end. **Item order is his**: he put the rule page's move out of `CLAUDE.md`
  first, ahead of the prose-path detector — and that move landed at the ingest of the same day
  ([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]],
  [[a-pre-task-runs-between-the-plan-and-its-approval]]). **No criterion is read off here.**
- **2026-08-17, at opening: criterion 2 was already met.** Rule 10 of `vault-check.sh` was built
  the day before this sprint opened, while closing S1. It is left in the list rather than struck
  out, because a criterion met early is still what the sprint is judged on — and because the
  measurement it produced belongs to the record: **37 of 165 titles carried a quantity where the
  criterion was written expecting eight.**
- **2026-08-17, at the end of the third session: criterion 6 was read off again, unchanged.**
  **NOT MET**, on the files. `0 of 13` became `1 of 13` and nine rules render, and neither moves the
  verdict, because the criterion counts files. **Criterion 5's own text has a clause that went false
  the same day** — *"none has, and the first migration is next session's work"* — noted in place
  rather than edited: reporting the state is the librarian's and judging the criterion is the
  owner's ([[a-sprint-closes-on-its-goal]]). **Criterion 4's material moved without being met**: the
  repository's `CLAUDE.md` lost `## Where things are` and gained nine rendered regions, and it is
  still not a table of pointers ([[the-repository-claude-md-after-the-rules-left-it]],
  [[where-things-are-is-deleted-now-and-generated-later]]).
- **2026-08-17, at the end of the second session: criteria 5 and 6 were read off by the owner.**
  **Criterion 5 is met** on its own decider; **criterion 6 is not met**, and is written that way
  rather than as *the decider is built*. The distinction was the owner's and it is the same one
  that forced S1's criterion 4 to be written unmet: **a mechanism that reports a gap is not the gap
  closed** ([[a-sprint-closes-on-its-goal]]).
- **2026-08-17, at opening: a sixth criterion was added, on the owner's call.** The draft carried
  the harness build into this sprint in a closing paragraph and then named it in no criterion, so
  S2 could have closed on its goal with the marked regions unbuilt — which is exactly the shape
  that forced criterion 4 of S1 to be written unmet. The gap is **narrowed and not closed**: the
  `asserts:` predicate set is the third of the three items that block construction
  ([[what-the-harness-build-waits-on]]) and is still named by no criterion here. Whether it earns
  one is the owner's, and it is written down rather than left to be noticed at the retrospective.

**The tail from S1 is settled.** Criterion 4 asked for *either a check that fires or a written
decision that there will be no check*, and deferring it into S2 was neither. On 2026-08-17 the
owner took the second of the two exits above: **the criterion is written unmet and S1 closed on its
goal** ([[a-sprint-closes-on-its-goal]]). The work itself is carried into S2 — the harness build,
in the order set by [[what-the-harness-build-waits-on]].

### The reading it was closed on, 2026-08-23

**The owner declared it closed on 2026-08-23, and the declaration is his:**

> **owner, 2026-08-23:** «Давай тогда частично закроем s2. Все, что в нем осталось - переносим на
> s3. На s3 нуже будет прям конкретный и детальный план, потому что я уже чувствую что мы
> расходимся в некоторых вещах»

**«Частично» is the word to read.** He closed the sprint **on its goal, with work outstanding**,
which is exactly what a closure here is for: closure on an empty backlog was rejected on
2026-08-13 and has never been the test ([[a-sprint-closes-on-its-goal]]). **Nothing was dropped**,
so **no `decisions/` page for a dropped item is owed** — everything outstanding carries into S3,
including every item of the *next* lists.

**No verdict below is the librarian's.** Where a criterion is marked open, that is a statement that
no verdict has been given — not a verdict.

| criterion | the reading it was closed on |
|---|---|
| 1. A template per record type | **open.** The field half is built; the wide half is deferred on the owner's own ruling |
| 2. No title carries a measurable quantity | **MET before S2 opened**, on 2026-08-17 |
| 3. `index.md` holds no copy of what `CLAUDE.md` or `sprint.md` own | **open — and its decider does not exist** |
| 4. The repository's `CLAUDE.md` is pointers | **open — and its decider is half-built** |
| 5. `rules` exists as a type and the injector places each rule | **MET**, the owner's verdict of 2026-08-17, unchanged |
| 6. Every governed file carries a marked region or is fully generated | **NOT MET**, the owner's verdict |
| 7. `authority:` on every page outside `wiki/rules/` | **MET**, the owner's verdict |

**Criterion 1's wide half is deferred on his ruling and not on a reading** — what a record of each
type *asserts* and what *expires* it is a conversation about each type rather than a task
([[the-wide-half-of-the-per-type-schema-is-a-conversation-not-a-task]],
[[a-schema-per-type-says-what-a-record-asserts]]).

#### Criteria 6 and 7 were read by the owner on 2026-08-22, and today's run confirms rather than replaces

**Those readings are what this sprint closes on.** The two commands were run again at the closing,
on 2026-08-23, and **the run confirms the readings rather than being a fresh verdict** — reading a
criterion is his ([[a-sprint-closes-on-its-goal]]):

- `bash scripts/vault-check.sh` **exits 0** and prints one advisory: **`a region or whole generation
  covers 7 of 15 harness markdown files`**, naming the eight that carry neither —
  `.claude/skills/grill-me/SKILL.md`, `.claude/skills/retro/SKILL.md`,
  `.claude/skills/sprint/SKILL.md`, `.claude/skills/vault-ask/SKILL.md`,
  `.claude/skills/vault-lint/SKILL.md`, `.claude/templates/handoff.md`, `.claude/templates/retro.md`
  and the vault's own `CLAUDE.md`. **Same numerator and same denominator as the reading of
  2026-08-22**, and the criterion is a file count
  ([[a-governed-file-with-no-region-is-an-advisory]],
  [[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).
- `bash scripts/vault-authority.sh --check --binding` **exits 0**. The register and the tree agree
  over **514 slugs**, against the 509 of his reading on 2026-08-22, and `decisions/` declares
  **182 prohibitions, 23 deferrals and 10 divergences**, with every `DIVERGENCE:` title declaring
  divergence and nothing else doing so ([[a-decision-declares-whether-it-binds]]).

#### The findings on criteria 3 and 4 are this session's, and not his

Both come from reading `scripts/vault-check.sh` on 2026-08-23. They are reported, and neither is a
verdict on its criterion.

- **Criterion 3's decider does not exist.** No rule in `vault-check.sh` reads the *content* of
  `index.md`. The file is named twice and neither naming looks inside it: rule 1 asks only whether
  it is present, and the link sweep harvests its `[[wikilinks]]` for reachability. **Nothing in the
  gate can tell whether `index.md` still carries a categories table, a naming rule or a sprint
  identifier**, which is the whole of what the criterion asks
  ([[the-index-reads-and-the-schema-writes]]).
- **Criterion 4's decider is half-built.** Rule 5b — at `scripts/vault-check.sh:605` as the file
  stood on 2026-08-23 — resolves the `[[wikilinks]]` in the repository's `CLAUDE.md` against the
  corpus and reports the ones that point at nothing. **The extension the criterion names, a second
  kind of target covering the skills and agents that file names, is unwritten**
  ([[the-repository-claude-md-becomes-a-dispatch-table]]).

**Both of those deciders are named by criterion 4 of S3**, together with region coverage, which is
where the work goes.

#### What carries

**Criteria 1, 3, 4 and 6 carry into S3, and so does every item of the *next* lists** — 24 numbered
items, plus the list of 2026-08-20 and the *carried unchanged* paragraph that stand beneath them
unrestated. They are enumerated in the S3 block above, with their numbers kept. **Nothing is
dropped and nothing is merged.**
