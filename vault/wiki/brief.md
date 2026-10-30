# Brief — 2026-10-30, librarian of session 0304

## Where things stand

- Session 0304 of the sprint `plugin`. Cases ratified: 919 (919.1, 919.2); 920 (920.1–920.5); 921; 922; 923; 924; 925 (925.1–925.6); 926. The first `/pre-spec` sent Cases 921–926 back on 11 findings of `ask-guppi` and 5 lines of the check; Cases 924 and 926 were ratified a third time. Frontier item C1 was put off with no Case (handoff).
- Code: `.guppi/guppi/grepguard.py` runs on `Read` and `Grep` and refuses by `permissionDecision: deny` a `Read` or a `Grep` of `ask-guppi` whose path is `vault/wiki/decisions/` or lies in it. Tests: `.guppi/tests/test_grepguard.py`, `.guppi/tests/test_ship.py` (`live_code_lines` and two `live_code` tests), `.guppi/tests/test_render.py` (the pointer of a docstring moved into a bracket). `guppi test` 1803 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L1 and L2 at `/hi`; seven at Retro (L33–L39), all `passed`. No lesson (handoff).
- `guppi materialize` printed `written with 39 entries` for `vault/raw/2026-10-30/0304/materialize.yaml` and `extended with 0 entries` for the yaml of `2341`. The yaml holds 38 entries (lines 1–33, 35–39); the reading of line 34 (`estimate-clean-branch-tests-judge-the-live-code`, `passed`) is folded into the `create` entry of line 4. The ledger has 39 lines (`wc -l`), so every line is accounted for. Kinds: 26 `update`, 4 `create` (all estimates), 8 `estimate`, 0 `lesson`.
- Marks: 59 `applied` lines in the yaml; no entry `failed`, `incomplete`, `exists`, `near`, `merged` or `librarian`.
- `guppi generate` printed 61 pages written or changed for `0304` and 0 for `2341`. `guppi cleanup` printed `8 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`.
- Pages created (25), from `git status`: decisions 21 (`decision-case-919`, `919.1`, `919.2`, `920`, `920.1`–`920.5`, `921`, `922`, `923`, `924`, `925`, `925.1`–`925.6`, `926`); estimates 4 (`estimate-clean-branch-tests-judge-the-live-code`, `passed`; `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-search-leaves-out-decisions-refuses-ask-guppi`, `pending`).
- Pages updated (29), from `git status`: estimates 15; rules 9 (`rule-ask`, `rule-case-build`, `rule-clean-branch`, `rule-hook-registry`, `rule-orchestration`, `rule-search-leaves-out-decisions`, `rule-skill-hi` by entries; `rule-plugin-install`, `rule-synthesis` by the cascade alone); insights 4 (`insight-orchestration-writes-from-its-own-reading`, `insight-case-build-changes-a-step-without-reading-its-readers`, `insight-case-build-claims-what-code-does-without-reading-it`, `insight-ask-guppi-reads-a-decision-outside-its-frame`, each `actioned` with `addressed_by` `decision-case-923`, `924`, `926`, `925.1`); decisions 1 (`decision-case-893.1` `superseded` by `decision-case-920.5`).
- Archived by the cascade and `cleanup` (8, under `vault/archive/plugin/2026-10-30/`): `decision-case-893.1` (superseded); lessons `lesson-ask-guppi-read-a-decision-page-without-a-reason`, `lesson-prespec-ask-guppi-opened-a-decision-outside-its-frame`, `lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes`, `lesson-case-build-changes-a-step-without-reading-what-reads-it`, `lesson-case-build-judged-a-check-by-the-last-stretch-of-the-transcript`, `lesson-orchestration-claimed-a-reading-before-taking-it`, `lesson-orchestration-retyped-a-ratification-line` (insight actioned). 25 created plus 29 updated plus 7 lessons make the 61 pages `generate` printed.
- Cascade (log): `rule-ask`, `rule-search-leaves-out-decisions`, `rule-synthesis` `built → draft`; `rule-plugin-install` `draft → built`.
- The handoff's instructions, checked in `git diff -- vault/wiki/log.md`, the pages' fields and `.claude/settings.json`: `rule-clean-branch` took the update of Case 919.2 and that of Case 920.5, holds no `deferred_by` and stands `built`; `decision-case-893.1` was set `superseded`. `rule-case-build` took the updates of Cases 924 and 926, and `render` wrote `.claude/agents/case-guppi.md`. The four Insights stand `actioned` with the `addressed_by` the handoff names. The `Read` matcher of `PreToolUse` in `.claude/settings.json` holds `guppi pageread` and `guppi grepguard`. `estimate-clean-branch-code-holds-pointers-only-in-brackets` took the update of Case 919.1 (`pending`), then L33 (`passed`), in that order.
- `backlog.md` went from 15 items to 10: `rule-clean-branch` and the four Insights above left it.
- This run ticked 44 boxes of `vault/raw/2026-10-30/0304/spec.md` (7 of them render boxes) and the `read` box of `estimate-close-commits` in `vault/raw/2026-10-29/2341/spec.md`. Ten `read` boxes of the 0304 Spec stay unticked; the handoff named 54 boxes waiting.
- Index check: the 4 `create` entries are Estimates and have no index; no Grep of a category ran for them.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 59 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 12 lines. The yaml holds no `lesson` entry, so no line follows and the synthesis added no entry.

## Readings due

- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — `pending`; target `rule-search-leaves-out-decisions` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-30/0304/spec.md` (Case 925.1): `test_grepguard.py`, then after the first `/pre-spec` once the librarian's run has rendered `.claude/settings.json`. This run: `guppi render` wrote `.claude/settings.json` (modified in `git status`); its `Read` matcher of `PreToolUse` holds `uv run --project .guppi guppi pageread` and `uv run --project .guppi guppi grepguard`.
- `estimate-search-leaves-out-decisions-in-every-agent` — `pending`; target `rule-search-leaves-out-decisions` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 925.3): after a session that runs on the rendered `.claude/rules/search-leaves-out-decisions.md` and `.claude/agents/ask-guppi.md`.
- `estimate-ask-opens-a-decision-only-for-a-finding` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 925.4): after a `/pre-spec` whose `ask-guppi` runs on the rendered `.claude/agents/ask-guppi.md`.
- `estimate-ask-finds` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 925.5): after a `/pre-spec` whose `ask-guppi` runs on the rendered `.claude/agents/ask-guppi.md`.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.2): after a `case-guppi` builds a Case with a `create` without a `ref`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.3): after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: the yaml held no `lesson` entry; the synthesis added no entry.
- `estimate-synthesis-clusters` — `pending`; target `rule-synthesis` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 920.4): after a librarian's run whose `materialize.yaml` holds at least two lesson entries. This run: the yaml held 0 `lesson` entries; the two Greps printed 59 and 12 lines.
- `estimate-orchestration-states-a-subagent-fact-from-its-transcript` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 923): after the first reply of the main agent under the new Render that states what a subagent did.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 924): after the `/pre-spec` of the first session whose `case-guppi` runs on the Render with the sentence on the readers of a changed step.
- `estimate-case-build-reads-the-code-it-states` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 0304 Spec (Case 926): after a `/pre-spec` of a session whose Cases `case-guppi` built on the Render this run rendered.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); method: after a librarian's run whose `librarian-guppi.md`, when the run starts, holds the Render of `rule-close` with no limit of lines, the person's answer on the report. This run: `.claude/agents/librarian-guppi.md` was not modified by this run (`git status`), and its Render of `rule-close` names no limit of lines; the report goes to `/handoff` after the commit.
- `estimate-guppi-package-is-ready-after-the-install` — `pending`; target `rule-guppi-package` (`draft`); method: after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z` in the history of HEAD, a clean copy by `guppi ship --allow-draft`, an install by the person at a stop of Work Mode, and the person's answer. This run: `git merge-base --is-ancestor prod-0.2.0 HEAD` exited 0.
- `estimate-orchestration-shows-the-built-case` — `pending`; target `rule-orchestration` (`draft`); method: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` naming a Case of the session under the new Render.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch taken up together under the new Render in which a summary carries a line `Other Case` naming a Case of the session.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes both.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); method: after a session whose ledger holds a lesson with the Case that closes its cause, a Case taking up a decision with more than one Case in `deferred_by`, and a lesson line declaring a new tag.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: `test_ship.py`, and a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: an install from a clean copy in a session of `plugin` before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: a pull request from a second account, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer at the `/hi` after the session that writes `README.md`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- No entry `incomplete`, `failed`, `near` or `unparsed`. No `failed` Estimate.
- MOC candidates: none named by any step of this run.
- Stale defer: `backlog.md` lists `rule-work-mode`, put off in 31 sessions.
- Contradictions: none found by this run.
- Lint (`guppi check`, exit 1, 13 lines): 12 pages with `core: true` stand `draft` — `entity-sprint`, `rule-ask`, `rule-case-build`, `rule-close`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-search-leaves-out-decisions`, `rule-skill-hi`, `rule-synthesis`, `rule-work-mode`; `estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`. The `backlog.md` line and the `ship:` line of the handoff's Baseline are no longer printed.
- Handoff, Observations: it expected `rule-compact-recall` to stand `draft` after this run; `estimate-compact-recall-reloads` took L35 `passed`, and the cascade moved no status of `rule-compact-recall`. `rule-search-leaves-out-decisions` stands `draft`, which the handoff did not list.
- `guppi materialize` printed 39 entries; the yaml holds 38 `- line:` entries, line 34 folded into the entry of line 4.
- A read the frame says the job does not need: a Grep of `sprint-close` over `vault/raw/2026-10-30/0304/spec.md` printed line 405, a paragraph of the Spec past its unticked lines; step 2 of the run needed it, to learn whether an unticked task line holds `guppi sprint-close --apply`. The handoff did not ask for it.

## Next session

### Cases

- The milestone item of the clean branch, `rule-clean-branch` with `estimate-sprint-plugin-ci-writes-a-clean-branch`, was put off again: the owner's push of `plugin` and a tag `prod-x.y.z`, and the reading of the CI run it starts (handoff, For the next session).
- Whether the `method` of `estimate-clean-branch-code-holds-pointers-only-in-brackets` should name `--allow-draft` for `guppi ship --review`, since that command, while a page with `core: true` stands `draft`, exits 1 and writes nothing (handoff, For the next session).
- `estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with` stands in the output of `guppi check` (lint).

### Work

- none

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — After the agent writes a clean copy by `guppi ship --allow-draft` in the repository of GUPPI, and you, at a stop of Work Mode, add it as a catalogue, install `guppi`, type `/guppi:install` in an empty project, reopen Claude Code and type `/hi`: did the output of the install, the order of its steps, the files of the project and its `.guppi/.venv/` match the Criterion?
- `estimate-close-reports-the-run` — needs the person — Did the report that `/handoff` showed after the librarian's run of 2026-10-30 give each part the Criterion names — the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags, the lint total and each part another step of the frame sends to the report — and no test result and no list of files?

## Readings at the close

- `uv run --project .guppi guppi test`: 1803 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1, 13 lines (Flags).
- Pages under `vault/wiki/`: rules 86, estimates 322, entities 5, lessons 52, insights 12, decisions 386. Files `*.md` under `vault/archive/`: 2990, after `guppi archive` moved `raw/2026-10-29/2341` to `archive/plugin/2026-10-29/2341/raw`.
