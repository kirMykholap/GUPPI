<!-- approved 17:11:14 · session 4df9d181 -->

# Spec — session 1432, 2026-09-29

## Case 510 — Slice 4: the parked pages and the documents of 2026-08 are deleted, and the reading moves to the close

> **context:**
> `vault/parked/` holds the old vault, which was moved out of the live vault on 2026-09-07 and 2026-09-09. It holds 531 pages: 147 concepts, 218 decisions, 47 entities (44 under `2026-09-09`, 3 under `2026-09-07`), 36 rules (35 under `2026-09-09`, 1 under `2026-09-07`), 52 proposals and 31 lessons. It also holds eight register files (seven `.md` files and `pages.base`), six `_schema.yaml` files and two `.gitkeep` files. These counts come from three tool runs:
> - A Grep count over `vault/parked/` limited to `*.md` printed "across 538 files". That is 531 pages and the seven register `.md` files.
> - A Glob of `vault/parked/*/entities/*.md` listed 47 files.
> - A Glob of `vault/parked/2026-09-09/registers/*` listed 8 files.
>
> The rule under `2026-09-07` is `an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test.md`. The pre-spec count of 35 rules and 530 pages missed it.
> `docs/` holds 40 files, by a Glob of `docs/**/*`: the plans and specs of the job-hunt app, lesson drafts and notes of the old harness, a handoff, the six session-rule drafts, the migration plan with its README, and the harness map of 2026-09-07. The harness they describe no longer runs, the job-hunt app's code is gone from the tree, and each session-rule draft now has its live rule page. No module, test, hook, `Makefile` target or `pyproject.toml` entry reads either folder. The sprint cannot close while they stand. The Estimate `estimate-sprint-migration-leftovers-gone` lets a parked page only become a live page or go to the archive, so deleting it would make that promise false.
> In three rounds the person decided the following:
> - This Case covers only the parked pages and the documents. The old archive root, the empty raw date folders, and `git pull` and `gh` stay questions for the close.
> - The parked pages are deleted, not archived and not converted.
> - Every file under `docs/` is deleted except `docs/migration/migration-plan.md`. The plan says of itself "Discard this document once migration is complete", and the sprint page names it in its purpose, so the Case that closes the sprint deletes it.
> - The leftovers item moves from Slice 4 to Slice 5, and Slice 4 leaves the sprint page. The Estimate is read only at the close. Until then the item would come back on every Frontier, and `generate` moves an item that is passed over three sessions in a row to the Backlog (`rule-sprint`, case 354.1).
>
> Git history keeps every deleted file, at commit `f9a27b8` and before.
> The Case stays one Case with two items, not two sub-cases. Its first ratification already wrote the line of case 510 for the Estimate, and a split would leave that line with no item under its own Case. `materialize.py` lifts `when` and `then` only into an Estimate's item that sets `status` and writes no Criterion, so the item on the sprint page lifts nothing. For that reason `then` holds the promise alone, and the move on the sprint page stands in `tasks`: a `then` line about the render would enter the Criterion.
> The Criterion is replaced whole. The check of the answer notes that two old lines are not carried; both are left out on purpose:
> - "`vault/parked/` is empty or absent: each of its pages became a live vault page or lies in the archive" becomes "`vault/parked/` is absent: its pages were deleted". This is the person's choice.
> - "What to do with each thing this promise does not decide: those are the Cases of Slices 4 and 5" becomes two `－` lines. This Case decides the Slice 4 part, so what is left is the migration plan and the Slice 5 items.
>
> The lines on the documents, the archive, the raw folders, `git pull` and `gh` stay word for word.
> The sprint page changes by one `replace` pair in `## Milestones`. The pair runs from the Slice 4 heading to the Slice 5 heading, which hits the page once. It puts the item, with its text updated, first under Slice 5. Pre-spec asks for an `update` of the sprint page from a Case that closes a sprint item (case 314.2). After the change, `guppi sprint` renders Slice 5 as the current milestone, and the next `/hi` puts its items on the Frontier. No Estimate of `entity-sprint-migration` or `rule-sprint` has a Criterion about the order of the milestones, so none is touched. `## Closed` and the other items of Slice 5 stay word for word. The Slice 4 work is recorded in the History of the sprint page.
> The deletions are one-off commands in `tasks`, not decision lines. A decision line names a page, and `generate` fails on a `delete` of files that are not a page, as it did on the old-harness line of 2026-09-09 (case 48).
> What was found in the frame, and why each item stands:
> - `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction` names a parked concept as its `source`. The person chose to leave it: a lesson is a record of what was studied, `rule-lessons-schema` asks for "url or reference", and git keeps the file.
> - Old decision pages that name `vault/parked/` or `docs/` (among them 102.1–102.4, 166.1–166.4 and `decision-case-6`'s `source`) are records of their day and stay.
> - `make lint` reads only `vault/wiki/`.
>
> The Case creates no page, so no vault query was run. The reading of the Estimate waits for the close of the sprint (case 428.1). Not done here: the old archive root, the raw date folders, `git pull`, `gh` and the deletion of the migration plan, which are all Cases of Slice 5.

> **problem:**
> The parked pages and the documents of 2026-08 no longer serve any purpose, but the sprint's done-condition allows a parked page only to become a live page or to lie in the archive. Deleting them needs that promise changed and a decision. What is left of the item after the deletion is a reading at the close, but the item still stands as the current milestone, so it would come back on every Frontier.

> **given:**
> `estimate-sprint-migration-leftovers-gone` — the promise, its Criterion replaced whole
> **＋** `entity-sprint-migration` — the sprint page it is a done-condition of; its item moves from Slice 4 to Slice 5, and `vault/wiki/sprint.md` renders it
> **＋** `vault/parked/` — the parked pages of the old vault, deleted
> **＋** `docs/` — the documents of 2026-08, deleted
> **＋** `docs/migration/` — the rule documents of the migration, deleted
> **＋** `docs/migration/migration-plan.md` — the migration plan, left to the closing Case
> **＋** `vault/archive/` — the archive and its roots
> **＋** `vault/raw/` — the date folders

> **when:**
> Someone reads the tree of the repository at the close of the sprint.

> **then:**
> `vault/parked/` is absent: its pages were deleted by a decision named in the reading, and git history keeps them.
> **＋** Under `docs/` no 2026-08 document remains, and no rule document of `docs/migration/`; each became a page, was archived, or was deleted by a decision named in the reading.
> **＋** `vault/archive/` has no root outside the folders of its sprints; `vault/raw/` has no date folder without a session.
> **＋** A decision stands on `git pull` without an upstream and on `gh` without a login — keep as is, or repair — and is named in the reading.
> **－** `docs/migration/migration-plan.md` is outside this promise: the Case that closes the sprint deletes it.
> **－** What to do with the old archive root, the date folders of `vault/raw/`, `git pull` and `gh`: those are the Cases of Slice 5.

```then
update:
- slug: estimate-sprint-migration-leftovers-gone
  set:
    status: pending
  change: the Criterion replaced whole — the parked pages deleted, not archived; the migration plan left to the closing Case (case 510)
- slug: entity-sprint-migration
  replace:
  - old: |-
      ### Slice 4 — conversion of the parked pages by group

      - [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

      ### Slice 5 — closing
    new: |-
      ### Slice 5 — closing

      - [[estimate-sprint-migration-leftovers-gone]] — `vault/parked/` and the documents of 2026-08 under `docs/` deleted (case 510); the old archive root, the empty raw date folders, `git pull` and `gh`, and the reading, at the close
  change: 'Slice 4 done: the parked pages and the documents of 2026-08 deleted, the item moved to Slice 5 for its reading at the close; Slice 4 removed (case 510)'
```

```tasks
- [x] update `estimate-sprint-migration-leftovers-gone`
- [x] update `entity-sprint-migration`
- [x] `git rm -r vault/parked` — one-off: the parked pages, the register files, the `_schema.yaml` and `.gitkeep` files, and both date folders
- [x] `git rm -r docs/superpowers docs/migration/README.md docs/migration/rule-*.md` and every file at the root of `docs/` — one-off: `docs/` holds only `docs/migration/migration-plan.md` after it
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-migration-leftovers-gone` — by hand on the tree at the close of the sprint
```

## Case 511 — The options and the lists of a round stand on their own lines

> **context:**
> A round of questions from `case-guppi`, and the person's own `/grill-me`, follows the question template of the skill `grill-me`. Today the options come right after the `**Now:**` text as ordinary bullet items `- **(a) name**`, and no word introduces them. A list inside the Now text uses the same bullet, so the options blend into the text above them. Enumerations are also written inside a sentence. For example, "the hook checks (1) the heading, (2) the ledger lines and (3) the fence" runs as one line where three lines would read better.
> The person asked for three changes. Every list, numbered or not, starts on a new line. A word stands before the options to say that a list of choices follows. The options carry their own mark, so they look different from any other list. In the round the person settled the details: the label `**Options:**`, the mark `🔹` in place of the bullet, what counts as a list, and a list allowed inside an `**After:**` item and under the `➡️` line. The person saw an example question in the new form and accepted it. The person also asked for the same list rule in the `**Context:**` paragraph that opens a first round of `case-guppi`. That was sub-case 511.2, which Case 512 of this session superseded and which now carries the change, so 511.2 has left the Spec and Case 511 keeps only 511.1.
> The Render of `rule-skill-grill-me` holds the template. No code reads the shape of a round: a search of the `.py` files for the round's labels and marks finds nothing, so no reader has to accept an old form beside the new one. The Case creates no page, so no vault query was needed.
> From the frame: the Criterion of `estimate-skill-grill-me-asks-in-rounds` describes the option shape, so it is replaced whole, and the old option line and its wording are dropped on purpose. The lines of `rule-case-protocol`, and `estimate-case-protocol-shows-the-built-case`, say that the main agent shows each question closing with its `➡️` line and translates the recommended answer in place. They stand: a list under `➡️` is part of the recommended answer, and the showing translates it line by line. The rule "an option has nothing else under it" stands, because a list inside an `**After:**` item is part of that item. The Render of `rule-skill-wait-what` and the Criterion of `estimate-skill-wait-what-re-pitches` both say that options take "the question shape of `.claude/skills/grill-me/SKILL.md`". They point to the template and do not repeat its shape, so they stay true and pick up the new shape as they stand. The shape itself is read by `estimate-skill-grill-me-asks-in-rounds`, as that Criterion says.

> **problem:**
> The template does not introduce the options, gives them the same bullet as any other list, and has no rule against enumerations written inside a sentence. A round is harder to scan than it needs to be.

### Case 511.1 — The grill-me template introduces the options with a label, marks them with 🔹 and puts every list on its own lines

> **given:**
> `rule-skill-grill-me` — the rule page whose Render holds the question template.
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill rendered from it.
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by `skills: [grill-me]`.
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise on the shape of a question.
> **＋** `rule-case-protocol` — the rule on how the main agent shows a round, translated line by line.

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` item a list stands nested inside that item.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** A short series of words inside a sentence stays in the sentence.
> **－** No line of a question except an option starts with `🔹`.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-case-protocol`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The `**Context:**` paragraph of a round of `case-guppi`, its lists included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

```then
update:
- slug: rule-skill-grill-me
  replace:
  - old: |2-
          - **(a) <option name>**
            - **After:** <what holds with this option>
          - **(b) <option name>**
            - **After:** <what holds with this option>
    new: |2-
          **Options:**

          🔹 **(a) <option name>**
            - **After:** <what holds with this option>

          🔹 **(b) <option name>**
            - **After:** <what holds with this option>
  - old: 'Each option starts on its own line as a list item with its name in bold, and under it stands one nested `**After:**` item: what holds with this option.'
    new: 'The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark 🔹 and its name in bold, and under it stands one nested `**After:**` item: what holds with this option. No other line of a question starts with 🔹.'
  - old: In the language of the chat the labels may stand translated; the shape stays.
    new: |-
      In the language of the chat the labels may stand translated; the shape stays.

      A list starts on a new line and never runs inside a sentence. Items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things, stand one per line; a short series of words inside a sentence stays in it. In the `**Now:**` text a list stands under the sentence that introduces it. Under an `**After:**` item it stands nested one level deeper, inside that item. In the recommended answer it stands on the lines under `➡️`, which close the question.
  change: the options of a question stand under an Options label, each marked with 🔹; every list stands one item per line (case 511.1)
- slug: estimate-skill-grill-me-asks-in-rounds
  set:
    status: pending
  change: the Criterion replaced whole — the Options label, the 🔹 mark and a list one item per line (case 511.1)
```

```tasks
- [x] update `rule-skill-grill-me`
- [x] update `estimate-skill-grill-me-asks-in-rounds`
- [x] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
- [ ] read `estimate-skill-grill-me-asks-in-rounds` — in a later session after the render: one round of `case-guppi` or of the person's `/grill-me`, read in the chat
```

## Case 512 — A number in a round stands only beside a quotation of what it points to

> **context:**
> When a Case needs a choice, `case-guppi` first asks the person a round of questions. Today its instructions say that case numbers, the history of a slug and facts of the frame stay out of the context and the question bodies and stand in the `➡️` line as the source of the recommendation. The last reading of `estimate-case-build-writes-a-plain-round` failed. One first round named "case 193" in its Context, and another round named "Cases 506 and 507" in a Now line. The person looked at the problem more widely than where the number stands. A bare number tells them nothing: to use it they must already know what that Case says, and the agent then argues from it as if they did. In the person's words, translated from the chat: "If the agent refers to some case or historical fact, it is better to give it as a quotation from what it refers to."
> Over four rounds the person decided the following:
> - The rule is for rounds only. The `context` of a Case is read mainly by the agent and becomes history on the Decision page, so it keeps its numbers and details. `problem` and `recommend` work well as they are, so the rule on the story of a Case (`rule-case-protocol`) does not change.
> - A round says things in plain words and uses no number where plain words are enough. A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in a round only beside a short quotation of the words it points to, as the source of that quotation. This holds in any line, the `➡️` line included.
> - A page name in a code span is not such a reference. It stays where the question is about that page.
> - This Case supersedes Case 511.2, which replaced the Criterion of the same Estimate earlier in this session and kept the old line on case numbers. Signing that Criterion again in a second wording is the fault recorded in `lesson-case-build-signs-one-criterion-twice-in-a-session`. So this Case carries both changes of 511.2. The list lines of the Criterion are carried word for word. The list sentence of `rule-case-build` now only points to the grill-me template and says no list shape of its own. Pre-spec found that the wording of 511.2 said the shape again, which the `then` line "word no shape of their own" forbids, and the person accepted the fix. Case 511.1 stands, and the Frontier line that Case 511 closed stays closed by it. The parent text of Case 511 still says the Case splits into two sub-cases. That is now true only of its record, and the person sees it when 511 is shown again, if ever.
>
> The Criterion is replaced whole. The check of the answer notes four lines of the live Criterion that are not carried word for word. Each is dropped on purpose:
> - "The instructions of `case-guppi` point each question to the question shape…" is carried in the wording of Case 511.2, which adds the lists of the Context.
> - "The shape of a question is read by `estimate-skill-grill-me-asks-in-rounds`, not here" is carried in the wording of Case 511.2, which adds what counts as a list.
> - "Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line…" is replaced by the plain-words line and the quotation line. "Facts of the frame" is dropped because the person named numbers and history. A frame fact said in plain words does the harm the person described no more than any other sentence.
> - "The `context` of a Case keeps its case numbers and frame facts…" is widened to the `context`, `problem` and `recommend` of a Case, as the person chose rounds only.
>
> The `purpose` of the Estimate still says "case numbers only in the recommended answer", and its `method` counts "four parts", so both are set new.
>
> From the frame, these stand:
> - `rule-skill-wait-what` and `estimate-skill-wait-what-re-pitches` say the main agent's re-pitch holds no case number and that "A quoted line keeps its case numbers as written". This agrees with a number that stands beside its quotation.
> - `estimate-skill-grill-me-asks-in-rounds` leaves "the place of its case numbers" to this Estimate. That remains true.
> - `rule-case-protocol` lets the story sections of a Case "name a case number as the source of a claim". This Case leaves that as it is.
> - `estimate-case-build-writes-the-case` does not speak of numbers.
>
> No code reads a round: a search of `guppi/` for case numbers and `➡️` finds nothing. So no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: the story sections of a Case, and a mechanical check of a round, which the person did not choose.

> **problem:**
> A round sends the person to a bare case number, a session id or the history of a page. That tells them nothing unless they already know what it points to, and the agent argues from it as if they did. The instructions allow such numbers in the `➡️` line, and the numbers still slipped into the Context and the Now lines.

> **given:**
> `rule-case-build` — the rule page whose Render holds the round instructions of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from it.
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill whose template sets the question shape and what a list is.
> **＋** `estimate-case-build-writes-a-plain-round` — the promise on a readable round.
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape of a question and of a list.
> **＋** `rule-case-protocol` — the rule on the story sections of a Case, left as it is.
> **＋** `rule-skill-wait-what` — the rule on the main agent's re-pitch, whose quoted lines keep their numbers.

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** A list in the `**Context:**` stands one item per line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a list.
> **＋** The instructions of `case-guppi` point each question, and each list of the Context, to `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
> **＋** The round says what it rests on in plain words and uses no number where plain words are enough.
> **＋** A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in any line of the round, the `➡️` line included, only beside a short quotation of the words it points to, as the source of that quotation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** A page name in a code span is no such reference: it stays where the question is about that page.
> **－** The shape of a question, and what counts as a list, are read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** The `context`, `problem` and `recommend` of a Case keep their numbers as `rule-case-protocol` allows: this promise is about a round only.

```then
update:
- slug: rule-case-build
  replace:
  - old: a part with nothing to say left out. Write the round for a person who has not opened the pages
    new: a part with nothing to say left out. A list in the context stands as the grill-me template sets a list. Write the round for a person who has not opened the pages
  - old: case numbers, the history of a slug and facts of the frame stay out of the context and the question bodies, and stand in the `➡️` line as the source of the recommendation, and in the `context` of the Case;
    new: say in plain words what the round rests on, and use no number where plain words are enough; a case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in a round, in any line and the `➡️` line too, only beside a short quotation of the words it points to, as the source of that quotation, never alone; a page name in a code span is no such reference and stays where the question is about that page; the `context`, `problem` and `recommend` of the Case keep their numbers;
  change: a list in the Context of a first round stands as the grill-me template sets a list; a number in a round stands only beside a quotation of what it points to (case 512, supersedes 511.2)
- slug: estimate-case-build-writes-a-plain-round
  set:
    status: pending
    purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a number only beside a quotation of what it points to, and an unknown term explained
    method: 'by hand, in a session after the render: one first round and one later round of case-guppi read in the chat against the Criterion'
  change: the Criterion replaced whole — a list in the Context one item per line; a number in any line of a round only beside a quotation of what it points to (case 512, supersedes 511.2)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-a-plain-round`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render: one first round and one later round of `case-guppi` read in the chat against the Criterion
```

## Case 513 — A Decision page keeps the Problem, and the Case file keeps the rest

> **context:**
> When a Case is ratified, the librarian's `guppi generate` writes a Decision page into `vault/wiki/decisions/`. Today the page copies three sections of the Case: `## Context`, `## Problem` and `## Given`. It adds the lists of the pages the Case created, updated, deleted or deferred, `## Deferred` for a Case that put something off, and `## History`. Since session 2026-09-27/1819 (case 457), the `SubagentStop` hook of `rule-case-check` also writes every Case that `case-guppi` builds to `raw/<date>/<HHMM>/cases/case-<N>.md`, with all eight sections. The session folder then moves whole into `vault/archive/<sprint>/<date>/<HHMM>/raw/`. So the same text is stored three times: in the Case file, in `spec.md` (which holds no `recommend`) and on the Decision page. The Context is the longest of these copies and is written for the agent. For example, the page of case 506.2 repeats a context of several hundred words that its Case file already holds.
> In one round the person accepted every recommendation. A new Decision page keeps only `## Problem`, the lists, `## Deferred` and `## History`. The schema's text says where the Case file lies, and no new field is added. The page of a short-form deferred decision keeps `## Context`, because the main agent writes that form and it gets no Case file. The pages already written are not rewritten, so `## Context` becomes optional in the schema.
> What `case-guppi` found in the frame. I checked the facts the person was given. `case-510.md` holds all eight sections. `spec.md` holds no `recommend`. The archive holds Case files from `2026-09-27/1819` on, and the older sessions hold only `spec.md`. `rule-decisions-schema` says that `recommend` is "recoverable from the archived ledger", which is false today. 513.1 changes that sentence, the required sections, the `## Context` and `## Given` descriptions, the `origin` field and the example page. It also replaces the Criterion and the `method` of `estimate-decisions-schema-checked`. `estimate-generate-writes-the-decision-page` names the body `## Context` and `## Problem`, so 513.2 replaces its Criterion whole. `estimate-generate-writes-the-given` promises a `## Given` that is no longer written, so 513.2 deletes it and carries its `－` line on the old pages into the other Criterion. The cascade takes it out of the `estimates` of `rule-page-generation`, as in case 506.2. That rule's Purpose names no body section, so the rule stands. Two sentences of `rule-case-protocol` say that `given` "stays in the Case and on the Decision page", so 513.3 changes them. That rule's Estimates speak of the form of a Case, not of a Decision page, and an `update` of its Render touches no Estimate of the live reading (case 378.5).
> The person accepted four fixes from pre-spec. First, a Case superseded in its own session keeps its two-line body, `## Context` included (case 299.4), and `decision-case-511.2` of this session gets that body. So the schema text of 513.1 and its `then` name that body next to the short form. Second, the `method` of the Estimate said the pages of Cases 1–28 lack "Context and Problem". With Context optional, only Problem is a finding on them, so 513.1 sets the `method` anew. Third, I checked `## Given` on the live Decision pages. The pages of Cases before 201 carry it, from the model of case 52.1. The pages of Cases 201 to 375 carry none. The pages from 376 on carry it again. The new description says exactly this and no longer says "before case 378.3". Fourth, the sentence on this session's pages below is corrected.
> What the check of the answer notes, and why each note stands. Three Criterion lines are not carried word for word, on purpose. In 513.1 the line on the sections moves `## Context` from the required list to the optional one. In 513.2 the body line names `## Problem` alone. The old `－` line on no `## When` and no `## Criterion` becomes one `－` line that also says no `## Given`, and no `## Context` for a Case with `given`. Every other line is kept word for word. Three `then` lines of 513.2 share words with 513.1: the `## Context` of a Case without `given`, the sections the page does not hold, and the old pages that are not rewritten. This is expected. 513.1 promises what the schema file says and what lint accepts, while 513.2 promises what `generate` writes and leaves alone. They are separate promises with separate tests.
> Several sentences stay true and stand. `ask-guppi.md` reads the `## Problem` of a deferred decision, and that section stays. The case schema says that a deferred decision is taken up "from its page — `context` and `problem` as they stand". That page keeps its Context. `estimate-lint-catches`, `estimate-generate-renames` and `estimate-generate-cascades` speak of Decision pages but not of their body sections.
> Code and timing. `guppi/materialize.py` still lifts `context` and `given` into `case_text`, and `generate` uses `given` to tell the short form apart. The code changes in Work Mode, and the yaml is rendered in the librarian's run. So the pages of 510, 511.1 and 512 to 516 are written without Context. 511.2, superseded in its session, gets the two-line body, and 517 and 518, in the short form, keep Context. A `make lint` run before the render reports `missing section ## Context` on the pages written without it. `lint` only goes red, so no old form is kept, and that red is a note for the handoff by `rule-retro`. The Case creates no page, so no vault query was run.
> Not done: the old pages are not rewritten; `materialize`, `ask-guppi` and the archive are unchanged; no `case_file` field is added; the short form still writes no Case file.

> **problem:**
> The Decision page repeats the Case's Context and Given, which the Case file now keeps whole. The repeated Context is long, written for the agent, and makes the page hard to read. The schema also sends a reader to the ledger for the recommendation, but the ledger does not hold it.

### Case 513.1 — The Decision schema makes Context optional and points to the Case file

> **given:**
> `rule-decisions-schema` — the rule; its Render is the schema of a Decision page
> **＋** `vault/wiki/decisions/schema.yaml` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `guppi/lint.py` — reads the lists of the file for every page of `vault/wiki/decisions/`
> **＋** `cases/case-<N>.md` — the Case file in the folder of `origin`, which the schema names as the whole record of a Case
> **＋** `estimate-decisions-schema-checked` — the promise; its Criterion and `method` are replaced
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by`; values `status: current | superseded | archived`; the sections `## Problem` and `## History` required, `## Context`, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
> **＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
> **＋** A Decision page without `## Context` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
> **＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.
> **＋** The file says that the Case file, `cases/case-<N>.md` in the folder of `origin` with N the id of the top-level Case, holds the whole Case, `recommend` included, and moves into the archive with its session.
> **＋** The file says that a new page carries `## Context` only for a Case without `given`, the short form of a deferred decision, and in the two-line body of a Case superseded in its own session; that it never carries `## Given`; and that the pages written before keep the sections they carry.
> **－** The example page holds no `## Context` and no `## Given`.

```then
update:
- slug: rule-decisions-schema
  replace:
  - old: Either way the original is conversation history, recoverable from the archived ledger.
    new: Either way the original stays in the Case file, `cases/case-<N>.md` in the folder of `origin` (case 513).
  - old: The body is the Case that produced it, minus what belongs to the conversation rather than the decision.
    new: 'The body is the `problem` of the Case that produced it: the one paragraph a reader needs at the end of a link. The rest of the Case — `context`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` — stays in its Case file. A Case without `given`, the short form of a deferred decision, has no Case file, so its page keeps `## Context` as well; the page of a Case superseded in its own session has the two-line body of `## Context` and `## Problem` that names the superseding Decision (case 299.4). A page written before case 513 keeps the sections it carries and is not rewritten (case 513).'
  - old: 'required: ["## Context", "## Problem", "## History"]'
    new: 'required: ["## Problem", "## History"]'
  - old: 'optional: ["## Given", "## When",'
    new: 'optional: ["## Context", "## Given", "## When",'
  - old: The folder also holds the Spec with the Case.
    new: The folder also holds the Spec with the Case and, for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file `cases/case-<N>.md` with every section, N the id of the top-level Case; once the session is archived, the folder lies under `vault/archive/<sprint>/` (case 513).
  - old: required. What this is about.
    new: optional. What this is about. Written for a Case without `given`, the short form of a deferred decision, which has no Case file, and in the two-line body of a Case superseded in its own session (case 299.4); kept on the pages written before case 513; any other Case keeps it in its Case file (case 513).
  - old: written by `generate` on the page of a Case that has one (case 378.3); a page written between case 201.2 and case 378.3 carries none.
    new: 'written by `generate`, before case 513, on the page of a Case that had one: the pages of Cases before 201 carry it by the model of case 52.1, and the pages from case 376 on by case 378.3; the pages of Cases 201 to 375 carry none. A page written after case 513 carries none, and the Case file holds it (case 513).'
  - old: '## Context The site has checkout but no cart — items go straight from the catalogue to payment. ## Problem'
    new: '## Problem'
  - old: '## Given `entity-cart` — the page this Case creates. **＋** `entity-checkout` — the page the cart precedes. ## History'
    new: '## History'
  change: a new page carries Problem and no Context or Given, a short-form defer and a Case superseded in its session keep Context; the Case file named as the whole record, recommend included (case 513.1)
- slug: estimate-decisions-schema-checked
  set:
    status: pending
    method: 'pytest tests/test_schemas.py -k decisions on the live vault/wiki/decisions/schema.yaml — a page in the shape, a page without ## Context, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/ but the pages of Cases 1–28 without Problem (Slice 5)'
  change: the Criterion replaced whole and the method set anew — Context optional, the Case file named, the example without Context and Given (case 513.1)
```

```tasks
- [x] update `rule-decisions-schema`
- [x] update `estimate-decisions-schema-checked`
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] `tests/test_schemas.py`: a test that a Decision page without `## Context` has no finding against the live `schema.yaml`, skipped until the librarian renders the file of 513.1
- [x] read `estimate-decisions-schema-checked` — `pytest tests/test_schemas.py -k decisions`, then `make lint` with no `schema` finding on `vault/wiki/decisions/` but the pages of Cases 1–28, at a later session
```

### Case 513.2 — `generate` writes the Problem, and Context only for a short-form defer

> **given:**
> `guppi/generate.py` — `decision` and the docstring paragraph on the Decision page
> **＋** `tests/test_generate.py` — the tests of the Decision page and their fixture schema
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml` — the input; its `decisions` records carry `case_text`
> **＋** `vault/wiki/decisions/decision-case-<N>.md` — the Decision page of a Case
> **＋** `estimate-generate-writes-the-decision-page` — the promise; its Criterion is replaced whole
> **＋** `estimate-generate-writes-the-given` — the promise of `## Given`, deleted
> **＋** `rule-page-generation` — the rule of `generate`; the cascade drops the deleted Estimate from its `estimates`

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` from `case_text`, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A Case whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given`.
> **－** The Decision pages already written are not rewritten.

