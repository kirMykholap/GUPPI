# Cleanup review table — the families

Built 2026-08-30 at `a4a3e00` by `scripts/build-families-table.py`, which reads `job_hunt_ai_vault/authority.md`, the frontmatter of every live page under `wiki/`, and the hand-written verdicts in `docs/vault-cleanup-verdicts.md`. This file is derived: rerun the script rather than editing its output. Nothing here is written by hand.

## How to read it

**Part one — the prohibitions.** Each family of `authority.md` collects the pages answering one question. One verdict per family, applied to all its pages at once:

- **vault-facing** — the family's text is addressed to pages of the vault itself, so it becomes one page in `wiki/rules/` under `render: authority`, carrying the `authority:` of one of its decisions, and the clauses are the titles below;
- **harness-facing** — the text belongs in a harness file and needs `governs:` with a written region, which is a different kind of work; nothing is built for it now and its decisions stay where they are;
- **none** — the family produces no rule, and its decisions stay where they are.

**Only a `vault-facing` family releases its decisions to `archive/`.** The repeal frees a prohibition once the family rule carrying its clause exists, and the other two verdicts produce no such rule.

**Part two — `concepts` and `entities`.** The same families, a different question: `concepts` become non-functional requirements and `entities` functional ones. The verdict says what stays in the pair and what goes.

## What was measured, and with what

- **166 pages** carry `binding: prohibition` in `wiki/decisions/` — `grep -l '^binding: prohibition' job_hunt_ai_vault/wiki/decisions/*.md | wc -l`
- they sit in **36 families** of the 63 registered in `authority.md`
- `concepts` and `entities` sit in **51 families**
- **0 slugs** are carried by a page and grouped by no family

---

# Part one — the prohibitions

## the feedback loop back to the librarian

*how a wrong or missing answer is reported, in what vocabulary, and how the vault is measured by use rather than by reading. Answers "the vault answered badly — now what".*

Prohibitions: 12.

**verdict:** harness-facing

- A feedback record opens at column zero and the kind is written without backticks  
  `the-feedback-record-opens-at-column-zero-and-the-kind-is-written-without-backticks` — `feedback-record-grammar`
- A quotation written for the librarian carries its context  
  `a-quote-written-for-the-librarian-carries-its-context` — `quote-context-requirement`
- The `VAULT-FEEDBACK` requirement is owned by one hook, registered on each event it needs  
  `the-feedback-requirement-is-owned-by-one-hook-and-registered-on-each-event-it-needs` — `feedback-requirement-owner`
- The feedback reminder fires on the owner's prompt and speaks only when the channel has gone quiet  
  `the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet` — `feedback-reminder-trigger`
- The first measurement to keep is whether the vault changed what a session did  
  `the-measurement-is-whether-the-vault-changed-what-a-session-did` — `vault-usefulness-measure`
- The librarian writes its own log, and the brief carries what it hands back to a session  
  `the-librarian-writes-its-log-and-the-brief-carries-what-it-hands-back` — `librarian-feedback-write`
- The reply-silence threshold is its own, and the prompt threshold is left where it was  
  `the-reply-silence-threshold-is-its-own-and-the-prompt-threshold-is-unchanged` — `reply-silence-threshold`
- The vault is verified by use, not by reading: a wrong answer is written down in the turn it is noticed  
  `feedback-is-recorded-in-the-turn-it-is-noticed` — `fidelity-verification`
- Whoever filed a feedback line is the ritual that empties it  
  `whoever-filed-a-feedback-line-empties-it` — `feedback-drain-ownership`
- `divergence:` is not minted as a feedback kind, and the line that used it is refiled as a `miss:`  
  `the-divergence-kind-is-not-minted-and-the-line-is-refiled-as-a-miss` — `divergence-kind-refusal`
- `harness:` joins the feedback vocabulary as a kind of its own, rather than the template being corrected  
  `harness-is-a-feedback-kind-of-its-own` — `harness-feedback-kind`
- `lint:` and `process:` stop being session kinds, and `decision:` joins the vocabulary a session writes  
  `lint-and-process-stop-being-session-kinds-and-decision-joins` — `feedback-kinds`

## the sprint and the work that belongs to it

*what a sprint admits, how a slice is executed, how commits are made, and what a session may do to a file it did not open. Answers "am I allowed to be doing this work now".*

Prohibitions: 10.

**verdict:** harness-facing

- A sprint closes on its goal, not on an empty backlog — and the librarian never closes it  
  `a-sprint-closes-on-its-goal` — `sprint-closure`
- An answered item leaves the next-session list by being struck in place, on one line naming the page that holds the answer  
  `an-answered-item-leaves-the-next-list-by-being-struck-in-place` — `next-list-strike`
- Commits go straight to `main` in this repository, against the harness default  
  `main-is-this-repositorys-branch-convention` — `branching-convention`
- Do not change a working file mid-work, and this session did  
  `do-not-change-a-working-file-mid-work` — `mid-work-file-changes`
- Product work does not interleave into the vault sprint  
  `product-work-does-not-interleave-into-the-vault-sprint` — `product-interleave`
- The cleanup is a forced session outside any sprint, and the sprint takes no part in it  
  `the-cleanup-is-a-forced-session-outside-any-sprint` — `cleanup-session-standing`
- The day is scoped to the optimisation, archiving and process items of S3, and the owner narrowed it again after the plan was sized  
  `the-day-is-scoped-to-the-optimisation-archiving-and-process-items-of-s3` — `session-scope-2026-08-29`
- The harness changes nobody asked for stand, and each is recorded as unrequested  
  `the-harness-changes-nobody-asked-for-stand` — `unrequested-harness-change`
- The plan is committed, and the execution moves to a session of its own  
  `the-plan-is-committed-and-the-execution-moves-to-a-session-of-its-own` — `plan-execution-split`
- `/vault-lint` runs every session, so the sweep inside it actually fires  
  `vault-lint-runs-every-session-so-the-sweep-fires` — `lint-cadence`

## the ingest

*when the ingest runs, how it picks its source, what counts as compiled, and where a unit of a journal ends up. Answers "how does a journal become pages".*

Prohibitions: 9.

**verdict:** harness-facing

- A harness change is recorded the moment it is decided, and cut out at ingest on a section boundary  
  `a-harness-change-is-recorded-when-it-is-decided` — `harness-change-capture`
- An ingest of a session that built nothing writes `decisions/` and `proposals/`, and the output splits by who produced it  
  `an-ingest-of-a-session-that-built-nothing-writes-decisions-and-proposals` — `ingest-without-a-build`
- Ingest is units with verdicts, because «fully processed» has to be a question a script can answer  
  `ingest-is-units-and-verdicts` — `ingest-completeness`
- The librarian dispatches its own reading agents, waits for them, and returns once  
  `the-librarian-dispatches-its-own-reading-agents-and-returns-once` — `librarian-dispatch-owner`
- The librarian prints each criterion's decider output at the ingest, and it goes into the brief  
  `the-librarian-prints-each-criterions-decider-output-into-the-brief` — `criterion-reporting-at-ingest`
- The librarian's agent file carries its capabilities, and the ingest process lives in the skill  
  `the-librarian-agent-file-carries-capabilities-and-the-ingest-process-lives-in-the-skill` — `librarian-file-scope`
- This session is compiled by an ordinary ingest, without compressing what it wrote  
  `this-session-is-compiled-without-compressing-what-it-wrote` — `ingest-compression`
- `/ingest` chooses its source by sidecar absence, because a date prefix stops ordering sessions once there is more than one a day  
  `the-ingest-chooses-its-source-by-the-sidecar` — `ingest-source-selection`
- `/ingest` runs after `/handoff` at the end of a session, and the end-of-session skill is renamed  
  `ingest-runs-after-handoff-at-the-end-of-a-session` — `ingest-cadence`

## the selftest of the vault's own scripts

*the sandbox it works in, its cost, its parallelism, and the floor under it. Answers "how are the checks themselves checked".*

Prohibitions: 9.

**verdict:** harness-facing

- No `wiki/rules/` page holds the suite's case list, because `--list` computes it at every run  
  `no-rules-page-holds-the-suites-case-list` — `case-list-page-refusal`
- The `--only` cases live in the hook suite, and the expensive pair is kept  
  `the-only-cases-live-in-the-hook-suite-and-the-expensive-pair-is-kept` — `only-case-placement`
- The checks get a single entry point, and `make` is revived as the candidate  
  `the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate` — `check-entry-point`
- The green-gate selftest case is thrown out for good, because it makes the sprint's first criterion unreadable exactly when the criterion is needed  
  `the-green-gate-selftest-case-is-thrown-out-rather-than-deferred-again` — `green-tree-case-deferral`
- The renamed-vault case is graded on the question it asks, and not on a property nobody chose for it  
  `the-renamed-vault-case-is-graded-on-the-question-it-asks` — `renamed-vault-case-scope`
- The selftest works in its own fixture and never reaches into the corpus for a file  
  `the-selftest-works-in-its-own-fixture-and-never-in-the-corpus` — `selftest-fixture-source`
- The selftest's sandbox is fixed by making it a faithful mirror, not by pointing the check at its copy  
  `the-selftest-sandbox-is-a-mirror-rather-than-a-renamed-copy` — `selftest-sandbox-fidelity`
- The smoke runner is built first thing next session, its selection is named by the session rather than guessed, and a floor always runs  
  `the-smoke-runner-is-built-first-thing-next-session` — `smoke-runner-build-order`
- `gate`, `smoke` and `suite` name different things, and `gate` keeps the meaning it already had  
  `gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning` — `check-system-naming`

## who may write the vault

*the one-writer property, what it covers, where it has been broken and what the exceptions are. Answers "may I edit this file, or does the librarian".*

Prohibitions: 9.

**verdict:** harness-facing

- The librarian writes the vault unattended: detection replaces permission  
  `the-librarian-writes-unattended` — `librarian-write-permission`
- The one-writer clause is extended: a session repoints a citation in the change that renames what it points at  
  `the-one-writer-clause-reaches-a-citation-and-not-only-a-register` — `one-writer-scope`
- The one-writer note speaks once per session, and its scope is untouched  
  `the-one-writer-note-speaks-once-per-session` — `one-writer-note-channel`
