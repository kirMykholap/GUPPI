# Handoff — 2026-10-17, sprint plugin: the Criteria of shipped Estimates, a built Case of put-offs in the Spec

## Notes from memory

- The person took every recommended answer of each round of Cases 878, 879 and 880 with "Согласен".
- After Case 878 the person asked to make the 17 rule updates of Case 875 a separate Case and put it off. The main agent had said wrongly that they still waited; they were applied by the librarian of session 0027, and the person did not ask again.
- Finding 7 of `/pre-spec` (880.21, a `then` only the librarian's run can show) stays open by the person's choice: `estimate-backlog-checks-the-file` reads `guppi check` after the librarian's run.
- `case-guppi` rebuilt Case 878 after `/pre-spec` as Case 880, a new number, and not under 878; the file of Case 878 stands as ratified.
- The person put off C1, the milestone item `rule-clean-branch` / `estimate-sprint-plugin-ci-writes-a-clean-branch`, once more.

## Direct instructions to the librarian

- Case 880 retires Case 878 and each of its sub-cases (`{supersedes:case 878.N}` on each line, `{supersedes:case 878}`, `{supersedes:case 878.10}` and `{supersedes:case 878.22}` on 880.21); 878.10 has no successor: `estimate-orchestration-asks-in-the-grill-me-shape` keeps its page and is named in the put-off of 880.21. Check that no entry of Case 878 is applied.
- 880.21 carries `{supersedes:case 875}`: `decision-case-875` goes `superseded`, the pages it changed stay, and `rule-clean-branch` is put off by the Decision page of 880.21 alone; `backlog.md` keeps its line for `rule-clean-branch`. Its reading is the `guppi backlog --check` of your `guppi check`; report it in the brief.
- The ledger line of the reading of `estimate-clean-branch-ships-neutral-texts` (`failed`, L1) carries the list of the Criterion sentences true only in the repository of GUPPI that Case 880 rewrote in part.

## What actually got done

- Cases ratified: 879 (879.1–879.4), 880 (880.1–880.21).
- Code: `.guppi/guppi/ratified.py` (`defer_only(records, reply)` takes a Case of `defer` lines as a short put-off only when the reply shows it in the short form, by `casecheck.is_short_form`; `ratified_cases(records, reply)`; the docstring). Tests: `.guppi/tests/test_ratified.py`, six tests with `built_defer` and the bare-reply refusal of `test_write_a_defer_not_shown_or_without_its_item_is_refused`.
- `uv run --project .guppi guppi test`: 1756 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 at `/hi` (`estimate-clean-branch-ships-neutral-texts` failed); L53 at the Work readings (`estimate-case-build-reads-the-code-it-states` passed, from the `/pre-spec` of this session); L54–L77 at Retro, 23 passed and `estimate-spec-write-writes-a-defer` failed. Lesson: L78 `lesson-brief-lists-transcript-readings-under-work`.

## Debt

- None.
- 52 boxes wait for the librarian (page, defer and `read` lines).
- `estimate-close-commits` — its clause on the librarian's report needs a transcript; no file or command takes it.
- `estimate-clean-branch-writes-the-session-files` — an install by hand in an empty folder with no git, with a tag `prod-x.y.z`.

## Observations

- Red before the work, in `## Baseline` of `work.md`: `guppi check` exit 1 — `backlog: vault/wiki/backlog.md differs from its sources`, ten draft pages with `core: true`, `estimate-harness-make-runs-in-both-shells` (`method: the Makefile has no target with`).
- After Case 879 a reply that carries `defer` lines of a Case it does not show in the short form is refused with `not built and checked by case-guppi — dispatch it`, not with the old "does not show it"; the short form must stand in the same reply as its `LEDGER` block.
- `estimate-spec-write-writes-a-defer` is `failed` only because no short-form defer the person asked for came in this session; its tests pass. Its `rule-spec-write` may go `draft` at your run.
- The reading of the clean version at `/hi` found, beyond the Criterion sentences, ten rules and three Estimates whose `purpose`, `method` or text holds only in the repository of GUPPI (L1); they belong to the item `rule-clean-branch`.
- The reading of `estimate-case-build-reads-the-code-it-states` used the `/pre-spec` of this session, since the first one, of session 0027, stands only in its transcript.

## For the next session

- `estimate-spec-write-writes-a-defer`: read it again at the first short-form defer the person asks for, or change its `method`.
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, put off again; the texts of the clean version the reading of L1 lists and ten draft pages with `core: true` still stop every build of `prod`.
- `estimate-close-commits`: its `method` needs a transcript, so no `/hi` closes it; a Case changes the method or puts it into the backlog (lesson L78).
- The rest of the Criterion rewrite, named in the put-off of 880.21.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
