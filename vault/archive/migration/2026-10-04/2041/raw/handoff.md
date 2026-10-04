# Handoff — 2026-10-04, Slice 5: the findings on Cases 627–629, the answer of ask-guppi, and how /pre-spec checks a Spec

## Notes from memory

- Case 633, the question on a count over Decision pages: the person did not take the recommendation and gave an answer of their own. Decision pages are not counted again, since each states its own at its moment, and reading them again means editing history.
- Case 634, the question on a rebuilt Case: the person asked whether a new `ask-guppi` would run, and said a new run always finds something, so the checks would never end. The person accepted that a small point a fifth check would show can wait and show itself later. The confirmation by the same run, once, came from that.
- The 1439 findings left one point as it stands, by the agent's proposal at `/pre-spec`: 632.3, the `given` of 632.4 and the new paragraph of `rule-orchestration` still point to `rule-sprint-close` for facts that leave its page. The Estimates of that Leaf hold them.
- The person deferred the two sprint items of Slice 5, `rule-sprint-close` and the close of migration, which is a session of its own by case 628.9.

## Direct instructions to the librarian

- `rule-ask` takes five `update` entries in one run (633.1, 633.2, 634.1, 634.2). The `/pre-spec` found that each `replace` anchor matches once and none breaks a later one when applied in case order. Check that each lands.
- `rule-orchestration` takes 632.1, 632.10 and 634.3, and `rule-prespec` takes 634.1 and 634.2, each on a different anchor.
- Cases 632 and 634 were built again on the findings of `/pre-spec` and ratified again. Their decision lines stand once in the ledger, and the line of `estimate-case-build-checks-the-finished-case` (634.1) was added at the second ratification. The Spec holds the second answer.
- The `## How it works` sections of `rule-cleanup` and `rule-sprint-close` were removed by hand in Work Mode, as in cases 589.2 and 592. The 632.1 entry of `rule-cleanup` carries a `change` alone, and the entry of `rule-sprint-close` carries `sections.Purpose` and a `change`.

## What actually got done

- Cases ratified: 632 (632.1–632.10), 633 (633.1, 633.2), 634 (634.1–634.3).
- Code: the docstring of `guppi/cleanup.py` (632.1). No test changed.
- `make test`: 1166 passed, 6 skipped. `make style` clean.
- Readings at `/hi`: L1–L6 passed (`estimate-sprint-close-archives-the-decisions`, `-archives-done-insights-and-lone-lessons`, `-archives-the-sprint-page-and-keeps-the-rest`, `-settles-unread-estimates`, `estimate-sprint-ticks-the-spec`, `estimate-generate-writes`), and L7 failed (`estimate-handoff-holds-each-fact-once`).
- The Work reading L37 (`estimate-case-check-sends-back-a-faulty-round`) passed. Lesson: L38.

## Debt

- No box is debt.
- 52 boxes wait for the librarian: the page, render and sprint lines of the Spec, and its `read` lines.
- `estimate-sprint-migration-lint-clean` — the Work Mode of the session that closes migration.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-hi-writes-frontier` — the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` after the close of a sprint.
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — a live send-back of the hook for that reason.
- `estimate-insights-schema-checked` — its test and `make lint` after the librarian's run of this session.
- `estimate-orchestration-asks-in-the-grill-me-shape` — a later session in which the main agent puts a question of its own.
- `estimate-ask-finds` — the `/hi` after a `/pre-spec` that follows the render by 633.1.
- `estimate-ask-searches-at-prespec` — the `/hi` after a `/pre-spec` that follows the render by 633.2.
- `estimate-prespec-reconciles` — a `/pre-spec` after the render by 634.1.
- `estimate-case-build-checks-the-finished-case` — a `/pre-spec` after the render by 634.1, with the answers of its runs.
- `estimate-prespec-confirms-the-findings-once` — a `/pre-spec` after the render by 634.2 whose findings send a Case back.
- `estimate-orchestration-shows-the-built-case` — a showing of a Case after the render by 634.3.
- `estimate-ask-query-before-a-create` — a `case-guppi` that builds a Case with a `create` without a `ref`.
- `estimate-case-build-writes-the-case` — live dispatches that add a `create` without a `ref`, a change of a hook and a change on one sub-case to the fork with a round this session gave.
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — a live answer of sub-cases alone.
- `estimate-case-check-requires-each-question-of-the-rounds` — a Case the hook sends back for a missing title.
- `estimate-case-check-sends-back-a-clash-with-another-case` — a live send-back for a clash with another Case.
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — a live send-back for that reason.
- `estimate-lint-runs-every-step` — a Baseline whose backlog step is red.
- `estimate-session-start-context` — a session opened without `/hi` whose reply carries a `LEDGER` block.
- `estimate-spec-write-reaches-the-approved-spec` — a Case ratified in Work Mode.
- `estimate-sprint-close-runs-in-the-librarian-run` — the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes migration.
- `estimate-sprint-migration-merges` — the Work Mode of the session that closes migration.
- `estimate-synthesis-clusters` — a librarian's run whose yaml holds two lesson entries.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the `/work` of a session that closes a sprint.
- `estimate-backlog-renders` — the librarian's run of the session that closes a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.

## Observations

- `make lint` was red before the work with 35 finding lines: 4 stale defers and 31 unread Estimates. After the work it printed the same lines. Its backlog step was not red. No expected red.
- The `/pre-spec` of this session ran by the rule as it stands, one `ask-guppi` over the whole plan, since 634 takes effect only at its render.
- The `case-guppi` of Case 634 first wrote a `replace` anchor of 634.2 on a text that 633.1 adds and that the page does not hold yet; the check of the answer sent it back, and the anchor moved.
- The `/hi` reading of the 1934 handoff failed only on one line per Estimate in Debt.

## For the next session

- `estimate-handoff-holds-each-fact-once` failed again: decide whether the Debt of `handoff.md` keeps one line per Estimate, or the Criterion allows the lines grouped by moment.

## Ask the person