```then
update:
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  change: the Criterion replaced whole — the body is Problem, Context only for a Case without given, no Given (case 513.2)
delete:
- slug: estimate-generate-writes-the-given
  impact: A new Decision page carries no Given; the Case file holds it (case 513). The promise that no Given is written and old pages are not rewritten stands in estimate-generate-writes-the-decision-page; rule-page-generation loses it from estimates by the cascade
```

```tasks
- [x] update `estimate-generate-writes-the-decision-page`
- [x] delete `estimate-generate-writes-the-given`
- [x] `guppi/generate.py`: `decision` writes `## Problem` from `case_text`, `## Context` only when `case_text` has no `given`, and no `## Given`; the docstring paragraph on the Decision page says so
- [x] `tests/test_generate.py`: the Decision-page tests assert `## Problem` then `## History` with no `## Context` or `## Given` for a Case with `given`; `## Context` then `## Problem` for a Case without `given`; the fixture schema takes `## Context` as optional
- [x] read `estimate-generate-writes-the-decision-page` — `pytest tests/test_generate.py`, the tests of the Decision page, and the pages of the librarian's run, at a later session
```

### Case 513.3 — The case schema keeps `given` in the Case, not on the Decision page

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render

> **when:**
> `case-guppi` or the main agent reads `vault/wiki/case-schema.md`.

> **then:**
> The row of `given` and the paragraph on `when` and `then` say that `given` stays in the Case, in its Case file and in the Spec, and not on a Decision page.
> **－** The row of `recommend` still says that it is not carried onto the Decision page.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: It stays in the Case and on the Decision page and never enters an Estimate (case 378.1).
    new: It stays in the Case, in its Case file and in the Spec, and never enters an Estimate or a Decision page (cases 378.1, 513).
  - old: '`given` stays in the Case and on the Decision page, so `when` names'
    new: '`given` stays in the Case file and in the Spec, so `when` names'
  change: given stays in the Case file and the Spec, not on a Decision page (case 513.3)
```