- The session hand-edited the vault's `CLAUDE.md`, authorised in the retro, and the clause naming who may write that file is still owed  
  `the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed` — `schema-hand-edit-divergence`
- The session writes one `authority.md` row instead of the librarian, and the one-writer clause stands  
  `the-session-writes-one-authority-row-and-the-one-writer-clause-stands` — `register-writer-exception`
- The session wrote `wiki/` by hand, and it is recorded as one divergence rather than as a series of small permissions  
  `hand-edits-of-the-wiki-are-a-recorded-divergence` — `wiki-write-exception`
- The steward is a script that runs after the librarian, not another unattended writer  
  `the-steward-is-scripts-that-run-after-the-librarian` — `harness-writer`
- What the gate reads as its own input is the session's to write, and no divergence is recorded for it  
  `what-the-gate-reads-as-its-own-input-is-the-sessions-to-write` — `vault-schema-write-permission`
- `authority.md` is a register only the librarian writes, and the one-writer clause names it too  
  `authority-md-is-a-register-the-one-writer-clause-names` — `one-writer-register-set`

## finding a page in this store

*how retrieval works here, what the index is and is not, and why a search engine was not built. Answers "how do I find the page I need".*

Prohibitions: 7.

**verdict:** harness-facing

- The `authority.md` ceiling on how many slugs a family holds is deleted rather than enforced  
  `the-authority-registers-family-ceiling-is-deleted` — `authority-family-ceiling`
- The pgvector image is in place but CREATE EXTENSION vector has not been run  
  `pgvector-extension-not-enabled` — `vector-extension`
- `authority:` uniqueness becomes a question asked within a type, and a shared slug becomes the route between kinds  
  `authority-uniqueness-becomes-a-per-type-question` — `authority-per-type-uniqueness`
- `index.md` is for whoever reads the vault and the vault's `CLAUDE.md` for whoever writes it  
  `the-index-reads-and-the-schema-writes` — `index-and-schema-roles`
- `pages.base` stays tracked and stops being watched: a session commits it without discussion  
  `pages-base-is-not-a-review-item` — `pages-base-review`
- `vault-catalogue.sh` gains no `binding:` column, and the question is withdrawn rather than deferred  
  `the-catalogue-gains-no-binding-column-and-the-question-is-withdrawn` — `catalogue-binding-column`
- index.md stays at the vault root, because it is a part for the agent and not the knowledge base itself  
  `index-md-stays-at-the-vault-root` — `index-location`

## the end of a session

*what the retro is, what it is not, what it routes into, and what a ritual nobody announced is worth. Answers "what do I do when the work is finished".*

Prohibitions: 7.

**verdict:** harness-facing

- Retro and handoff are different genres and stay apart  
  `retro-interrogates-and-handoff-routes` — `retro-and-handoff-split`
- The forks the session closed without asking are ratified, and each one is named with where it landed  
  `the-forks-the-session-closed-without-asking-are-ratified` — `session-closed-forks-ratification`
- The frontier is one concept whose carriers are named, and the collision on the word is closed  
  `the-frontier-is-one-concept-with-three-carriers` — `frontier-definition`
- The retro list is worked by the session, with the items only he can answer carved out  
  `the-retro-list-is-worked-by-the-session-with-items-carved-out-for-the-owner` — `retro-list-method`
- The retro routes into addresses that exist, and opens no queue of its own  
  `the-retro-has-no-action-queue` — `action-queue`
- The retro writes its own transit file, kept apart from the feedback draft  
  `the-retro-writes-its-own-transit-file` — `retro-transit-file`
- The suite stops running every session, and runs at a sprint's close or in a rare case  
  `the-suite-stops-running-every-session` — `retro-suite-launch`

## line endings

*what is pinned to LF, when a class is pinned, and what a checkout rewrites underneath a working copy. Answers "why does this file look changed when nothing changed".*

Prohibitions: 6.

**verdict:** harness-facing

- A divergence: the `*.yaml` pin was written into `.gitattributes` before the owner ratified it  
  `the-yaml-pin-was-written-before-the-owner-ratified-it` — `yaml-pin-ratification-order`
- A file class is pinned to LF after it costs something, never before  
  `a-file-class-is-pinned-after-it-costs-something` — `line-ending-widening`
- Markdown is pinned to LF, and the rule was not widened past it  
  `markdown-is-pinned-to-lf` — `line-ending-policy`
- The vault's CRLF files are renormalised, no new rule is written, and `/vault-lint` gains a count step  
  `the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them` — `vault-crlf-renormalisation`
- `*.py` is pinned to LF against the principle that a class is pinned after it costs something  
  `the-python-class-is-pinned-to-lf-before-it-cost-anything-in-this-repository` — `python-line-ending-pin`
- `*.yaml` is pinned to LF, after the one extension left unpinned cost a debugging pass  
  `the-yaml-class-is-pinned-to-lf` — `yaml-line-ending-pin`

## the journal a session writes

*the handoff, the template it is written to, what `raw/` may hold, and how it is emptied. Answers "where does what happened get written down".*

Prohibitions: 6.

**verdict:** harness-facing

- The handoff template moves out of `raw/`, loses its numbers, and gains a `Harness` section last  
  `the-handoff-template-moves-out-of-raw-and-drops-its-numbers` — `handoff-template-form`
- `raw/` gains its internal structure before the archive move, not after  
  `raw-gains-its-internal-structure-before-the-move` — `raw-structure-ordering`
- `raw/` holds testimony; a spec and a plan are artefacts, frozen and cited rather than compiled  
  `raw-holds-testimony-and-artefacts-are-frozen` — `raw-scope`
- `raw/` is emptied by a script rather than by hand, and the move lives inside the ingest  
  `raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest` — `raw-emptying-mechanism`
- `raw/handoffs/` is swept whole today, and the forward-only clause of 2026-08-21 is overturned by the owner  
  `raw-handoffs-is-swept-whole-today-and-the-forward-only-clause-is-overturned` — `raw-sweep-backlog`
- docs/HANDOFF.md is not retired until every unit vault-units.sh counts carries a verdict  
  `handoff-retires-only-when-every-unit-has-a-verdict` — `handoff-retirement-gate`

## the pre-task ritual

*when `/pre-task` fires, what it dispatches, what it writes about itself, and what it is worth. Answers "do I owe a pre-task here, and what happens if I do".*

Prohibitions: 6.

**verdict:** harness-facing

- One `/pre-task` per approved scope, and the answer comes back per item  
  `one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item` — `pre-task-dispatch-unit`
- The `/pre-task` rule leaves `CLAUDE.md` and its addressee becomes a hook  
  `the-pre-task-rule-leaves-claude-md-for-a-hook-message` — `pre-task-rule-delivery`
- The `/pre-task` was skipped because the ritual was unavailable, and the rule has no by-hand form  
  `the-pre-task-was-skipped-and-the-rule-has-no-by-hand-form` — `pre-task-fallback-gap`
- The `pre_task` column gains a state for asserting nothing, rather than defaulting to `no`  
  `the-pre-task-column-gains-a-state-for-asserting-nothing` — `pre-task-column-states`
- `/pre-task` always dispatches its narrow phase, and the standing instruction against spawning agents does not reach a ritual  
  `the-pre-task-always-dispatches-its-narrow-phase` — `pre-task-phase-2-obligation`
- `/pre-task` keeps `binding: deferral` in its first phase and drops `divergence` alone, and the paragraph telling the agent to reach past the filter is deleted  
  `the-pre-task-keeps-deferral-in-phase-one-and-drops-divergence-alone` — `pre-task-binding-filter`

## the repository's CLAUDE.md

*what stays in that file, what left it, on what criterion, and what a cut to it can lose. Answers "does this belong in CLAUDE.md".*

Prohibitions: 6.

**verdict:** harness-facing

- Core is a decision about what bootstraps the asking, not a summary of what matters  
  `core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed` — `claude-md-core-criterion`
- No frequency cache for `CLAUDE.md`, and the statistics are collected before adoption is considered  
  `no-frequency-cache-for-claude-md` — `rule-frequency-cache`
- The map's region replaces the prose it duplicates rather than standing beside it, and the placement was made before the question was answered  
  `the-maps-region-replaces-the-prose-it-duplicated` — `map-region-placement`
- The paragraph was deleted on purpose, so the question is no longer what catches a loss but what tells a loss from a deletion  
  `the-paragraph-was-deleted-on-purpose` — `claude-md-loss-vs-deletion`
- The repository's `CLAUDE.md` becomes a dispatch table pointing at skills and agents  
  `the-repository-claude-md-becomes-a-dispatch-table` — `claude-md-dispatch-table`
- \"The file stops carrying assertions\" means no *unsourced* assertions, so a record may render into `CLAUDE.md`  
  `an-assertion-may-render-into-claude-md-but-not-be-typed-there` — `claude-md-assertions`

## how the owner is asked

*how a question is put to the owner, how his answer is read, and what a proposal from him is and is not. Answers "did he decide that, or was he thinking out loud".*

Prohibitions: 5.

**verdict:** harness-facing

- A divergence: a question the corpus already answered was put to the owner at the retro  
  `a-question-the-corpus-answers-was-put-to-the-owner-at-the-retro` — `retro-corpus-question-divergence`
- A list the owner must confirm or correct is enumerated prose in chat, not a rendered menu  
  `a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu` — `review-list-shape`
- A reversible fork is decided by the session rather than presented to the owner  
  `a-reversible-fork-is-decided-rather-than-presented` — `reversible-fork-decision`
- Every question put to the owner carries context, how it works today, what would be built, and a recommendation  
  `every-question-put-to-the-owner-carries-context-and-a-recommendation` — `question-shape`
- The list of open questions is built every session, and the conversation is offered rather than assumed  
  `the-open-questions-list-is-built-whether-or-not-it-is-discussed` — `open-questions-list`

## the brief a session starts from, and what goes stale

*what the brief carries, what it deliberately does not, how its growth is watched, and which staleness check answers which question. Answers "what am I handed at session start, and is it still true".*

Prohibitions: 5.

**verdict:** harness-facing

