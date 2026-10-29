# Brief — 2026-10-29, librarian of session 1930

## Where things stand

- Session 1930 of the sprint `plugin`. Cases ratified: 902; 903 (903.1, 903.2); 904 (904.1–904.3); 908 (908.1–908.3); 912 (912.1, 912.2). Short-form defers: 907 (`rule-ratification`), 909 (`rule-spec-capture`), 910 (`rule-skill-sprint-open`), 911 (`rule-plugin-install`). Case 905 is superseded whole by Case 912; Case 906 was dropped and holds no decision line (handoff).
- Code: `.guppi/guppi/casecheck.py` lost the old path of the `SubagentStop` check (`answer_of`, `write_case_files` removed); `.guppi/guppi/ratified.py` got a docstring; tests `.guppi/tests/test_casecheck.py` and `.guppi/tests/test_case_schema.py` changed. `guppi test` 1790 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L1 `estimate-clean-branch-ships-neutral-texts` `passed` (/hi); L22–L25 `passed`: `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, `estimate-case-example-passes-the-check`, `estimate-orchestration-forwards-a-discussion-question`. Lesson L26 (handoff, ledger).
- `guppi materialize` printed `written with 26 entries` for `vault/raw/2026-10-29/1930/materialize.yaml` and `extended with 0 entries` for the yaml of `0327`. The ledger has 26 lines; the yaml holds an entry for each of lines 1–26, `unparsed: []`. Kinds: 13 `update`, 3 `create` (2 estimates, 1 superseded), 4 `defer`, 5 `estimate`, 1 `lesson` — and the librarian added 3 entries (synthesis), 29 in all.
- Marks: no entry `failed`, `near` or `merged`; 4 `defer` entries `exists: true` (907, 909, 910, 911); the 2 entries of Case 905 (L10, L11) carry `superseded_by: 912.1`, L11 also `incomplete: [criterion]`; 3 entries `librarian: synthesis`.
- `guppi generate` printed 47 pages written or changed for `1930` and 0 for `0327`. `guppi cleanup` printed 1 page moved (`decision-case-905`, to `vault/archive/plugin/2026-10-29/1930/decisions/`). `guppi render`, `sprint`, `backlog`, `glossary` printed nothing on stderr.
- Pages created (23): decisions 20 (`decision-case-902`, `903`, `903.1`, `903.2`, `904`, `904.1`–`904.3`, `905`, `907`, `908`, `908.1`–`908.3`, `909`, `910`, `911`, `912`, `912.1`, `912.2`; `905` born superseded and archived); estimates 2 (`estimate-close-reports-in-twenty-lines`, `estimate-plugin-install-runs-no-hook-before-uv-sync`); lessons 1 (`lesson-case-build-changes-a-step-without-reading-what-reads-it`, `clustered`); insights 1 (`insight-case-build-changes-a-step-without-reading-its-readers`, `open`, severity 2).
- Pages updated (23): estimates 10; rules 10 (`rule-case-example`, `rule-clean-branch`, `rule-close`, `rule-guppi-package`, `rule-permissions`, `rule-plugin-install`, `rule-ratification`, `rule-skill-sprint-open`, `rule-spec-capture`, `rule-spec-reconcile`); lessons 1 (`lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes`, `new → clustered`); archived decisions 2 (`decision-case-885` superseded by 902 and 903.1; `decision-case-891` superseded by 902; both stay archived).
- Cascade: `rule-clean-branch` `draft → built`; `rule-guppi-package`, `rule-permissions`, `rule-plugin-install` `built → draft` (log).
- The handoff's instructions, checked: no page took an entry of Case 905; `estimate-spec-write-writes-a-defer` and `estimate-close-commits` carry no `deferred_by` and are gone from `backlog.md`; `rule-spec-reconcile` holds no `## How it works`; the render wrote `plugin/skills/install/SKILL.md` and ticked its box.
- This run ticked 19 boxes of `vault/raw/2026-10-29/1930/spec.md` and 1 of `vault/raw/2026-10-29/0327/spec.md` (`read estimate-clean-branch-ships-neutral-texts`). No `guppi sprint-close --apply` line stands in the Spec.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 55 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 11 lines.
  - `lesson-case-build-changes-a-step-without-reading-what-reads-it` joined `lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes` under the new `insight-case-build-changes-a-step-without-reading-its-readers`.

## Readings due

