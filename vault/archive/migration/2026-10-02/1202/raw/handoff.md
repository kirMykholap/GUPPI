# Handoff — 2026-10-02, make lint, the Estimate update, the language finding, one turn judgment, the Spec box

## Notes from memory

- The person took the Spec box (`rule-spec-box`) as a build, not as a lint fix. They spent the most time on how documentation avoids merge conflicts between branches. They chose: only the shared branch writes `vault/wiki/`; a conserved Spec is checked again when taken up; one session at a time. They first wrote "4) b / 5) a" for the round on Q5 and Q6, then said the numbers were mixed up and confirmed Q4 (a), Q5 (b), Q6 (a), Q7 (a).
- Q5 (b), taking a conserved Spec after other Cases of the session, was ratified in the rounds, but Q11 moved it to the second part. The first part refuses a box session that ratified a Case of its own. The second part stands as the Backlog line of `entity-sprint-migration` that 593.2 writes.
- The person refused a hand edit of the ledger when the lines of a first ratification were left with no item in the plan. Supersede by new Cases was chosen (592 for 590.1, 593 for 591.2, 591.5 and 591.6). They asked to think later about a better mechanism (defer 594).
- On Case 588 the person asked what the History line of an Estimate was for when the script writes History. The answer was the `change` text a Case gives to close a put-off question. They then agreed to change the scripts.

## Direct instructions to the librarian

- Lines of 591.2, 591.5 and 591.6 stand twice in the ledger: the first ratification with the slugs `…saved-plan` and `…stale-plan`, and the re-ratification with the `…conserved-spec` slugs. Case 593 supersedes all of them with `{supersedes:case 591.2}`, `{supersedes:case 591.5}` and `{supersedes:case 591.6}`. The line of 590.1 on `rule-case-check` is superseded the same way by 592. Check that `materialize` marks every line of 590.1, 591.2, 591.5 and 591.6 superseded, and that no `estimate-hi-takes-a-saved-plan`, `estimate-spec-box-runs-a-saved-plan` or `estimate-spec-box-refuses-a-stale-plan` page is created.
- The `## How it works` sections of `rule-case-check`, `rule-ledger-write` and `rule-context-size` were removed by hand in Work Mode, as one-off tasks of 589.2, 590.2 and 592. The `update` items of those pages carry only `change`, so `generate` writes a History line and nothing else. With 588.2 built, `change` alone no longer lifts a Criterion.
- 593.2 sets `parent: [[rule-end-of-work]]` on `rule-spec-box`, and 591.4 sets the `children` of `rule-end-of-work` with `rule-spec-box` last. Both must land for the orphan finding to go.
- The `given` of 589.2, 590.2 and 590.3 still says "as 590.1 sets it". 590.1 has left the plan, and 592 holds its content. The person agreed to leave this, since `given` stays in the Case and the Spec.
- 593.2 writes the Render of `.claude/skills/box/SKILL.md`, a new skill. 591.7, 591.8, 591.9, 591.10, 591.12 and 593.1 change the Renders of `/work`, `/retro`, `/handoff`, `where-to-stop.md` and `/hi`, and 591.1 the Render of `/carry`.

## What actually got done