- The `ingested:` line stays a filename, and the hook resolves it wherever the journal now lives  
  `the-ingested-line-stays-a-filename-and-the-hook-resolves-it-wherever-the-journal-lives` — `ingested-line-resolution`
- The brief carries the commit it was generated at, because a stale brief looks exactly like a fresh one  
  `the-brief-is-stamped-with-its-commit` — `brief-staleness`
- The brief has no active-tasks section, because a section that never says anything trains the reader past it  
  `the-brief-has-no-active-tasks-section` — `task-tracker-boundary`
- The growth alarm measures the brief itself, and its threshold is measured, not invented, over the sprint that collects sizes and raises no alarm  
  `the-growth-signal-is-the-brief` — `growth-signal`
- `/pre-task` was not run before the first items of this session, and the rule requires it  
  `pre-task-was-not-run-before-the-first-items-of-this-session` — `brief-is-not-a-pre-task`

## the form of a reply, and the frontier it opens with

*what a message to the owner is made of, in what order, how many questions it may work at once, and where the list of open questions lives between sessions. Answers "how do I write to him, and what do I show him first". Distinct from *the prose this project writes*, which is about how a sentence is built rather than what a message contains.*

Prohibitions: 5.

**verdict:** harness-facing

- A session does not read the previous session's handoff, and the brief plus the feedback file is the whole inheritance  
  `a-session-does-not-read-the-previous-sessions-handoff` — `session-inheritance`
- The feedback line carries its target inside the bracket, and never between the kind and the colon  
  `the-feedback-line-carries-its-target-inside-the-bracket` — `feedback-target-grammar`
- The reply format becomes a rule, and the context rule is absorbed whole  
  `the-reply-format-becomes-a-rule-and-the-context-rule-is-absorbed-whole` — `reply-form-ratification`
- The reply-format rule gets a hook that checks the form, and the earlier objection does not reach it  
  `the-reply-format-rule-gets-a-hook-that-checks-the-form-and-not-the-fact` — `reply-form-instrument`
- `brief.md` generates its frontier section from `sprint.md`  
  `the-brief-generates-its-frontier-section-from-sprint-md` — `brief-frontier-generation`

## the gate

*`vault-check.sh` itself — its severities, its exit codes, what it guarantees, and how a verdict is proved to fire. Answers "what does the gate actually check, and what does green mean".*

Prohibitions: 5.

**verdict:** harness-facing

- The clause about the gate's input requires the owner to read the diff, and its own first application did not wait for that  
  `the-gate-input-clause-was-not-exercised-on-its-first-application` — `gate-input-clause-first-application`
- The gate rule delegating to the measure writer is built before the scanner exclusion, and the suite cost is accepted  
  `the-gate-rule-is-built-before-the-scanner-exclusion-and-the-cost-is-accepted` — `gate-rule-build-order`
- The verdict comparing a marker's type against its page's `type:` is dropped as unreachable, and replaced by one that fires  
  `the-unreachable-verdict-is-dropped-and-replaced` — `dropped-type-verdict`
- `--rules` is a mode rather than a filter, and therefore stands outside the prohibition on hiding a verdict behind a flag  
  `the-rules-flag-is-a-mode-rather-than-a-filter-and-stands-outside-the-flag-prohibition` — `mode-versus-filter`
- `vault-check.sh` exits on a usage error with a code of its own, which is the house convention  
  `the-gate-exits-on-a-usage-error-with-a-code-of-its-own` — `gate-exit-codes`

## the vacancy table

*which rows are on screen, in what order, under which profile, and what the columns say. Answers "why is this row here, or here rather than there".*

Prohibitions: 5.

**verdict:** harness-facing

- Application statuses stay English identifiers inside a Russian interface  
  `statuses-stay-english-identifiers` — `status-vocabulary`
- Profile.name is not unique in the schema, only in the CLI  
  `profile-name-not-unique` — `profile-name-uniqueness`
- Sorting reads the vacancy's objective dates, so «long open to me» and «long open on the exchange» have diverged  
  `sorting-reads-objective-dates-only` — `list-ordering-source`
- The collection panel shows local time and the «Обновлена» column does not  
  `the-collection-panel-shows-local-time-and-the-posted-at-column-does-not` — `time-display`
- The end of a collection resets the chip row, and showing what was collected beats preserving the manual choice  
  `collection-end-resets-the-chips` — `chip-state-after-collection`

## a file the repository generates

*what a generated file is, who owns and deletes it, and what a hand edit to one costs. Answers "who wrote this file, and may I edit it".*

Prohibitions: 4.

**verdict:** harness-facing

- A `.claude/rules/` file is generated whole by a script and deleted only by its own marker  
  `a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker` — `generated-file-ownership`
- A hand edit to a generated `.claude/rules/` file is red, because the repair moves no address  
  `a-hand-edit-to-a-generated-rules-file-is-red` — `generated-file-hand-edit-verdict`
- The AST rule moves to prove the mechanism, and not for what the move saves  
  `the-ast-rule-moves-to-prove-the-mechanism` — `ast-move-ground`
- The guard is built, and the AST rule's move went ahead behind it  
  `the-guard-is-built-and-the-ast-move-went-ahead-behind-it` — `ast-move-blocker`

## an advisory rather than a red verdict

*when a finding is printed and not failed, what shape an advisory takes, and what a false alarm costs. Answers "should this be red, or a note".*

Prohibitions: 4.

**verdict:** harness-facing

- The filename advisory prints one name per line, and only its first line carries the word that counts it  
  `the-filename-advisory-prints-one-name-per-line` — `advisory-line-shape`
- The filename half of the rule prints an advisory while the title half stays red  
  `the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red` — `filename-verdict-severity`
- The tag-density advisories move behind `vault-check.sh --lint`, and the bare run keeps only what is about this run  
  `the-tag-density-advisories-move-behind-lint` — `advisory-channel-split`
- The tag-density advisories run at every ingest, and the owner ruled with the reason against it in front of him  
  `the-tag-density-advisories-run-at-every-ingest` — `advisory-cadence`

## the front end's stack

*what is deliberately not adopted in the browser, and what our own JavaScript may and may not do. Answers "may I write this in the browser".*

Prohibitions: 4.

**verdict:** harness-facing

- Our own JavaScript is allowed where it cannot show a wrong list  
  `javascript-policy` — `js-scope`
- The hand-written palette grows into a design system; no framework is vendored  
  `the-palette-grows-into-a-design-system` — `stylesheet-approach`
- The server keeps rendering the vacancy table; no grid library is adopted  
  `server-renders-the-table` — `table-rendering-approach`
- The stack stays htmx, and React arrives as islands only where a screen's state must live in a tab  
  `the-stack-stays-htmx` — `frontend-stack`

## the hooks that refuse

*the librarian lock and the write net — the two places a hook says no, what each matches on, and what a refusal hides while it stands. Answers "why was I stopped".*

Prohibitions: 4.

**verdict:** harness-facing

- The gate on `/handoff` refuses, and is argued against the refusal test rather than inheriting a licence  
  `the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test` — `handoff-gate-refusal`
- The lock's matcher is pinned by a selftest case rather than widened to everything  
  `the-locks-matcher-is-pinned-by-a-selftest-case-rather-than-widened` — `lock-matcher-strategy`
- The vault is excluded from the pre-task net, in every path class it has  
  `the-vault-is-excluded-from-the-pre-task-net` — `pre-task-net-vault-exclusion`
- The write net requires a `session_id`, and says nothing without one  
  `the-write-net-requires-a-session-id` — `net-session-id-requirement`

## the hooks that stand around a session

*which hook fires when, what each of them cannot do, and how one is measured. Answers "what runs by itself around my work".*

Prohibitions: 4.

**verdict:** harness-facing

- A hook refuses on a measured condition, a measurement reliable where it stands, and a refusal that says how to clear it  
  `a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it` — `hook-refusal-test`
- A refusal is conditional or absolute, and there is no other shape  
  `a-refusal-is-conditional-or-absolute-and-nothing-else` — `refusal-shapes`
- The rule server is a hook of its own, and not a branch inside the one that already runs  
  `the-rule-server-is-a-hook-of-its-own` — `rule-server-hook`
- The schema files leave the one-writer note by a flag of their own, so the pre-task exclusion keeps them  
  `the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own` — `schema-exception-flag`

## the two job sites

*what each source gives us, what it does that nothing else does, and how a raw listing becomes a stored vacancy. Answers "where does a vacancy come from, and what is odd about it there".*

Prohibitions: 4.

**verdict:** harness-facing

- Politeness to a job site is counted per process, so profiles collecting at once each knock at the full rate  
  `politeness-is-per-process` — `request-politeness`
- Salary cannot be re-parsed, because no raw salary string is stored  
  `salary-cannot-be-reparsed` — `salary-reparse`
- The HTTP cache empties dou's cookie jar, so collection degrades to the first page  
  `http-cache-breaks-dou-csrf` — `http-cache-side-effect`
- description_is_full has no producer in production — the guard is correct and the case cannot arise  
  `description-is-full-has-no-producer` — `description-fullness-producer`

## what `/vault-lint` looks for, and the axes it has not got

*the semantic passes a librarian runs once a sprint rather than a script running on every write — which of the owner's asks were made mechanical, which were built by nothing, and why no grep could answer them even in principle. Answers "is this a gate rule or a lint item". Added 2026-08-21 with the `authority` back-fill. It is not the severity question — that is *an advisory rather than a red verdict* — it is the question of what a semantic pass looks for.*

Prohibitions: 4.

**verdict:** harness-facing

- A citation from anywhere takes a lesson out of the queue, and a permanently live lessons folder is noise  
  `a-citation-from-a-decision-takes-a-lesson-out-of-the-queue` — `lessons-queue-membership`
- Every rule in `wiki/rules/` owes a mechanical instrument, and the ones that have none are named  
  `every-rule-in-wiki-rules-owes-a-mechanical-instrument` — `rule-instrument-obligation`
- The instrument criterion closes more ways than its decider counts, and the command is what changes  
  `the-instrument-criterion-closes-more-ways-than-its-decider-counts` — `instrument-criterion-decider`
- The lessons-queue counter prints `CITED` and `LANDED` apart, where it printed one conflated meaning  
  `the-lessons-queue-counter-prints-cited-and-landed-apart` — `lessons-queue-counter-split`