```tasks
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 514 — Generate applies a Case to a page once

> **context:**
> When a Case is approved a second time in its session, its decision lines are written into the ledger again. The ledger hook skips a line only when it is word for word the same as a stored one. So a line that gained a `{supersedes:case N}` mark at the second approval is stored a second time. `materialize` makes one entry per line, and `generate` applies every entry, so the same change of one Case to one page runs twice. In session 1134 this happened to Case 508.2. L15–L16 stood without the mark and L67–L68 with it. L15 applied the `replace` pairs to `rule-skill-hi`, so L67 did not find its anchor and failed. L68 applied the Criterion of `estimate-hi-writes-frontier` a second time and wrote its History line twice, and `vault/wiki/log.md` holds that line twice too. `generate` tries an unapplied entry again at every run (case 53.3), so L67 fails again at each librarian run. The person chose these points in the rounds. The fix lives in `generate`, not in `materialize`: `materialize` never rewrites an entry it wrote, so a merge there would leave L67 failed. The doubled History and `log.md` lines stay as a record. `case-schema.md` stays as it is, because its sentence that the hook does not append a line it already holds stays true. The promise joins the Criterion of `estimate-generate-fails-alone`, whose trigger already covers an entry already handled. With the change, L67 finds L15 applied at the next librarian run, gets `applied` and loses its `failed` mark, with no one-off migration. The mark the repeated line carries still reaches the yaml, since `materialize` handles each line's `{supersedes}` as it does today. The Case creates no page, so no vault query was needed. Four texts in the frame stay true. `estimate-generate-ticks-the-spec` stands: the repeat is marked `applied` and its tick finds no open line, which is no error. `estimate-generate-writes` stands, because its trigger is an entry applied to a page and a repeat changes no page. `estimate-materialize-assembles` stands, because every line still has its entry. The dedupe sentence of `rule-ledger-write` stands. W15, the reading of `estimate-generate-fails-alone` on this session's Frontier, waits for a later session, because the ledger hook refuses a reading of a page the session changes (case 428.1).

> **problem:**
> A Case approved again in its session, with a mark added to its lines, is applied twice to each page it names. The second application fails a text edit, or writes the same History line again, and a failed entry fails again at every run.

> **given:**
> `guppi/generate.py` — applies the entries of a yaml to the pages
> **＋** `materialize.yaml` — the entries `generate` reads
> **＋** `vault/wiki/log.md` — the log `generate` appends per entry
> **＋** `rule-page-generation` — the rule of `generate`
> **＋** `estimate-generate-fails-alone` — the promise on failed, skipped and marked entries
> **＋** `tests/test_generate.py` — the tests of `generate`

> **when:**
> `uv run guppi generate` meets an entry of `materialize.yaml` it cannot apply, or one already handled.

> **then:**
> An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
> **＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
> **＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
> **＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
> **＋** An `update` with no content prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, changes no page and is marked applied.
> **＋** A `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` marked `applied` is marked `applied`, loses a stale `failed` mark, changes no page, appends nothing to `vault/wiki/log.md` and prints `generate: <slug>: line N repeats line M of case C; nothing applied` on stdout, whichever of the two lines stands first in the ledger.
> **－** The failure of one entry changes no other page: `vault/wiki/log.md` after it is level with the pages.
> **－** An `update` with `sections.Criterion` on an Estimate page does not fail for want of a `method` field.
> **－** An `estimate` or a `lesson` entry is never taken for a repeat: it carries no `case`.

```then
update:
- slug: rule-page-generation
  replace:
  - old: reported, and the rest apply (case 47).
    new: reported, and the rest apply (case 47). An entry whose Case, kind and slug match an entry of the same yaml that already applied is marked applied and changes no page, so a Case approved again in its session, its lines written again with a mark added, changes each page once (case 514).
  change: an entry whose Case, kind and slug match an applied entry of the same yaml is marked applied and changes no page (case 514)
