<!-- approved 16:17:18 · session 020ed9d9 -->

# Spec — session 1555, 2026-10-10

## Case 755 — The sprint migration closes

> **context:**
> A sprint closes in three steps. Work Mode of the closing session takes each reading whose moment has come. Retro takes the reading whose moment is the end of Work Mode. Then the librarian runs the close line `uv run guppi sprint-close --sprint migration --apply`, after `guppi generate`. The close moves to `vault/archive/` the sprint page, each Estimate it lists, the Decision pages of `migration`, its `actioned` Insights and its `error` lessons that joined no Insight. It then moves the finished sessions of `vault/raw/` and the old event logs. It sets `status: archived` on each page it moves, with a History line that keeps the old status, and the record lines of the close keep the status of each Estimate that stood `pending` or `failed` (`guppi/sprint_close.py`). Before it moves anything, it refuses while an Estimate that stands `pending` or `failed` is not settled: carried by `--carry`, archived by `--archive-unread`, or an Estimate of the sprint page that reads `failed`. The command also refuses a `--carry` on an Estimate of the sprint page, and a slug that no longer stands `pending` or `failed` (`guppi/sprint_close.py`). Nine Estimates stand `pending` and none stands `failed`. They fall into four groups by the moment their `method` names. `entity-sprint-migration` lists six Estimates. Three stand `passed`: `estimate-sprint-migration-rule-class-files-dissolved`, `estimate-sprint-migration-index-dissolved` and `estimate-sprint-migration-file-route-gone`. Group 1 holds the other three, which stand `pending`: `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone` and `estimate-sprint-migration-merges`. The close moves all six. Work Mode reads them before the librarian's run. Group 2 is `estimate-sprint-close-takes-the-readings-in-groups`, read after Work Mode, so Retro reads it and the close line does not name it. Group 3 holds `estimate-sprint-close-runs-in-the-librarian-run` and `estimate-brief-written`, read after the librarian's run of this session. Group 4 holds `estimate-sprint-close-next-session-opens-the-sprint`, `estimate-hi-writes-frontier` and `estimate-hi-takes-a-conserved-spec`, read in the session that opens the next sprint. The person chose to carry groups 3 and 4 by `--carry`. The sprint ran on the branch `migration`, so the Case holds the merge line, which Work Mode leaves to the session that opens the next sprint. In the frame, `case-guppi` found that `estimate-sprint-migration-lint-clean` will most likely read `failed`. The last brief shows the lint finding `rules/rule-morph: deferred: 3 times since case 239`. `rule-morph` stays a placeholder after the close. The unread line of group 2 also stands when Work Mode runs `make lint`. The Criterion of the Estimate excuses neither line. The person chose to read it as it stands. A `failed` reading of an Estimate of the sprint page does not block the close: the Estimate goes to the archive with the sprint page, and the record of the close keeps its status. The Criterion of `estimate-sprint-migration-leftovers-gone` says that the Case that closes the sprint deletes `docs/migration/migration-plan.md`, and this Case does so. A Grep for `migration-plan` over the repository, with `vault/raw/` and `vault/archive/` left out, printed three files: `vault/wiki/sprint.md`, `vault/wiki/entities/entity-sprint-migration.md` and `vault/wiki/estimates/estimate-sprint-migration-leftovers-gone.md`. The first two name the file as the plan the sprint followed, which stays true as a record. The third is the sentence this Case makes true. The exception of `estimate-sprint-migration-merges` says that the merge is a line of the `## Backlog` of `entity-sprint-migration`, and that page holds no such line. The sentence stands. Its point holds, since the merge is not part of that promise. The merge line of this Case now carries the merge, and the page goes to the archive at the close. Two Estimates already check this Case, and their Criteria stand, since they describe this session as built: `estimate-sprint-close-takes-the-readings-in-groups` checks the groups, the tasks and the readings, and `estimate-sprint-close-runs-in-the-librarian-run` checks the close line in the librarian's run. `estimate-skill-sprint-close-leads-the-closing-session` stands `passed` and speaks of the closing Case too: the groups, the tasks, the close line with the choice per unread Estimate, the merge line, and a `## Backlog` of `entity-sprint-migration` with no merge line. Its Criterion stands, and it needs no reading in this session: its `method` read the skill, `vault/wiki/orchestration.md` and `entity-sprint-migration` at the Retro of the session of case 746, and this Case changes none of those texts but the History of `entity-sprint-migration`. The moves of Decision pages, Insights, lessons, sessions and event logs are checked by `estimate-sprint-close-archives-the-decisions`, `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-sweeps-raw` and `estimate-sprint-close-moves-old-event-logs`, which stand `passed`; this Case does not change that behaviour, so their Criteria stand. A reading written in Work Mode stands in the ledger, and the Estimate page changes only when `guppi generate` applies it at the librarian's run. So the preview of the close in Work Mode still lists the three Estimates of group 1 and the Estimate of group 2 as not settled, and the person chose to expect exactly those lines and stop on any other refusal line. The decision line is an `update` of `entity-sprint-migration` with `change` alone, as the ledger needs a decision line of the closing Case.

> **problem:**
> The sprint `migration` has reached its last milestone, the close. The close needs its readings sorted and taken, a choice for each Estimate still unread after Work Mode, and the close line that the librarian runs.