## a collection run

*what starts a run, what finishes it, what it may not do, and what state it leaves in the database. Answers "what happens when I press collect".*

Prohibitions: 3.

**verdict:** harness-facing

- A restart interrupts a collection run rather than resuming it  
  `restart-interrupts-a-run` — `run-interruption-policy`
- STALE_AFTER is thirty minutes because liveness is marked once per source+tag pair, not once per request  
  `stale-after-thirty-minutes` — `staleness-window`
- The startup sweep runs only under Docker; a bare uvicorn waits for the staleness window  
  `sweep-runs-only-under-docker` — `startup-sweep-coverage`

## dispatching an agent

*when a subagent is worth its cost, what it can and cannot report about itself, and which of its claims to measure. Answers "should I dispatch, and do I believe what came back".*

Prohibitions: 3.

**verdict:** harness-facing

- The `/pre-task` is performed by dispatch, and the rule forbidding an unasked dispatch is the wrong one  
  `the-pre-task-is-performed-by-dispatch-and-the-unasked-dispatch-rule-is-the-wrong-one` — `unasked-dispatch-resolution`
- The audit is its own dispatch, run after the writes, and the extra fixed cost was paid on purpose  
  `the-audit-is-dispatched-after-the-writes` — `audit-dispatch-order`
- The read-only scouts proposal is refused, and the correctness case it also carried is untouched  
  `the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched` — `scout-dispatch-design`

## the permission mode and the approved scope

*what mode a session is in, who can see it, what an approval covers, and what survives a compaction or a clear. Answers "am I allowed to do this now, and does that still hold".*

Prohibitions: 3.

**verdict:** harness-facing

- Narrowing an approved scope is a notification; replacing or widening it is a question  
  `narrowing-a-scope-notifies-and-widening-it-asks` — `scope-change-protocol`
- The approved-scope bit survives a `/compact` and not a `/clear`, by construction  
  `the-approved-scope-survives-a-compact-and-not-a-clear` — `approved-scope-lifetime`
- `plan` stays the project's default permission mode, and a headless run that must write passes its mode by flag  
  `plan-stays-the-projects-default-permission-mode-and-a-headless-run-passes-its-own` — `default-permission-mode`

## a vacancy that disappeared

*how we decide a vacancy is gone, what that decision is scoped to, and when it must be refused. Answers "why did this row go grey, or why did it not".*

Prohibitions: 2.

**verdict:** harness-facing

- An orphan pair is never deactivated, and it is hidden rather than lingering in the list  
  `orphan-pairs-never-deactivate` — `orphan-deactivation`
- The collection frame is checked against the stored location string, not against the site's current one  
  `frame-checked-against-the-stored-string` — `frame-source-of-truth`

## draining a folder into the archive

*why the working wiki is swept at all, which criterion each folder leaves by, what a sweep does when a move is refused, and what the mark a drained page carries means. Answers "should this page still be in `wiki/`, and what decides that". Distinct from *retiring a page*, which answers "this one has gone false".*

Prohibitions: 2.

**verdict:** vault-facing

- The cleanup suspends the rules that would refuse it, and says so in one place  
  `the-cleanup-suspends-the-rules-that-would-refuse-it` — `cleanup-rule-suspension`
- `processed` is repealed, and what it distinguished is derived from the tree instead  
  `processed-is-repealed-and-the-mark-it-carried-is-derived` — `processed-status-mint`

## the harness transcript and what is read out of it

*what the Claude Code transcript holds, what it cannot hold, who separates the owner from the harness inside it, and the extractor that reads one session's dialogue out of it. Answers "what was actually said in this session, and can I check it". Added 2026-08-24, when the store was read for the first time: 37 files and 255 MB had existed for the life of the project with nothing in the repository reading them.*

Prohibitions: 2.

**verdict:** harness-facing

- The floor under a session is read, because the record already existed and nothing read it  
  `the-floor-under-a-session-is-read-because-the-record-already-existed` — `session-floor-reading`
- The session extract is read whole at every retro, and making that conditional is refused  
  `the-session-extract-is-read-whole-at-every-retro` — `extract-reading-obligation`

## the injector

*the writer that renders rules into files, the delivery modes it knows, and the blindspots the check found in it. Answers "how does the text get there, and how do we know it is the same text".*

Prohibitions: 2.

**verdict:** harness-facing

- An absent `render:` on a page that renders is red, printed by the injector and surfaced by the gate  
  `an-absent-render-is-red-on-a-page-that-renders` — `absent-render-verdict`
- `render:` is reinstated and required on a rule page, now that another delivery mode has a writer  
  `render-is-reinstated-and-required-now-that-another-mode-has-a-writer` — `delivery-mode-field`

## the prose this project writes

*the style the sessions, the plans and this store are written in, and what the owner can and cannot read. Answers "how should this be written for him". Added 2026-08-23 with one member, narrow on purpose: no existing family asks about the prose itself. *How the owner is asked* is about the shape of a question put to him; this is about the writing. Extended 2026-08-23, the same day, when the rule was finally written: `style-rule-ratification` is a second question and not the same one — *what was ratified, and where its text came from* — and the words a future reader arrives with are about the recovery rather than the style. The text was believed lost because a repository-wide grep cannot see the plan the owner approves, which lives outside the tree.*

Prohibitions: 2.

**verdict:** harness-facing

- The style rule's slice is amended rather than superseded, and plain language stops being something to ask for  
  `the-style-rules-slice-is-amended-rather-than-superseded` — `style-rule-amendment`
- The style rule's watcher is the owner, and it governs what a session says rather than what the librarian writes  
  `the-style-rules-watcher-is-the-owner-and-it-governs-chat-alone` — `style-rule-watch-and-scope`

## the two pages and how they update themselves

*the shell, the swaps, the polling and the address bar — the htmx mechanics of the interface, and how a claim about the screen is checked. Answers "how does the page change without a reload".*

Prohibitions: 2.

**verdict:** harness-facing

- The address bar is updated by an HX-Push-Url header, never by hx-push-url  
  `address-bar-updated-by-header` — `address-bar-updates`
- The page polls only while a run is in progress, so an idle tab never learns about someone else's collection  
  `polling-only-during-a-run` — `idle-page-polling`

## what actually reaches a subagent

*what text an agent is handed, by which mechanism, and how that was measured rather than assumed. Answers "will this rule be in front of the agent that needs it".*

Prohibitions: 2.

**verdict:** harness-facing

- Moving a rule from unconditional to conditional delivery needs a `decisions/` page before the move  
  `a-rule-moving-to-conditional-delivery-needs-its-page-first` — `conditional-delivery-gate`
- The probe scaffolding is archived whole into `specs/`, and dated by the day it left the working set  
  `the-probe-scaffolding-is-archived-whole-into-specs` — `probe-teardown-destination`

## a dependency of this repository

*what may be added, what is merely declared, and what the no-new-dependencies rule actually reaches. Answers "may I depend on this". Added 2026-08-22, when a package that was installed, imported and undeclared turned out to sit outside a rule that is entirely about it. Narrow on purpose: no existing family asks about a package rather than about a field, a mechanism or a script. `register-file-format` is the obvious second member and moving it is a judgement about the corpus rather than about this slug, so it was left where it is.*

Prohibitions: 1.

**verdict:** harness-facing

- PyYAML is declared rather than added, and the no-new-dependencies rule is not opened  
  `pyyaml-is-declared-rather-than-added-and-the-dependency-rule-is-not-opened` — `dependency-declaration`

## the pre-task ledger

*the file the ritual appends to, what is read out of it, what its columns mean to a human, and how it is rotated. Answers "where is the record that the ritual ran".*

Prohibitions: 1.

**verdict:** harness-facing

- The pre-task ledger holds one session and is rotated at `startup`, filing its rows away rather than deleting them  
  `the-pre-task-ledger-holds-one-session-and-rotates-at-startup` — `ledger-retention`

## the shell this repository is driven from

*the quoting, the pipes, the exit codes and the encodings that have broken a script here. Answers "why did my command do something other than what it says".*

Prohibitions: 1.

**verdict:** harness-facing

- \"File content is written with Write or Edit and never through a shell\" becomes a written rule  
  `file-content-is-written-with-the-tool-and-never-through-a-shell` — `shell-write-prohibition`

---

# Part two — `concepts` and `entities`

Families that already hold a pair come first: there the work is only to name which of the two is the functional requirement. Then the ones holding concepts alone, which is the imbalance this part was opened for.

## Families with a pair (24)

### a file the repository generates

*what a generated file is, who owns and deletes it, and what a hand edit to one costs. Answers "who wrote this file, and may I edit it".*

**verdict:** harness-facing

- **C** Deletion keys on the marker and nothing else, and an orphan is found by a cheap way and a dear one  
  `deletion-keys-on-the-marker-and-nothing-else` — `generated-file-deletion`
- **E** `.claude/rules/ast-boundaries.md` — the first harness file this project generates rather than writes  
  `the-generated-ast-boundaries-rule-file` — `generated-rules-file`

### dispatching an agent

*when a subagent is worth its cost, what it can and cannot report about itself, and which of its claims to measure. Answers "should I dispatch, and do I believe what came back".*

**verdict:** harness-facing

- **C** A skill is a role mask and a subagent is an extra body  
  `a-skill-is-a-mask-and-a-subagent-is-a-body` — `skill-versus-subagent`
- **C** A subagent cannot report its own token cost, so a measurement reaches the log only through the feedback section  
  `a-subagent-cannot-report-its-own-cost` — `agent-cost-reporting`
- **E** The `decisions-agent` — its modes, its verdicts, and the class no check will ever find  
  `the-decisions-agent` — `decisions-agent-file`
- **E** The `lessons-agent` — it reads past `lessons/`, because a lesson leaves when a page outside that folder cites it  
  `the-lessons-agent` — `lessons-agent-file`
- **E** `vault-ask` — the forked search skill, and the first `context: fork` in this repository  
  `the-vault-ask-skill` — `vault-ask-skill`

### finding a page in this store

*how retrieval works here, what the index is and is not, and why a search engine was not built. Answers "how do I find the page I need".*

