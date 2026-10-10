# Handoff — 2026-10-10, Slice 5 — the close of migration

## Notes from memory

- The person took the close at once and agreed to every recommended answer of the rounds of Case 755, with no change of their own.
- Case 755 was built twice: the pre-spec run of `ask-guppi` found four facts or wordings to fix (what a `failed` Estimate keeps, the six Estimates of the sprint page, an Estimate the Case did not name, the other units the close moves), and the person added the preview task. `ask-guppi` confirmed each of its findings closed.
- Caveat on the preview: the readings of Work Mode reach the pages only at `guppi generate`, so the preview of the close in Work Mode listed four Estimates as not settled by design — the three of the sprint page and `estimate-sprint-close-takes-the-readings-in-groups`. The real close line must find them settled once `generate` has applied this session's readings.

## Direct instructions to the librarian

- Run the close line of the Spec after `guppi generate`, as `.claude/agents/librarian-guppi.md` sets it. Before it, check that `generate` set the four readings of this session on their pages: `estimate-sprint-migration-leftovers-gone` and `estimate-sprint-migration-merges` `passed`, `estimate-sprint-migration-lint-clean` `failed`, `estimate-sprint-close-takes-the-readings-in-groups` `passed`. If one still stands `pending`, the close refuses.
- The preview in Work Mode printed 1497 lines and nothing on stderr: 1423 `move` (1331 decisions, 49 lessons, 36 insights, 6 estimates, 1 entity), 30 `keep` (26 knowledge lessons, 4 decisions named in a `deferred_by`), 30 `archive` (the raw session 1508 and 29 event logs), 9 `unread`, 4 `not settled` refusals. Compare the close's own output with it.
- `estimate-sprint-migration-lint-clean` reads `failed`: it goes to the archive with the sprint page, and the record of the close keeps its status. It does not block the close.

## What actually got done

- Case ratified: 755 (the closing Case of `migration`), ratified twice, the second time after `/pre-spec`.
- Code and tests: none changed. `docs/migration/migration-plan.md` deleted; `docs/` is gone.
- `make test`: 1490 passed, 6 skipped. `make style`: clean.
- Readings: L2 `estimate-sprint-migration-leftovers-gone` `passed`, L3 `estimate-sprint-migration-merges` `passed`, L4 `estimate-sprint-migration-lint-clean` `failed`, L5 `estimate-sprint-close-takes-the-readings-in-groups` `passed`.
- Lessons: L6 `lesson-prespec-preview-expected-before-generate-applies-the-readings`.

## Debt

- No box is debt.
- 6 boxes wait for the librarian: the `update` of `entity-sprint-migration`, the four `read` lines of the readings above, and the close line.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of this session; carried.
- `estimate-brief-written` — at the `/hi` after the librarian's run of this session; carried.
- `estimate-sprint-close-next-session-opens-the-sprint` — at the librarian's run of the session that opens the next sprint; carried.
- `estimate-hi-takes-a-conserved-spec` — at the `/hi` of the session that opens the next sprint; carried.

## Observations

- `make lint` was red before the work, with the same 10 lines as in Work Mode (`work.md`, Baseline): the stale defer of `rule-morph` and nine `unread: pending` lines.
- `estimate-sprint-close-settles-unread-estimates` (`passed`) says a `failed` Estimate outside the sprint page "is carried into the next sprint", but `guppi/sprint_close.py` settles it only when `--carry` or `--archive-unread` names it (`ask-guppi`, pre-spec).
- The `－` line of `estimate-sprint-migration-merges` puts the merge on a line of the `## Backlog` of `entity-sprint-migration`, and that page holds no such line; the page goes to the archive at the close.

## For the next session

- Open the next sprint by `/sprint-open`. Its first work after the opening Case: the merge of `migration` into `main`, the last task line of the Spec of this session, left unticked by design.
- `rule-morph` stays deferred, the stale-defer lint line with it, into the next sprint.
- The sentence of `estimate-sprint-close-settles-unread-estimates` on a `failed` Estimate outside the sprint page disagrees with the code; one of them needs a decision.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session that opens the next sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
