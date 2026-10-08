# Handoff — 2026-10-08, the Frontier of the brief: Ask lines, MOC methods at pre-spec, case-guppi reading by meaning

## Notes from memory

- The person took C3, C5 and C4 of the brief and put off both items of Slice 5 (`rule-sprint-close` and the close of `migration`) as `· sprint · defer`. Once a Case that was not about the close was ratified, this session could no longer be the session of its own that closes the sprint.
- The person agreed to every recommended option in each round, with no change.
- At `/hi` the agent put A1 (`estimate-hi-writes-frontier`) to the person, though its question names the `/hi` after the close of a sprint. That is the gap Case 732 closes. The person gave no answer, and the line stands open.
- At `/pre-spec`, `ask-guppi` made 4 findings: 1 on 732, 2 on 733, 1 on 734. All were fixed and confirmed closed, and Cases 732, 733 and 734 were ratified a second time. `ask-guppi` reported that three of its Greps from the repository root also covered `vault/archive/`; no finding rests on them.
- In the `context` of Case 732, one sentence has a grammar slip ("The second is the Criterion of … speaks of the same question"). `ask-guppi` noted it, and it was left as it stands.

## Direct instructions to the librarian

- `estimate-prespec-catches-a-method-without-a-form`: the `update` of Case 733 replaces its Criterion and sets `pending`, and the reading L8 sets it `failed` after that. Check that the page ends `failed`, with the new Criterion, `purpose` and `method` of the Spec.
- `insight-workflow-case-written-without-reading-the-pages-it-changes`: Case 734 sets `status: actioned` and `addressed_by: decision-case-734`. The new lesson L10 (`lesson-case-build-misses-the-example-a-changed-check-runs-over`) carries no `addressed_by`. Judge in synthesis whether it clusters under this Insight, which would set it `open` again, or stands apart: its cause is a test example that a changed check runs over, not a sentence of a changed page.
- `rule-skill-hi` and `rule-case-build` change by a `replace` each. Their Renders, `.claude/skills/hi/SKILL.md` and `.claude/agents/case-guppi.md`, follow at the render.

## What actually got done

- Cases ratified: 732, 733, 734 (L1–L6). None is superseded.
- Code and tests: none changed in the end. The code of Case 733 (`guppi/lint.py`, `guppi/prespec.py`, `tests/test_prespec.py`) was written, then reverted into a patch (see Debt).
- `make test`: 1428 passed, 6 skipped. `make style`: clean.
- Readings: L7 `estimate-hi-takes-its-readings` `passed`, L8 `estimate-prespec-catches-a-method-without-a-form` `failed`, L9 `estimate-case-build-checks-the-finished-case` `passed`.
- Lesson: L10 `lesson-case-build-misses-the-example-a-changed-check-runs-over`.

## Debt

- The code of Case 733 turned `make test` red at Retro, in `tests/test_case_schema.py::test_case_schema_the_example_passes_the_check`. It is reverted into `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff`.
- Four boxes of Case 733 are unticked: the `guppi/lint.py` box, the `guppi/prespec.py` box, the `tests/test_prespec.py` box and the `tests/test_lint.py` box.
- 11 boxes wait for the librarian.
- `estimate-hi-takes-a-conserved-spec` — waits for a session that takes a conserved Spec and for the `/hi` of the session after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — waits for a `/work` that `/box` calls and for the `/work` of the session that closes a sprint.
- `estimate-brief-written` — waits for the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — waits for the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — waits for the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — waits for the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — waits for the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — waits for the Work Mode of the session that closes `migration`.
- `estimate-sprint-migration-lint-clean` — waits for the Work Mode of the session that closes `migration`.
- `estimate-sprint-migration-merges` — waits for the Work Mode of the session that closes `migration`.

## Observations

- `make lint` was red before the work, exit 2, with 13 finding lines: `backlog: vault/wiki/backlog.md differs from its sources`, `rules/rule-morph: deferred`, and 11 `unread` lines on the `pending` Estimates.
- The example Case of `rule-case-example` (`vault/wiki/case-example.md`) creates `entity-cart` as a MOC. Its Estimate `estimate-cart-renders-in-time` names only `uv run pytest tests/test_cart_view.py -k render_time` in the Case, and the `then` example below it names a `method` with no form at all. Under Case 733 the first is a finding.
- In the code of the patch, `tests/test_prespec.py` was 1 file that `make style` would reformat. That is a long line in `test_a_moc_is_judged_as_the_plan_leaves_it`.
- Work Mode ran `tests/test_prespec.py` and `tests/test_lint.py` alone, 298 passed. The full suite ran only at Retro.

## For the next session

- Take Case 733 up again: an `update` of `rule-case-example` that gives the cart Estimate of its example a `method` a MOC takes (a `make <target>` or `by hand`), then apply `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff`, format it with `make style`, and read `estimate-prespec-catches-a-method-without-a-form`.
- `lesson-case-build-misses-the-example-a-changed-check-runs-over` has no fix. No step finds the example texts that a test runs through a check a Case changes, and Work Mode runs only the test files the Spec names.
- New tags `case-build` and `prespec`: the ledger hook refused them on L10, which carries `workflow, tests` instead. A Case may declare them.
- The close of `migration` and `rule-sprint-close`: a session of its own.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
