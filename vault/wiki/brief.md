# Brief — 2026-10-17, librarian of session 1805

## Where things stand

- Session 1805 of the sprint `plugin`. Cases ratified: 879 (879.1–879.4), 880 (880.1–880.21); Case 878 ratified, then retired whole by Case 880 (handoff).
- Code: `.guppi/guppi/ratified.py` (`defer_only(records, reply)`, `ratified_cases(records, reply)`); tests in `.guppi/tests/test_ratified.py`. `guppi test` 1756 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- The session's readings: L1 at `/hi` (`estimate-clean-branch-ships-neutral-texts` failed), L53 at the Work readings (`estimate-case-build-reads-the-code-it-states` passed), L54–L77 at Retro (23 passed, `estimate-spec-write-writes-a-defer` failed). One lesson, L78 `lesson-brief-lists-transcript-readings-under-work` (handoff, ledger).
- `guppi materialize` printed `written with 78 entries` for `vault/raw/2026-10-17/1805/materialize.yaml` and `extended with 0 entries` for the yaml of `0027`, which gained `superseded_by: [878.22, 880.21]` marks on its entries of Case 875. The ledger has 78 lines; the yaml holds 74 entries (lines 1–78 but 54, 64, 66 and 77, readings folded into the `create` entries of 880.1, 880.7, 880.9 and 880.20, whose pages stand `passed`) and 51 items under `decisions`. Kinds: 42 `update` (38 estimates, 4 rules), 22 `estimate`, 7 `create` (estimates), 2 `defer` (`rule-clean-branch`, both marked `exists`), 1 `lesson`. 51 entries and all 51 decision items are marked `applied`; the 23 entries of Case 878 carry `superseded_by` and no `applied`. `unparsed: []`; none `failed` or `merged`.
- Pages created (32): decisions 27 (`decision-case-879`, `879.1`–`879.4`, `decision-case-880`, `880.1`–`880.21`), estimates 4 (`estimate-spec-write-copies-a-built-defer-only-case`, `estimate-guppi-repository-remote-on-github`, `estimate-guppi-repository-keeps-the-development-project`, `estimate-guppi-repository-stops-in-the-merge-tasks`, all four `passed`), lessons 1 (`lesson-brief-lists-transcript-readings-under-work`, `new`). `guppi generate` also wrote the 23 Decision pages of Case 878 (`decision-case-878`, `878.1`–`878.22`), each `superseded`, and archived them.
- Pages updated: estimates 22 (19 by Case 880 and 3 by Case 879, each read at Retro, plus `estimate-clean-branch-ships-neutral-texts` by L1 and `estimate-case-build-reads-the-code-it-states` by L53); rules 3 (`rule-spec-write`, `rule-spec-capture` by 879.1; `rule-clean-branch` updated and put off again by 880.21, `deferred_by: decision-case-880.21`); entities 1 (`entity-guppi-repository`, three Estimates added, `draft → built` by the cascade); decisions 1 (`decision-case-875` superseded, then archived). `rule-spec-write` went `built → draft` by the cascade. `guppi generate` printed 82 pages for `1805` and 0 for `0027`.
- The handoff's instructions, checked: no entry of Case 878 is marked `applied`; the 23 Decision pages of Case 878 went `superseded` (878.1–878.9, 878.11–878.21 by their 880 successors, 878, 878.10 and 878.22 by 880.21) and stand under `vault/archive/plugin/2026-10-17/1805/decisions/`; `estimate-orchestration-asks-in-the-grill-me-shape` keeps its page (`passed`, unchanged by this run); `decision-case-875` went `superseded` and was archived, `rule-clean-branch` is put off by `decision-case-880.21` alone and `backlog.md` keeps its line (`put off in 6 sessions`); the reading of 880.21, the `guppi backlog --check` inside `guppi check`, printed no `backlog` line; the result of L1 on `estimate-clean-branch-ships-neutral-texts` carries the list of the Criterion sentences true only in GUPPI (33 Estimates named).
- This run ticked 52 boxes of `vault/raw/2026-10-17/1805/spec.md`, all by `generate`; the Spec holds no unticked task line. No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` printed `24 page(s) moved`: `decision-case-875` and the 23 Decision pages of Case 878, into `vault/archive/plugin/2026-10-17/1805/decisions/`. `guppi render` changed no file. `guppi sprint` changed one line of `vault/wiki/sprint.md` (the item `rule-clean-branch`). `guppi glossary` changed nothing. `guppi backlog`: 13 items before and after; only the count of `rule-clean-branch` changed, 5 → 6 sessions.
- `guppi archive` printed nothing and moved nothing: `raw/2026-10-17/0027` is dated the day of the run, and `raw/2026-10-17/1805` is the session of the run; both stay.
- Index check: the yaml holds no `create` outside estimates; the one lesson was checked. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 44 lines. No line names the same cause; the lesson is marked `near: lesson-hi-unread-sprint-reading-made-a-case-line`.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 44 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 8 lines.
  - `lesson-brief-lists-transcript-readings-under-work`: none — no index line names the brief putting under Work a reading whose `method` reads a transcript of an earlier session; `lesson-hi-unread-sprint-reading-made-a-case-line` names a gap in `rule-skill-hi` for an Estimate of the live sprint page, another cause; no Insight names the brief. The lesson stays `new`.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (failed) — `rule-clean-branch` (draft) — result (L1): `guppi ship --allow-draft` exit 0, ten core draft pages named; it fails on sentences true only in the repository of GUPPI in 10 rules, the purpose or method of 3 Estimates and the Criterion of 33 Estimates, with more doubtful. Read by its `method`: by hand, after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty folder, each sentence read whole, the Criterion sentences true only in GUPPI listed. This run: no step ran `guppi ship`; `git tag --merged HEAD --list 'prod-*'` prints `prod-0.2.0`, `prod-1`, `prod-2`.
- `estimate-spec-write-writes-a-defer` (failed) — `rule-spec-write` (draft) — result (L55): `pytest test_ratified.py -k defer` 24 passed, a bare reply refused with `not built and checked by case-guppi — dispatch it`; the by-hand part, a defer the person asks for, did not come in session 1805. Read by its `method`: `test_ratified.py -k defer`, then by hand a defer the person asks for.
- `estimate-close-commits` (pending) — `rule-close` (draft) — by its `method`: `test_render.py -k paths`, then by hand after the librarian's run of the next session whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close`: `git log`, `git status` and the report in the transcript. This run: `rule-close` and `.claude/agents/librarian-guppi.md` last changed in `6cb614d0`; `guppi render` changed no file; `guppi render --paths` printed 32 paths, none of them modified or untracked before the close commit; the close commit of this run comes after this brief.
- `estimate-clean-branch-writes-the-session-files` (pending) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then by hand after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z` in the history of HEAD: an install in an empty folder with no git, `/hi` until `git init -b main`, the next `/hi`, and the three `--check` commands. This run: no install; `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (pending) — `rule-case-build` (draft) — by its `method`: after the first Case built under the Render of `rule-case-build` that names a test over a live file which changes a reader in code and the text it reads, or a test or the code of a check and a live file the test reads; not seen in the handoff or the ledger of 1805.
- `estimate-case-build-reads-no-sibling-file-mid-send` (pending) — `rule-case-build` (draft) — by its `method`: after the first send of two or more Cases to `case-guppi` at once under the new Render; not seen in the handoff or the ledger of 1805.
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
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen: L78 carries no `addressed_by`, Case 880.21 takes up `rule-clean-branch` with one Case in its `deferred_by`, and `librarian` and `workflow` stand in `tags.md`.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge leaves a conflicted page; `git log --merges` prints none.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen in the handoff of 1805.