**verdict:** harness-facing

- **C** A register row is stale only when no page anywhere carries the slug, and the other direction still asks about `wiki/`  
  `a-register-row-is-stale-only-when-no-page-anywhere-carries-the-slug` — `authority-check-staleness`
- **C** A slug shared across types is the graph the `Links:` field would have cached  
  `a-slug-shared-across-types-is-the-graph-the-links-field-would-have-cached` — `cross-type-slug-as-graph`
- **C** Narrowing comes before the grep, and the folder is the first narrowing  
  `the-folder-is-the-first-narrowing` — `retrieval-narrowing`
- **C** The authority register groups the corpus, and the family is the unit of a cleanup rather than the page  
  `the-authority-register-groups-the-corpus-and-the-family-is-the-unit-of-a-cleanup` — `authority-family-grouping`
- **C** The index is a map, not a catalogue, because retrieval is grep plus links  
  `the-index-is-a-map-not-a-catalogue` — `index-purpose`
- **C** The store is compiled, not retrieved — which is what makes grep plus links enough  
  `the-vault-is-compiled-not-retrieved` — `compilation-vs-retrieval`
- **E** `pages.base` — the list of every page, held as a query instead of as rows  
  `pages-base` — `page-list-artefact`

### how a measurement is written down

*whether a number is testimony for a claim or a gauge of how much now, where each lives, and the marked section they are written in. Answers "this number - where does it go".*

**verdict:** vault-facing

- **C** The measure region's spelling fences the command in backticks, and the reading follows the last one  
  `the-measure-regions-spelling-fences-the-command-in-backticks` — `measure-region-spelling`
- **E** `scripts/vault-measure.py` — the only writer of a gauge's number, and what it refuses to write  
  `vault-measure-py` — `measure-writer-script`

### retiring a page

*how a page leaves the working set, what an archived one still asserts, when a proposal is retired, and what a text corrected in place owes instead. Answers "this page has gone false — is it retired or repaired".*

**verdict:** vault-facing

- **C** A deprecated rule does not render, or its successor's file would carry the retired text  
  `a-deprecated-rule-does-not-render` — `deprecated-rule-rendering`
- **C** The order of a refusal and its archive move rests on a written rule, and nothing mechanical enforces it  
  `the-order-of-a-refusal-and-its-archive-move-rests-on-a-written-rule-and-not-on-a-gate` — `refusal-archive-ordering`
- **E** `scripts/vault-archive.sh`, the first tool here that moves a path and rewrites its citations  
  `vault-archive-sh` — `archive-script`

### the application's own structure

*the layers, the boundary tests that hold them, the database the suite runs against, and what has to be running at all. Answers "how is this codebase put together, and what keeps it that way".*

**verdict:**

- **C** A guard remembered per file is a guard forgotten in the next file, so the guard is a test  
  `a-guard-remembered-per-file-is-forgotten-in-the-next-file` — `guard-enforcement-shape`
- **C** AST tests hold the layering, and each states what it does not catch  
  `architectural-boundaries` — `boundary-tests`
- **C** Migrations are not allowed to drift from the models, and only one test file can tell  
  `migrations-do-not-drift-from-the-models` — `migration-drift`
- **C** Parsers yield raw strings, normalisation yields canonical values, and the boundary is held by an AST test  
  `normalisation-layer` — `normalisation-boundary`
- **C** The test database is created by a fixture and TRUNCATEd before every test, which is why its URL is never production's  
  `the-test-database-is-built-and-truncated-by-its-fixtures` — `test-database`
- **E** Docker Desktop — often not running, and the symptom does not say so  
  `docker-desktop` — `docker-startup`
- **E** The test-database guard, and the meta-test that makes it unforgettable  
  `the-test-database-guard` — `test-database-guard`

### the feedback loop back to the librarian

*how a wrong or missing answer is reported, in what vocabulary, and how the vault is measured by use rather than by reading. Answers "the vault answered badly — now what".*

**verdict:** harness-facing

- **C** A feedback record opens at column zero, and indentation is what marks a continuation  
  `a-feedback-record-opens-at-column-zero-and-indentation-marks-a-continuation` — `feedback-record-parsing`
- **C** A reminder that fires every time becomes furniture, and a silence counter is what avoids it  
  `a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it` — `reminder-fatigue`
- **C** The reply-silence counter is split between the hook that sees and the hook that speaks  
  `the-reply-silence-counter-is-split-between-the-hook-that-sees-and-the-hook-that-speaks` — `reply-silence-mechanism`
- **E** The acceptance questions the vault must answer, and the run of 2026-08-14 that was the first honest one  
  `the-acceptance-questions` — `acceptance-instrument`
- **E** `.superpowers/sdd/vault-feedback.md` — the session-local draft that becomes the feedback section  
  `vault-feedback-file` — `feedback-channel`

### the gate

*`vault-check.sh` itself — its severities, its exit codes, what it guarantees, and how a verdict is proved to fire. Answers "what does the gate actually check, and what does green mean".*

**verdict:** harness-facing

- **C** A check asks its question by running the writer, so writer and check cannot disagree  
  `a-check-asks-by-running-the-writer-it-checks` — `check-by-regeneration`
- **C** A new verdict is proved by planting an offender in the real tree, because the check resolves its vault relative to itself  
  `a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox` — `verdict-proof-procedure`
- **C** A non-zero exit from `vault-check.sh` no longer names one event  
  `a-non-zero-exit-from-the-gate-no-longer-names-one-event` — `gate-exit-ambiguity`
- **C** A verdict reads every field it needs in the pass that already opened the page  
  `a-verdict-reads-every-field-it-needs-in-the-pass-that-already-opened-the-page` — `single-pass-field-reading`
- **C** An interpreter probe must choose what works rather than what exists, and a hanging candidate falls outside the reasoning that excused a broken one  
  `an-interpreter-probe-must-choose-what-works-rather-than-what-exists` — `interpreter-probe-selection`
- **C** Severity in `vault-check.sh` is decidable, which is what lets a flag be safe  
  `severity-in-the-gate-is-decidable-which-is-what-lets-a-flag-be-safe` — `gate-severity`
- **C** The gate delegates by running the writer it checks, and reads its lines rather than its exit code  
  `the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes` — `gate-delegation-reading`
- **C** The gate is a shared pass over the corpus plus the scripts it delegates to, and the shared pass dominates  
  `the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to` — `gate-cost-decomposition`
- **C** The gate judges more writers than the librarian, which is why it exists even though `wiki/` has one writer  
  `the-gate-judges-more-writers-than-the-librarian` — `gate-subject-writers`
- **C** The gate's frontmatter pass reads `wiki/` alone, so a page in `archive/` is validated by no schema  
  `the-gates-frontmatter-pass-reads-wiki-alone-and-archive-is-validated-by-no-schema` — `gate-frontmatter-scope`
- **E** The scripts that hold the vault, and the one that proves the others still check anything  
  `vault-scripts` — `vault-scripts`

### the harness transcript and what is read out of it

*what the Claude Code transcript holds, what it cannot hold, who separates the owner from the harness inside it, and the extractor that reads one session's dialogue out of it. Answers "what was actually said in this session, and can I check it". Added 2026-08-24, when the store was read for the first time: 37 files and 255 MB had existed for the life of the project with nothing in the repository reading them.*

**verdict:** harness-facing

- **C** A menu resolves to a state, and pressing stop counts as an answer  
  `a-menu-resolves-to-a-state-and-an-interrupt-counts-as-an-answer` — `menu-state-set`
- **C** A transcript carries what was said and never what was reasoned, and a user-role block is not always the owner  
  `a-transcript-carries-what-was-said-and-not-what-was-reasoned` — `transcript-contents`
- **E** `session-dialogue.py` and the extract it writes, which is the first reader the transcript has had  
  `the-session-dialogue-extract` — `session-dialogue-extract`

### the hooks that refuse

*the librarian lock and the write net — the two places a hook says no, what each matches on, and what a refusal hides while it stands. Answers "why was I stopped".*

**verdict:** harness-facing

- **C** A lock on a red tree hides the health of the thing it guards  
  `a-lock-on-a-red-tree-hides-the-health-of-what-it-guards` — `lock-diagnostic-masking`
- **C** A refusal is possible on `PreToolUse` alone, and the register of which hook refuses is a test  
  `a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test` — `refusal-event-bound`
- **C** The guard branch is another trigger inside a hook that already runs, and it reads no marker  
  `the-guard-branch-lives-inside-a-hook-that-already-runs` — `guard-branch-mechanism`
- **C** The guard chain appends the net rather than branching on it  
  `the-guard-chain-appends-the-net-rather-than-branching-on-it` — `guard-chain-order`
- **E** The lock hook on the librarian dispatch, the first hook here that refuses  
  `the-librarian-lock-hook` — `librarian-dispatch-lock`

### the hooks that stand around a session

*which hook fires when, what each of them cannot do, and how one is measured. Answers "what runs by itself around my work".*

**verdict:** harness-facing

- **C** A hook finds `bash` by walking up from `git`, because it cannot name it  
  `a-hook-finds-bash-by-walking-up-from-git` — `hook-bash-discovery`
- **C** A hook that observes another tool's run reads a printed marker, and not an exit code  
  `a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code` — `observed-run-verdict-source`
- **C** Hooks configured in `settings.json` do apply inside subagents  
  `hooks-in-the-settings-file-apply-inside-subagents` — `subagent-hook-reach`
- **C** The dispatch tool is `Agent` with `Task` as an alias, and `SubagentStart` cannot block  
  `the-dispatch-tool-is-agent-and-subagent-start-cannot-block` — `dispatch-hook-surface`
- **C** The smoke gate records observations and the reader derives the refusal  
  `the-smoke-gate-records-observations-and-the-reader-derives-the-refusal` — `smoke-gate-inference`
- **C** `MessageDisplay` fires once with the whole message, and its own description says otherwise  
  `message-display-fires-once-with-the-whole-message` — `message-display-event`
- **E** The dispatch-record hook, and the ledger row a returned dispatch writes  
  `the-dispatch-record-hook` — `dispatch-record-hook`
- **E** The hooks that stand around a session, and what each of them cannot do  
  `session-hooks` — `session-hooks`
