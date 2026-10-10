# Handoff — 2026-10-10, Slice 5 — closing

## Notes from memory

- The person took up C1 and C3 in one answer "so that the next session can close the sprint"; the two went out as a batch, and the person agreed with every recommendation of both rounds in one word.
- The agent proposed to leave C2 (the close of `migration`) as an item of the sprint and then go on to `/pre-spec`, in one question; the person's "да" was taken as the word for both, and `/pre-spec` ran with no second question.
- Case 753 was built again on two findings of `/pre-spec` and ratified again; the decision line is the same, and the ledger holds it once.
- Case 753 leaves the three `pending` Estimates of `rule-sprint-close` to the closing Case. Its `context` names the limit of `estimate-sprint-migration-lint-clean`: `estimate-sprint-close-runs-in-the-librarian-run` and `estimate-sprint-close-next-session-opens-the-sprint` must be carried by `--carry`, or that Criterion fails.

## Direct instructions to the librarian

- Case 753: the `replace` of `entity-sprint-migration` takes out the `rule-sprint-close` line of Slice 5. Check after `guppi sprint` that Slice 5 of `sprint.md` holds the close line of `migration` alone.
- Case 754: the `replace` of `rule-case-build` adds one sentence after the sentence of case 736.1; check that `render` carries it into `.claude/agents/case-guppi.md`. The `update` of `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` sets `actioned` with `addressed_by: decision-case-754`; the lesson `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper` should go `archived` by the cascade, and the Insight leave `backlog.md`.

## What actually got done

- Cases ratified: 753, 754.
- No code file and no test changed.
- `make test`: 1490 passed, 6 skipped. `make style`: clean.
- Readings: L5 `estimate-case-build-reads-the-test-code-over-a-changed-text` `passed`. Lessons: none.

## Debt

- No box is debt; 7 boxes wait for the librarian.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-lint-clean` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-merges` — the Work Mode of the session that closes the sprint.

## Observations

- `make lint` was red before the work, exit 2, with 10 finding lines: 1 `deferred` (`rules/rule-morph`) and 9 `unread: pending`.
- The first build of Case 753 stated in its `context` that `guppi sprint` ticks an item only when its page stands `built`; `rule-sprint` says `built`, `passed` or `archived`. `/pre-spec` caught it, together with the unnamed `estimate-sprint-migration-lint-clean`.

## For the next session

- The close of `migration` by `/sprint-close`, in a session of its own; Slice 5 holds that line alone after this run.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
