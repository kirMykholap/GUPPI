# Handoff — 2026-10-04, Slice 5: the readings that wait — the check of a cited search, and seven methods that no longer wait for a rare live event

## Notes from memory

- The person is not ready to close migration yet and asked to close as many readings as possible. The two sprint items of Slice 5 were put off for that, and Cases 636 and 637 were taken for it.
- The person asked why `estimate-handoff-holds-each-fact-once` kept failing. Its `case-guppi` answered that the first failure came from a rule that could not be met and the second from one slip of the writer. The person kept one line per Estimate, and the item closed with a reading and no Case.
- Case 636 leaves one cause open: the lesson of Case 620 also gives the cascade of a `set` that was not searched, and no line of the Criterion of `estimate-case-build-checks-the-finished-case` covers it. The person accepted that the lesson goes to the archive with the Insight.
- Case 637.2: the step of `case-guppi` after a clash enters `rule-case-build` with no check of its own, and the main agent's step after a clash stays as text in `orchestration.md` with no check either. Both by the person's choice.

## Direct instructions to the librarian

- `rule-case-build` takes two `replace` entries, 636 and 637.2, on two different sentences of its Render, one after the other. Check that both land, then render `.claude/agents/case-guppi.md` once.
- The update of `estimate-case-check-sends-back-a-clash-with-another-case` (637.2) carries its Criterion under `sections.Criterion`. Check that the line on what `case-guppi` does after a clash, which stands in the `then` of 637.2, is not in it.
- 637.3 carries `{supersedes:case 631}`: check that the `deferred_by` of `estimate-lint-runs-every-step` is cleared.
- 636 sets the Insight `actioned`; the cascade then archives its four `clustered` lessons. Synthesis decides where the new lesson goes.

## What actually got done

- Cases ratified: 636, 637 (637.1–637.4).
- Code: `tests/test_lint.py`, two tests whose names hold `every_step` (637.3).
- `make test`: 1168 passed, 6 skipped. `make style` clean.
- Readings: L1 (`estimate-insights-schema-checked`) and L2 (`estimate-handoff-holds-each-fact-once`) passed in Plan Mode. Work readings: L14, L15 and L17 passed (`estimate-orchestration-asks-in-the-grill-me-shape`, `estimate-prespec-reconciles`, `estimate-orchestration-shows-the-built-case`); L16 failed (`estimate-prespec-confirms-the-findings-once`). Lesson: L18.

## Debt

- No box is debt.
- 13 boxes wait for the librarian: the page and render lines of the Spec.
- `estimate-sprint-migration-lint-clean` — the Work Mode of the session that closes migration.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-hi-writes-frontier` — the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` after the close of a sprint.
- `estimate-ask-finds` — the `/hi` of the next session, on the answers of `ask-guppi` at the `/pre-spec` of this session.
- `estimate-ask-searches-at-prespec` — the `/hi` of the next session, on the calls of `ask-guppi` at the `/pre-spec` of this session.
- `estimate-ask-query-before-a-create` — a `case-guppi` that builds a Case with a `create` without a `ref`.
- `estimate-backlog-renders` — the librarian's run of the session that closes a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-case-build-checks-the-finished-case` — a `/pre-spec` after the render by 636.
- `estimate-case-build-writes-the-case` — live dispatches that add a `create` without a `ref`, a change of a hook and a change on one sub-case to the fork with a round this session gave.
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — its pytest, in the next session.
- `estimate-case-check-requires-each-question-of-the-rounds` — its pytest, in the next session.
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — its pytest, in the next session.
- `estimate-case-check-sends-back-a-clash-with-another-case` — `uv run pytest tests/test_casecheck.py -k session_clash`, in the next session.
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — its pytest, in the next session.
- `estimate-lint-runs-every-step` — `uv run pytest tests/test_lint.py -k every_step`, in the next session.
- `estimate-session-start-context` — `make test-session-start`, in the next session.
- `estimate-spec-write-reaches-the-approved-spec` — a Case ratified in Work Mode.
- `estimate-sprint-close-runs-in-the-librarian-run` — the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes migration.
- `estimate-sprint-migration-merges` — the Work Mode of the session that closes migration.
- `estimate-synthesis-clusters` — a librarian's run whose yaml holds two lesson entries.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the `/work` of a session that closes a sprint.

## Observations

- `make lint` was red before the work with 35 finding lines: 4 stale defers and 31 unread Estimates. No expected red.
- The first answer of the `case-guppi` of Case 637 held sub-case 637.3 alone, and the case file held only it. It was sent back for the whole Case before any showing. Why it answered so was not looked into.
- The first `case-guppi` of the session got the number 635 for the handoff item and answered with a round and a fact only, so no Case 635 stands.
- The harness marked two answers of the `case-guppi` of Case 637 as shaped like settings-json. They name `.claude/settings.json` in `context`, where the hook is registered, and ask for no change to it.
- The third build of Case 636, on the wording of finding 3.1, was not sent to `ask-guppi` again (case 634.2).
- Whether the two changes of `rule-case-build` meet in meaning was not judged; the run of 637 only saw that their anchors stand in two different sentences.
- In the tests of 637.3, `make` and the sh of Git for Windows ran the fake `uv`, a script with no extension, from the first directory of PATH.

## For the next session

- `estimate-prespec-confirms-the-findings-once` failed: the answers of `ask-guppi` at the confirmation did not hold one line per finding with one sentence, and the main agent's message invited a new defect. Decide whether the form of the answer is enforced or the Criterion allows a short paragraph per finding.
- The close of migration, when the person is ready: a session of its own (case 628.9).

## Ask the person
