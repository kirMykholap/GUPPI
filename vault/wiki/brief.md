# Brief — 2026-10-16, librarian of session 1712

## Where things stand

- Session 1712 of the sprint `plugin`. Cases ratified: 856 (856.1, 856.2, 856.3), 857, 859, 860, 861; short defers 862 and 863. Case 858 was ratified, then taken back by Case 863 (handoff).
- Code: `.guppi/guppi/render.py` gets `--paths`, which prints each file the render writes and writes nothing; it is mutually exclusive with `--check` and `--sync`. Three new tests in `.guppi/tests/test_render.py`. The dirty `plugin/skills/install/SKILL.md` left by the librarian of session 0342 is committed with the work. `guppi test` 1722 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- The session's readings: L1 (`estimate-hi-no-read-calls`, passed, at `/hi`). Lessons L24, L25, L26 (handoff).
- `guppi materialize` printed `written with 26 entries` for `vault/raw/2026-10-16/1712/materialize.yaml` and `extended with 0 entries` for the yamls of `0104` and `0342`. The yaml holds 26 entries for the 26 lines of the ledger and 2 of the synthesis, 28 in all: 1 `estimate`, 16 `update`, 1 `delete`, 5 `defer` (each marked `exists`), 3 `lesson`, and the 2 `update` entries of the synthesis. 27 are marked `applied`; the entry of line 15 (Case 858) is marked `superseded_by: 863` and was not applied. One entry is marked `near`; none `failed`, `incomplete` or `merged`; `unparsed: []`.
- The ledger has 26 lines; the yaml has an entry for each of them.
- Pages created (14): decisions 11 (856, 856.1, 856.2, 856.3, 857, 858, 859, 860, 861, 862, 863), lessons 3. Pages updated: rules 5 (`rule-rules-schema` by 856.1 and 856.3, `rule-entities-schema`, `rule-ratification`, `rule-skill-sprint-close`, `rule-close`), estimates 14 (one reading, nine updates, four defers by Case 862), insights 1 (`insight-case-build-claims-what-code-does-without-reading-it`: one more child, severity 2 → 3), decisions 5 (828, 829, 833, 849 and 855 superseded, 855 also deferred by 863; `decision-case-858`, created this run, superseded by 863). Pages deleted: estimates 1 (`estimate-skill-sprint-close-migration-merged-into-main`). The cascade set `rule-close` and `rule-rules-schema` `built` → `draft`. `guppi generate` printed 40 pages for `1712` and 0 for `0104` and `0342`.
- This run ticked 21 boxes of `vault/raw/2026-10-16/1712/spec.md` (16 by `generate`, 5 render boxes after `guppi render`) and the `read` box of `estimate-hi-no-read-calls` in `vault/raw/2026-10-16/0342/spec.md`. It marked the entry of line 15 of `0342` (Case 855) `superseded_by: 859` and the entry of line 13 of `0104` `superseded_by: 860`. No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` moved 7 pages into `vault/archive/plugin/2026-10-16/1712/`: `decision-case-828`, `-829`, `-833`, `-849`, `-855`, `-858` and `estimate-skill-sprint-close-migration-merged-into-main`. `guppi render` changed `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml`, `vault/wiki/ratification.md` and `.claude/agents/librarian-guppi.md`. `guppi sprint` and `guppi glossary` changed nothing. `guppi backlog`: `rule-rules-schema`, `estimate-clean-branch-writes-the-session-files`, `estimate-guppi-tests-green` and `estimate-harness-pipeline` left it; `estimate-git-context-offers-git-init`, `estimate-guppi-package-is-ready-after-the-install`, `estimate-plugin-install-offers-to-install-uv` and `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` joined it.
- The handoff's instructions: line 15 (Case 858) did not change `decision-case-855`; its entry stands `superseded_by: 863`, and `decision-case-858` was written and archived as superseded. Case 859 retired the defer of 855 on `estimate-clean-branch-writes-the-session-files`, which holds no `deferred_by` now; the cascade archived `decision-case-855`. `generate` took the defer of Case 863 on that page as a History line `2026-10-16 deferred · [[decision-case-863]]` and a log line; it wrote no `deferred_by` field. After the run the page stands at `vault/archive/plugin/2026-10-16/1712/decisions/decision-case-855.md` with `status: archived`, `superseded_by: decision-case-859`, `defer: estimate-clean-branch-writes-the-session-files`, and that History line; `backlog.md` has no line for it. `estimate-page-schemas-one-file-per-rule` keeps `deferred_by: decision-case-829` and stands in `backlog.md`. Both `replace` pairs of 856.1 and 856.3 on `rule-rules-schema` were applied. The close commit uses the four fixed paths, run with the Bash tool.
- `guppi archive` printed nothing and moved no unit. It does not walk `raw/2026-10-16/1712`, the session of this run, or `raw/2026-10-16/0104` and `raw/2026-10-16/0342`, dated today; `raw/2026-10-14/1907` holds no `ledger.md`.
- Index check: the yaml holds no `create` entry but the three `lesson` entries; they were compared by the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 54 lines. `lesson-case-build-states-a-predicate-wider-than-the-code` is marked `near: lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read`. No entry was merged.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 54 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 8 lines.
  - `lesson-case-build-states-a-predicate-wider-than-the-code` joined `insight-case-build-claims-what-code-does-without-reading-it` (status `open`, kept): a claim about what a function decides, made without reading the whole function.
  - `lesson-case-build-leans-on-a-precedent-it-did-not-read`: none; its cause is the form of a precedent copied without its Problem. The nearest line, `insight-case-build-recommends-without-reading-the-governing-rule`, names an option built from the item's own words.
  - `lesson-case-build-states-what-a-past-decision-did-from-its-effect-on-one-page`: none; its cause is the reach of a past Decision judged from one page. No line of either Grep names a claim about a past Decision.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (pending) — `rule-clean-branch` (draft) — by `read` at line 111 of `vault/raw/2026-10-16/1712/spec.md`; by hand, after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty folder, each sentence read whole. This run: Case 856.1 rewrote the sentences of `rule-rules-schema`, `rule-entities-schema` and `rule-ratification`, and the render wrote `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml` and `vault/wiki/ratification.md`; no step ran `guppi ship`; `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-rules-schema-checked` (pending) — `rule-rules-schema` (draft) — by `read` at line 208 of `vault/raw/2026-10-16/1712/spec.md`; `test_schemas.py -k rules`, then by hand after the librarian's run of the session that set the `method`: the live `vault/wiki/rules/schema.yaml` and `guppi check`. This run: the render rewrote `vault/wiki/rules/schema.yaml`; `guppi check` printed 11 lines, its lines on `wiki/rules/` are `status: a page with core: true that is draft`, none a `schema` finding.
- `estimate-close-commits` (pending) — `rule-close` (draft) — by `read` at line 274 of `vault/raw/2026-10-16/1712/spec.md`; `test_render.py -k paths`, then by hand after the librarian's run of the next session, whose agent file holds the new Render of `rule-close`. This run: the render wrote the new Render into `.claude/agents/librarian-guppi.md`; this run's commit took the four fixed paths.
- `estimate-clean-branch-writes-the-session-files` (pending) — `rule-clean-branch` (draft) — by `read` at line 335 of `vault/raw/2026-10-16/1712/spec.md`; `test_ship.py -k skeleton`, then by hand after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z`: an install in an empty folder with no git, `/hi` until `git init -b main`, the next `/hi`, and the three `--check` commands over the copy. This run: no step ran `guppi ship`; `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-git-context-offers-git-init` (pending, `deferred_by` case 862) — `rule-git-context` (draft) — by `read` at line 124 of `vault/raw/2026-10-16/0342/spec.md`; by hand after the librarian's run: an install into an empty folder with no git. This run: no install session.
- `estimate-plugin-install-offers-to-install-uv` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by `read` at line 279 of `vault/raw/2026-10-16/0342/spec.md`; by hand after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install from a terminal with no `uv`. This run: no install session.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by `read` at line 378 of `vault/raw/2026-10-16/0342/spec.md`; by hand after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install offline with an empty cache of `uv`. This run: no install session.
- `estimate-guppi-package-is-ready-after-the-install` (pending, `deferred_by` case 862) — `rule-guppi-package` (draft) — by `read` at line 314 of `vault/raw/2026-10-16/0342/spec.md`; by hand after a tag `prod-x.y.z`: an install in an empty project with `uv`, `/hi`, and the person's answer.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: `test_ship.py`, then a run of `prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: in a session of the sprint before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a pull request from a second account, before the close.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` after the session that writes `README.md`, before the close.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen: the ledger of 1712 holds three lessons and no Case that closes their cause.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge leaves a conflicted page; not seen in `git log`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen in the handoff of 1712.