- **E** The plan-check hook  
  `the-plan-check-hook` — `plan-check-hook`
- **E** The smoke gate's hooks, and what each of them cannot do  
  `the-smoke-gate-hooks` — `smoke-gate-hooks`
- **E** `catch-the-feedback.ps1` — the hook that lifts a spoken feedback block into the file  
  `the-feedback-catcher-hook` — `feedback-catcher-hook`
- **E** `check-the-journal.ps1` — the gate that runs when a journal lands  
  `the-journal-gate-hook` — `journal-gate-hook`
- **E** `remind-the-feedback.ps1` — the hook that speaks when the feedback channel has gone quiet  
  `the-feedback-reminder-hook` — `feedback-reminder-hook`
- **E** `serve-the-rule.ps1` — the hook that hands over the rule governing the file being written  
  `the-rule-server-hook` — `rule-server-hook`

### the journal a session writes

*the handoff, the template it is written to, what `raw/` may hold, and how it is emptied. Answers "where does what happened get written down".*

**verdict:** harness-facing

- **C** A journal is judged against the template only while it is uncompiled  
  `a-journal-is-judged-only-while-it-is-uncompiled` — `journal-section-rule`
- **C** A journal is told from a form by a property, not by a filename  
  `a-journal-is-told-from-a-form-by-a-property-not-a-filename` — `journal-versus-form`
- **C** The handoff template and the mapping ingest files it by  
  `the-handoff-template-maps-onto-the-categories` — `handoff-template`
- **E** `.claude/templates/` — the forms a session's account is written from  
  `claude-templates-directory` — `templates-directory`
- **E** `docs/HANDOFF.md` is a pointer the project no longer routes through  
  `docs-handoff-is-a-pointer-nothing-routes-through` — `docs-handoff-pointer`

### the per-folder schema

*where the legal keys and values live, how the gate learns them, and in what order a schema change lands. Answers "is this frontmatter legal, and who says so".*

**verdict:** vault-facing

- **C** A field's legal values live beside its legal keys, and are read in the same pass  
  `a-fields-legal-values-live-beside-its-legal-keys` — `schema-value-parsing`
- **C** The unknown-key verdict orders a schema change ahead of the page that uses the field  
  `the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field` — `schema-change-order`
- **E** The `_schema.yaml` a folder carries, and the verdicts the gate reads off it  
  `the-per-folder-frontmatter-schema` — `per-folder-frontmatter-schema`

### the permission mode and the approved scope

*what mode a session is in, who can see it, what an approval covers, and what survives a compaction or a clear. Answers "am I allowed to do this now, and does that still hold".*

**verdict:** harness-facing

- **C** No hook event fires when the permission mode changes, and no hook output can cause one  
  `no-hook-event-fires-when-the-permission-mode-changes` — `permission-mode-visibility`
- **C** Plan mode blocks edits and not a subagent dispatch, which is what makes the ritual possible there  
  `plan-mode-blocks-edits-and-not-a-subagent-dispatch` — `plan-mode-and-subagents`
- **C** Switching permission modes is cache-safe, and a `/pre-task` dispatch costs the main context nothing  
  `switching-permission-modes-is-cache-safe` — `permission-mode-cache-safety`
- **C** The VS Code extension reads its starting permission mode from user settings and ignores the workspace  
  `the-vs-code-extension-reads-its-starting-mode-from-user-settings` — `vscode-initial-permission-mode`
- **C** The settings files have a documented precedence, and `defaultMode` is special-cased inside it  
  `the-settings-files-have-a-documented-precedence-and-defaultmode-is-special-cased` — `settings-file-precedence`
- **C** What survives a compaction is whatever has something that runs it again, and a scoped rule has nothing  
  `what-survives-a-compaction-is-whatever-has-something-that-runs-it-again` — `compaction-survival`
- **C** `ExitPlanMode` is an ordinary tool, and the owner performs the transition  
  `exit-plan-mode-is-an-ordinary-tool-and-the-owner-performs-the-transition` — `exit-plan-mode-events`
- **E** What a session start reloads for agents, skills and hooks, and what it does not  
  `claude-code-config-loading` — `config-reload`

### the pre-task ledger

*the file the ritual appends to, what is read out of it, what its columns mean to a human, and how it is rotated. Answers "where is the record that the ritual ran".*

**verdict:** harness-facing

- **C** One ledger is the record of a skipped ritual, the heartbeat of the hooks, and the mode the session started in  
  `one-ledger-is-the-record-the-heartbeat-and-the-permission-mode` — `ledger-jobs`
- **C** Rotation is a whole-file move and never a read-modify-write, because that is what the append-only ledger exists to protect  
  `rotation-is-a-whole-file-move-and-never-a-read-modify-write` — `ledger-rotation-mechanism`
- **C** The `session-start` row is the instrument, the reset and the rotation signal, and it is correct under either answer to the question it measures  
  `the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal` — `session-start-row`
- **E** The ledger archive directory  
  `the-ledger-archive-directory` — `ledger-archive`
- **E** The pre-task ledger and the session stamp  
  `the-pre-task-ledger` — `pre-task-ledger`

### the pre-task ritual

*when `/pre-task` fires, what it dispatches, what it writes about itself, and what it is worth. Answers "do I owe a pre-task here, and what happens if I do".*

**verdict:** harness-facing

- **C** The pre-task state machine has a flag for the plan and a flag for the write, and no special cases  
  `the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write` — `pre-task-state-machine`
- **C** The ritual records itself rather than being detected  
  `the-ritual-records-itself-rather-than-being-detected` — `ritual-self-recording`
- **C** `/pre-task` splits into a cheap enumeration and a narrow dispatch, and only the reading was narrowed  
  `the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch` — `pre-task-phase-split`
- **E** The `pre-task` agent  
  `the-pre-task-agent` — `pre-task-agent-file`
- **E** The pre-task state library  
  `the-pre-task-state-library` — `pre-task-state-library`

### the repository's CLAUDE.md

*what stays in that file, what left it, on what criterion, and what a cut to it can lose. Answers "does this belong in CLAUDE.md".*

**verdict:** harness-facing

- **C** A cut to the repository's `CLAUDE.md` can lose an assertion but cannot strand a page  
  `claude-md-can-lose-an-assertion-but-cannot-strand-a-page` — `claude-md-reachability`
- **E** The repository's `CLAUDE.md` after the rules left it: rendered regions, no map, and the prose that is still there on purpose  
  `the-repository-claude-md-after-the-rules-left-it` — `claude-md-scope`

### the selftest of the vault's own scripts

*the sandbox it works in, its cost, its parallelism, and the floor under it. Answers "how are the checks themselves checked".*

**verdict:** harness-facing

- **C** A destination that is also a citation loses to whichever loop runs first  
  `a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first` — `sandbox-loop-ordering`
- **C** A filter sits at the top of a dispatcher and still takes the case number  
  `a-filter-sits-at-the-top-of-a-dispatcher-and-still-takes-the-case-number` — `filter-placement`
- **C** A gate rule that runs a script is coupled to the suite's sandbox copy list, and the coupling is total  
  `a-gate-rule-that-runs-a-script-is-coupled-to-the-suites-sandbox-copy-list` — `sandbox-copy-list-coupling`
- **C** A rule that touches every page makes every unrelated test fragile, and the fix is in the harness rather than the rule  
  `a-rule-over-every-page-makes-every-test-fragile` — `global-rule-test-coupling`
- **C** A suite section is derived from where a case sits, and no list of it is maintained anywhere  
  `a-suite-section-is-derived-from-where-a-case-sits` — `selftest-section-derivation`
- **C** No verdict lives in a variable, which is the invariant that makes a parallel suite safe  
  `no-verdict-lives-in-a-variable-in-a-parallel-suite` — `parallel-suite-counting`
- **C** The case list is swept from the suite's file, because the cases written inline have no dispatcher  
  `the-case-list-is-swept-from-the-file-because-some-cases-have-no-dispatcher` — `case-list-sweep`
- **C** The parallel floor is measurable, and it bounds any further speedup of the suite  
  `the-parallel-floor-bounds-any-further-speedup` — `selftest-parallel-floor`
- **C** The selftest is a mutation test of the gate, and its cost follows from that shape  
  `the-selftest-is-a-mutation-test-of-the-gate` — `selftest-shape`
- **C** The selftest was serial because every case wrote into one directory, not by design  
  `the-selftest-was-serial-because-every-case-wrote-into-one-directory` — `selftest-parallelism`
- **E** The `Makefile`, and what each of its targets actually runs  
  `the-makefile` — `makefile-targets`

### the shell this repository is driven from

*the quoting, the pipes, the exit codes and the encodings that have broken a script here. Answers "why did my command do something other than what it says".*

**verdict:** harness-facing

- **C** A backtick inside a double-quoted PowerShell string is an escape, and it eats the command it was quoting  
  `a-backtick-in-a-double-quoted-powershell-string-is-an-escape` — `powershell-backtick-escape`
- **C** An MSYS signal does not reach a native Windows process, which is why a timeout wrapper fails here and so does a job stop  
  `an-msys-signal-does-not-reach-a-native-windows-process` — `msys-signal-reach`
- **C** An exit code read through a pipe belongs to the last stage, so it is a measurement only when nothing is downstream  
  `an-exit-code-read-through-a-pipe-belongs-to-the-last-stage` — `exit-code-through-a-pipe`
- **E** The host console is cp1252, so any entry point printing Cyrillic must reconfigure stdout  
  `windows-console-encoding` — `console-encoding`

### the two job sites

*what each source gives us, what it does that nothing else does, and how a raw listing becomes a stored vacancy. Answers "where does a vacancy come from, and what is odd about it there".*

**verdict:** harness-facing

- **C** An absent value never overwrites a known one, and a snippet never overwrites a full description  
  `absent-values-never-overwrite` — `field-overwrite-rules`
- **C** Source filters only reduce volume — the local re-check is the truth  
  `collection-modes-and-why-source-filters-do-not-decide` — `collection-modes`
- **E** dou.ua — HTML listings, POST pagination, a csrf token from a cookie  
  `dou-ua` — `dou-source`