- Ratified: 587, 588.1, 588.2, 588.3, 589.1, 589.2, 590.2, 590.3, 591.1, 591.3, 591.4, 591.7, 591.8, 591.9, 591.10, 591.11, 591.12, 592, 593.1, 593.2, 593.3. Deferred: 594 (`rule-ledger-line-withdrawn-on-re-ratification`). Superseded in the session: 590.1, 591.2, 591.5, 591.6.
- Code: `Makefile` (the `lint` recipe runs every step and exits non-zero when any is red); `guppi/materialize.py` (`names_a_part`: `change` alone names the History); `guppi/config.py` (`outside` accepts a Latin letter in a code span, by `CODE_SPAN` of `guppi/lint.py`); `guppi/ratified.py` and `guppi/prespec.py` (docstrings); `guppi/ledger.py` (`user_kind`, `opens_turn`, `own_refusals` by them, the docstring with the facts of `## How it works`); `guppi/casecheck.py` (`turn_of_reply` and `given_back` by `guppi/ledger.py`, the docstring with the facts of `## How it works`); `guppi/context.py` (`is_prompt` removed, D from the start of the turn); `guppi/box.py` (new: `conserved_spec_named`, `check`, `run`); `guppi/spec.py` (the box line in place of the fork); `guppi/cli.py` (the command `box`).
- Tests: `tests/test_materialize.py`, `tests/test_prespec.py`, `tests/test_config.py`, `tests/test_casecheck.py`, `tests/test_context.py`, `tests/test_ledger.py` (`test_kind_of_a_user_record_sets_the_turn_and_the_stretch`), `tests/test_spec.py` (`-k box`), `tests/test_box.py` (new). `make test` 1074 passed, 6 skipped; `make style` clean.
- By hand: `make lint` after the change in Git Bash and in PowerShell. Every step printed, the page findings of `guppi lint` included after the red backlog step, and the exit code was 2 in both shells.
- Pages by hand: `## How it works` removed from `vault/wiki/rules/rule-case-check.md`, `rule-ledger-write.md` and `rule-context-size.md`.
- Readings: ledger lines 55 and 56 (`estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-prespec-gathers-the-answers-after-findings`), both `passed`. Lessons: none.

## Debt

- None.
- Boxes that wait for the librarian: 47. Of these, 46 are page and render lines, and one is the by-hand check of 591.11, `make lint` after the librarian's run with no `fence` line on `decision-case-13`, which the librarian's `make lint` reads.
- `read` lines whose slug this session creates or updates: `estimate-lint-runs-every-step`, `estimate-estimates-schema-checked`, `estimate-materialize-changes-a-named-part-alone`, `estimate-materialize-lifts-when-and-then`, `estimate-language-spec-prose-in-english`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-context-size-shown-after-each-reply`, `estimate-case-check-refuses-text-before-a-round`, `estimate-carry-over-writes`, `estimate-spec-capture-offers-the-fork`, `estimate-end-of-work-order`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-retro-loads`, `estimate-handoff-dispatches`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-takes-the-work-readings`, `estimate-ledger-write-names-the-kind-of-a-user-record`, `estimate-hi-takes-a-conserved-spec`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-box-refuses-a-stale-spec`.

## Observations

- Red before the work: the Baseline `make lint` exited 2 at its backlog step, the old recipe stopping there. The page step run alone gave the `rule-spec-box` schema and orphan findings, the open fence of `decision-case-13`, 7 deferred lines and 28 unread lines.
- The tasks of 589.2, 590.2 and 590.3 were run after the code of 592's tasks, against the order of the Spec, since all three read the function of `guppi/ledger.py` that 592 adds.
- `guppi/config.py` now imports `CODE_SPAN` from `guppi/lint.py`. The import makes no cycle: `guppi/lint.py` imports neither `guppi/config.py` nor `guppi/ratified.py`.
- `make lint` stays red at the close of the sprint after this run by five `deferred` lines, by design. `estimate-sprint-migration-lint-clean` cannot pass while they stand.
- Not read, their moment not yet come: `estimate-retro-onward-sends-the-agent-to-the-handoff` and `estimate-ledger-write-lifts` (the end of this Retro, readable from this session's transcript and ledger); `estimate-retro-runs-on-to-the-handoff` and `estimate-handoff-holds-each-fact-once` (the close of this run); `estimate-case-protocol-ledger-line-form` (its Case half came — 593.2 carries one `{supersedes}` per Case of the `deferred_by` of `rule-spec-box`, side by side — but no lesson and its Case stood together); `estimate-case-check-requires-each-question-of-the-rounds` and `estimate-case-check-shows-only-the-checked-case` (no refusal of the hook); `estimate-case-build-writes-the-case` and `estimate-plan-mode-verified` (no `create` without a `ref`); `estimate-ask-finds`, `estimate-compact-recall-reloads`, `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-session-start-context`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-synthesis-clusters`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`.

## For the next session

- The close of the sprint (Slice 5) and `rule-orchestration` were put off at the end of Plan Mode with no Case, as a sprint item and a backlog item kept.

## Ask the person