## Flags

- `near`: `lesson-case-build-states-a-predicate-wider-than-the-code` → `lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read` (both now children of `insight-case-build-claims-what-code-does-without-reading-it`).
- Lint (`guppi check`, exit 1, 11 lines): draft pages with `core: true` — `entity-sprint`, `rule-close`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-ratification`, `rule-rules-schema`, `rule-skill-hi`, `rule-work-mode` (nine; seven before the run, `rule-close` and `rule-rules-schema` set `draft` by the cascade).
- Lint: `method` — `estimate-harness-make-runs-in-both-shells` (the Makefile has no target with), `estimate-page-schemas-one-file-per-rule` (says by hand while `estimate-entities-schema-checked` names a test file).
- Failed Estimates: none.
- The defer of Case 863 on `decision-case-855` stands only as a History line on a page the same run archived: the page has no `deferred_by`, and `backlog.md` does not list it. `vault/wiki/decisions/schema.yaml` says of `defer` that each target carries this page in `deferred_by`, and `deferred_by` is not among the fields it allows on a Decision page (this run, `generate` and `cleanup`).
- `estimate-page-schemas-one-file-per-rule` keeps `deferred_by: decision-case-829`, a page this run archived (handoff, as Case 861 sets it).
- Contradiction: the Context of `decision-case-855` says that Case 851 makes `/hi` go on to `/sprint-open`, while the ratified Case 851 ends that `/hi`; the correction of Case 858 was taken back (handoff).
- The new close command of Case 857 joins `git add` and `git commit` with `&&`, which Windows PowerShell 5.1 does not parse; the claim that the `$(...)` form runs in both shells was not checked in PowerShell (handoff, Observations).
- At /pre-spec ask-guppi read `decision-case-829`, `-833`, `-849` and `-855` and used their `defer` lists, beyond the reason `.claude/rules/search-leaves-out-decisions.md` asks for (handoff, Observations).
- Read beyond the frame: the frontmatter fields and one History line of the archived `decision-case-855` and the frontmatter fields of the five other Decision pages this run archived, to say what `decision-case-855` holds after the run; the handoff asked for it (Direct instructions to the librarian).

## Next session

### Cases

- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, was left for later again: the draft pages with `core: true` stop every build of `prod`, and the next tag after `prod-0.2.0` is open; `rule-guppi-package` and `rule-work-mode` in the backlog are two of them (handoff).
- Whether `rule-estimates-schema` and `names_a_moc_form` of `.guppi/guppi/lint.py` let a MOC with no parent name `guppi test` alone (the person's doubt on Case 861) (handoff).
- The Context of `decision-case-855` still says that Case 851 makes `/hi` go on to `/sprint-open`; Case 863 deferred it, and `rule-decisions-schema` allows no correction line (handoff).
- `estimate-page-schemas-one-file-per-rule` still needs a `method` that lint accepts; its `deferred_by` points at `decision-case-829`, which this run archived (handoff).
- Defect: a `defer` on a Decision page writes no `deferred_by`, and the cascade archived `decision-case-855` in the same run, so the defer of Case 863 reaches no `backlog.md` line (this run, `generate`, `cleanup`, `guppi backlog`).
- Defect: the close command of Case 857 joins two commands with `&&`, which Windows PowerShell 5.1 does not parse (handoff, Observations).

### Work

- `estimate-clean-branch-ships-neutral-texts` (its `read` box at line 111 of `vault/raw/2026-10-16/1712/spec.md`).
- `estimate-rules-schema-checked` (its `read` box at line 208 of `vault/raw/2026-10-16/1712/spec.md`).
- `estimate-clean-branch-writes-the-session-files` (its `read` box at line 335 of `vault/raw/2026-10-16/1712/spec.md`).
- Ledger line 15 (Case 858) was not applied: superseded by Case 863.

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1722 passed, 6 skipped, 1 deselected (exit 0).
- `uv run --project .guppi guppi check`: 11 lines (exit 1), as in Flags.
- Pages (`.md`) under `vault/wiki/`: decisions 209, estimates 299, rules 86, lessons 57, insights 7, entities 5. Under `vault/archive/`: 2768.
