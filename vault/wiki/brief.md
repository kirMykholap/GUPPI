# Brief — 2026-10-30, librarian of session 1713

## Where things stand

- Session 1713 of the sprint `plugin`. Cases ratified: 927; 928; 929; 931; 932 (932.1–932.5); 934; 935 (935.1, 935.2). Cases 929, 931 and 932 were built again in the loop after `/pre-spec` and ratified again; Case 935 was born there. Cases 930 and 933 were dropped with no decision line (handoff).
- Code: `.guppi/guppi/materialize.py` (`drop` in `ITEM_KEYS`, `drops_criterion`, `lift_criterion`), `.guppi/guppi/generate.py` (`Generator.drop`), `.guppi/guppi/ratified.py` (docstring). Tests: `test_commands.py`, `test_generate.py` (seven `drop` tests), `test_materialize.py`, `test_ratified.py`. `guppi test` 1814 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L22–L28, all `passed`. Lessons: L29, L30 (handoff).
- `guppi materialize` printed `written with 30 entries` for `vault/raw/2026-10-30/1713/materialize.yaml` and `extended with 0 entries` for the yaml of `0304`. The ledger has 30 lines (`wc -l`); the yaml holds entries for lines 1–30, so every line is accounted for. Kinds: 18 `update`, 2 `create` (both estimates), 1 `defer`, 7 `estimate`, 2 `lesson`.
- Marks: 45 `applied` lines in the yaml; one `exists: true` (line 16, the `defer` of `rule-spec-capture`); no entry `failed`, `incomplete`, `near`, `merged` or `librarian`; `unparsed: []`.
- `guppi generate` printed 45 pages written or changed for `1713` and 0 for `0304`. `guppi cleanup` printed `6 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`.
- Pages created (18), from `git status`: decisions 14 (`decision-case-927`, `928`, `929`, `931`, `932`, `932.1`–`932.5`, `934`, `935`, `935.1`, `935.2`); estimates 2 (`estimate-plugin-install-sets-aside-the-files-of-the-project`, `estimate-morph-takes-in-the-set-aside-files`, both `pending`); lessons 2 (`lesson-orchestration-dispatch-named-a-case-of-the-same-wording-not-related`, `lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case`, both `new`).
- Pages updated (22), from `git status`: rules 9 (`rule-lint`, `rule-guppi-config`, `rule-guppi-package`, `rule-page-generation`, `rule-case-protocol`, `rule-plugin-install`, `rule-morph`, `rule-materialize`, `rule-spec-capture`); estimates 12 (9 by `update` entries, 7 by readings, 4 of them both); decisions 1 (`decision-case-897`, its child `897.3` archived, by `cleanup`).
- Archived (6, under `vault/archive/plugin/2026-10-30/1713/decisions/`): `decision-case-834`, `838`, `848`, `897.3`, `909`, `911`, each superseded by a Case of this session (927, 929, 929, 931, 934, 932.1). 18 created, 21 updated by `generate` and the 6 superseded decisions make the 45 pages `generate` printed.
- Cascade (log): `rule-guppi-config` and `rule-plugin-install` `built → draft`.
- Render wrote `guppi.toml` (`test = ["uv run --project .guppi pytest -q .guppi/tests"]`), `plugin/skills/install/SKILL.md` and `vault/wiki/case-schema.md` (`drop` among the update keys), as the handoff named.
- The handoff's instructions, checked in `git diff`: `rule-spec-capture` holds one `deferred_by`, `decision-case-934`, in place of `909`, and stays in `backlog.md`. `estimate-harness-make-runs-in-both-shells` took only its new `method` and stands `passed`; `guppi check` prints no `method` line for it. No entry of the yaml carries `drop`. The two entries of Case 935 on `rule-materialize` both applied.
- `backlog.md` went from 10 items to 6: `rule-guppi-package`, `rule-lint`, `rule-page-generation` and `rule-plugin-install` left it.
- This run ticked 28 boxes of `vault/raw/2026-10-30/1713/spec.md` (3 of them render boxes) and the `read` boxes of `estimate-search-leaves-out-decisions-in-every-agent`, `estimate-ask-opens-a-decision-only-for-a-finding` and `estimate-ask-finds` in `vault/raw/2026-10-30/0304/spec.md`. Six `read` boxes of the 1713 Spec stay unticked; the handoff named 34 boxes waiting (28 plus 6).
- Index check: the 2 `create` entries are Estimates and have no index; no Grep of a category ran for them.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 52 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 12 lines. The synthesis added no entry.
  - `lesson-orchestration-dispatch-named-a-case-of-the-same-wording-not-related` — none: its cause is the main agent's test of which Cases are related, which leaves out a Case of another subject that writes text one check reads; `insight-case-build-sibling-texts-unchecked-before-the-showing` is about sibling Cases on one subject built apart, which the main agent had named related.
  - `lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case` — none: its cause is that `orchestration.md` names no closer for a backlog item a Case defers again; `lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page` had a closer (`· sprint · defer`) the agent did not take.