## Flags

- Lint (`guppi check`, exit 1, 14 lines): draft pages with `core: true` — `entity-sprint`, `rule-case-build`, `rule-close`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-spec-write`, `rule-work-mode` (eleven; `rule-spec-write` joined by the cascade of this run, after the failed reading of `estimate-spec-write-writes-a-defer`).
- Lint: `unread: failed` — `estimate-clean-branch-ships-neutral-texts`, `estimate-spec-write-writes-a-defer`.
- Lint: `method` — `estimate-harness-make-runs-in-both-shells` (the Makefile has no target with).
- Failed Estimates: `estimate-clean-branch-ships-neutral-texts` (L1), `estimate-spec-write-writes-a-defer` (L55).
- `incomplete`: the entries of 878.7, 878.9 and 878.21 (`criterion`), not applied since Case 880 retires them; the decision item `decision-case-878` (`context`, `problem`), its page written and archived.
- `near`: `lesson-brief-lists-transcript-readings-under-work` → `lesson-hi-unread-sprint-reading-made-a-case-line`.
- No entry `failed` or `unparsed`. No MOC candidate.
- Defers: each `deferred_by` on a live page names a live Decision page (616, 793, 834, 838, 839, 848, 862, 876, 880.21).
- Case 878.22, retired, still left a trace: `guppi generate` set `decision-case-875` superseded by `decision-case-878.22` before 880.21, and wrote the History line `defer by decision-case-875 superseded · [[decision-case-878.22]]` on `rule-clean-branch` and the matching line in `log.md`; `[[decision-case-878.22]]` now points into `vault/archive/`.
- The baseline red `backlog: vault/wiki/backlog.md differs from its sources` of `work.md` is gone from `guppi check` after this run (handoff, Observations).
- Read outside the job: `git diff` of `vault/raw/2026-10-17/0027/materialize.yaml`, the earlier yaml, for Where things stand, to say what `guppi materialize` changed in it; the handoff did not ask for it.

## Next session

### Cases

- `estimate-spec-write-writes-a-defer` (failed): read it again at the first short-form defer the person asks for, or change its `method` (handoff, For the next session).
- `estimate-clean-branch-ships-neutral-texts` (failed): the sentences true only in the repository of GUPPI its reading of L1 lists stand in 10 rules, the purpose or method of 3 Estimates and the Criterion of 33 Estimates (ledger L1).
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, put off again; the texts of the clean version the reading of L1 lists and the draft pages with `core: true` still stop every build of `prod` (handoff, For the next session).
- The rest of the Criterion rewrite, named in the put-off of 880.21 (handoff, For the next session).
- `estimate-close-commits`: its `method` needs a transcript, so no `/hi` closes it; a Case changes the `method` or defers it into `backlog.md`, since its session did not take its reading (handoff, For the next session and Debt; lesson L78).
- `estimate-clean-branch-writes-the-session-files`: defer it into `backlog.md`, since its session did not take its reading — an install by hand in an empty folder with no git, with a tag `prod-x.y.z` (handoff, Debt).
- Defect: a retired sub-case still acts — the `supersedes` of 878.22 superseded `decision-case-875` and wrote a History line naming `decision-case-878.22` on `rule-clean-branch`, though Case 880 retires Case 878 and no entry of it was applied (`git diff` of `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/log.md`, this run).

### Work

- none

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1756 passed, 6 skipped, 1 deselected (exit 0).
- `uv run --project .guppi guppi check`: 14 lines (exit 1), as in Flags.
- Pages (`.md`) under `vault/wiki/`: decisions 257, estimates 308, rules 86, lessons 45, insights 8, entities 5. Under `vault/archive/`: 2860, after `guppi archive`.
