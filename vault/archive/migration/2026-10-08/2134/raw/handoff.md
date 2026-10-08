# Handoff — 2026-10-08, the MOC method patch, cascade notes, the three open Insights

## Notes from memory

- The person took C3 and C4 of the brief, then took up the three open Insights from the backlog as a batch (C5–C7). Both items of Slice 5, `rule-sprint-close` and the close of `migration`, were closed `· sprint · defer`: once a Case not about the close was ratified, this session could not be the session of its own that closes the sprint.
- Case 739: the person answered the first question outside its options. They chose a check by script that reuses the logic of the cascade, not a new step of `case-guppi`. On the question of a Case that both sets the status and updates the page, the person chose (b) against the recommendation: one Case, and two sub-cases of one Case, give the note too.
- Case 738: the person agreed that the four unticked code boxes of Case 733 in the 0213 Spec stay as that session left them. The code landed in this session's boxes.
- At `/hi` the person said the Frontier looked fine for A1 (`estimate-hi-writes-frontier`). Its method names the `/hi` after the close of a sprint, so no reading was written, and the person agreed to take it then.
- At `/pre-spec`, `ask-guppi` made 3 findings on Cases 738 and 739: the module docstring of `guppi/prespec.py` that both Cases change, and `estimate-case-example-passes-the-check`, which neither named. All 3 were fixed and confirmed closed, and 738 and 739 were ratified a second time. The note `case 741: given holds 8 ＋ lines` was answered: 741 sets one stop and is atomic.

## Direct instructions to the librarian

- Cases 740, 741 and 742 set three Insights `actioned`. Check that the cascade archives their clustered lessons: 3 under `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line`, 2 under `insight-permissions-classifier-weighs-the-rules-not-the-persons-word`, 1 under `insight-ledger-ratified-line-never-withdrawn`. Also check that `backlog.md` no longer lists the three Insights.
- `addressed_by`: 740 writes the quoted wikilink `[[decision-case-725.2]]`, 742 writes `[[decision-case-725.1]]`, and 741 writes the bare slug `decision-case-741`, a decision of its own session.
- Case 741 sets `estimate-where-to-stop-stops-only-on-its-conditions` `pending` and replaces its Criterion. Its reading, L13 `passed`, comes after that `update`, so the page should end `passed` with the new Criterion.
- Cases 739.1 and 739.2 create two Estimates, read `passed` by L11 and L12. The new Estimate of `rule-case-check` may move that page `built` → `draft` and back by the cascade. Check where it ends.
- The render writes condition 8 into `vault/wiki/where-to-stop.md`, which `/work` and `/box` load. `rule-case-check` gains one sentence in its Purpose.

## What actually got done

- Cases ratified: 738, 739 (739.1, 739.2), 740, 741, 742. None is superseded.
- Code: `guppi/lint.py` and `guppi/prespec.py` (the patch of Case 733: `names_a_moc_form`, `check_form` by `plan_kind`); `guppi/generate.py` (`archived_by_cascade`, which `cascade` now calls); `guppi/prespec.py` (`cascade_notes`, added to the notes of `plan_findings`); `guppi/casecheck.py` (`check_answer` adds the cascade notes and stores a note under the Case of the file it names).
- Tests: `tests/test_prespec.py` (the four tests of the patch, eight `cascade` tests), `tests/test_casecheck.py` (eight `cascade` tests).
- `make test`: 1448 passed, 6 skipped. `make style`: clean.
- Readings: L10 `estimate-prespec-catches-a-method-without-a-form` `passed`, L11 `estimate-prespec-notes-a-page-the-cascade-archives` `passed`, L12 `estimate-case-check-notes-a-page-the-cascade-archives` `passed`, L13 `estimate-where-to-stop-stops-only-on-its-conditions` `passed`. No lesson.

## Debt

- No box is debt, and no test was reverted.
- 14 boxes wait for the librarian.
- `estimate-hi-takes-a-conserved-spec` — waits for a session that takes a conserved Spec and for the `/hi` of the session after the close of a sprint.
- `estimate-brief-written` — waits for the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — waits for the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — waits for the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — waits for the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — waits for the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — waits for the Work Mode of the session that closes `migration`.
- `estimate-sprint-migration-lint-clean` — waits for the Work Mode of the session that closes `migration`.
- `estimate-sprint-migration-merges` — waits for the Work Mode of the session that closes `migration`.

## Observations

- `make lint` was red before the work, exit 2, with 13 finding lines: `backlog: vault/wiki/backlog.md differs from its sources`, `rules/rule-morph: deferred`, 10 `unread: pending` and 1 `unread: failed` (`estimate-prespec-catches-a-method-without-a-form`). The same `make lint` run at `/hi`, before any Case of this session, did not print the `backlog` line.
- The patch of Case 733 applied cleanly to today's files. `make style` reformatted one file of it.
- `cascade_notes` judges by the live lesson and Insight pages and reads only the Decision pages that the plan updates or that a mark names. A page the cascade would archive anyway, without the plan, gives no note.
- A cascade note ends with the ask `drop the update, or say in its context why it stands`, for `/pre-spec` and for the check of the file of a Case alike.
- Work Mode changed `guppi/generate.py` once through a Python script in the shell. The `shellwrite` hook turned its CRLF line endings into LF. The diff stayed limited to the changed lines, and every later change went through Edit.

## For the next session

- The close of `migration` and `rule-sprint-close`: a session of its own, put off again.
- `rules/rule-morph: deferred` stays a lint finding until a Case decides `rule-morph`.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