## Readings due

- `estimate-guppi-config-runs-the-test-and-style-commands` — `pending`; target `rule-guppi-config` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/1713/spec.md` (Case 929): `test_commands.py`, then after the librarian's run that renders `guppi.toml` with the key `test` that names `.guppi/tests`, `guppi test`, `guppi style` and a Grep for `make test` and `make style`. This run: `guppi render` wrote `guppi.toml` with `test = ["uv run --project .guppi pytest -q .guppi/tests"]`.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`; target `rule-plugin-install` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.1): after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z` in the history of HEAD, an install by hand into three projects. This run: the librarian's run of 1713; `git tag --merged HEAD` prints `prod-0.2.0`; `guppi render` wrote `plugin/skills/install/SKILL.md`.
- `estimate-plugin-install-writes-guppi-into-an-empty-project` — `pending`; target `rule-plugin-install` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.3): `test_ship.py -k plugin_skill`, then after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z` in the history of HEAD, an install by hand into an empty project. This run: as above.
- `estimate-plugin-install-runs-no-hook-before-uv-sync` — `pending`; target `rule-plugin-install` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.4): after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z` in the history of HEAD, an install by hand into two empty projects. This run: as above.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.2): after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); read by its unticked `read` box in the 1713 Spec (Case 932.5): after the session whose Work Mode builds the setup skill of `rule-morph`, its step in `/hi` and in `/sprint-open`.
- `estimate-synthesis-clusters` — `pending`; target `rule-synthesis` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/0304/spec.md` (Case 920.4): after a librarian's run whose `materialize.yaml` holds at least two lesson entries, the yaml and the report. This run: the yaml held 2 `lesson` entries; the two Greps printed 52 and 12 lines; the synthesis added no entry and gave each lesson a line with none and why; the report names the two pages opened at synthesis.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.3): after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: no `lesson` entry carried `addressed_by`; the synthesis added no entry.
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — `pending`; target `rule-search-leaves-out-decisions` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 925.1): `test_grepguard.py`, then after the first `/pre-spec` once the librarian's run has rendered `.claude/settings.json`, each Read and Grep of `ask-guppi` on `vault/wiki/decisions/` refused. The handoff: the `/pre-spec` of 1713 came, its `ask-guppi` made no such call.
- `estimate-orchestration-states-a-subagent-fact-from-its-transcript` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 923): after the first reply of the main agent under the new Render that states what a subagent did. The handoff: the event came in 1713; Retro did not read it.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 924): after the `/pre-spec` of the first session whose `case-guppi` runs on the new Render. The handoff: the event came in 1713; Retro did not read it.
- `estimate-case-build-reads-the-code-it-states` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 926): after a `/pre-spec` of a session whose Cases `case-guppi` built on the new Render. The handoff: the event came in 1713; Retro did not read it.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.2): after a `case-guppi` builds a Case with a `create` without a `ref`.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); method: after a librarian's run whose `librarian-guppi.md`, when the run starts, holds the Render of `rule-close` with no limit of lines, the person's answer on the report. This run: `.claude/agents/librarian-guppi.md` is not modified (`git status`), and its Render of `rule-close` names no limit of lines; the report goes to `/handoff` after the commit.
- `estimate-guppi-package-is-ready-after-the-install` — `pending`; target `rule-guppi-package` (`draft`); method: after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z` in the history of HEAD, a clean copy by `guppi ship --allow-draft`, an install by the person at a stop of Work Mode, and the person's answer. This run: `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-orchestration-shows-the-built-case` — `pending`; target `rule-orchestration` (`draft`); method: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` naming a Case of the session under the new Render.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch taken up together under the new Render in which a summary carries a line `Other Case` naming a Case of the session.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes both.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); method: after a session whose ledger holds a lesson with the Case that closes its cause, a Case taking up a decision with more than one Case in `deferred_by`, and a lesson line declaring a new tag.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of `/sprint-open`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged into main by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: `test_ship.py`, then after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: in a session of the sprint before its close, a clean copy installed in an empty project and `/hi` typed.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`. Line 16 (`defer` of `rule-spec-capture`) carries `exists: true`. No failed Estimate.
- `guppi check`: 13 lines, exit 1 — 13 pages with `core: true` stand `draft`: `entity-sprint`, `rule-ask`, `rule-case-build`, `rule-close`, `rule-guppi-config`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-search-leaves-out-decisions`, `rule-skill-hi`, `rule-synthesis`, `rule-work-mode`. The handoff counted 14 lines before the work (12 such pages, the `backlog` line, the `method` line); `rule-guppi-config` went `built → draft` by the cascade of this run.
- The `## Debt` line of `estimate-harness-make-runs-in-both-shells` names an Estimate that stands `passed`; its `method` waits for "the Work Mode that builds this change", an event this run has not seen, so it has no line in Next session.
- Stale defer: `rule-work-mode` is put off in 31 sessions (`backlog.md`).
- No MOC candidate and no contradiction found.
- Read outside the frame: `git diff -U0 -- vault/wiki/decisions/decision-case-897.md` printed its `children` line and a History line, text of a Decision page; read to count the pages updated for Where things stand. No handoff asked for it.

