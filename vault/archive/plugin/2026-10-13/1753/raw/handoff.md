# Handoff — 2026-10-13, sprint plugin: the clean branch, the install step, two lessons

## Notes from memory

- The person called the rebuild of Case 804 in Work Mode "a bad step": a Case checked at /pre-spec and approved in the Spec was taken out and changed. The person asked for a defer of that question; Work Mode holds no moment for a short defer, so it stands under `## For the next session`.
- On C3 (`rule-morph`) the person proposed the design themselves: an install skill like `init`, and pages that grow Case by Case from the code an item touches, never a scan of the whole codebase. Case 803 was split out of Case 802 by the person's answer.
- On Case 804 the person proposed the field `core`, so that a page can stay in `main` while it is tried live. On shipping Estimates the person hesitated ("я вот не знаю") and agreed to ship none "to try it that way"; shipping them with `tests/` was named as a possible backlog line for the milestone The plugin.
- At /pre-spec the person replaced the owner's run by hand with a tag `prod-*`, after the GitHub fact that `workflow_dispatch` runs only a workflow file on the default branch.
- `guppi ship` treats a case id after `:case ` (as in `{supersedes:case N}`) as the form of a line, like `[case ` and `#case-`, which the Case names; the Case does not name `:case `. The person was told and did not object.

## Direct instructions to the librarian

- Case 804.5 sets `core: true` on 81 rule pages and three Entities by `set` alone; Cases 800.1, 801, 803 and 804.5 all update `rule-case-build`, 800.2 and 804.5 `rule-ask`, 802 and 804.5 `rule-morph` and `rule-guppi-config`, 803 and 804.5 `rule-case-protocol`, 804.1–804.3 and 804.5 the three schema pages. Apply the `replace` pairs before the `set` lines touch the same file, and check each pair found its anchor once.
- Case 802 and Case 804.7 both update `entity-sprint-plugin` on different lines (the milestone The plugin gains `[[rule-morph]]`; the item of The clean branch gains `[[rule-clean-branch]]`, `[[estimate-sprint-plugin-ci-writes-a-clean-branch]]`). Check both lines after the run and that `guppi sprint` renders them.
- Case 802 sets `kind: Leaf` and `tags` on `rule-morph` and its four `{supersedes}` marks clear `deferred_by`: the `deferred` lint line of `rule-morph` should go, and no `schema` line should come.
- Case 804 was ratified three times in this session (first, after /pre-spec, after the rebuild in Work Mode); the ledger holds each line once, the last line of 804.7, the update of `entity-sprint-plugin`, from the second showing. The case file holds the last text.

## What actually got done

- Cases ratified: 800 (800.1, 800.2), 801, 802, 803, 804 (804.1–804.7).
- Code: `guppi/pages.py` (`SHIPPED`, `is_core`), `guppi/lint.py` (`check_origin` accepts `origin: guppi` on a page with `core: true`), new `guppi/ship.py` (`guppi ship <folder>`), `guppi/cli.py` (`ship`), new `.github/workflows/prod.yml` (push to `main` or a tag `prod-*`, pushes to `prod` with the deploy key of `PROD_DEPLOY_KEY`). Tests: `tests/test_schemas.py`, `tests/test_lint.py`, new `tests/test_ship.py`.
- On GitHub, by the owner's hand: an SSH deploy key with write access, the repository secret `PROD_DEPLOY_KEY`, and `Deploy keys` on the bypass list of the ruleset `prod`; checked by `gh api` (ruleset bypass actors DeployKey and RepositoryRole 5; one deploy key, `read_only=false`; the secret listed; no key file left in the repository folder).
- `make test`: 1601 passed, 6 skipped. `make style`: clean.
- Readings: ledger line 1 (the Work line of `/hi`), lines 113–120. Lesson: line 121.

## Debt

- No box of code, a test or a command is unticked.
- 129 boxes wait for the librarian.
- `estimate-ask-opens-a-decision-only-for-a-finding` — waits for a /pre-spec whose ask-guppi runs on `.claude/agents/ask-guppi.md` as rendered by case 800.2.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — waits for the session whose Work Mode builds the install skill of `rule-morph`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — waits for the session of this sprint that finishes the clean branch: the rewording Case done and a run by a tag `prod-*` on `plugin` read, or the close of the sprint.

## Observations

- `make lint` was red before the work, by `## Baseline` of `work.md`: `rules/rule-morph: deferred: 4 times since case 239` and `estimates/estimate-case-build-reads-the-last-output-of-a-check: unread: failed`. Cases 802 and 801 address both.
- `uv run guppi ship` over the working tree exited 1 with 206 lines, all in `guppi/*.py`: 199 references to a case inside a sentence (such as "Case 72.6:" opening a docstring) and 7 mentions of a session (such as "session 0051"); the list stands in `vault/raw/2026-10-13/1753/ship.txt`. No page carries `core` before this librarian run, so every harness file and schema a page renders in full was left out of that run; the leftovers of the pages, `.claude/`, `CLAUDE.md` and the schemas come from the first CI run, which the owner starts by a tag `prod-*` on a commit of `plugin` after pushing the librarian's commit.
- A contract that turned out imprecise: Case 804.7 put the GitHub Actions app on the bypass list; GitHub refuses it for a repository of a personal account ("Actor GitHub Actions integration must be part of the ruleset source or owner organization", HTTP 422). Work Mode stopped, the person chose a deploy key, and Case 804 was built again and ratified again (lesson on ledger line 121).
- The auto mode classifier of Claude Code refused the agent's own `gh api -X PUT` on the ruleset; the owner ran it after `!`.

## For the next session

- How Work Mode meets a fork that changes the contract of a ratified Case of the approved Spec: today the rules let its `case-guppi` build it again in Work Mode; the person thinks this is wrong work and asked to discuss it (the person asked for a defer).
- The rewording Case of the milestone The clean branch: reword at their source the 206 lines of `ship.txt`, and the page leftovers the first CI run prints.
- Whether the Estimates of shipped rules ship together with `tests/`, as a backlog line for the milestone The plugin (the person's open question on Case 804).

## Ask the person