- `estimate-close-commits` — `pending`; target `rule-close` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/1930/spec.md`: `test_render.py -k paths`, then after a librarian's run whose `librarian-guppi.md` holds the Render of `rule-close`, `git log` and `git status`. This run: `guppi render --paths` printed 32 paths, `plugin/skills/install/SKILL.md` among them; the commit of this run is made after this brief.
- `estimate-close-reports-in-twenty-lines` — `pending`; target `rule-close` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/1930/spec.md`: the person's answer on the report `/handoff` shows after such a run. This run: the report is written after this brief.
- `estimate-plugin-install-runs-no-hook-before-uv-sync` — `pending`; target `rule-plugin-install` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/1930/spec.md`: two installs by hand from a clean copy, one normal, one offline with an empty `uv` cache. This run: `git tag --merged HEAD` printed `prod-0.2.0`, `prod-1`, `prod-2`; the render wrote `plugin/skills/install/SKILL.md`.
- `estimate-guppi-package-is-ready-after-the-install` — `pending`; target `rule-guppi-package` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/1930/spec.md`: the person's answer on an install from a clean copy. This run: `git tag --merged HEAD` printed `prod-0.2.0`, `prod-1`, `prod-2`; the render wrote `plugin/skills/install/SKILL.md`.
- `estimate-permissions` — `pending`; target `rule-permissions` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/1930/spec.md`: the person's word on prompts at a Case file write in Plan Mode and at a Grep on the transcripts folder.
- `estimate-orchestration-shows-the-built-case` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/1930/spec.md`: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` naming a Case of the session (not seen: handoff).
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch taken up together in Plan Mode under the new Render in which a summary carries a line `Other Case`.
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

- `incomplete`: L11 (Case 905, `create estimate-plugin-install-runs-no-hook-before-uv-sync`) lacks `criterion`; it carries `superseded_by: 912.1` and wrote no page; the page comes from L19 (Case 912.1).
- No entry `failed`, `near` or `unparsed`. No `failed` Estimate.
- MOC candidates: none named by any step of this run.
- Stale defer: `rule-clean-branch` went `draft → built` by the cascade in this run and keeps `deferred_by: decision-case-893.1`; `backlog.md` lists it, put off in 12 sessions.
- Contradictions: none found by this run.
- Lint (`guppi check`, exit 1, 11 lines): 10 pages with `core: true` stand `draft` — `entity-sprint`, `rule-case-build`, `rule-close`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-permissions`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`; and `estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`. The handoff counted 10 lines before the work; the `backlog` line is gone, and `rule-guppi-package` and `rule-permissions` went `draft` in this run.
- Handoff, Notes: the summary of Case 902 carried an `Other Case` line naming an item that was not yet a Case; no input says whether that is the event the `method` of `estimate-orchestration-signs-items-taken-together` waits for.

## Next session

### Cases

- `vault/wiki/orchestration.md` does not set what the main agent does with an `**Other Case:**` line that names a Frontier item not yet built as a Case (handoff, For the next session).
- The /hi reading of `estimate-clean-branch-ships-neutral-texts` lists Criterion sentences that hold only in the repository of GUPPI and remain: `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` (English named), `estimate-guppi-package-is-ready-after-the-install` (its new Criterion of Case 912.2 to check against that list), `estimate-sprint-close-moves-old-event-logs` (`.gitignore`), `estimate-python-utf8-output-intact` (cp1252), `estimate-synthesis-keeps-actioned-by-the-mark` (`(302.2)` in its prose), and the four Estimates under the defer of `decision-case-893.1` (handoff, For the next session).
- The `method` of `estimate-sprint-close-moves-old-event-logs` reads a line of `.gitignore`; the clean version holds no `.gitignore`, and no module writes one (handoff, For the next session).
- `rule-clean-branch` stands `built` and keeps `deferred_by: decision-case-893.1`, whose defer waited for its Estimates to pass (Flags).

### Work

- `estimate-close-commits`: `uv run --project .guppi pytest .guppi/tests/test_render.py -k paths`, and `git log` and `git status` on the commit of this run, against its Criterion.
- `estimate-plugin-install-runs-no-hook-before-uv-sync`: two installs by hand from a clean copy, one normal, one offline with an empty `uv` cache.
- L10–L11 of `vault/raw/2026-10-29/1930/ledger.md` (Case 905) not applied: superseded whole by Case 912, as the handoff asked.

### Ask the person

- `estimate-permissions` — needs the person — In this session's Plan Mode, did Claude Code ask you before `case-guppi` wrote each case file under `vault/raw/2026-10-29/1930/cases/`? And did you see any prompt at a Grep or Read of a subagent on the folder of saved transcripts? (The allow list of `.claude/settings.json` matches the Criterion, and `test_render.py -k json` passed, 4 tests.)
- `estimate-close-reports-in-twenty-lines` — needs the person — Did the report that `/handoff` showed after the librarian's run of session 1930 give the counts, the flags and the lint total in twenty lines or fewer?
- `estimate-guppi-package-is-ready-after-the-install` — needs the person — After an install from a clean copy written by `guppi ship --allow-draft`, `/guppi:install` in an empty project, a reopen and `/hi`: did the output of the install, the order of its steps, the files of the project and its `.guppi/.venv/` match the Criterion?

## Readings at the close

- `uv run --project .guppi guppi test`: 1790 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1, 11 lines (Flags).
- Pages under `vault/wiki/`: rules 86, estimates 315, entities 5, lessons 56, insights 12, decisions 349. Files `*.md` under `vault/archive/`: 2935.
