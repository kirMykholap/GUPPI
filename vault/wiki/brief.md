# Brief — 2026-10-26, librarian of session 0118

## Where things stand

- Session 0118 of the sprint `plugin`. Cases ratified: 888, 889 (889.1, 889.2), 890 (890.1–890.4); short-form defer 891 (handoff).
- Code: `.guppi/guppi/generate.py` (`Vault.decision` writes the new page of a record with `superseded_by` as `superseded`, naming each slug by `take_superseded_by`), `.guppi/guppi/onward.py` (`cases_out`, `case_out`, `to_out`/`TO_OUT`, the third reason, `ONLY_THE_PERSON` reworded), `.guppi/guppi/casecheck.py` (`other_blocks` takes a Case of the plan built again as the store holds it), `.guppi/guppi/materialize.py` (docstring). Tests in `test_generate.py`, `test_onward.py`, `test_casecheck.py`. `guppi test` 1780 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L17–L24 all `passed`; no lesson (handoff, ledger).
- `guppi materialize` printed `written with 24 entries` for `vault/raw/2026-10-26/0118/materialize.yaml` and `extended with 0 entries` for the yaml of `2307`; the yaml of `2307` gained `superseded_by: [890.1, 890.3]` on its two `defer` entries of Case 887 and `superseded_by: [decision-case-890.1, decision-case-890.3]` on its record `decision-case-887`. The ledger has 24 lines; the yaml holds 22 ledger entries (lines 1–24 but 20 and 22, the readings of the two new Estimates, folded into their `create` entries of lines 8 and 11) and 10 items under `decisions`. Kinds: 12 `update` (6 rules, 5 estimates, 1 entity), 2 `create` (estimates), 2 `defer` (estimates, both marked `exists`), 6 `estimate`. All 22 entries and all 10 decision items are marked `applied`; none `failed`, `incomplete`, `near` or `merged`; `unparsed` is empty. The librarian added no entry.
- Pages created (12): decisions 10 (`decision-case-888`, `889`, `889.1`, `889.2`, `890`, `890.1`–`890.4`, `891`); estimates 2 (`estimate-case-check-takes-a-case-built-again-from-its-file`, `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`, both `passed` by their folded readings).
- Pages updated (16): rules 7 (`rule-page-generation`, `rule-decisions-schema`, `rule-prespec-onward`, `rule-case-check`, `rule-orchestration`, `rule-prespec`; `rule-spec-write` `draft → built` by the cascade); estimates 7 (`estimate-generate-writes-the-decision-page`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-prespec-onward-tells-the-loop-from-its-end`, `estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-prespec-gathers-the-answers-after-findings` — Criterion replaced and read `passed`; `estimate-spec-write-writes-a-defer` — put off by 891 and read `failed → passed`; `estimate-clean-branch-ships-neutral-texts` — put off by 891, `failed` kept); entities 1 (`entity-glossary`); decisions 1 (`decision-case-887`, superseded by 890.1 and 890.3, archived by the cascade). `guppi generate` printed 28 pages for `0118` and 0 for `2307`, nothing on stderr.
- The handoff's instructions, checked: `decision-case-887` was set `superseded` with `superseded_by: [decision-case-890.1, decision-case-890.3]`, then archived by the cascade (`log.md`); `rule-case-check` lost `deferred_by` whole; `rule-orchestration` has `deferred_by: [decision-case-884]` and stays in `backlog.md`. `estimate-spec-write-writes-a-defer` stands `passed` with `deferred_by: [decision-case-885, decision-case-891]`, and `guppi backlog` still lists it (put off in 4 sessions). `guppi render` changed `vault/wiki/decisions/schema.yaml`, `vault/wiki/orchestration.md` and `.claude/skills/pre-spec/SKILL.md`; `guppi glossary` changed the row Decision (status) of `vault/wiki/glossary.md`. No `replace` failed.
- This run ticked 25 boxes of `vault/raw/2026-10-26/0118/spec.md`; the Spec holds no unticked task line. No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` printed `1 page(s) moved`: `decision-case-887`, into `vault/archive/plugin/2026-10-26/0118/decisions/`. `guppi render` printed nothing. `guppi sprint` left `vault/wiki/sprint.md` unchanged. `guppi backlog`: 17 items → 17 (`rule-case-check` gone; `estimate-clean-branch-ships-neutral-texts` added; `rule-clean-branch` put off in 8 sessions, `estimate-spec-write-writes-a-defer` in 4).
- `guppi archive` printed `raw/2026-10-17/2307 → archive/plugin/2026-10-17/2307/raw`; `raw/2026-10-26/0118` is the session of the run and stays; `raw/2026-10-14/1907` holds no `ledger.md` (only `cases/` and `frontier.md`), so it is no unit.
- Index check: both `create` entries are Estimates, so no Grep of the index check ran.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 46 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 9 lines. The yaml holds no `lesson` entry.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (failed, `deferred_by` case 891) — `rule-clean-branch` (draft) — result (2026-10-17, /hi of 1805): `guppi ship --allow-draft` exit 0, ten core draft pages named; it fails on sentences true only in the repository of GUPPI. Read by its `method`: by hand, after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty folder, each sentence read whole. This run: no step ran `guppi ship`; `git tag --merged HEAD --list 'prod-*'` prints `prod-0.2.0`, `prod-1`, `prod-2`.
- `estimate-close-commits` (pending, `deferred_by` case 885) — `rule-close` (draft) — by its `method`: `test_render.py -k paths`, then by hand after the librarian's run of the next session whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close`: `git log`, `git status` and the report in the transcript. This run: `rule-close` and `.claude/agents/librarian-guppi.md` last changed in `6cb614d0`; `guppi render --paths` printed 32 paths, 3 of them modified before the close commit (`.claude/skills/pre-spec/SKILL.md`, `vault/wiki/decisions/schema.yaml`, `vault/wiki/orchestration.md`); the close commit of this run comes after this brief.
- `estimate-clean-branch-writes-the-session-files` (pending, `deferred_by` case 885) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then by hand after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z`: an install in an empty folder with no git, `/hi` until `git init -b main`, the next `/hi`, and the three `--check` commands. This run: no install.
- `estimate-git-context-offers-git-init` (pending, `deferred_by` case 862) — `rule-git-context` (draft) — by its `method`: by hand after the librarian's run, an install into an empty folder with no git, `/hi` three times. This run: no install.
- `estimate-plugin-install-offers-to-install-uv` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install from a terminal with no `uv`. This run: no install.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install offline with an empty cache of `uv`. This run: no install.
- `estimate-guppi-package-is-ready-after-the-install` (pending, `deferred_by` case 862) — `rule-guppi-package` (draft) — by its `method`: after a tag `prod-x.y.z`, an install in an empty project with `uv`, `/hi`, and the person's answer.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (pending) — `rule-case-build` (draft) — by its `method`: after the first Case built under the Render of `rule-case-build` that names a test over a live file which changes a reader in code and the text it reads; not seen in the handoff or the ledger of 0118.
- `estimate-case-build-reads-no-sibling-file-mid-send` (pending) — `rule-case-build` (draft) — by its `method`: after the first send of two or more Cases to `case-guppi` at the same time under the new Render; seen: the handoff of 0118, Observations, names Cases 889 and 890 built side by side in the loop after `/pre-spec` and a second pass that closed their clash.
- `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` (pending) — `rule-orchestration` (draft) — by its `method`: after the first send of two or more Cases at the same time under the new Render of `rule-orchestration`; seen, as above (handoff of 0118, Observations).
- `estimate-orchestration-shows-the-built-case` (pending) — `rule-orchestration` (draft) — by its `method`: at the Retro of the session that changes it, and after the first summary of `case-guppi` in Plan Mode with a line `Other Case` under that Render; not seen in the handoff or the ledger of 0118.
- `estimate-orchestration-signs-items-taken-together` (pending) — `rule-orchestration` (draft) — by its `method`: after the first batch of items taken up together in Plan Mode under the new Render in which a summary carries a line `Other Case`; not seen.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: `test_ship.py`, then a run of `prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: in a session of the sprint before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a pull request from a second account, before the close.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` after the session that writes `README.md`, before the close.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen whole: the ledger of 0118 holds no lesson; 890.3 takes up 887 on `rule-orchestration`, whose `deferred_by` held 884 and 887.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge leaves a conflicted page; `git log --merges` prints none.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen in the handoff of 0118.

## Flags

- Lint (`guppi check`, exit 1, 14 lines): draft pages with `core: true` — `entity-sprint`, `rule-case-build`, `rule-close`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode` (ten).
- Lint: `unread: failed` — `estimate-clean-branch-ships-neutral-texts`.
- Lint: `method` — `estimate-harness-make-runs-in-both-shells` (the Makefile has no target with).
- Lint: `ship` — `.guppi/tests/test_casecheck.py:2695` and `:2740`, `a reference to a case: Case 5`.
- Failed Estimates: `estimate-clean-branch-ships-neutral-texts` (put off by case 891).
- No entry `failed`, `incomplete`, `near` or `unparsed`. No MOC candidate.
- Defers: each `deferred_by` on a live page names a live Decision page; `decision-case-887` left every `deferred_by` it stood in.
- The handoff's Debt names five Estimates waiting for an install from a tag `prod-x.y.z`; each already carries `deferred_by` (891, 885 or 862) and stands in `backlog.md`, so Next session carries no proposal to defer them.
- Read outside the job: `git diff` of `vault/raw/2026-10-17/2307/materialize.yaml`, the earlier yaml, for Where things stand, to say what `guppi materialize` changed in it; the handoff did not ask for it.
- Read outside the job: the `status` and `superseded_by` lines of `vault/wiki/decisions/decision-case-887.md`, the text of a Decision page, to check the handoff's instruction that `decision-case-887` end superseded; the handoff asked for it.

## Next session

### Cases

- The frontier item C1 of the sprint (`rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`) stays the current milestone: the owner pushes `plugin` and a tag `prod-x.y.z`, and the CI run is read; the draft pages with `core: true` still stop a build of `prod` (handoff, For the next session).
- The growing context of `case-guppi`, put off on `rule-orchestration` by Case 884, stays open (handoff, For the next session).
- `estimate-clean-branch-ships-neutral-texts` (failed): its reading of 2026-10-17 lists sentences true only in the repository of GUPPI; put off by Case 891 into `backlog.md` (lint, handoff Debt).
- A defect: the new tests of `.guppi/tests/test_casecheck.py` at lines 2695 and 2740 hold `Case 5`, which the `ship` check of `guppi check` names as a reference to a case (lint).

### Work

- `estimate-case-build-reads-no-sibling-file-mid-send`: its event is seen in the handoff of 0118 (Cases 889 and 890 built side by side, a second pass).
- `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: its event is seen in the handoff of 0118, as above.

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1780 passed, 6 skipped, 1 deselected (exit 0).
- `uv run --project .guppi guppi check`: 14 lines (exit 1), as in Flags.
- Pages (`.md`) under `vault/wiki/`: decisions 300, estimates 311, rules 86, lessons 46, insights 9, entities 5. Under `vault/archive/`: 2892, after `guppi archive`.