- **E** work.ua — a promo block that ignores filters, and no container at all on an empty query  
  `work-ua` — `work-ua-source`

### the two pages and how they update themselves

*the shell, the swaps, the polling and the address bar — the htmx mechanics of the interface, and how a claim about the screen is checked. Answers "how does the page change without a reload".*

**verdict:** harness-facing

- **C** An empty state that points at a control must bring that control with it  
  `empty-state-must-bring-the-panel` — `empty-state-recovery`
- **C** Every htmx swap target must exist in the rendered page, and the check strips script blocks on the declaration side and the presence side  
  `htmx-swap-target-invariant` — `swap-target-invariant`
- **C** One shell, a vacancies page and a collection page, and exactly one poller on each  
  `one-shell-the-vacancies-and-collection-pages-and-one-poller-on-each` — `shell-and-pages`
- **C** The end of a run resets the chips first and re-reads the table after them, through one listener  
  `table-refreshes-itself` — `post-collection-refresh`
- **C** The global error handler honours hx-swap only for text/html, or an unhandled server error kills the panel permanently  
  `error-swap-gated-on-content-type` — `error-swap-safety`
- **E** Playwright MCP drives Edge, and its argument change takes effect only in the next process  
  `playwright-mcp` — `browser-harness`
- **E** uvicorn runs without --reload and Jinja auto_reload is off, so every change needs a restart  
  `app-restart-required` — `restart-to-see-changes`

### what actually reaches a subagent

*what text an agent is handed, by which mechanism, and how that was measured rather than assumed. Answers "will this rule be in front of the agent that needs it".*

**verdict:** harness-facing

- **C** A forked skill starts empty and a `/subtask` fork inherits everything, under the same word  
  `a-forked-skill-starts-empty-and-a-subtask-fork-inherits-everything` — `fork-word-collision`
- **C** A path-scoped rule is delivered by a read and by nothing else, so an edit needs a guard  
  `a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else` — `scoped-rule-trigger`
- **C** Block-level HTML comments are stripped from `CLAUDE.md` before it reaches the model, and the blank line between adjacent regions goes with them  
  `block-comments-are-stripped-before-claude-md-reaches-the-model` — `marker-context-cost`
- **C** How Claude Code loads `.claude/rules/`, as documented — and the one thing the documentation is silent about  
  `claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read` — `rules-file-loading`
- **C** What reaches a subagent, measured: a path-scoped rule does, and the HTML comment in it does not  
  `what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not` — `scoped-rule-delivery-measured`
- **E** The probe that measures whether a path-scoped rule reaches a subagent  
  `the-conditional-delivery-probe` — `delivery-probe`

### what the vault is and what its answers are worth

*why the store exists, its root principle, what ranks one page's claim against another's, and how a claim from it has already been misread. Answers "how much may I lean on this page".*

**verdict:** vault-facing

- **C** Fidelity to a source and fidelity to the tree are different properties, and only the first has ever been checked  
  `fidelity-to-a-source-and-fidelity-to-the-tree` — `fidelity-axes`
- **C** Journal, vault, brief — each artefact has exactly one owner, and the brief is never a source  
  `journal-vault-brief-each-artefact-has-one-owner` — `vault-artefacts`
- **E** The vault's directory name is the owner's to change, so nothing may depend on it  
  `the-vault-directory` — `vault-location`

### who may write the vault

*the one-writer property, what it covers, where it has been broken and what the exceptions are. Answers "may I edit this file, or does the librarian".*

**verdict:** harness-facing

- **C** One librarian behind every caller, because duplicated instructions diverge  
  `one-librarian-behind-every-caller` — `librarian-modes`
- **C** The verdict and the pen are held by different parties, which is the review rule applied to judgement  
  `the-verdict-and-the-pen-are-held-by-different-parties` — `verdict-and-pen-separation`
- **E** The vault-librarian agent — the only writer of `wiki/`, reached through every skill that asks it  
  `vault-librarian` — `vault-librarian`

## Concepts only (22)

### a collection run

*what starts a run, what finishes it, what it may not do, and what state it leaves in the database. Answers "what happens when I press collect".*

**verdict:** harness-facing

- **C** A collection batch has exactly one finaliser  
  `batch-lifecycle` — `batch-finalisation`
- **C** A summary names only non-zero counters, because a clause that always says the same thing stops being read  
  `name-only-non-zero-counters` — `summary-line-content`
- **C** Collection runs in a daemon thread, and its whole state lives in the database  
  `collection-runs-in-a-thread` — `collection-execution`

### a copy of a list drifts

*why a duplicated list is repaired by deleting it rather than extending it, and where a copy has already gone stale here. Answers "should I write this list down a second time".*

**verdict:** vault-facing

- **C** A printed register cannot drift, and a maintained one always has  
  `a-printed-register-cannot-drift-and-a-maintained-one-always-has` — `derived-register-proof`
- **C** The mapping is documented at each hop and copied nowhere  
  `the-mapping-is-documented-at-each-hop-and-copied-nowhere` — `mapping-location`

### a fixture and what it must materialise

*what a test's setup has to put on disk, why a planted offender is read back, and how a fixture stops being a fixture of its subject. Answers "is my setup actually the situation I mean".*

**verdict:**

- **C** A fixture that renames what the corpus names by name stops being a fixture of that corpus  
  `a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it` — `fixture-renames-its-subject`

### a number this project quotes

*where a figure came from, what its denominator is, and every way a number here has been wrong. Answers "may I write this number down".*

**verdict:** vault-facing

- **C** A denominator is walked off the input list, never off what the scanner managed to read  
  `a-denominator-is-walked-off-the-input-list` — `coverage-denominator-source`

### a test that proves nothing

*the ways a green test carries no evidence, and the procedures that settle whether it does. Answers "does this test actually test anything".*

**verdict:**

- **C** `pytest --collect-only` cannot exercise an assertion message, and neither can `ruff`  
  `collect-only-cannot-exercise-an-assertion-message` — `collect-only-blindspot`

### a vacancy that disappeared

*how we decide a vacancy is gone, what that decision is scoped to, and when it must be refused. Answers "why did this row go grey, or why did it not".*

**verdict:** harness-facing

- **C** Deactivation is profile-scoped because «the site closed this vacancy» cannot be known  
  `why-deactivation-is-profile-scoped` — `deactivation-scope`
- **C** The collection frame is checked against every city in the raw string, not just the first  
  `collection-frame-city-check` — `city-frame-matching`
- **C** The deactivation cycle: every condition guarded by a test that fails when its guard is removed  
  `deactivation-cycle` — `deactivation-rules`

### admitting a frontmatter field

*what a new field has to earn before it exists, what a self-declaration costs, and the fields that were admitted or withdrawn. Answers "may I add a field for this".*

**verdict:** vault-facing

- **C** A declaration that silences a check must expire or be re-derived, because what it silences is what would have found it wrong  
  `a-declaration-that-silences-a-check-must-expire-or-be-re-derived` — `silencing-declaration`
- **C** A field earns its place by being read, or by being a checksum against a fact the tree already asserts  
  `a-field-earns-its-place-by-being-read-or-by-being-a-checksum` — `field-admission-test`

### an advisory rather than a red verdict

*when a finding is printed and not failed, what shape an advisory takes, and what a false alarm costs. Answers "should this be red, or a note".*

**verdict:** harness-facing

- **C** A clean-run assertion cannot test an advisory exemption, so the absent-case is the instrument  
  `a-clean-run-cannot-test-an-advisory-exemption` — `advisory-exemption-testing`
- **C** A mark that opens a state is not a mark that names a place, and the gate may only judge an address  
  `a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place` — `mark-state-versus-address`
- **C** An advisory sorts what it names, so an unchanged tree prints unchanged output  
  `an-advisory-prints-one-line-and-sorts-what-it-names` — `advisory-form`

### draining a folder into the archive

*why the working wiki is swept at all, which criterion each folder leaves by, what a sweep does when a move is refused, and what the mark a drained page carries means. Answers "should this page still be in `wiki/`, and what decides that". Distinct from *retiring a page*, which answers "this one has gone false".*

**verdict:** vault-facing

- **C** A citation is not a test in a corpus this densely linked  
  `a-citation-is-not-a-test-in-a-corpus-this-densely-linked` — `citation-as-predicate`
- **C** A link pass that keeps the filename beside each link is linear, and the warning the link rules carry is about a different shape  
  `a-link-pass-that-keeps-the-filename-beside-the-link-is-linear` — `link-pass-shape`
- **C** A selector is one pass over the corpus, and never one pass per page  
  `a-selector-is-one-pass-over-the-corpus-and-never-one-pass-per-page` — `sweep-selector-shape`
- **C** A status value is either an address or a stage, and the gate treats them oppositely  
  `a-status-value-is-either-an-address-or-a-stage-and-the-gate-treats-them-oppositely` — `status-value-gate-treatment`
- **C** The deprecated-link advisory keys on the literal value, not on \"the target's status\  
  `the-deprecated-link-advisory-keys-on-the-literal-value-and-not-on-the-targets-status` — `deprecated-link-advisory-key`
- **C** The sweep is a mode of the archiver, so it inherits its refusals instead of acquiring an opinion  
  `the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals` — `sweep-mode-inheritance`

### line endings

*what is pinned to LF, when a class is pinned, and what a checkout rewrites underneath a working copy. Answers "why does this file look changed when nothing changed".*

**verdict:** harness-facing

- **C** `git status` reports a file modified from a cached stat size, and renormalising never refreshes it  
  `the-stale-stat-cache-behind-git-status` — `git-status-stat-cache`

### renaming a page

*what a move costs, what a sweep may touch, what it strands, and why a rewriter needs a detector. Answers "may I rename this, and what breaks if I do".*

**verdict:** vault-facing

- **C** A page rename is sed-and-verify, and the blocked framing was overpriced  
  `a-page-rename-is-sed-and-verify` — `rename-cost`
- **C** A path is never a pattern, and a `sources:` line is the only place a rewrite may touch  
  `a-path-is-never-a-pattern` — `path-rewrite-mechanism`
- **C** `log.md` is outside the link set the check reads, so a rename can strand it silently  
  `log-md-is-outside-the-link-set-the-check-reads` — `log-link-blindness`