- slug: estimate-generate-fails-alone
  set:
    status: pending
  change: the Criterion replaced whole — an entry that repeats an applied entry of its Case, kind and slug is marked applied, changes no page and prints one line
```

```tasks
- [x] update `rule-page-generation`
- [x] update `estimate-generate-fails-alone`
- [x] `guppi/generate.py`: in `apply`, before an entry of kind `create`, `update`, `delete` or `defer` is applied, look for an entry of the same yaml with the same `case`, `kind` and `slug` marked `applied`; when found, mark the entry `applied`, drop its `failed`, print the stdout line and apply nothing; the docstring says so beside the no-content update
- [x] `tests/test_generate.py`: a repeated `update` whose `replace` anchor the first entry consumed is marked applied, fails nothing, changes no page, adds no History or `log.md` line and prints the stdout line; the same with the first entry failed and the second applied, on the rerun; a repeat of a `create` writes no collision; an `estimate` entry of the same slug is applied as before
- [x] read `estimate-generate-fails-alone`
```

## Case 515 — Each glossary row points at the page that defines its term

> **context:**
> The glossary that `/hi` loads is the `## Terms` table of `entity-glossary`. `guppi glossary` renders the table into `vault/wiki/glossary.md`. Each row holds a term, its meaning in one line, and in `where` one wikilink to the page that defines the term. The script stops on a `where` cell that holds more than one link. The promise `estimate-glossary-terms-defined` says that each `where` page defines its term. The reading at the `/hi` of this session failed on six rows. "Plan Mode" points at `rule-plan-mode`, whose Purpose names neither the term nor its meaning. "Page fields" and "Category fields" point at `rule-page-schemas`, which leaves the fields to its six child schemas. "Scripts" points at `rule-harness`, which names the renderer and lint but not page generation or cleanup. "Decision, Lesson, Insight (status)" points at `rule-page-generation`, which names none of `current`, `clustered` or `actioned`. "Working files" points at `rule-raw-archive`, which names neither `log.md` nor `tags.md`. The main agent found a seventh row. "Executable plan, Work Mode" says "subagents transcribe, a fork comes back as a Case", but `rule-work-mode` says "Subagents in Work Mode, the test of each Estimate written first and the rest of the model are not decided yet (case 479.2)".
>
> In one round the person chose to fix only the glossary table. Each row points at a page that already defines its term. A term spread over several pages becomes one row per page, and each meaning is cut down to what its page says. The rule pages stay as they are. The person rejected adding sentences to those pages, because `rule-page-schemas` would copy what its children hold. The person also rejected several links in one `where` cell, which would change `guppi/glossary.py`, its tests and the Criterion. About Work Mode, the person said "Executable plan" is a term for a future Work Mode: after the Spec is approved, a plan that maps the tasks is written. That plan is not built yet, and the person left the wording of the row to `case-guppi`. No live page defines "Executable plan". Its only other uses are `docs/migration/`, which Case 510 deletes, and old Decision pages. So the term leaves the table. It comes back as a row with the Case that decides the plan. The row "Work Mode" says what `rule-work-mode` says today. The rule that a subagent never decides and returns at a fork stays in the row "Main agent, Subagent", whose `where` is `rule-case-protocol`.
>
> At pre-spec, `ask-guppi` found an eighth row, and the person accepted the fix. The row "Decision page" says the body is "Context, Problem, Given — the frame of the Case (case 378.3)". Case 513.1 of this session changes `rule-decisions-schema`. After it, a new Decision page carries `## Problem`, `## Deferred` for a Case that put something off, and `## History`. It carries `## Context` only for a Case without `given`, such as the short form of a deferred decision, and never carries `## Given`. The Case file `cases/case-<N>.md` in the folder of `origin` holds the whole Case, and a page written before case 513 keeps its Context and Given. This Case rewrites the row to say what that schema will say. Both pages land at the same librarian run, so the reading in a later session finds them in agreement.
>
> What `case-guppi` found in the frame. Each new meaning was checked against its page. `rule-case-protocol` defines Plan Mode in "Plan Mode and the Frontier". The schema rules list the fields and the status values of their categories. The old "Page fields" row said `code_ref` is on an Entity Leaf only, but `rule-entities-schema` allows it on both kinds, so the new row follows the schema. `rule-lint` and `rule-render-harness` define lint and the renderer. Page generation and cleanup already have rows: `origin`, `deferred_by`, "Entity / Rule (status)" and `archived`. `rule-vault-layout` names `log.md` as written by `generate` and `cleanup`, so the old words "by hook" were wrong. It also names `tags.md` as the registry of ratified tags, and `raw/` and `archive/` as the working folders. `rule-raw-archive` defines the session folders and `event_log.md`. The rows move to the groups of their new pages' parent MOCs, as `rule-glossary` says. `glossary.py` accepts the new rows as they are, so no reader has to accept an old form.
>
> This session's other Cases touch two pages this Case names. Case 513.1 updates `rule-decisions-schema`, and the row "Decision page" follows it. Case 513.3 updates `rule-case-protocol` only in its sentences on `given`, so the Plan Mode section that the row "Plan Mode" rests on stays as it is. Cases 511, 512 and 514 touch none of the pages named here. The Criterion of `estimate-glossary-terms-defined` stands. It already promises what this Case makes true, and the Case does not change the promise. The reading waits for a later session, after the librarian's run renders the table. The other 41 rows passed the reading and are not touched. The Purpose of `entity-glossary` says a term enters, changes or leaves by an `update` of the page, and its `change` line is the History. That stays true. No other page or test uses the removed terms except the old Decision pages, which are records. The Case creates no page, so no vault query was run. Not done: "Executable plan" gets no page and no defer here. That would be a Case of its own.

