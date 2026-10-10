# Handoff — 2026-10-09, Slice 5: the repairs after Case 743

## Notes from memory

- The person asked for the four Frontier items of Case 743's defect (the type, the parents, the two failed Estimates) as one Case, not a batch of four; one `case-guppi` built Case 746 for them, against the batch form of case 684.1, at the person's word.
- Case 746 fixes the parents on the live pages and does not build Case 743 again: ledger lines 15 and 19 of session 2352 stand with their stale `{ref:rule-session}`; Case 749 is the check that stops such a line before the Spec from now on.
- Case 747 drops from the Criterion of `estimate-case-check-sends-back-a-faulty-round` the clause that `case-guppi` answers again; the person chose a staged run of the hook in place of a live send-back.
- `/pre-spec` sent Cases 746, 748 and 749 back on six findings of `ask-guppi`, all confirmed closed; the person ratified them again with their lines unchanged. `ask-guppi` did not check that `generate` writes a `set` of `parent` and `children` as given on an `update`, nor the Spec of case 39 the context of Case 746 cites for that form.
- The person put off C1 and C2 (`rule-sprint-close`, the close of `migration`) as items of the sprint, and `rule-morph` by the short Case 750.

## Direct instructions to the librarian

- Check first that `generate` applies the `set: parent` of 746.1 on `rule-skill-sprint-open` and `rule-skill-sprint-close`, and the `set: children` on `rule-session`, `rule-session-start` and `rule-plan-mode`, as the Spec writes them; `rule-session` must end with the five phases alone.
- Case 749 sets `insight-ledger-ratified-line-never-withdrawn` `actioned`, `addressed_by` `decision-case-749`; its clustered lesson `lesson-ledger-rebuilt-create-keeps-the-stale-ref` is then archived by the cascade.
- The lesson of this session, `lesson-case-build-task-copies-an-existing-judgment`, may cluster with an Insight on `rule-one-judgment-one-implementation` or on what `case-guppi` checks before a task.
- Case 749 updates `rule-case-protocol`, so `vault/wiki/case-schema.md` changes at the render.

## What actually got done

- Ratified: Case 746 (746.1, 746.2, 746.3), Case 747, Case 748 (748.1, 748.2), Case 749, and the short-form defer Case 750.
- Code: `guppi/materialize.py` (`SINGULAR` moved here, `fill_type`, `create_lacks`, `create_fields`); `guppi/generate.py` and `guppi/prespec.py` import `SINGULAR` from it; `guppi/prespec.py` (`check_required` in `judge`); `guppi/casecheck.py` (`changed_create_findings`, `create_line`). Tests: `tests/test_materialize.py` (`type_from_the_category`), `tests/test_prespec.py` (`required_field`, and five fixtures given the fields the new check requires), `tests/test_casecheck.py` (`changed_create_line`).
- `make test`: 1486 passed, 6 skipped. `make style`: clean.
- Readings, ledger lines 16–22, each `passed`: `estimate-session-phases-in-order`, `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-materialize-fills-the-type-from-the-category`, `estimate-prespec-hook-reports-a-create-without-a-required-field`, `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`. Lesson, line 23: `lesson-case-build-task-copies-an-existing-judgment`.
- The `W` line of the four unticked code boxes of Case 733 closed as work: Case 738 keeps them unticked, and the code landed in its session.

## Debt

- No box of the Spec is debt; no patch.
- 22 boxes wait for the librarian: the page lines, the render line and the read lines.
- `estimate-hi-takes-a-conserved-spec` — the `/hi` of the session after the close of a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` — the Work Mode of the session that closes `migration`.

## Observations

- `make lint` was red before the work, exit 2, 14 finding lines, `backlog: vault/wiki/backlog.md differs from its sources` among them (the defer of Case 750 counts before `guppi backlog` runs).
- The new check of 748.2 is a finding in `/pre-spec`, in the check of a case file and in the check after a write, all through `judge`; five test fixtures of `tests/test_prespec.py` held `create` items short of `kind` or `purpose` and were given them.
- The staged run of the round check: the copy of a `case-guppi` transcript must be read by a script that sets its stdout to UTF-8; under `python -I` the environment variable for the encoding is ignored on this machine.

## For the next session

- `rule-sprint-close` and the close of `migration` stay the items of Slice 5; the close takes a session of its own by `/sprint-close`.
- `lesson-case-build-task-copies-an-existing-judgment`: nothing before `/pre-spec` checks that a task of a Case adds no second copy of a judgment the code already holds.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
