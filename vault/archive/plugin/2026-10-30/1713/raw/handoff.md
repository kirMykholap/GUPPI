# Handoff — 2026-10-30, the items of the brief of 0304 and four items of the backlog

## Notes from memory

- On C7 the person first chose (c) for Q1 — the person brings back set-aside files by ordinary Cases — then stopped the round and changed the answer to (b): the setup Case of `rule-morph` shows what each set-aside file holds at the first `/hi`. Case 932 stands on (b).
- On C9 the person suspects the terminal, not Claude Code: the test install ran in a standalone PowerShell window. Case 934 keeps the approval flow as it is and puts the item off as a bug with a test; nothing on the cause is known from a source.
- On C2 the person asked for a plain explanation of the round (`/wait-what`) before answering.
- 931.Q6 was raised by the `case-guppi` of Case 931 inside the loop after `/pre-spec`: where the promise that the lift carries `drop` stands. The person chose a new Case beside it, Case 935.
- Before the person answered 935.Q1, the main agent told the person that a `drop` names whole sections only and that `generate` already fails a `drop` of a section the schema requires, so the guard of 935.2 adds a second, earlier mark at the lift.
- The `ask-guppi` finding on Case 934 and the `root_cause` of `lesson-plugin-cli-withholds-approval-of-a-long-plan` was left as it is by the person's word: the lesson stays, and the test of Case 934 is to record the cause.

## Direct instructions to the librarian

- Case 931 adds `drop` to the update keys in the code; this run's own `materialize` and `generate` already carry and apply it, but no entry of this yaml uses `drop`.
- Case 935 has two sub-cases that both update `rule-materialize`; the two entries change different sentences of the page.
- Case 934 is a `defer` of `rule-spec-capture` with `{supersedes:case 909}`: the page keeps one `deferred_by`, the new Decision in place of 909, and stays in `backlog.md`.
- Case 927 updates only the `method` of `estimate-harness-make-runs-in-both-shells`; its Criterion and status stand. The `guppi check` of this run should no longer print its `method` line.
- `.claude/skills` and `vault/wiki/case-schema.md` change at this run's render: `plugin/skills/install/SKILL.md` from `rule-plugin-install`, `case-schema.md` from `rule-case-protocol`, `guppi.toml` from `rule-guppi-config`.

## What actually got done

- Cases ratified: 927; 928; 929; 931; 932 (932.1–932.5); 934; 935 (935.1, 935.2). Cases 929, 931 and 932 were built again in the loop after `/pre-spec` and ratified again; Case 935 was born there. Cases 930 and 933 were dropped with no decision line.
- Code: `.guppi/guppi/materialize.py` (`drop` in `ITEM_KEYS`, `drops_criterion`, `lift_criterion` and docstrings), `.guppi/guppi/generate.py` (`Generator.drop`, the docstring), `.guppi/guppi/ratified.py` (the docstring of sub-points).
- Tests: `.guppi/tests/test_commands.py` (pytest finds the settings of `.guppi/pyproject.toml` with and without a root `pyproject.toml`), `.guppi/tests/test_generate.py` (seven `drop` tests), `.guppi/tests/test_materialize.py` (the lift of `drop`, the mark of a `drop` of the Criterion, `drop` among the update keys), `.guppi/tests/test_ratified.py` (a `drop` sub-point read into a list; `drop` among the update keys of `key_judge`).
- `uv run --project .guppi guppi test`: 1814 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L22–L28, all `passed`. Lessons: L29, L30.

## Debt

- No box is debt; no test was reverted.
- 34 boxes wait for the librarian.
- `estimate-harness-make-runs-in-both-shells` — after the Work Mode that builds the change: `make help`, `make style`, `make test` and `make lint` from PowerShell and from Git Bash.
- `estimate-guppi-config-runs-the-test-and-style-commands` — after the librarian's run that renders `guppi.toml` with the key `test` that names `.guppi/tests`.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — after the librarian's run of this session, with a tag `prod-x.y.z` in the history of HEAD and an install by hand from a local copy.
- `estimate-plugin-install-writes-guppi-into-an-empty-project` — after the librarian's run of this session, with a tag `prod-x.y.z` and an install by hand.
- `estimate-plugin-install-runs-no-hook-before-uv-sync` — after the librarian's run of this session, with a tag `prod-x.y.z` and an install by hand.
- `estimate-morph-takes-in-the-set-aside-files` — after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — the `/pre-spec` of this session came, but its `ask-guppi` made no Read or Grep on `vault/wiki/decisions/`, so no refusal could be read; it waits for such a call.
- `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-case-build-reads-the-code-it-states` — their events came in this session (a reply stating what a subagent did; a `/pre-spec` of Cases built on the new Render), but Retro did not read them; the transcripts of this session's subagents are under the session's task folder of Claude Code.

## Observations

- `guppi check` was red before the work, 14 lines: `backlog: vault/wiki/backlog.md differs from its sources`, the 12 pages with `core: true` that stand `draft`, and the `method` line of `estimate-harness-make-runs-in-both-shells`.
- `ITEM_KEYS` stands in two lists of tests beside the code — `test_item_keys_answers_for_each_kind_as_the_lift_does` of `test_materialize.py` and `test_write_the_keys_of_a_create_are_judged_by_its_schema` of `test_ratified.py`; adding `drop` failed the second until it was written there too.
- `Generator.drop` judges a required section by running `check_schema` of `.guppi/guppi/lint.py` over the page with and without it, so lint and `generate` share one judgment of the schema.
- At Retro the `--review` of `guppi ship` showed a bracket of this session's own work, in `.guppi/guppi/ratified.py`, holding words the sentence needs; it was reworded before the reading.
- The methods of `estimate-guppi-config-runs-the-test-and-style-commands` and `estimate-lint-runs-every-step` still say "make with the target"; Case 929 rewords the first, the second stands, and `guppi ship` leaves it out of the clean copy for the misread word.

## For the next session

- The milestone item of the clean branch, `rule-clean-branch` with `estimate-sprint-plugin-ci-writes-a-clean-branch`, was put off again: the owner's push of `plugin` and a tag `prod-x.y.z`, and the reading of the CI run it starts.
- `estimate-clean-branch-pages-hold-pointers-only-in-brackets` still reads by `guppi ship --review` into a folder with no flag, which exits 1 while a page with `core: true` stands `draft`; the person chose to leave it in Case 928.
- Eleven Leaf rules still carry `## How it works`; once `drop` is live, a Case that touches one of them can remove the section.
- `orchestration.md` names no Frontier closer for a backlog item that a Case defers again with a new wording (L30).
- When the main agent judges which Cases of the session are related, a Case that writes text one check reads in the same way as another Case is not counted (L29).

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — After the agent writes a clean copy by `guppi ship --allow-draft` in the repository of GUPPI, and you, at a stop of Work Mode, add it as a catalogue, install `guppi`, type `/guppi:install` in an empty project, reopen Claude Code and type `/hi`: did the output of the install, the order of its steps, the files of the project and its `.guppi/.venv/` match the Criterion?
- `estimate-close-reports-the-run` — needs the person — Did the report that `/handoff` showed after the librarian's run of 2026-10-30 give each part the Criterion names — the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags, the lint total and each part another step of the frame sends to the report — and no test result and no list of files?
