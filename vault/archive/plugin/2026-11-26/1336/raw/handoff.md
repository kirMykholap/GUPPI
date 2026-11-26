# Handoff — 2026-11-26, the readings of the case-guppi levels and form, the number of a changed Case, the backlog of a closed sprint

## Notes from memory

- The person answered each round with a plain "ok" to the recommended option; no option was changed by the person.
- At A1 the person confirmed the README and asked for more information and a diagram in a Case of its own later; that is Case 1068, a defer on `entity-guppi-repository`.
- The person put off C1 (`rule-clean-branch`, the clean branch) at the close of Plan Mode with no Case, as a sprint item.
- The two `failed` readings at `/hi` (L1, L2) were both judged as gaps in the wording of their Criterion, not as wrong behaviour of the agents; Cases 1064 and 1065 replaced the two Criteria.
- `/pre-spec` sent Cases 1065, 1066 and 1067 back on eight findings of `ask-guppi`; it confirmed every finding closed. One finding, that Case 1064 gives no `update` to `estimate-sprint-plugin-case-guppi-level-trial-decided`, the main agent left with the reason in the `context` of 1064, and `ask-guppi` accepted that reason.

## Direct instructions to the librarian

- Cases 1064 and 1066 both update `rule-orchestration` with `replace` pairs in different sentences of the Render; apply 1064 first, then 1066, and check that each anchor hits once (`ask-guppi` did not check this by `generate`'s own matching).
- `estimate-orchestration-dispatches-case-guppi-at-a-level` and `estimate-case-build-settles-form-by-itself` carry a `failed` reading from this `/hi` (L1, L2) and then an `update` that replaces the Criterion and sets `pending` (Cases 1064, 1065); `estimate-case-build-settles-form-by-itself` then has a `passed` reading at Retro (L13). Apply in ledger order.
- After the run, `guppi backlog` should no longer list `rule-work-mode` (its line in the `## Backlog` of the archived `entity-sprint-migration`), since that page stood `built` on 2026-10-08, before the close of `migration` on 2026-10-10, and again after it; the count should fall by one, and Case 1068 adds `entity-guppi-repository`, so check both moves.
- Case 1068 is a short-form defer on an existing entity page, `entity-guppi-repository`, whose `code_ref` holds `README.md`.

## What actually got done

- Cases ratified: 1064, 1065, 1066, 1067, and the defer Case 1068.
- Code: `.guppi/guppi/pages.py` (`HISTORY_DATE`, `STATUS_SET`, `status_lines`; `is_draft_core` judges by `status_lines`, `SET_BUILT` gone), `.guppi/guppi/box.py` (imports `HISTORY_DATE`), `.guppi/guppi/backlog.py` (`closed_on`, `stood_finished`, `finished` with the day of the close). Tests: six new tests in `.guppi/tests/test_backlog.py`.
- `uv run --project .guppi guppi test`: 2000 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 `estimate-orchestration-dispatches-case-guppi-at-a-level` failed, L2 `estimate-case-build-settles-form-by-itself` failed, L3 `estimate-sprint-plugin-readme-describes-the-project` passed, L12 `estimate-backlog-renders` passed, L13 `estimate-case-build-settles-form-by-itself` passed. Lesson: L14 `lesson-frontier-line-closed-in-two-changes-through-bash`.

## Debt

- No box is debt, and no test was reverted.
- 11 boxes wait for the librarian (the page, render and read lines of Cases 1064 to 1067).
- `estimate-orchestration-dispatches-case-guppi-at-a-level` — waits for a session whose `orchestration.md` holds the Render that Case 1064 writes: each Agent call of `case-guppi` in its transcript. The new Render in the Spec holds every line of the new Criterion.
- `estimate-orchestration-leaves-the-number-to-case-guppi` — waits for a session in which a ratified Case comes back in another shape: the messages of the main agent to its `case-guppi` and the showing. The new Render in the Spec holds the two sentences of Case 1066.

## Observations

- Expected red: `guppi backlog --check`, a step of `uv run --project .guppi guppi check`, names `vault/wiki/backlog.md` until the librarian's run writes it, since `.guppi/guppi/backlog.py` now leaves out the `rule-work-mode` line of the archived `entity-sprint-migration`.
- The Baseline held no failing test and no lint finding.
- The number 1062 of session 2003 still stands as an empty `cases/case-1062.md` in that session's folder; nothing of this session touched it.

## For the next session

- Whether frontierguard should also judge a Bash command that changes `frontier.md`, or whether a guard should refuse such a command, so that the box and the closer of a line always change in one edit; L14 records the cause.

## Ask the person