> **problem:**
> Eight rows of the glossary point at a page that does not define their term, claim what the page leaves undecided, or will be made false by a change ratified this session. So the glossary that `/hi` loads sends the reader to the wrong page, and in some places it states a fact no page holds.

> **given:**
> `entity-glossary` — the page whose `## Terms` table this Case changes
> **＋** `vault/wiki/glossary.md` — the file `guppi glossary` renders from the table
> **＋** `estimate-glossary-terms-defined` — the promise the table is brought back in line with; its Criterion stands
> **＋** `rule-case-protocol` — the page that defines Plan Mode
> **＋** `rule-entities-schema`, `rule-rules-schema`, `rule-estimates-schema`, `rule-lessons-schema`, `rule-insights-schema`, `rule-decisions-schema` — the schema rules that define the fields and the status values of each category, and the Decision page and its Case file
> **＋** `rule-lint` and `rule-render-harness` — the pages of lint and of the renderer
> **＋** `rule-vault-layout` and `rule-raw-archive` — the pages of the working files and of the session folders
> **＋** `rule-work-mode` — the page of Work Mode, which leaves subagents undecided

> **when:**
> `uv run guppi glossary` writes `vault/wiki/glossary.md` from the `## Terms` table of `entity-glossary` at the librarian's run, and a reader reads each row against the page its `where` names.

