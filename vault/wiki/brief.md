# Brief — 2026-10-17, librarian of session 0027

## Where things stand

- Session 0027 of the sprint `plugin`. Cases ratified: 875, 876, 877 (877.1, 877.2) (handoff).
- Code: `.guppi/guppi/pages.py` (`has_no_parent`), `.guppi/guppi/glossary.py` (`group_of` imports it), `.guppi/guppi/lint.py` (`GUPPI_TEST`, `names_a_moc_form(method, top)`, `check_method`), `.guppi/guppi/prespec.py` (`plan_parent`, `form_finding`); tests in `.guppi/tests/test_lint.py` and `.guppi/tests/test_prespec.py`. `guppi test` 1750 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- The session's readings at Retro: `estimate-lint-checks-the-method` passed (L57), `estimate-prespec-catches-a-method-without-a-form` passed (L58). One lesson, L59 `lesson-ratified-defer-only-case-wants-its-fence-in-the-reply` (handoff, ledger).
- `guppi materialize` printed `written with 59 entries` for `vault/raw/2026-10-17/0027/materialize.yaml` and `extended with 0 entries` for the yaml of `2104`. The ledger has 59 lines; the yaml holds one entry for each, lines 1–59, plus 5 items under `decisions`. Kinds: 53 `update` (17 rules, 36 estimates), 3 `defer` (`rule-clean-branch`, `rule-ledger-write`, `rule-orchestration`, each marked `exists`), 2 `estimate`, 1 `lesson`. Every entry and every decision item is marked `applied` (64 marks); none `failed`, `incomplete`, `near` or `merged`; `unparsed: []`. The yaml of `2104` gained three `superseded_by` marks (lines 37 and 38, the decision item of 873).
- Pages created (6): decisions 5 (`decision-case-875`, `decision-case-876`, `decision-case-877`, `decision-case-877.1`, `decision-case-877.2`), lessons 1 (`lesson-ratified-defer-only-case-wants-its-fence-in-the-reply`).
- Pages updated: rules 20 (17 updates; `rule-clean-branch` deferred by 875, `rule-ledger-write` and `rule-orchestration` deferred by 876), estimates 36 (34 by Case 875 and 2 by Case 877; two of them read `passed` at Retro), decisions 4 (`decision-case-874` superseded by 875, `decision-case-836` and `decision-case-863` by 876, `decision-case-873` by 877.1; all four archived by the cascade). `guppi generate` printed 66 pages for `0027` and 0 for `2104`. No page changed its status by the cascade.
- The handoff's instructions, checked: `decision-case-836` and `decision-case-863` went `superseded`, then archived; `rule-guppi-package` keeps `deferred_by: decision-case-834, decision-case-848`; `estimate-clean-branch-ships-neutral-texts` left `backlog.md` and `rule-clean-branch` entered it; `rule-estimates-schema` left `backlog.md`; `vault/raw/2026-10-17/0027/spec.md` holds one heading `## Case 876` (line 536).
- This run ticked 59 boxes of `vault/raw/2026-10-17/0027/spec.md` (56 by `generate`, 3 render boxes by `guppi render`). No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` moved 4 pages into `vault/archive/plugin/2026-10-17/0027/decisions/`: `decision-case-836`, `-863`, `-873`, `-874`. `guppi render` changed `.claude/agents/librarian-guppi.md`, `.claude/skills/retro/SKILL.md` and `vault/wiki/estimates/schema.yaml`. `guppi sprint` changed one line of `vault/wiki/sprint.md` (the item `rule-clean-branch` now carries `decision-case-875`). `guppi glossary` changed nothing. `guppi backlog`: 13 → 14 items; `rule-clean-branch`, `rule-ledger-write` and `rule-orchestration` joined it; `rule-estimates-schema` and `estimate-clean-branch-ships-neutral-texts` left it.
- `guppi archive` moved `raw/2026-10-16/2104` into `archive/plugin/2026-10-16/2104/raw`; `raw/2026-10-17/0027`, the session of this run, stays.
- Index check: the yaml holds one `create` that is not an Estimate, the lesson. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 43 lines. No line names the same cause; no entry merged or marked `near`.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 43 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 8 lines.
  - `lesson-ratified-defer-only-case-wants-its-fence-in-the-reply`: none — no index line names `deferred_section` of `.guppi/guppi/ratified.py` reading a full Case whose lines are all `defer` as a short-form Case; `lesson-spec-write-skips-the-reply-that-answers-a-refusal` names the same hook with another cause (`stop_hook_active`). The lesson stays `new`.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (pending) — `rule-clean-branch` (draft) — by `read` at line 404 of `vault/raw/2026-10-17/0027/spec.md`; by hand, after the librarian's run of the session that set the `method` (this run), with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty folder, each sentence read whole, the Criterion sentences of shipped Estimates true only in GUPPI listed. This run: no step ran `guppi ship`; `git tag --merged HEAD --list 'prod-*'` prints `prod-0.2.0`, `prod-1`, `prod-2`.
- `estimate-close-commits` (pending) — `rule-close` (draft) — by its `method`: `test_render.py -k paths`, then by hand after the librarian's run of the next session, whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close`: `git log`, `git status` and the report in the transcript. This run: `rule-close` and `.claude/agents/librarian-guppi.md` last changed in `2981db5b` (librarian of 2104); `guppi render` wrote `.claude/agents/librarian-guppi.md`, `.claude/skills/retro/SKILL.md` and `vault/wiki/estimates/schema.yaml`; `guppi render --paths` printed 32 paths; the close commit of this run comes after this brief.
- `estimate-clean-branch-writes-the-session-files` (pending) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then by hand after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z` in the history of HEAD: an install in an empty folder with no git, `/hi` until `git init -b main`, the next `/hi`, and the three `--check` commands. `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-case-build-reads-the-code-it-states` (pending) — `rule-case-build` (draft) — by its `method`: by hand, after the first `/pre-spec` of a session whose Cases `case-guppi` built with `.claude/agents/case-guppi.md` rendered from the new Render. Seen: `case-guppi.md` was last rendered in `2981db5b` (librarian of 2104), and session 0027 ran `/pre-spec` over Cases built by `case-guppi` (handoff, Notes).
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (pending) — `rule-case-build` (draft) — by its `method`: after the first Case built under the Render of `rule-case-build` that names a test over a live file which changes a reader in code and the text it reads, or a test or the code of a check and a live file the test reads; not seen in the handoff or the ledger of 0027.
- `estimate-case-build-reads-no-sibling-file-mid-send` (pending) — `rule-case-build` (draft) — by its `method`: after the first send of two or more Cases to `case-guppi` at once under the new Render; not seen in the handoff or the ledger of 0027.
- `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` (pending) — `rule-orchestration` (draft) — by its `method`: after the first such send under the new Render of `rule-orchestration`; not seen.
- `estimate-orchestration-shows-the-built-case` (pending) — `rule-orchestration` (draft) — by its `method`: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` under the new Render; not seen.
- `estimate-orchestration-signs-items-taken-together` (pending) — `rule-orchestration` (draft) — by its `method`: after the first batch in Plan Mode under the new Render in which a summary carries a line `Other Case`; not seen.
- `estimate-git-context-offers-git-init` (pending, `deferred_by` case 862) — `rule-git-context` (draft) — by its `method`: by hand after the librarian's run, an install into an empty folder with no git. This run: no install.
- `estimate-plugin-install-offers-to-install-uv` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install from a terminal with no `uv`. This run: no install.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install offline with an empty cache of `uv`. This run: no install.
- `estimate-guppi-package-is-ready-after-the-install` (pending, `deferred_by` case 862) — `rule-guppi-package` (draft) — by its `method`: after a tag `prod-x.y.z`, an install in an empty project with `uv`, `/hi`, and the person's answer.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: `test_ship.py`, then a run of `prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: in a session of the sprint before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a pull request from a second account, before the close.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` after the session that writes `README.md`, before the close.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen: L59 carries no `addressed_by`, Case 875 updates `rule-guppi-package` (two Cases in `deferred_by`) with no `supersedes`, and `hooks` and `case-build` stand in `tags.md`.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge leaves a conflicted page; `git log --merges` prints none.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen in the handoff of 0027.