> **recommend:**
> - **When is the group 2 check read**
>   - Recommended: (a) read at Retro of this session, with the close line not naming it.
>   - Answer: agreed, (a).
> - **What happens to the five checks of groups 3 and 4**
>   - Recommended: (a) carry all five by `--carry`, to be read by the session that opens the next sprint.
>   - Answer: agreed, (a).
> - **What to do about the lint-clean check that will fail**
>   - Recommended: (a) read it as it stands; a `failed` reading goes to the archive with the sprint page, its status kept.
>   - Answer: agreed, (a).
> - **Is the old migration plan deleted in this session**
>   - Recommended: (a) delete it in Work Mode, before the last commit and `make test`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec` — the `then` line on a `failed` Estimate worded as the code does it, the count of the Estimates of `entity-sprint-migration` fixed, `estimate-skill-sprint-close-leads-the-closing-session` named, and the other moves of the close named; and a `by hand` task in Work Mode that runs the preview of the close with the same `--carry` flags, a refusal in it a stop for the person's word.
>   - Taken: the four findings fixed in `context`, `given` and `then`; the preview task added, with what it expects set by the question below.
> - **What the preview in Work Mode should show**
>   - Recommended: (a) expect the lines "not settled" for exactly the three Estimates of the sprint page and `estimate-sprint-close-takes-the-readings-in-groups`, and stop Work Mode on any other refusal line.
>   - Answer: agreed, (a).

> **given:**
> `entity-sprint-migration`: the sprint page that closes, with the Estimates it lists.
> **＋** `vault/wiki/estimates/`: the Estimates that stand `pending`, sorted into groups by the moment of their `method`.
> **＋** `guppi/sprint_close.py`: the close command that the librarian runs from the close line.
> **＋** `vault/raw/2026-10-10/1555/spec.md`: the Spec of this session, which holds the close line.
> **＋** `docs/migration/migration-plan.md`: the plan of the sprint, deleted by this Case.
> **＋** `vault/raw/`: the sessions and event logs that the close moves when they are finished or old.
> **＋** `estimate-sprint-close-takes-the-readings-in-groups`: the Estimate that Retro reads, which checks the closing Case.
> **＋** `vault/archive/`: where the close moves the sprint page and its Estimates.

> **when:**
> The session that closes `entity-sprint-migration` runs its Work Mode, its Retro and the librarian's run, which runs the close line `uv run guppi sprint-close --sprint migration --apply` of `vault/raw/2026-10-10/1555/spec.md`.

> **then:**
> Work Mode deletes `docs/migration/migration-plan.md` and commits its changes on the branch `migration` before it runs `make test`.
> **＋** Work Mode reads each Estimate of `entity-sprint-migration` before the librarian's run, `make test` on the last commit of `migration`.
> **＋** After its readings, Work Mode runs the close line without `--apply`, and the preview lists as not settled only the Estimates of `entity-sprint-migration` and `estimate-sprint-close-takes-the-readings-in-groups`; any other refusal line stops Work Mode until the person gives their word.
> **＋** Retro reads `estimate-sprint-close-takes-the-readings-in-groups`.
> **＋** The close line names by `--carry` each Estimate under `vault/wiki/estimates/` whose `method` names a moment at or after the librarian's run, and each such Estimate stays live and `pending` for the next sprint.
> **＋** The librarian runs the close line after `guppi generate`, and the close moves to `vault/archive/` `entity-sprint-migration`, each Estimate it lists, the Decision pages of `migration`, its `actioned` Insights and its `error` lessons that joined no Insight; the record of the close keeps the status of an Estimate that reads `failed`.
> **＋** The close then moves the finished sessions of `vault/raw/` and its old event logs to `vault/archive/`.
> **－** Work Mode neither runs nor ticks the close line, and leaves the merge of `migration` into `main` unticked.
> **－** The close line names no Estimate that is read before the librarian's run.

```then
update:
- slug: entity-sprint-migration
  change: 'the close of the sprint, case 755: its readings taken in the closing session, the close line run by the librarian'
```

```tasks
- [x] update `entity-sprint-migration`
- [x] `docs/migration/migration-plan.md`: deleted in Work Mode, before the last commit and `make test`.
- [x] by hand: in Work Mode, commit the changes of this session on the branch `migration`, so that its last commit holds them, before `make test` runs.
- [x] read `estimate-sprint-migration-leftovers-gone`
- [x] read `estimate-sprint-migration-merges`
- [x] read `estimate-sprint-migration-lint-clean`
- [x] by hand: in Work Mode, after its readings, run the preview `uv run guppi sprint-close --sprint migration` with the same `--carry` flags as the close line and without `--apply`, and read its output: the lines "not settled" name exactly `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-merges` and `estimate-sprint-close-takes-the-readings-in-groups`, whose readings `guppi generate` applies at the librarian's run, and no other refusal line stands; the preview lists the Estimates of `entity-sprint-migration` and the other pages, sessions and logs it would move. Any other refusal line stops Work Mode for the person's word.
- [x] read `estimate-sprint-close-takes-the-readings-in-groups` — at Retro of this session
- [x] read `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of this session, carried
- [x] read `estimate-brief-written` — at the `/hi` after the librarian's run of this session, carried
- [x] read `estimate-sprint-close-next-session-opens-the-sprint` — in the session that opens the next sprint, carried
- [x] read `estimate-hi-writes-frontier` — at the `/hi` of the session that opens the next sprint, carried
- [x] read `estimate-hi-takes-a-conserved-spec` — at the `/hi` of the session that opens the next sprint, carried
- [x] `uv run guppi sprint-close --sprint migration --apply --carry estimate-sprint-close-runs-in-the-librarian-run --carry estimate-brief-written --carry estimate-sprint-close-next-session-opens-the-sprint --carry estimate-hi-writes-frontier --carry estimate-hi-takes-a-conserved-spec`
- [x] the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case
```