> **then:**
> `uv run guppi glossary` exits 0, and each row names in `where` one live page that defines the term of the row.
> **＋** The row of Plan Mode names `rule-case-protocol`.
> **＋** The fields of each page category stand in a row of their own, whose `where` is the schema rule of that category.
> **＋** The status values of Decision, Lesson and Insight stand in a row each, whose `where` is the schema rule of that category.
> **＋** The row of the Decision page says what `rule-decisions-schema` says of the body of a new page and of the Case file that holds the whole Case.
> **＋** A row for lint names `rule-lint`, and a row for the renderer names `rule-render-harness`, in place of the row Scripts.
> **＋** The row of the working files names `rule-vault-layout`, and a row of the session folders names `rule-raw-archive`.
> **＋** The row of Work Mode says what `rule-work-mode` says, and names no subagent.
> **－** No row names the term "Executable plan", since no live page defines it yet.

```then
update:
- slug: entity-glossary
  replace:
  - old: '| Plan Mode | Frontier items discussed as Cases until each is ratified or deferred | [[rule-plan-mode]] |'
    new: '| Plan Mode | Frontier items discussed as Cases until each is ratified or deferred | [[rule-case-protocol]] |'
  - old: |-
      | Page fields | `type` the kind; `purpose` one line the index is built from; `children` MOC only, ordered on a Rule; `estimates` cross-cutting on a MOC; `code_ref` (Entity Leaf), `implementation_ref` (`hook`, `check` rules) | [[rule-page-schemas]] |
      | Category fields | Estimate: `purpose`, `method`, `checked`, the sections `Criterion` and `Result` (case 193). Lesson: `trigger`, `root_cause`, `source` (in a ledger line, the external origin). Insight: `severity` (children not archived), `addressed_by` | [[rule-page-schemas]] |
    new: |-
      | Entity fields | `type` the category; `purpose` one line, from which the index line is built; `children` on a MOC; `estimates` on a Leaf its own checks, on a MOC the cross-cutting ones; `code_ref` paths to code, on either kind | [[rule-entities-schema]] |
      | Rule fields | `purpose` one line, what the rule prevents; `enforcement` `hook`, `check` or `render`; `implementation_ref` on `hook` and `check`; `governs` and `render_mode` on `render`; `children` ordered, on a MOC; `estimates` that the rule does what it claims | [[rule-rules-schema]] |
      | Estimate fields | `method` required, how the promise is checked; `purpose` the promise in one line; `checked` the date of the last reading, written by `generate`; the sections `Criterion` and `Result` | [[rule-estimates-schema]] |
      | Lesson fields | `root_cause` one line, what clustering compares; `source` on a `knowledge` lesson, where the material came from; the sections `Trigger` and `Root cause` | [[rule-lessons-schema]] |
      | Insight fields | `pattern` one line, the shared root cause; `children` the Lessons clustered; `severity` the count of children not archived, computed by `generate`; `addressed_by` the one decision that actioned it | [[rule-insights-schema]] |
  - old: '| Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`, body Context, Problem, Given — the frame of the Case (case 378.3); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |'
    new: '| Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`; body `## Problem`, `## Deferred` for a Case that put something off, and `## History`; `## Context` only for a Case without `given`, such as the short form of a deferred decision, and never `## Given`; the whole Case, `recommend` included, stays in its Case file `cases/case-<N>.md` in the folder of `origin`; a page written before case 513 keeps its Context and Given (case 513); never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |'
  - old: '| Scripts | Page generation (fills `origin`, `slug`, `status`); cleanup (moves `archived` pages); lint (refs, schema, statuses, orphans); renderer (Rule body into the file it governs) | [[rule-harness]] |'
    new: |-
      | Lint | `guppi lint`, run by `make lint` after the render, sprint, backlog and glossary checks: reports a page that breaks its schema, points at nothing, claims a status its Estimates do not support, or waits for a reading; red is a signal, not a gate | [[rule-lint]] |
      | Renderer | `guppi render` writes the text of a Rule page into the harness file it governs, so the page stays the source; it runs with lint and as the librarian's step after `cleanup` | [[rule-render-harness]] |
  - old: '| Decision, Lesson, Insight (status) | `current`/`superseded`/`archived`; `new`/`clustered`/`archived`; `open`/`actioned`/`archived`, a new Lesson reopens `actioned` unless a decision of its own session closed its cause (case 284.4) | [[rule-page-generation]] |'
    new: |-
      | Decision (status) | `current` / `superseded` / `archived`; `superseded` once a later Case names it in `supersedes`, `archived` when the cascade of `generate` then meets it | [[rule-decisions-schema]] |
      | Lesson (status) | `new` / `clustered` / `archived`; `clustered` once it belongs to an Insight, `archived` when its Insight is `actioned` | [[rule-lessons-schema]] |
      | Insight (status) | `open` / `actioned` / `archived`; `actioned` when a ratified decision addressed it; a new Lesson of the same root cause reopens it unless a decision of its own session closed its cause (case 284.4); `archived` when the cascade finds an `open` Insight with no live child | [[rule-insights-schema]] |
  - old: '| Working files | `log.md` and page `History`, the feed of page changes by hook; `raw/`: `event_log.md` of the day and one folder per session, named by its `hi` time (case 73.1), with its ledger, yaml, Spec, Frontier and handoff, moved whole into the archive once applied (cases 100.1, 103.6); `tags.md`, ratified tags with Russian aliases | [[rule-raw-archive]] |'
    new: |-
      | Working files | `log.md`, the feed of page changes written by `generate` and `cleanup`; `tags.md`, the registry of tags ratified in a Case; `raw/` and `archive/`, the working folders of a session | [[rule-vault-layout]] |
      | `raw/` | One folder per session, `raw/<date>/<HHMM>/`, with its `ledger.md` and `materialize.yaml`; `guppi archive` moves it whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/` once every entry is applied; `event_log.md` stays in `raw/<date>/` | [[rule-raw-archive]] |
  - old: '| Executable plan, Work Mode | The Spec as tasks with code, paths, checkboxes; subagents transcribe, a fork comes back as a Case | [[rule-work-mode]] |'
    new: '| Work Mode | `/work` runs the approved Spec on a branch other than `main`: a baseline of `make test` and `make lint` first, the tasks in the order of the Spec, each box ticked, then the Work readings; it ends with `/retro` | [[rule-work-mode]] |'
  change: 'each row points at the page that defines its term: Plan Mode, the fields and statuses by category, the Decision page by its schema after case 513, lint and the renderer for Scripts, the working files and raw/, Work Mode without subagents; Executable plan leaves until it is decided (case 515)'
```

