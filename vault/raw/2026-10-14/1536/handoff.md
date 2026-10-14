# Handoff — 2026-10-14, the clean branch and guppi caseid

## Notes from memory

- The person took the recommended answer on every question of both rounds (Case 813: a sentence only, no read mode of `guppi caseid`; Case 815: drop both exceptions, read the CI again in this session).
- The deploy key of `prod` was the owner's work alone, with no Case: `case-guppi` answered with a fact, and the id 814 it was dispatched under is held and names no Case.
- The first reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` (on `prod-1`) was the main agent's judgment `failed`, on four bracket pointers in the prose of the example file; the person did not object and asked for the Case that fixed it.
- The second reading judged as samples the `origin: raw/2026-09-08/…` values in the `examples` block of the `schema.yaml` files (example pages with the sprint `2026-Q3-s4`) and the id `case 785.1` in a code span of `ratification.md` (the form of an old id). A stricter reading of "no mention of a session" would make it `failed`.
- The two `－` lines of that Criterion (ship exits 1; a clean version equal to the last commit) were read from the text of `.github/workflows/prod.yml` both times, never seen in a run.

## Direct instructions to the librarian

- Case 815 was ratified twice: once before `/pre-spec`, and again after the check asked for an `update` of `entity-sprint-plugin` and `ask-guppi` found a wrong line number in its `context`. The ledger holds its first two decision lines once and the third line from the second ratification; the Case file holds the last text.
- Case 815 sets `estimate-clean-branch-writes-a-clean-copy` `pending` and replaces its Criterion; ledger line 9 reads it `passed` after that. Case 813 does the same for `estimate-ratification-case-id-carries-the-sprint`, read on line 8.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` has two readings in this ledger: line 3 `failed`, line 10 `passed`. The later one is the result.
- The `replace` of Case 815 on `entity-sprint-plugin` rewrites the "what remains" of the milestone The clean branch; with line 10 `passed` the milestone line should tick at `guppi sprint`.
- The lesson of line 4 carries the `addresses` mark of Case 815 on the decision line of `rule-clean-branch`. The lesson of line 11 has no mark.

## What actually got done

- Cases ratified: 813, 815.
- Code: `guppi/ship.py` — `EXAMPLE` and `EXAMPLE_FILE` removed; `masked` no longer sets aside the Render of `rule-case-example`; `judged` no longer skips `vault/wiki/case-example.md`; the docstrings reworded. Tests: `tests/test_ship.py` — `test_a_sample_is_no_pointer` changed, `test_a_pointer_in_the_prose_of_the_example_file_exits_1` added.
- `make test`: 1620 passed, 6 skipped. `make style`: clean. `make lint` in Work Mode: exit 0, no line.
- On GitHub, by the owner: a new deploy key `prod_deploy_pub` with write access and a new `PROD_DEPLOY_KEY`; run 38489789184 rerun on `prod-1` (attempt 2, success, wrote `prod` 34ae3bee); `plugin` and the tag `prod-2` pushed; run 38585781386 on `prod-2` succeeded and wrote `prod` c363e8a9 on top of 34ae3bee. No local copy of the key pair remains.
- Readings: ledger lines 3 (`failed`), 8, 9, 10 (`passed`). Lessons: lines 4 and 11.

## Debt

- No box is debt.
- 9 boxes wait for the librarian: Case 813 — two `update` lines, the render of `orchestration.md`, one `read`; Case 815 — three `update` lines, `guppi sprint`, one `read`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — after the session whose Work Mode builds the install skill of `rule-morph`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — after the first pull request from another account merged into `main` by `/pr-review` after the close of `plugin`.
- `estimate-hi-writes-frontier` — the session after the close of a sprint.
- `estimate-sprint-plugin-installs-as-a-plugin` — the Retro of the session that installs the clean branch into an empty project, or the close of the sprint.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — the Retro of the session that reads a pull request from a second account, or the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — the `/hi` after the session that writes `README.md`, or the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — the end of Work Mode of the session that closes `plugin`.

## Observations

- `/pre-spec` found that a Case closing a sprint item had no `update` of the sprint page; `case-guppi` had not added one at the first build.
- The ruleset of `prod` reported "Cannot create ref due to creations being restricted" on the first push and "Cannot update this protected ref" on the second, each under "Bypassed rule violations": the deploy key passes the bypass as `rule-github-repository` sets it.
- The `!` prompt in this setup runs PowerShell 5.1 (line 11).

## For the next session

- The milestone The clean branch is done once the librarian's run ticks it; the next milestone is The plugin — 4 items: the clean version made into a Claude Code plugin, `rule-morph`, the README, the close of `plugin`.

## Ask the person
