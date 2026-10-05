# Handoff — 2026-10-05, the Estimate reading loop

## Notes from memory

- The person asked to end the loop of Estimates read again every session. The person chose to close 15 Estimates as `passed` by decision (Case 669), with "if problems come, we return to them", and agreed to the recommended option of every round and of the pre-spec question.
- The person got lost when the main agent built Cases 669 and 670 side by side and showed a question of 670 next to the showing of 669 (lesson L10). From then on the Cases went one at a time, and at pre-spec the questions were numbered `<Case id>.Q<n>`.
- 670.2 keeps one exception the person did not decide in a round: an update that changes a single part of an Estimate page is neither read nor set `failed` at Retro. The builder of 670 named it, and the person ratified 670 with it.
- At pre-spec the person chose to leave finding 669 2.1 open: 669 does not name `estimate-retro-loads`, whose old Criterion line 21 says the handoff names a changed Estimate as a reading of a later session. 670.2 replaces that Criterion in this Spec.
- C3 (`rule-sprint-close`) and C4 (the close of migration) were put off as `· sprint · defer` by the main agent's recommendation, which the person's "Идём работать" accepted.

## Direct instructions to the librarian

- Apply the `/hi` readings L1–L9 before the 669 updates: L8 sets `estimate-ask-searches-at-prespec` `failed`, and 669.15 then sets it `passed` with that reading kept under its Result.
- The ledger holds two lines each for 669.6, 669.7 and 669.10: L16, L17 and L20 from the first ratification, and L41–L43 with the same target and the `{supersedes:case …}` marks added at the re-ratification. Both name the same update. Check that the page is updated once and that 659, 630, 617 and 622 are set superseded.
- `rule-case-protocol` gets three updates in this Spec (669.16, 670.4, 671.2), each a `replace` pair in a different paragraph. Check the pairs apply in ledger order and `case-schema.md` renders once.
- 671.2 deletes `rule-ledger-line-withdrawn-on-re-ratification`; `backlog.md` should then count one item fewer. 671.1 sets `insight-ledger-ratified-line-never-withdrawn` actioned and rewrites its Proposal line.
- The cascade may set `built` on rules whose Estimates all become `passed` by 669 (for example `rule-case-check`, `rule-case-build`); report which.

## What actually got done

- Cases ratified: 669 (669.1–669.16), 670 (670.1–670.7), 671 (671.1, 671.2). All three were built again on the findings of pre-spec and ratified again.
- Code: `guppi/ledger.py` (`refused_readings` waits for the `retro` mark of the session, case 670.1), `guppi/onward.py` (`retro_mark`, `retro_moment` beside `retro_marked`), `guppi/lint.py` (`waits_for_another_session`), `guppi/prespec.py` (the finding `method waits for another session`), `guppi/casecheck.py` (`target_findings`, `lined_numbers`, `supersede_marks`).
- Tests: `tests/test_ledger.py` (4 new: the mark opens the reading, another session's mark does not, a line before the mark stays refused, a line after it is written), `tests/test_lint.py` (2 new), `tests/test_prespec.py` (2 new; a form example and a moment example moved off a method that now waits), `tests/test_casecheck.py` (6 new, `-k dropped_target`).
- `make test`: 1258 passed, 6 skipped. `make style`: clean.
- Readings: L1–L9 at `/hi` (8 passed, L8 failed). Lesson: L10.

## Debt

None: every box of code and tests is ticked; the box of this handoff (names none of the fifteen of 669) is met by this file.

44 boxes wait for the librarian.

Readings that cannot be taken yet:
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — updated by 670.1; pytest, at the next `/hi`.
- `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` — created by 670.4; pytest `-k waits`, at the next `/hi`.
- `estimate-case-check-sends-back-a-ratified-case-without-a-target` — created by 671.1; pytest `-k dropped_target`, at the next `/hi`.
- `estimate-retro-loads` — updated by 670.2; by hand at the next `/retro`.
- `estimate-work-mode-takes-the-work-readings` — updated by 670.7; by hand at the next `/work` and `/retro`.
- `estimate-handoff-holds-each-fact-once` — updated by 670.3; by hand, a handoff written after the render of 670.3.
- `estimate-hi-takes-its-readings` — updated by 670.5; by hand at the next `/hi`.
- `estimate-hi-writes-frontier` — updated by 670.6; by hand at the `/hi` after the close of the sprint.
- The ten other Estimates of the close of migration (`estimate-sprint-migration-leftovers-gone`, `-lint-clean`, `-merges`, `estimate-sprint-close-runs-in-the-librarian-run`, `-next-session-opens-the-sprint`, `-takes-the-readings-in-groups`, `estimate-brief-written`, `estimate-backlog-renders`, `estimate-hi-takes-a-conserved-spec`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`) — the session that closes the sprint.

## Observations

- `make lint` was red before the work (Baseline of `work.md`): 5 `deferred` and 34 `unread` lines.
- The ledger hook code of 670.1 is live from this commit, while the rendered Retro text still says a changed Estimate has no reading in its session. This Retro took none; from the next session the two agree once the librarian renders 670.2.
- A re-ratification that only adds `{supersedes}` marks to a line leaves the first line in the ledger beside the marked one (669.6, 669.7, 669.10). The check of 671.1 does not catch this, since the target stands; it is harmless only if the two updates apply as one.
- The Estimates 670 updates keep their old methods, and several name a later `/hi` (`estimate-handoff-holds-each-fact-once`, `estimate-hi-takes-its-readings`). The new pre-spec finding of 670.4 judges only a method a plan writes, so these stand.
- The `/hi` of this session spent one transcript agent of about 112k tokens to take the readings of six Estimates. That cost started the work of 670.

## For the next session

- Under 670.5 the next `/hi` reads no transcript: each open W line it cannot take from files and commands becomes a Cases line. Expect `estimate-hi-takes-its-readings` and `estimate-handoff-holds-each-fact-once` among them, since their methods name a later session: decide whether their methods are rewritten to run in their own session.
- The two ledger lines for 669.6, 669.7 and 669.10 (see Observations): decide whether a re-ratification that changes only marks needs a check or a rule.
- C3 `rule-sprint-close` and C4 the close of migration stay for the session that closes the sprint.

## Ask the person
