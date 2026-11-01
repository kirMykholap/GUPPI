# Handoff — 2026-11-01, the STOP: line after /pre-spec and the closer of a Frontier line

## Notes from memory

- The person took every recommended answer with a short "Ок". No round was argued.
- Case 990 was ratified and then replaced whole by Case 992 under a new number, with `{supersedes:case 990}` on each line, while still in Plan Mode. `case-guppi` proposed the new number because a ratified Case cannot take a second behaviour without the person saying where it goes. `orchestration.md` sets a rebuild under the Case's own number in Plan Mode. The person chose the new number.
- Case 991.2 kept its `read` line for `estimate-hi-writes-frontier` against finding 4.1 of `/pre-spec`. The person then agreed to rewrite its `method` into the `by hand, after <event>:` form, so the finding closed.
- Finding 4.2 of `/pre-spec` stays open and was judged known: `estimate-orchestration-closes-a-line-by-what-its-case-does` reads the text of the Render at Retro, not the agent closing a line. Precedent: case 937.2.

## Direct instructions to the librarian

- Case 992 supersedes Case 990 whole. Apply the lines of 992.1 and 992.2 only. Case 990's two lines name the same pages as 992.1.
- `rule-orchestration` gets updates from 991.1 (closer passages in `## Plan Mode and the Frontier`, `## The short form — deferred decisions`, and the take-back sentence of `## Showing and signing a Case`) and from 992.2 (`## The acknowledging reply` only). The two Cases' `old` texts do not overlap. Check that each `old` still matches once after the other applies.
- `insight-frontier-line-closed-by-the-case-built-on-its-item` goes `actioned`, with `addressed_by: decision-case-991.1`. It has no `deferred_by`.
- `estimate-hi-writes-frontier`: 991.2 sets its `method` as well as `status: pending`.

## What actually got done

- Cases ratified: 991 (991.1, 991.2, 991.3, 991.4) and 992 (992.1, 992.2).
- Code: `.guppi/guppi/onward.py` (`ONLY_THE_PERSON` and the module docstring) and `.guppi/tests/test_onward.py` (2 new tests).
- `uv run --project .guppi guppi test`: 1898 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L14 `estimate-orchestration-names-related-cases-in-the-dispatch` passed; L15 `estimate-close-reports-the-run` passed; L16 `estimate-handoff-dispatches` passed; L17 `estimate-case-build-reads-the-readers-of-a-new-files-folder` failed; L18 `estimate-orchestration-closes-a-line-by-what-its-case-does` passed; L19 `estimate-orchestration-takes-back-a-ratified-case` passed; L20 `estimate-orchestration-defers-in-one-reply` passed; L21 `estimate-prespec-onward-sends-the-agent-on` passed; L22 `estimate-orchestration-acknowledging-reply` passed.
- Lesson: L23 `lesson-showing-sent-only-the-files-of-the-case-headings` (error).

## Debt

- No box is debt.
- 19 boxes wait for the librarian: page, render and `read` lines.
- `estimate-hi-writes-frontier` waits for the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint.

## Observations

- `guppi check` exited 1 before the work, with 10 lines of `status: a page with core: true that is draft`. It was red before the work.
- `estimate-close-reports-the-run`: the librarian of session 0141 gave its report only in its handback. Its last plain text was a one-line note before its commit. The frame asks for the report as the last text and the same text in the handback. The hook copied the handback, so `report.md` is right, but the frame's wording and the run differ.
- `estimate-handoff-dispatches`: in session 0141 the dispatch of the librarian went out in the same message as the Write of `handoff.md`, and `report.md` was committed before its text was shown. Neither breaks the Criterion.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` failed. The new file `.claude/skills/approve-spec/SKILL.md` of Case 987.1 is under `.claude/`, and `callers()` of `.guppi/tests/test_guppi_package.py` reads every file under `.claude`. The rendered skill holds no `uv run guppi` or `uv run pytest`: this was checked by a grep, not by running that test. The test passed in this session's full run.
- `estimate-orchestration-acknowledging-reply` was read on the Render before Case 992.2. The new `STOP:` line was not exercised.

## For the next session

- `estimate-case-build-reads-the-readers-of-a-new-files-folder` failed: case-guppi did 2 of 8 searches and readings in full for a new file outside `vault/wiki/` and missed 5. Decide what changes in `rule-case-build`, or whether the Criterion asks too much.
- The clean branch of the sprint (`rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`) was put off again. The push of `plugin` and a tag `prod-x.y.z` waits for the owner, and 10 `draft` pages with `core: true` still keep `prod` empty.
- Whether the frame of the librarian should say that the report is returned by the handback alone, since the last run gave no plain text of it.

## Ask the person

- `estimate-skill-approve-spec-takes-the-spec` — needs the person — on a copy of the repository, in the Claude Code CLI in a standalone terminal: does `/approve-spec`, typed after Esc and Shift+Tab, append the plan to `spec.md`, and is it blocked when typed in Plan Mode?
- `estimate-orchestration-names-the-typed-approval` — needs the person — in the same CLI trial: does the reply that calls `ExitPlanMode` hold, before the call, the conditional line on Esc, Shift+Tab and `/approve-spec`?
- `estimate-spec-box-runs-a-conserved-spec` — needs the person — on a copy of the repository, one session saves a small Spec by `/carry` and a second runs it by `/box`: does it come out as the Criterion says?
