# Handoff — 2026-10-01, the check of ask-guppi, the test of section conditionals, the casecheck docstring

## Notes from memory

- On case 582, before choosing, the person asked whether anyone uses the file list that `ask-guppi` adds after its five lines, and whether the vault should compete with an instruction of Claude Code it cannot change. They chose to accept the list in the check (b), against the recommendation to forbid it in the frame (a). The librarian's own file list was left out of the Case by their choice.
- At `/pre-spec` the person agreed to keep case 584 to the docstring and its test, and to put off the question whether `turn_of_reply` of `guppi/casecheck.py` and the stretch of `guppi/ledger.py` are one judgment (case 586).
- The person put the remaining items off to go to work: the close of the sprint as a sprint item with no Case, and the Spec hook's handling of a Case ratified again with sub-cases by case 585.

## Direct instructions to the librarian

- Case 583 was ratified, built again on a `/pre-spec` finding (its `context` only) and ratified again; the ledger holds its decision line once (line 4). Its `{supersedes:case 576}` supersedes `decision-case-576`; `estimate-estimates-schema-checked` has no `deferred_by` field to clear, and the defer stands on it only as a History line.
- The `update` items of cases 583 (`estimate-estimates-schema-checked`) and 584 (`rule-case-check`) carry only `change`: a History line, no status and no Criterion.
- Case 586 defers `rule-turn-start-one-judgment`, a slug with no page and no `ref`: a placeholder page.
- Case 582 replaces the Criterion of `estimate-ask-finds` and sets its `purpose` and `status: pending`.

## What actually got done

- Ratified: 582, 583, 584; deferred: 585, 586.
- Code: `guppi/casecheck.py` — the module docstring gives the measured shape of a `Stop` refusal, a `user` record marked `isMeta`. Tests: `tests/test_schemas.py` — `test_a_section_conditional_not_met_is_one_finding_where_the_schema_has_one`; `tests/test_casecheck.py` — `test_stop_a_sending_before_a_refusal_counts_in_the_turn_of_the_reply`.
- `make test`: 1053 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 1 and 2 at `/hi` (`estimate-documentation-completes`, `estimate-brief-written`, both passed); lines 8 to 16 in Work Mode and Retro, all passed.
- Lessons: none.

## Debt

- None.
- 3 boxes of `spec.md` wait for the librarian: the three `update` lines.
- Read lines whose slug this session updates: `estimate-ask-finds`, `estimate-estimates-schema-checked`.

## Observations

- Red before the work: the Baseline `make lint` exit 2, stopped at its backlog step — `backlog: vault/wiki/backlog.md differs from its sources`, since the put-off lines of this session's `frontier.md` change the counts `guppi backlog` reads. The page step run alone: the `rules/rule-spec-box` schema (missing `kind`, missing `estimates`) and orphan findings, the open fence of `decisions/decision-case-13`, 6 deferred lines, 39 unread lines.
- Not read, their moment not yet come: `estimate-retro-onward-sends-the-agent-to-the-handoff` and `estimate-ledger-write-lifts` (the end of this Retro, which followed a refusal of `guppi onward --plan` in an earlier stretch; readable from this session's transcript and ledger); `estimate-retro-runs-on-to-the-handoff`, `estimate-end-of-work-order`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once` (the close of this run); `estimate-case-protocol-shows-the-frontier-after-a-closed-line` (no Plan Mode reply closed a line with neither a ratification nor a defer); `estimate-prespec-gathers-the-answers-after-findings` (the findings went to one `case-guppi`); `estimate-case-check-refuses-text-before-a-round` (no round of `case-guppi` after `/pre-spec`); `estimate-case-build-writes-the-case`, `estimate-plan-mode-verified` (no Case proposed a `create` without a `ref`); `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-shows-only-the-checked-case` (no refusal of the hook); `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (the agent called `/work` at the fork; no `/work` typed by the person); `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` (no expected red); `estimate-carry-over-writes`, `estimate-case-protocol-ledger-line-form`, `estimate-compact-recall-reloads`, `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-session-start-context`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-synthesis-clusters`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`.

## For the next session

- `make lint` stops at its first red step. Once a session puts an item off, its backlog step is red until the librarian runs `guppi backlog`, and the page findings of the Baseline are then not printed by `make lint`. Whether `make lint` should run every step and report each, or the Baseline should run the page step on its own, needs a decision.

## Ask the person

- none
