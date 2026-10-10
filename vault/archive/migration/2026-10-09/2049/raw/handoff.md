# Handoff — 2026-10-09, the layout of the replies of case-guppi and the search for an existing judgment

## Notes from memory

- The person added the item of Case 751 at `/hi` (rules between the replies of `case-guppi`) and took every recommended answer of its two rounds and of the one round of Case 752.
- After Case 752 the person said "Идём работать" ("let's go to work"). The agent took it as leaving C1 and C2 (`rule-sprint-close`, the close of `migration`) as items of the sprint, closed `[-] … · sprint · defer`, and went on to `/pre-spec` with no further question.
- The context of Case 751 said that `tests/test_orchestration.py` accepts the example of a showing as 751.6 changes it, judged by the check functions alone. That was wrong for the test's own helper `store_of_showing`, which Retro fixed (see Observations).

## Direct instructions to the librarian

- `rule-orchestration` takes three `replace` updates in this session (751.1, 751.2, 751.6). The second pair of 751.6 has a multi-line `new` (`|-`) that puts `---` and a blank line before `## Case 7 — Members get a reminder before a booking` inside the block tagged `showing`. Check that `generate` writes it as given, then that `uv run pytest tests/test_orchestration.py` passes on the rendered page.
- Case 752 sets `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned` with `addressed_by: decision-case-752`. The lesson `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper` of this session carries no `addressed_by`. If the synthesis joins it to that Insight, the Insight opens again: judge the root cause before joining.
- Cases 751 and 752 were ratified twice: once before and once after `/pre-spec`. The ledger holds each decision line once.

## What actually got done

- Ratified: Case 751 (751.1–751.6) and Case 752.
- Code: `guppi/casecheck.py` — `round_opening` skips a leading horizontal rule. `outside_the_list` passes over a rule before the first Case heading and reads past a rule that a Case heading follows. Both notes allow a rule. The module docstring says so.
- Tests: `tests/test_casecheck.py` has four new tests (a leading rule before a round; rules before and between the Cases of a batch; a text in the second Case after a rule; text after a last rule). `tests/test_orchestration.py` `store_of_showing` now reads the `ratification` under each Case heading by `split_cases`.
- `make test`: 1490 passed, 6 skipped. `make style`: clean.
- Readings: L14–L20, all `passed` (`estimate-orchestration-sets-off-each-reply-of-case-guppi`, `estimate-orchestration-marks-each-round-of-a-batch`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-refuses-text-outside-the-list`, `estimate-orchestration-showing-example-passes-the-check`, `estimate-case-build-finds-an-existing-judgment`).
- Lesson: L21 `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`.

## Debt

- No box of code, test or command is left unticked, and no patch was saved.
- 25 boxes wait for the librarian: page, render and read lines.
- `estimate-hi-takes-a-conserved-spec`: waits for a session that takes a conserved Spec and for the `/hi` after the close of a sprint.
- `estimate-brief-written`: waits for the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run`: waits for the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint`: waits for the librarian's run of the session after the close.
- `estimate-sprint-close-takes-the-readings-in-groups`: waits for the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`: waits for the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-lint-clean`: waits for the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-merges`: waits for the Work Mode of the session that closes the sprint.

## Observations

- `make lint` was red before the work, exit 2, with 10 finding lines: 1 `deferred` (`rules/rule-morph`) and 9 `unread: pending`. `## Expected red` of `work.md` stays empty: no check changed reads a page this Spec updates and goes red on it.
- The test `test_showing_example_passes_the_check` would have failed after the librarian's render of 751.6. `store_of_showing` ran `fence_ledger_lines` over the whole example, and that stops at the first `---`, so with the leading rule it read no line (`assert 0 >= 2`). Retro fixed the helper as work of 751.6. The Spec held no task for it. The fix was read on a copy of the page with the replace pairs applied: 6 passed.
- `guppi prespec --check` printed 37 `note:` lines and no finding. The notes covered Criterion lines not carried and then lines that share words across sub-cases, both explained in the context of 751.

## For the next session

- `rule-sprint-close` and the close of `migration` stay the items of Slice 5. The close takes a session of its own by `/sprint-close`.
- `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`: when a Case changes a live text that a test reads, nothing has `case-guppi` read the test's own helper code over that text, only the check functions the test runs (case 736.1 covers the tests that read a live file, not their helpers).

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
