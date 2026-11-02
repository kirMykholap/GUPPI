# Handoff — 2026-11-01, the clean build, the librarian's report, the readers of a new file's folder

## Notes from memory

- On C1 the person first asked to take `core: true` off the pages that block the build and to leave a backlog line to give it back. `case-guppi` showed that seven of the ten pages render a harness file in full, `/hi`, `/pre-spec` and the agents of Cases among them, so `prod` could not run a session. The person then chose to judge a draft page by its History.
- On C2 the person chose against the recommendation on Q2: `ask-guppi` at `/pre-spec` gets its own step and its own Grep of the code, beside the list that `case-guppi` writes. So Case 995 has three sub-cases on two agents.
- The person asked twice what an item held before answering. Both questions went to `case-guppi`, which answered before the round went on.
- `/pre-spec` raised 9 findings; 8 went back with a proposed fix, 1 (a page shipped as `draft` fails lint in an installed project) took the person's answer and became sub-case 996.3. `ask-guppi` confirmed all 9 closed.

## Direct instructions to the librarian

- Case 993, 994, 995 and 996 were ratified twice, the second time after `/pre-spec`; the ledger holds each decision line once. Apply the text of the case files as they stand after `/pre-spec`.
- `estimate-lint-checks-the-statuses` is updated by 996.1 (its `purpose`) and by 996.3 (its Criterion and `status: pending`). Apply both; they set different fields.
- `rule-clean-branch` takes two `replace` pairs from 996.1, the second now holding the sentence of case 822; check that each `old` matches once.
- `rule-prespec` takes two `replace` pairs from 995.2. `ask-guppi` checked the `old` of the second only against the rendered `.claude/skills/pre-spec/SKILL.md`, not against `rule-prespec` itself: check it there first.
- The lesson of L-line `lesson-acknowledging-reply-labels-left-in-english` has no Case of this session that fixed its cause.

## What actually got done

- Cases ratified: 993 (993.1, 993.2), 994, 995 (995.1, 995.2, 995.3), 996 (996.1, 996.2, 996.3).
- Code: `.guppi/guppi/pages.py` (`is_draft_core` takes the pages by slug and judges by `SET_BUILT` over `## History` and by a `failed` Estimate), `.guppi/guppi/ship.py` (`drafts` passes the pages by slug; docstring), `.guppi/guppi/lint.py` (`check_status` passes `by_slug`; the finding `draft while every Estimate is passed` only where `ship` stands; docstrings).
- Tests: `.guppi/tests/test_ship.py` (2 new `draft_core` tests), `.guppi/tests/test_lint.py` (4 new tests, the cascade test among them; `test_draft_with_every_estimate_passed_is_a_status_finding` sets the module of `ship` standing).
- `uv run --project .guppi guppi test`: 1904 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L19 `estimate-case-build-reads-the-readers-of-a-changed-step` failed; L20 `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed; L21 `estimate-orchestration-acknowledging-reply` failed; L22 `estimate-prespec-reconciles` passed; L23 `estimate-clean-branch-refuses-a-draft-core-page` passed; L24 `estimate-lint-checks-the-statuses` passed.
- Lesson: L25 `lesson-acknowledging-reply-labels-left-in-english` (error).

## Debt

- No box is debt.
- The boxes of pages, renders, `guppi sprint` and the `read` lines of the readings above wait for the librarian.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — waits for an acknowledging reply after `/pre-spec` that waits for the person's word.
- `estimate-close-reports-the-run` — waits for the next run of the librarian on the Render of Case 994.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — waits for the first Case that adds a file that is no page, built on the Render of Case 995.1.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — waits for the first `/pre-spec` on the Render of Case 995.2 whose plan holds such a Case.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — the live sprint page; waits for the owner's push of `plugin` and a tag `prod-x.y.z` after `rule-morph` and `rule-skill-approve-spec` are `built`, before the close of `plugin`.

## Observations

- `guppi check` was red before the work: 9 lines, 8 `a page with core: true that is draft` and `estimate-case-build-reads-the-readers-of-a-new-files-folder: unread: failed`. After the code of Case 996 the working tree prints the draft core finding only on `rule-case-build` (its failed Estimate), `rule-morph` and `rule-skill-approve-spec` (never built).
- The two Work readings were taken by general-purpose agents over the transcripts of session 2038; their scripts are in the scratchpad of this session. Both found a short read: a Read with a limit of 80 lines on the 84-line block of `rule-orchestration` in `.guppi/links.md`, and no second Read.
- `.guppi/links.md` is gitignored, so a reading cannot take the length of a block at an earlier commit by `git show`; the reader took it from the Read outputs in the transcripts.
- The `/pre-spec` of this session ran on the Render before Case 995, so the new question on the readers of a new file's folder was not asked; no Case of this session adds such a file.

## For the next session

- `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed again on a short read of a long block (limit 80 on 84 lines; in session 0141 `-A 40` on 96 lines). Decide whether `rule-case-build` sets how a block is read to its end, or a check of `case-guppi` names a cut block.
- `estimate-case-build-reads-the-readers-of-a-changed-step` failed again: 4 of 11 findings of `ask-guppi` in session 2038 were missed readers of a changed step. Decide what changes in `rule-case-build`, or whether the Criterion asks too much.
- `estimate-orchestration-acknowledging-reply` failed on the language of the labels; see the lesson. Decide whether `orchestration.md` names the translated labels, or the Criterion allows the English labels.

## Ask the person

- `estimate-skill-approve-spec-takes-the-spec` — needs the person — on a copy of the repository, in the Claude Code CLI in a standalone terminal: does `/approve-spec`, typed after Esc and Shift+Tab, append the plan to `spec.md`, and is it blocked when typed in Plan Mode?
- `estimate-orchestration-names-the-typed-approval` — needs the person — in the same CLI trial: does the reply that calls `ExitPlanMode` hold, before the call, the conditional line on Esc, Shift+Tab and `/approve-spec`?
- `estimate-spec-box-runs-a-conserved-spec` — needs the person — on a copy of the repository, one session saves a small Spec by `/carry` and a second runs it by `/box`: does it come out as the Criterion says?
