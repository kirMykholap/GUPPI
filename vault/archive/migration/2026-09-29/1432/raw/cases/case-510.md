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

> **recommend:**
> Delete `vault/parked/` whole. Delete every file under `docs/` but `docs/migration/migration-plan.md`. Replace the Criterion whole so that it allows the parked pages to be deleted and leaves the plan to the closing Case. Move the item into Slice 5 and remove Slice 4. The rejected options were archiving everything, which the cleanup script would move back into the live vault because the parked folders are named `rules/`, `lessons/`, `entities/` and `decisions/`; converting page by page, which would take several sessions for a harness that no longer runs; and keeping the item in Slice 4, which puts a finished item on every Frontier until `generate` moves it to the Backlog.

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

> **tasks:**
> - [ ] update `estimate-sprint-migration-leftovers-gone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the parked pages deleted, not archived; the migration plan left to the closing Case (case 510)`
> - [ ] update `entity-sprint-migration`
>   - old:
>     ```
>     ### Slice 4 — conversion of the parked pages by group
>
>     - [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision
>
>     ### Slice 5 — closing
>     ```
>   - new:
>     ```
>     ### Slice 5 — closing
>
>     - [[estimate-sprint-migration-leftovers-gone]] — `vault/parked/` and the documents of 2026-08 under `docs/` deleted (case 510); the old archive root, the empty raw date folders, `git pull` and `gh`, and the reading, at the close
>     ```
>   - change: `Slice 4 done: the parked pages and the documents of 2026-08 deleted, the item moved to Slice 5 for its reading at the close; Slice 4 removed (case 510)`
> - [ ] `git rm -r vault/parked` — one-off: the parked pages, the register files, the `_schema.yaml` and `.gitkeep` files, and both date folders
> - [ ] `git rm -r docs/superpowers docs/migration/README.md docs/migration/rule-*.md` and every file at the root of `docs/` — one-off: `docs/` holds only `docs/migration/migration-plan.md` after it
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-migration-leftovers-gone` — by hand on the tree at the close of the sprint

> **ratification:**
> ```
> - decision[case 510][update][estimate-sprint-migration-leftovers-gone]{ref:estimate-sprint-migration-leftovers-gone}
> - decision[case 510][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