```tasks
- [x] update `entity-glossary`
- [x] `uv run guppi glossary`
- [x] read `estimate-glossary-terms-defined` — by hand in a later session after the librarian's run: the table of `vault/wiki/glossary.md` and `make lint`
```

## Case 516 — The check of the lift on a schema change names its tests

> **context:**
> Each Estimate carries a `method`: the command that checks its promise. The `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change` runs `uv run pytest tests/test_materialize.py -k schema_change`. The promise is about a session that changes a `rule-<category>-schema`: a `create` of that category keeps every key and gets no `unknown`. `-k` picks tests by a word in their names, and no test name holds `schema_change`. The command runs zero tests, and pytest does not fail on that. At the last reading (1134 ledger, L28: "-k schema_change selects 0 tests; the two tests of case 308.2 run by name ... 2 passed") the reader ran the two real tests by other words, but the `method` was never fixed. The `method` also says the test holds a "create rule-rules-schema", but the test `update`s it. The Criterion says the lift holds "wherever the schema entry stands in the Spec, before or after". The test puts the schema decision first in the ledger and its Case after the creates in the Spec. The other order passed only because the code was read: `schema_changed()` in `guppi/materialize.py` reads the whole ledger before the lift.
>
> In one round the person chose three things:
> - The `method` names each test by its full node id, so pytest stops with "not found" when a test is renamed or removed and never quietly runs nothing.
> - A third test covers the other order: the schema decision after the creates in the ledger, and its Case before them in the Spec.
> - Only this `method` changes. The other `method`s that pick tests with `-k` are not checked here.
>
> What the frame shows:
> - The Case sets only the `method` field. Under `rule-case-protocol` an `update` that names a part alone keeps the Criterion and the `passed` status, so there is no `set.status` and no reading line.
> - `vault/wiki/estimates/schema.yaml` asks for a `method` in one of four forms. The new text holds the word `pytest` and a `tests/` path. Lint's `TEST_PATH` in `guppi/lint.py` takes `tests/test_materialize.py` from before the `::`, and that file exists, so the check of `estimate-lint-checks-the-method` stays green.
> - `rule-materialize` and its paragraph on case 308.2 describe behaviour that does not change. No other Estimate of the rule has a Criterion that speaks of this `method` or these tests.
> - No hook changes, and no code reads the `method` to run it.
> - The Case creates no page, so no vault query was run.
>
> Not done: the other `-k` methods of the vault are not checked. Lint gets no check that a `-k` picks at least one test.

