# Handoff — 2026-10-29, the clean copy's texts and the install readings

## Notes from memory

- The person took every recommended answer of the rounds and of the `/pre-spec` report. The narrowing of Case 899 to the Estimates read in this session was the person's choice at `/pre-spec`; the defer of `decision-case-893.1` was left as it stands, though its `## Deferred` names pointers that Case 901 now rewrites.
- Install A did not try the answer no of the git step; install B took it instead, in a second folder.
- The person asked whether the list of questions of the opening of a sprint was ever discussed; it was not discussed in this session. The person flagged that the opening Case of a new project asks no open question on what the project builds.
- The person switched between plan mode and auto mode several times during Work Mode; the installs ran in sessions that opened in plan mode.

## Direct instructions to the librarian

- Case 901 retires Case 899 whole: its lines carry `{supersedes:case 899}` and a mark for each of 899.1–899.10, so no line of Case 899 changes a page.
- The decision lines of Cases 898 and 900 stand once in the ledger: their re-ratification after `/pre-spec` added no line.
- Case 900 marks `{supersedes:case 862}` and `{supersedes:case 885}`: `deferred_by` is cleared only from its five Estimates; `estimate-close-commits` and `estimate-spec-write-writes-a-defer` keep `decision-case-885`, and `rule-clean-branch` and `rule-guppi-package` keep their own defers.
- The readings of Retro apply after the `update` of the same Estimate: each of the five Estimates of Case 901 is set `pending` by its `update` and `passed` by its reading, so `rule-sprint-close`, `rule-case-protocol` and `rule-materialize` stay `built` if the cascade reads both.
- The method of `estimate-clean-branch-ships-neutral-texts` that Case 898.1 sets waits for this run; the copy it reads must come after the render of this run.

## What actually got done

- Cases ratified: 898 (898.1–898.3), 900 (900.1–900.5), 901 (901.1–901.5). Case 899 is superseded by 901 and not counted.
- No code file and no test changed.
- `uv run --project .guppi guppi test`: 1792 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: all checks passed, 100 files already formatted.
- Readings: L1 `estimate-clean-branch-ships-neutral-texts` `failed` (Plan Mode); L32–L41 `passed`: `estimate-git-context-offers-git-init`, `estimate-clean-branch-writes-the-session-files`, `estimate-guppi-package-is-ready-after-the-install`, `estimate-plugin-install-offers-to-install-uv`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`, `estimate-sprint-close-next-session-opens-the-sprint`, `estimate-orchestration-batches-cases-out-at-once`, `estimate-case-protocol-case-form`, `estimate-materialize-lifts-a-lesson`, `estimate-materialize-judges-a-fence`.
- Lessons: L42 `lesson-plugin-cli-withholds-approval-of-a-long-plan`, L43 `lesson-sprint-open-asks-no-goal-of-a-new-project`, L44 `lesson-plugin-install-hooks-of-the-copy-run-at-once`, L45 `lesson-orchestration-retyped-a-ratification-line`.
- Work Mode: the skeleton tests in the repository, a clean copy for the three `--check` commands, a second copy as the catalogue, and three installs by the person into `C:\tmp\guppi-0327-a`, `-b` and `-c`.

## Debt

- No box of the Spec is debt.
- 30 boxes wait for the librarian: the `update` lines of 898, 900 and 901 and the `read` lines of 900 and 901.
- `estimate-clean-branch-ships-neutral-texts` — waits for the librarian's run of this session, with a tag `prod-x.y.z` in the history of HEAD, as its new `method` says.

## Observations

- Red before the work: `uv run --project .guppi guppi check` exit 1 with 13 lines, among them `backlog: vault/wiki/backlog.md differs from its sources`, which the brief of 2312 did not list, the ten `core: true` pages that stand `draft`, `estimate-clean-branch-ships-neutral-texts: unread: failed` and `estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`.
- In install A plan mode refused `git init -b main` after the person's yes, until the person switched to auto; the Criterion of `estimate-git-context-offers-git-init` says only that Claude Code asks the person to allow it.
- In install B `/guppi:install` asked whether to install `uv` by a picker, not by a plain question.
- The standalone installer of install B put a second `uv` (0.13.6) into `C:\Users\kir\.local\bin`; the machine's own `uv` stays in `C:\Users\kir\AppData\Roaming\Python\Python314\Scripts`.
- `/plugin marketplace add` repointed the `guppi-marketplace` added earlier from another scratchpad folder; the installs ran from the new copy.
- The first `uv run` in the copy for the checks built `.guppi/.venv` there, as the finding of `/pre-spec` on Case 900.2 foresaw.
- `/retro` did not launch while auto mode was off: the permission check of its embedded command `uv run --project .guppi guppi test` failed; it launched once auto mode was on.

## For the next session

- The Claude Code CLI withholds the approval of a plan of 15 KB, so a Spec cannot be approved there: how GUPPI keeps the plan file short enough, or approves the Spec another way, needs a Case (L42).
- The opening of the first sprint of a new project asks nothing of what the project builds: the setup skill of `rule-morph`, or the questions of `rule-skill-sprint-open`, need a Case (L43).
- The hooks of the settings that `/guppi:install` copies run in the install session itself: they build `.guppi/.venv` before `uv sync` and fail after a rollback; whether the install should keep them from running needs a decision (L44).
- `PLAIN_SPRINTS = ("migration", "plugin")` in the shipped `.guppi/guppi/caseid.py` was left to a Case of its own by Case 898; it stands in no backlog.
- The fallback paths in `subagent` of `.guppi/guppi/casecheck.py` and in `example` of `.guppi/tests/test_case_schema.py`, with the two Criteria that promise their removal (`estimate-case-check-sends-back-a-faulty-case`, `estimate-case-example-passes-the-check`), were left to a Case of their own; they stand in no backlog.
- The `method` of `estimate-close-commits` waits for "the next session"; it needs a rewording by the yardstick of Case 898.
- Seven Estimates left Case 899 and wait under the defer of `decision-case-893.1`: `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-glossary-terms-defined`, `estimate-ask-query-before-a-create`, `estimate-compact-recall-reloads`.
- The milestone line of `rule-clean-branch` and `estimate-sprint-plugin-ci-writes-a-clean-branch` was left for later; its reading waits for the owner's push of `plugin` and a tag `prod-x.y.z`.

## Ask the person