### the brief a session starts from, and what goes stale

*what the brief carries, what it deliberately does not, how its growth is watched, and which staleness check answers which question. Answers "what am I handed at session start, and is it still true".*

**verdict:** harness-facing

- **C** The staleness checks run at different times and ask different questions — and none subsumes another  
  `staleness-checks-run-at-different-times-and-ask-different-questions` — `staleness-timing`

### the form of a reply, and the frontier it opens with

*what a message to the owner is made of, in what order, how many questions it may work at once, and where the list of open questions lives between sessions. Answers "how do I write to him, and what do I show him first". Distinct from *the prose this project writes*, which is about how a sentence is built rather than what a message contains.*

**verdict:** harness-facing

- **C** A decision with a rule target cannot close inside a single ingest, and the mechanisms deciding it are named  
  `a-decision-with-a-rule-target-cannot-close-inside-a-single-ingest` — `rule-landing-two-parties`

### the ingest

*when the ingest runs, how it picks its source, what counts as compiled, and where a unit of a journal ends up. Answers "how does a journal become pages".*

**verdict:** harness-facing

- **C** A `page:` verdict is checked for the page's existence and never for the claim  
  `the-page-verdict-is-checked-for-the-pages-existence-and-not-for-the-claim` — `page-verdict-verification`
- **C** The sidecar is the single definition of *compiled*, and every reader that asks the question asks it the same way  
  `the-sidecar-is-the-single-definition-of-compiled` — `compiled-definition`
- **C** Writing the page is not a step after the verdict — the verdict is the write  
  `the-verdict-is-the-write` — `verdict-semantics`

### the injector

*the writer that renders rules into files, the delivery modes it knows, and the blindspots the check found in it. Answers "how does the text get there, and how do we know it is the same text".*

**verdict:** harness-facing

- **C** A fenced block inside a `<!-- text -->` slice survives into the destination, and the fence flag now gates recognition only  
  `a-fenced-block-inside-a-slice-survives-into-the-destination` — `injector-fence-defect`
- **C** A gate that claimed byte equality did not have it: `$( )` strips the trailing newline before either side is read  
  `a-command-substitution-strips-the-newline-a-gate-compares` — `injector-comparison-blindness`
- **C** The `governs:` list is expanded at the walk, and the address verdict asks membership  
  `the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership` — `governs-list-expansion`
- **C** The `whole` mode owns a file end to end, and its form is defined once in the writer  
  `the-whole-mode-owns-a-file-end-to-end` — `whole-delivery-mode`
- **C** The injector has no output channel that is not red  
  `the-injector-has-no-output-channel-that-is-not-red` — `injector-output-severity`
- **C** The injector reads `render:` only after it has skipped every page carrying no `governs:`  
  `the-injector-reads-render-only-after-it-has-skipped-a-page-without-governs` — `injector-render-blindspot`
- **C** The injector walks pages to files and the check walks files to pages, and neither sees what the other sees  
  `the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages` — `injector-check-directions`
- **C** The rendered form is defined once and read by the writer and by the comparison  
  `the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison` — `rendered-form-definition`

### the no-quantity rule

*why a title and a filename carry no measurable quantity, which words count, and what the check does about it. Answers "may this number be in the title".*

**verdict:** vault-facing

- **C** The title check asks and does not judge, and the answer it asks for is a retitle  
  `the-title-check-asks-and-the-answer-is-a-retitle` — `title-check-mechanism`

### the region a rule renders into

*the markers, their form, their placement, and the verdicts that read them. Answers "what does the rendered block look like, and where does it go".*

**verdict:** vault-facing

- **C** A marker is an address, and with the type in it the address is complete  
  `a-marker-with-its-type-is-a-complete-address` — `marker-as-address`
- **C** A marker is detected loosely and judged strictly, so a typo is wrong rather than invisible  
  `a-marker-is-detected-loosely-and-judged-strictly` — `marker-detection`
- **C** A region is a paired HTML comment named for a rule's slug, alone at column zero  
  `a-region-is-a-paired-comment-named-for-a-rule` — `region-form`
- **C** The address verdict catches the leftover copy, not the region in the wrong file  
  `the-address-verdict-catches-the-leftover-copy-not-the-wrong-file` — `address-verdict`

### the tag dictionary and the two languages

*what a tag is for, when one is split or kept, and how a question asked in Russian reaches a page written in English. Answers "what do I call this, and in which language".*

**verdict:** vault-facing

- **C** A tag's aliases are how a Russian question reaches an English page  
  `aliases-carry-the-question-across-languages` — `alias-purpose`

### the vacancy table

*which rows are on screen, in what order, under which profile, and what the columns say. Answers "why is this row here, or here rather than there".*

**verdict:** harness-facing

- **C** In build_vacancy_query the tag condition is the terminal step, and anything added after it is unreachable  
  `vacancy-query-tag-condition` — `tag-condition-placement`
- **C** Rules the vacancy list keeps: one PAGE_SIZE, one filter builder, an explicit tie-breaker, and empty strings that are not defaults  
  `vacancy-list-invariants` — `vacancy-list-rules`
- **C** The selected profile lives in a cookie, so navigation links and saved links are not portable  
  `profile-resolution` — `profile-selection`
- **C** tags_set separates «every chip cleared» from «the page was just opened»  
  `tags-set-marker` — `cleared-chips-vs-fresh-page`

### what `/vault-lint` looks for, and the axes it has not got

*the semantic passes a librarian runs once a sprint rather than a script running on every write — which of the owner's asks were made mechanical, which were built by nothing, and why no grep could answer them even in principle. Answers "is this a gate rule or a lint item". Added 2026-08-21 with the `authority` back-fill. It is not the severity question — that is *an advisory rather than a red verdict* — it is the question of what a semantic pass looks for.*

**verdict:** harness-facing

- **C** The librarian cannot see a recurring family from where the ingest stands  
  `the-librarian-is-blind-to-a-recurring-family-from-where-it-stands` — `librarian-repetition-blindness`

### what a review of the session's own record costs, and what it is worth

*the instruments this project points at its own output — the retro's steps, the plan check, the advisories — and the measurements of what each of them actually returned. Answers "was that review step worth running, and what did it catch that nothing else would".*

**verdict:**

- **C** What loads into every session before the first prompt, and the nested `CLAUDE.md` is re-injected  
  `what-loads-into-every-session-before-the-first-prompt` — `session-fixed-context-cost`

### where a rule's text is sent

*`governs:` and `paths:` — the destination, how it is resolved, who may carry it, and what the governed set is. Answers "which file does this rule end up in".*

**verdict:** vault-facing

- **C** A family rule's clauses are drafted from titles, because the no-quantity rule already made every title a claim  
  `a-family-rules-clauses-are-drafted-from-titles-because-a-title-names-its-claim` — `family-rule-from-titles`
- **C** A generated rule file with no `paths:` carries no frontmatter block at all  
  `a-generated-rule-file-with-no-paths-carries-no-frontmatter` — `generated-file-without-paths`
- **C** A rule differs from a prohibition by having an address, and by nothing else  
  `a-rule-differs-from-a-prohibition-by-having-an-address-and-by-nothing-else` — `rule-versus-prohibition`
- **C** A rule reaches a session by several routes, and only one transition between them had a written gate  
  `a-rule-reaches-a-session-by-several-routes-and-only-one-transition-had-a-gate` — `rule-delivery-modes`
- **C** A rule under `render: authority` is written into no file and found by its slug  
  `a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug` — `lookup-rule-delivery`
- **C** `governs:` is read on any page, and the red moved to a `<!-- text -->` slice that names no destination  
  `a-slice-with-no-governs-is-red-and-the-inert-field-is-gone` — `governs-outside-rules`

## Entities only (5)

### a dependency of this repository

*what may be added, what is merely declared, and what the no-new-dependencies rule actually reaches. Answers "may I depend on this". Added 2026-08-22, when a package that was installed, imported and undeclared turned out to sit outside a rule that is entirely about it. Narrow on purpose: no existing family asks about a package rather than about a field, a mechanism or a script. `register-file-format` is the obvious second member and moving it is a judgement about the corpus rather than about this slug, so it was left where it is.*

**verdict:** harness-facing

- **E** `python3` on this machine is the Microsoft Store stub, and it hangs rather than failing  
  `python3-on-this-machine-is-the-microsoft-store-stub` — `python3-store-stub`

### a rule page and the slice that travels

*what makes a page a rule, what part of it is rendered elsewhere, and how rules are numbered and ordered. Answers "should this be a rule, and what of it leaves the page".*

**verdict:** vault-facing

- **E** `wiki/rules/` holds the rules of the repository's `CLAUDE.md`, and from 2026-08-20 one page in it governs `.claude/rules/ast-boundaries.md` instead  
  `wiki-rules-holds-the-rules-of-the-repository-claude-md` — `rules-folder-inventory`

### how the owner is asked

*how a question is put to the owner, how his answer is read, and what a proposal from him is and is not. Answers "did he decide that, or was he thinking out loud".*

**verdict:** harness-facing

- **E** The owner's instructions note is design intent, and this is what was built from each line of it  
  `the-owners-instructions-note-and-what-was-built-from-it` — `owners-design-intent`
- **E** The owner's method note is the why under the instructions, and this is what was built from each line of it  
  `the-owners-method-note-and-what-was-built-from-it` — `owners-method-note`
- **E** `grill-me` — the owner's interview skill, added mid-session on 2026-08-16  
  `grill-me-skill` — `interview-skill`

### the end of a session

*what the retro is, what it is not, what it routes into, and what a ritual nobody announced is worth. Answers "what do I do when the work is finished".*

**verdict:** harness-facing

- **E** The retro step: its skill, its form, and the transit file it writes  
  `the-retro-step` — `retro-step`

### the toolkits this store was read against

*the published spec-driven-development tooling this vault has been compared with, what each has that this does not, and where they disagree with each other. Answers "has somebody already built this, and what did they do differently". Added 2026-08-23 with one member; it is not *a dependency of this repository*, because nothing here depends on either.*

**verdict:**

- **E** openspec and spec-kit, the published toolkits this store was read against  
  `openspec-and-spec-kit` — `external-spec-toolkits`