> **problem:**
> The command that checks this promise runs no test and still passes. So a reading that follows the `method` proves nothing, and one part of the Criterion, the other order, has no test at all.

> **given:**
> `estimate-materialize-lifts-unfiltered-on-a-schema-change` — the promise whose `method` changes.
> **＋** `tests/test_materialize.py` — the two tests the `method` names, and the new test of the other order.
> **＋** `rule-materialize` — the rule whose lift the tests check, left as it is.
> **＋** `vault/wiki/estimates/schema.yaml` — the forms a `method` may take.

> **when:**
> Someone runs the `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change`.

> **then:**
> pytest runs each test of `tests/test_materialize.py` that the `method` names by its node id, and runs no other test.
> **＋** A test runs a unit whose schema decision line stands after the `create` lines in the ledger, and whose schema Case stands before the creates in the Spec. That `create` is lifted whole: the key is in `fields`, and no key is `unknown`.
> **＋** When a test the `method` names is renamed or removed, pytest stops with a "not found" error and does not report a run of no tests.
> **－** The Criterion and the `passed` status of `estimate-materialize-lifts-unfiltered-on-a-schema-change` do not change.

```then
update:
- slug: estimate-materialize-lifts-unfiltered-on-a-schema-change
  set:
    method: uv run pytest tests/test_materialize.py::test_a_create_of_a_category_whose_schema_rule_the_unit_changes_is_lifted_whole tests/test_materialize.py::test_a_schema_line_after_the_create_still_lifts_it_whole tests/test_materialize.py::test_without_a_schema_line_the_lift_filters_as_before — a unit with update rule-rules-schema and create rule-x carrying a key the disk schema lacks, the key in fields and no unknown, with the schema line before and after the create; the same create without the schema entry, unknown as before
  change: the method names its tests by node id, -k schema_change selected none, and a test of the other order joins (case 516)
```

```tasks
- [x] update `estimate-materialize-lifts-unfiltered-on-a-schema-change`
- [x] `tests/test_materialize.py`: `test_a_schema_line_after_the_create_still_lifts_it_whole` — the schema decision line appended after the `create` lines of the ledger, the schema Case placed before the creates in the Spec; the `create` of `rule-x` lifted whole, the other category filtered as before
- [x] `uv run pytest tests/test_materialize.py::test_a_create_of_a_category_whose_schema_rule_the_unit_changes_is_lifted_whole tests/test_materialize.py::test_a_schema_line_after_the_create_still_lifts_it_whole tests/test_materialize.py::test_without_a_schema_line_the_lift_filters_as_before` — 3 passed
- [x] `make test`
```

## Deferred

## Case 517 — The librarian's reads beyond its list are put off

> **context:**
> The reading of `estimate-documentation-completes` failed: the librarian's run of commit ff62585 read beyond its list — the tail of `log.md`, the head of the old `brief.md`, a git diff of `sprint.md` and `backlog.md`, a grep of `sprint.md` and a count of `[x]` in the 0137 Spec. The brief of that run carried it to session 1432 as a Case item. In session 1432 the person put it off before any Case was built on it.

> **problem:**
> Whether the librarian's list of reads is too narrow for what its run needs, or the run strays from it, and what changes: the list in `rule-documentation` or the run.

```then
defer:
  - slug: rule-documentation
    type: rule
    purpose: Decide why the librarian's run reads beyond its list — the tail of log.md, the old brief, a git diff of sprint.md and backlog.md, a count of the Spec's ticks — and whether the list or the run changes; the reading of estimate-documentation-completes failed on the run of ff62585; put off in session 1432
```

## Case 518 — The question after a defer is put off

> **context:**
> The reading of `estimate-case-protocol-defers-in-one-reply` failed in session 1134: after the defer of Case 509, with no Cases line open, the question after the Frontier asked whether to take the W readings, not whether to run `/pre-spec`. The brief carried it to session 1432 as a Case item. In session 1432 the person put it off before any Case was built on it.

> **problem:**
> Whether the rule on the question after a defer needs a change or a guard, or the failure was a slip of the agent that the rule already covers.

```then
defer:
  - slug: rule-case-protocol
    type: rule
    purpose: Decide whether the question after a defer, when no Cases line is open, needs a guard so that it asks whether to run /pre-spec; the reading of estimate-case-protocol-defers-in-one-reply failed in session 1134, where it asked about the W readings; put off in session 1432
```

## Case 519 — The Estimate schema's word on the frame of a Case is put off

> **context:**
> Case 513 of session 1432 moved the frame of a Case, its `given`, off the Decision page into the Case file. The Render of `rule-estimates-schema` still says, in the description of `## Criterion` in `vault/wiki/estimates/schema.yaml`: "no `Given:`: the frame of the Case stays on its Decision page (case 378.2)". /pre-spec did not find it; Work Mode did, while it read the schema for a reading. Retro ratifies no update.

> **problem:**
> The sentence says the frame of a Case stays on its Decision page, which is false for every Case after case 513.

```then
defer:
  - slug: rule-estimates-schema
    type: rule
    purpose: Correct the description of ## Criterion in the Render of rule-estimates-schema, which says the frame of a Case stays on its Decision page; after case 513 it stays in the Case file; found at the Retro of session 1432
```
