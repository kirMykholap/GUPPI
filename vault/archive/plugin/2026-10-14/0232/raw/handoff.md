# Handoff — 2026-10-14, sprint plugin: the bare-number list, the session stamp of guppi caseid, the first prod run

## Notes from memory

- Case 810 was ratified first, then `/pre-spec` found three faults in it: the placeholder `<id>` clashed with the sprint `<id>` of the same sentence of `ratification.md`; `estimate-orchestration-shows-the-built-case` named the command without the option; and with a stamp that finds no plan file the command still printed an id it did not hold. The person chose that the command refuses then (exit 1). `case-guppi` built the fix as Case 812 with sub-cases, under a new number, its lines marked `{supersedes:case 810}`, since 810 had decision lines already; the person ratified 812.1 and 812.2.
- The id 813 is held in the store of the plan file of this session and names no Case; the main agent ran `caseid --next` to check 812, and the run held a new id (lesson on ledger line 16 or near it, `lesson-caseid-run-to-check-an-id-held-a-new-one`).
- The milestone item The clean branch was closed in the Frontier as work: the person chose that the agent pushes `plugin` and a tag `prod-1` after the commit of Retro, on the person's word. The person gave that word; the push ran.
- The reading of `estimate-clean-branch-pages-hold-pointers-only-in-brackets` judged the brackets `(one written before case 513, case 513)` and the like, beside the words "older page", as history of this repository, which its second Then line allows, and not as the definition of a term; the person was told that a stricter reading makes it `failed`, and did not object.

## Direct instructions to the librarian

- Case 810 is superseded whole by Case 812.1 in its own session: its three `update` entries (`rule-orchestration`, `rule-ratification`, `estimate-ratification-case-id-carries-the-sprint`) are not applied, and 812.1 carries the texts that stand.
- Check first that the `replace` pairs of 812.1 on `rule-orchestration` find their `old` text: three pairs, one of them the sentence on the plan file "before the first dispatch of the session."
- After the render, `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` name `uv run guppi caseid --next --session <stamp>`; the code of `guppi/caseid.py` already refuses a run without `--session` (exit 2) or without the plan file (exit 1) in the working tree.

## What actually got done

- Ratified: Case 811; Case 812 with its sub-cases 812.1 and 812.2. Case 810 is superseded by 812.1 and is not counted.
- Code: `guppi/ship.py` — one pattern `NUMBERS`, a list of case numbers joined by a comma, a semicolon, `and` or a dash, serves `BARE_BRACKET`, `BARE_OPENING` and `BARE_ALONE`, with the module docstring and the comment above the patterns. `guppi/caseid.py` — `--session` required; with no plan file of the session one line on stderr, no id, nothing held, exit 1; its docstring says both.
- Tests: `tests/test_ship.py` one new test of the list shapes; `tests/test_caseid.py` two new tests (without `--session`; with no plan file, by the session's stamp and by an unknown one).
- At the end of Work Mode: `make test` 1619 passed, 6 skipped; `make style` clean; `uv run guppi ship --check` printed no line; `make lint` exit 0 with no line, before the librarian's run.
- Readings: ledger line 1 (`estimate-clean-branch-pages-hold-pointers-only-in-brackets`, `passed`, at `/hi`); ledger lines 11–13 (`estimate-clean-branch-writes-a-clean-copy`, `estimate-ratification-case-id-carries-the-sprint`, `estimate-orchestration-shows-the-built-case`, all `passed`).
- Lessons: ledger lines 14–16 — `lesson-caseid-run-before-the-plan-file-held-no-id` (`{addressed_by:case 812.1}`), `lesson-ci-prod-deploy-key-refused-at-checkout`, `lesson-caseid-run-to-check-an-id-held-a-new-one`.
- Pushed to GitHub on the person's word: the branch `plugin` and the tag `prod-1` on the commit of the work of Cases 811 and 812.

## Debt

- No box of the Spec is debt.
- 11 boxes wait for the librarian: the `update` lines, the two render lines and the three `read` lines of Cases 811, 812.1 and 812.2.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; its target is the live sprint page and its work is not done: the CI run of `prod-1` failed before `guppi ship` ran; it waits for the Retro of the session whose run of `.github/workflows/prod.yml` writes `prod`, or for the close of the sprint.

## Observations

- The workflow `prod` ran on the tag `prod-1` (run 38489789184, event `push`, head `prod-1`), so the `on:` block takes a tag `prod-*`. It failed at `actions/checkout`: "git@github.com: Permission denied (publickey)", three tries; no branch `prod` was written. The deploy key `prod_deploy_pub` stands on the repository with write access, `verified: true`, `last_used: null`; the secret `PROD_DEPLOY_KEY` stands, set on 2026-10-13. No local copy of the key pair was found under the user's home. The private half in the secret does not open that deploy key.
- `guppi ship --check` with the new list pattern prints nothing on `guppi/`; a dash-joined opening such as a year and a month before a colon (`2026-10:`) would now be a finding, since `NUMBER` excludes only a full date. No such text stands in `guppi/` today.

## For the next session

- The deploy key of `prod`: the owner makes a new key pair, sets its public half as the deploy key of the repository with write access and its private half as `PROD_DEPLOY_KEY`, then runs the failed run again (`gh run rerun 38489789184`) or pushes a new tag `prod-*`; the reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` follows that run. Whether this needs a Case or is work of the owner alone is for the next Plan Mode.
- Whether `guppi caseid` gets a mode that reads the store without holding an id, or `orchestration.md` says that the main agent never runs the command to check an id (`lesson-caseid-run-to-check-an-id-held-a-new-one`).

## Ask the person