## Next session

### Cases

- The milestone item of the clean branch, `rule-clean-branch` with `estimate-sprint-plugin-ci-writes-a-clean-branch`, was put off again: the owner's push of `plugin` and a tag `prod-x.y.z`, and the reading of the CI run it starts (handoff).
- `estimate-clean-branch-pages-hold-pointers-only-in-brackets` still reads by `guppi ship --review` into a folder with no flag, which exits 1 while a page with `core: true` stands `draft`; the person chose to leave it in Case 928 (handoff).
- Eleven Leaf rules still carry `## How it works`; once `drop` is live, a Case that touches one of them can remove the section (handoff).
- `orchestration.md` names no Frontier closer for a backlog item that a Case defers again with a new wording (L30, handoff).
- When the main agent judges which Cases of the session are related, a Case that writes text one check reads in the same way as another Case is not counted (L29, handoff).
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — defer into `backlog.md`: its `/pre-spec` came in 1713 but its session did not take its reading (handoff `## Debt`).
- `estimate-orchestration-states-a-subagent-fact-from-its-transcript` — defer into `backlog.md`: its event came in 1713 but its session did not take its reading (handoff `## Debt`).
- `estimate-case-build-reads-the-readers-of-a-changed-step` — defer into `backlog.md`: its event came in 1713 but its session did not take its reading (handoff `## Debt`).
- `estimate-case-build-reads-the-code-it-states` — defer into `backlog.md`: its event came in 1713 but its session did not take its reading (handoff `## Debt`).

### Work

- `estimate-guppi-config-runs-the-test-and-style-commands`
- `estimate-plugin-install-sets-aside-the-files-of-the-project`
- `estimate-plugin-install-writes-guppi-into-an-empty-project`
- `estimate-plugin-install-runs-no-hook-before-uv-sync`
- `estimate-synthesis-clusters`

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — After the agent writes a clean copy by `guppi ship --allow-draft` in the repository of GUPPI, and you, at a stop of Work Mode, add it as a catalogue, install `guppi`, type `/guppi:install` in an empty project, reopen Claude Code and type `/hi`: did the output of the install, the order of its steps, the files of the project and its `.guppi/.venv/` match the Criterion?
- `estimate-close-reports-the-run` — needs the person — Did the report that `/handoff` showed after the librarian's run of 2026-10-30 give each part the Criterion names — the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags, the lint total and each part another step of the frame sends to the report — and no test result and no list of files?

## Readings at the close

- `uv run --project .guppi guppi test`: 1814 passed, 6 skipped, 1 deselected, exit 0.
- `uv run --project .guppi guppi check`: 13 lines, exit 1 (the 13 `core: true` pages that stand `draft`, above).
- Pages under `vault/wiki/`: decisions 394, entities 5, estimates 324, insights 12, lessons 54, rules 86. Pages under `vault/archive/`: 2996.
