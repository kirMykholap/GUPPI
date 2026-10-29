# Brief — 2026-10-29, librarian of session 0327

## Where things stand

- Session 0327 of the sprint `plugin`. Cases ratified: 898 (898.1–898.3), 900 (900.1–900.5), 901 (901.1–901.5). Case 899 is superseded whole by Case 901 and not counted (handoff).
- No code file and no test changed. `guppi test` 1792 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Work Mode: the skeleton tests in the repository, a clean copy for the three `--check` commands, a second copy as the catalogue, and three installs by the person into `C:\tmp\guppi-0327-a`, `-b` and `-c` (handoff).
- Readings: L1 `estimate-clean-branch-ships-neutral-texts` `failed` (Plan Mode); L32–L41 `passed`: `estimate-git-context-offers-git-init`, `estimate-clean-branch-writes-the-session-files`, `estimate-guppi-package-is-ready-after-the-install`, `estimate-plugin-install-offers-to-install-uv`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`, `estimate-sprint-close-next-session-opens-the-sprint`, `estimate-orchestration-batches-cases-out-at-once`, `estimate-case-protocol-case-form`, `estimate-materialize-lifts-a-lesson`, `estimate-materialize-judges-a-fence`. Lessons L42–L45 (handoff, ledger).
- `guppi materialize` printed `written with 45 entries` for `vault/raw/2026-10-29/0327/materialize.yaml` and `extended with 0 entries` for the yaml of `2312`. The ledger has 45 lines; the yaml holds an entry for each of lines 1–45 and 27 records under `decisions`, `unparsed: []`. Kinds: 30 `update` (estimates), 11 `estimate`, 4 `lesson`. The librarian added 3 entries (synthesis), so 48 entries in all.
- Marks: 38 entries `applied` (2 of them `near`, 3 `librarian: synthesis`); the 10 `update` entries of Case 899 carry `superseded_by` and no `applied`, as the handoff says (no line of Case 899 changes a page). None `failed`, `exists` or `merged`. The record `decision-case-899` under `decisions` is marked `incomplete: [context, problem]`.
- `guppi generate` printed 58 pages written or changed for `0327` and 0 for `2312`.
- Pages created (32): decisions 27 (`decision-case-898`, `898.1`–`898.3`, `899`, `899.1`–`899.10`, `900`, `900.1`–`900.5`, `901`, `901.1`–`901.5`; the 11 pages of Case 899 born superseded and archived in this run); lessons 4 (`lesson-plugin-cli-withholds-approval-of-a-long-plan`, `lesson-sprint-open-asks-no-goal-of-a-new-project`, `lesson-plugin-install-hooks-of-the-copy-run-at-once`, all `new`; `lesson-orchestration-retyped-a-ratification-line`, `clustered`); insights 1 (`insight-orchestration-writes-from-its-own-reading`, `open`, severity 2).
- Pages updated (26): estimates 20 (the ten of Case 898 — `method` set, `estimate-clean-branch-ships-neutral-texts` also its Criterion replaced and `failed → pending`; the five of Case 900 — defer retired, read `passed`; the five of Case 901 — Criterion replaced, set `pending` and read `passed`); rules 3 (`rule-git-context`, `rule-guppi-package`, `rule-plugin-install`, `draft → built` by the cascade); lessons 1 (`lesson-orchestration-claimed-a-reading-before-taking-it`, `new → clustered`); decisions 2 (`decision-case-862` superseded by 900.1, 900.3–900.5; `decision-case-885` superseded by 900.2; both archived).
- The handoff's instructions, checked: `rule-sprint-close`, `rule-case-protocol` and `rule-materialize` stand `built`; the five Estimates of Case 901 stand `passed`; `deferred_by` is gone from the five Estimates of Case 900; `estimate-close-commits` and `estimate-spec-write-writes-a-defer` keep `decision-case-885` in `deferred_by`; `rule-clean-branch` keeps `decision-case-893.1` and `rule-guppi-package` keeps `decision-case-834` and `decision-case-848`.
- This run ticked 30 boxes of `vault/raw/2026-10-29/0327/spec.md` (15 `update` lines of 898 and 900, 5 `update` lines of 901, 10 `read` lines of 900 and 901). One task line stays unticked: `read estimate-clean-branch-ships-neutral-texts`. No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` printed `13 page(s) moved`: `decision-case-862`, `decision-case-885`, `decision-case-899` and `decision-case-899.1`–`899.10`, into `vault/archive/plugin/2026-10-29/0327/decisions/`. `guppi render` printed nothing and changed no file of its 32 paths. `guppi sprint` and `guppi glossary` left their files unchanged. `guppi backlog`: 16 items → 12 (the five Estimates of Case 900 gone; `insight-orchestration-writes-from-its-own-reading` added).
- `guppi archive` printed `raw/2026-10-28/2312 → archive/plugin/2026-10-28/2312/raw`; `raw/2026-10-29/0327` is the session of the run and stays; `raw/2026-10-14/1907` holds no `ledger.md`, so it is no unit. No `pending` Estimate's `method` names the archive step.
- Index check: `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 51 lines, for the 4 lesson entries; no other `create` entry but the Insight of the synthesis. `lesson-sprint-open-asks-no-goal-of-a-new-project` marked `near: lesson-hi-fails-outside-a-git-repository` (both: what an install from the clean version leaves undone before the first `/hi`). `lesson-plugin-install-hooks-of-the-copy-run-at-once` marked `near: lesson-hooks-stop-payload` (that line records that a hook added to `settings.json` fires in the same session).
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 51 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 10 lines.
  - `lesson-plugin-cli-withholds-approval-of-a-long-plan` — none: no line names the size of the plan file or the approval of a plan in the CLI; `lesson-hooks-exitplanmode-payload` is about the payload of `ExitPlanMode`.
  - `lesson-sprint-open-asks-no-goal-of-a-new-project` — none: no line names the setup skill of `rule-morph` or the goal question of the opening Case; `lesson-hi-fails-outside-a-git-repository` is a missing `git init`.
  - `lesson-plugin-install-hooks-of-the-copy-run-at-once` — none: a fact of Claude Code; `lesson-hooks-stop-payload` records the same pick-up of `settings.json` within its payload facts, a knowledge line and no shared cause of an error.
  - `lesson-orchestration-retyped-a-ratification-line` — joined `lesson-orchestration-claimed-a-reading-before-taking-it` in the new `insight-orchestration-writes-from-its-own-reading`: both are the main agent writing what a source of record holds from its own reading of it. No `addressed_by`; the Insight is born `open`.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (pending) — `rule-clean-branch` (draft) — read by the unticked `read estimate-clean-branch-ships-neutral-texts` of the Spec of 0327; its `method`: by hand, after the librarian's run of the session that replaces this Criterion, with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty temporary folder, each sentence read whole. This run: the Criterion replaced by `decision-case-898.1` after the L1 reading `failed`; `guppi render` printed nothing; no step ran `guppi ship`; `git tag --merged HEAD` prints `prod-0.2.0`, `prod-1`, `prod-2`; the commit of this run comes after this brief.
- `estimate-close-commits` (pending, `deferred_by` case 885) — `rule-close` (draft) — by its `method`: `test_render.py -k paths`, then by hand after the librarian's run of the next session whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close`: `git log`, `git status` and the report. This run: `guppi render --paths` lists 32 paths, none modified before the close; the close commit of this run comes after this brief.
- `estimate-case-build-goes-on-after-a-live-compaction` (pending) — `rule-case-build` (draft) — by its `method`: by hand, after the first compaction of a `case-guppi` in a working session; not seen in `git log`, the ledger or the handoff of 0327.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (pending) — `rule-case-build` (draft) — by its `method`: after the first Case built under the Render of `rule-case-build` that names a test over a live file; not seen in the handoff or the ledger of 0327.
- `estimate-orchestration-shows-the-built-case` (pending) — `rule-orchestration` (draft) — by its `method`: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` under the new Render; not seen in the handoff or the ledger of 0327.
- `estimate-orchestration-signs-items-taken-together` (pending) — `rule-orchestration` (draft) — by its `method`: after the first batch taken up together in Plan Mode in which a summary carries a line `Other Case`; not seen in the handoff or the ledger of 0327.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen in the ledger of 0327.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode; not seen in the handoff or the ledger of 0327.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` that leaves a conflicted page; not seen.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: `test_ship.py`, then by hand after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` of a commit of `plugin`, before the close of the sprint; the person's answer at the close when no such run comes.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: by hand, in a session of the sprint `plugin` before its close: the clean version installed as a plugin into an empty project, `/guppi:install`, `/hi`.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: by hand, a pull request from a second account read on GitHub, in a session of the sprint `plugin` before its close.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- `incomplete`: the record `decision-case-899` under `decisions` of the yaml of 0327 lacks `context` and `problem`; the page was written without them and archived as superseded.
- `near`: `lesson-sprint-open-asks-no-goal-of-a-new-project` → `lesson-hi-fails-outside-a-git-repository`; `lesson-plugin-install-hooks-of-the-copy-run-at-once` → `lesson-hooks-stop-payload`.
- No entry `failed`, no entry `unparsed`. No Estimate stands `failed` after `generate`; the L1 reading of `estimate-clean-branch-ships-neutral-texts` was `failed`, and the `update` of 898.1 set it `pending`.
- `decision-case-885` moved to `vault/archive/plugin/2026-10-29/0327/decisions/` by `guppi cleanup` as superseded by 900.2, while `estimate-close-commits` and `estimate-spec-write-writes-a-defer` still name it in `deferred_by` and `backlog.md` lists both as deferred.
- No stale defer and no MOC candidate printed by any step. `guppi generate`, `cleanup`, `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Lint (`guppi check`, exit 1, 9 lines): 8 pages with `core: true` that stand `draft` (`entity-sprint`, `rule-case-build`, `rule-close`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`); `estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`.
- Read outside what the frame says the job needs: none.

## Next session

### Cases

- The Claude Code CLI withholds the approval of a plan of 15 KB, so a Spec cannot be approved there: how GUPPI keeps the plan file short enough, or approves the Spec another way (L42; handoff, For the next session).
- The opening of the first sprint of a new project asks nothing of what the project builds: the setup skill of `rule-morph`, or the questions of `rule-skill-sprint-open` (L43; handoff, For the next session).
- The hooks of the settings that `/guppi:install` copies run in the install session itself, build `.guppi/.venv` before `uv sync` and fail after a rollback: whether the install keeps them from running (L44; handoff, For the next session).
- `PLAIN_SPRINTS = ("migration", "plugin")` in the shipped `.guppi/guppi/caseid.py`, left to a Case of its own by Case 898; it stands in no backlog (handoff, For the next session).
- The fallback paths in `subagent` of `.guppi/guppi/casecheck.py` and in `example` of `.guppi/tests/test_case_schema.py`, with `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-example-passes-the-check` that promise their removal; they stand in no backlog (handoff, For the next session).
- The `method` of `estimate-close-commits` waits for "the next session" and needs a rewording by the yardstick of Case 898 (handoff, For the next session).
- Seven Estimates left Case 899 and wait under the defer of `decision-case-893.1`: `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-glossary-terms-defined`, `estimate-ask-query-before-a-create`, `estimate-compact-recall-reloads` (handoff, For the next session).
- The milestone line of `rule-clean-branch` and `estimate-sprint-plugin-ci-writes-a-clean-branch` was left for later; its reading waits for the owner's push of `plugin` and a tag `prod-x.y.z` (handoff, For the next session).
- Defect: `decision-case-885` stands in `vault/archive/` while `estimate-close-commits` and `estimate-spec-write-writes-a-defer` name it in `deferred_by` (from `guppi cleanup` and the frontmatter of the two pages).

### Work

- The reading of `estimate-clean-branch-ships-neutral-texts`, the unticked `read` box of `vault/raw/2026-10-29/0327/spec.md`: its moment, the librarian's run of 0327, is this run; `git tag --merged HEAD` prints `prod-0.2.0`, `prod-1`, `prod-2`.

### Ask the person

- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1792 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1, 9 lines (Flags).
- Files under `vault/wiki/` by folder (`ls`): decisions 331, entities 6, estimates 314, insights 12 (11 pages and `schema.yaml`), lessons 56 (55 pages — 50 `new`, 5 `clustered` — and `schema.yaml`), rules 87. Markdown files under `vault/archive/`: 2927.