## Flags

- Lint (`guppi check`, exit 1, 11 lines): draft pages with `core: true` — `entity-sprint`, `rule-case-build`, `rule-close`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode` (ten).
- Lint: `method` — `estimate-harness-make-runs-in-both-shells` (the Makefile has no target with).
- No entry `incomplete`, `failed`, `near` or `unparsed`. No failed Estimate. No MOC candidate. No contradiction found.
- Defers: each `deferred_by` on a live page names a live Decision page (616, 793, 834, 838, 839, 848, 862, 875, 876). `backlog.md` counts `rule-work-mode` put off in 31 sessions, `rule-orchestration` in 8, `rule-clean-branch` in 5.
- The `ratified` Stop hook and the case-file check clash on a full Case whose lines are all `defer` (Case 876); worked around by showing the Case again in the short form (handoff, Observations; lesson L59).
- One `/pre-spec` finding on the context of Case 877 was fixed after the confirmation run of `ask-guppi`; that fix has no confirmation (handoff, Notes).
- The bash guard refused a heredoc whose body held a backslash; the tests changed by Edit instead (handoff, Observations).
- Read outside the job: a Grep of `876` over `vault/raw/2026-10-17/0027/spec.md`, beyond its unticked lines, for the handoff's instructions to the librarian, which asked to check that the Spec holds Case 876 once.

## Next session

### Cases

- The clash of the `ratified` hook and the case-file check on a full Case whose lines are all `defer`: which of the two changes (handoff, For the next session).
- The sentences inside the `## Criterion` of shipped Estimates true only in the repository of GUPPI, put off by Case 875 on `rule-clean-branch`, listed by the next reading of `estimate-clean-branch-ships-neutral-texts` (handoff, For the next session).
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, put off again; ten draft pages with `core: true` still stop every build of `prod` (handoff, For the next session).

### Work

- `estimate-clean-branch-ships-neutral-texts` (its `read` box at line 404 of `vault/raw/2026-10-17/0027/spec.md`).
- `estimate-close-commits`.
- `estimate-clean-branch-writes-the-session-files`.
- `estimate-case-build-reads-the-code-it-states`.

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1750 passed, 6 skipped, 1 deselected (exit 0).
- `uv run --project .guppi guppi check`: 11 lines (exit 1), as in Flags.
- Pages (`.md`) under `vault/wiki/`: decisions 231, estimates 304, rules 86, lessons 44, insights 8, entities 5. Under `vault/archive/`: 2836, after `guppi archive`.
