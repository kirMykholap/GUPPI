# Brief — 2026-10-14, after the librarian run of session 1536

## Where things stand

- Session 1536 (dated 2026-10-14) of the sprint `plugin` ratified Case 813 and Case 815 (handoff, What actually got done). The id 814 is held in the store and names no Case (handoff, Notes from memory).
- Code: `guppi/ship.py` — `EXAMPLE` and `EXAMPLE_FILE` removed; `masked` no longer sets aside the Render of `rule-case-example`; `judged` no longer skips `vault/wiki/case-example.md`; docstrings reworded. Tests: `tests/test_ship.py` — `test_a_sample_is_no_pointer` changed, `test_a_pointer_in_the_prose_of_the_example_file_exits_1` added. At the end of Work Mode: `make test` 1620 passed, 6 skipped; `make style` clean; `make lint` exit 0, no line (handoff).
- On GitHub, by the owner: a new deploy key `prod_deploy_pub` with write access and a new `PROD_DEPLOY_KEY`; run 38489789184 rerun on `prod-1` (attempt 2, success, wrote `prod` 34ae3bee); `plugin` and the tag `prod-2` pushed; run 38585781386 on `prod-2` succeeded and wrote `prod` c363e8a9 on top of 34ae3bee (handoff).
- Readings of the session: ledger lines 3 (`failed`), 8, 9, 10 (`passed`); lessons on ledger lines 4 and 11 (handoff; yaml).
- The yaml `vault/raw/2026-10-14/1536/materialize.yaml`: 11 entries from an 11-line ledger, one entry per line, so every ledger line is accounted for; 2 decisions (813, 815). All 11 entries and both decisions carry `applied`. No entry carries `failed`, `incomplete`, `exists` or `merged`; one carries `near`; `unparsed: []`. The yamls of 0101 and 0232 were extended with 0 entries. `guppi generate` wrote or changed 0 pages for 0101, 0 for 0232 and 10 for 1536, and printed nothing on stderr.
- Created: decisions 2 (`decision-case-813`, `decision-case-815`); lessons 2 (`lesson-ship-example-file-exempt-whole-left-case-pointers`, `lesson-shell-bang-commands-given-in-bash-syntax-ran-in-powershell`, both `new`).
- Updated: rules 2 (`rule-orchestration` by 813, `rule-clean-branch` by 815); estimates 3 (`estimate-ratification-case-id-carries-the-sprint` by 813 and its reading, `pending` → `passed`; `estimate-clean-branch-writes-a-clean-copy` by 815 and its reading, `pending` → `passed`; `estimate-sprint-plugin-ci-writes-a-clean-branch` by its two readings, `pending` → `failed` → `passed`); entities 1 (`entity-sprint-plugin` by 815).
- `guppi cleanup` moved 0 pages. `guppi render` printed nothing on stderr and changed `vault/wiki/orchestration.md` (the sentence of Case 813). `guppi sprint`, `guppi backlog` and `guppi glossary` printed nothing on stderr; `vault/wiki/sprint.md` ticks the reading of the CI Estimate (`passed`) and the milestone The clean branch, and lists the four items of The plugin; `backlog.md` and `glossary.md` did not change. No unticked line of the Spec holds `guppi sprint-close --apply`; no close ran.
- `guppi archive` printed nothing on stdout or stderr and moved no unit: the units left in `vault/raw/` are `2026-10-14/0101`, `2026-10-14/0232` and `2026-10-14/1536`, all dated the day of the run, and 1536 is the session of the run; the folders of 2026-10-09 to 2026-10-13 hold only `event_log.md`. No `pending` Estimate's `method` names the archive step.
- Handoff check (Case 815 ratified twice): the ledger holds lines 5–7 for Case 815 and the yaml one decision `decision-case-815` with three targets; all applied.
- Handoff check (Estimates set `pending` then read): the History of `estimate-clean-branch-writes-a-clean-copy` reads the 815 update, then `pending → passed` from line 9; that of `estimate-ratification-case-id-carries-the-sprint` the 813 update, then `pending → passed` from line 8.
- Handoff check (CI Estimate): its History reads `pending → failed` (line 3), then `failed → passed` (line 10); its status is `passed`.
- Handoff check (milestone): after `guppi sprint`, `vault/wiki/sprint.md` holds `### [x] The clean branch`.
- Handoff check (lesson marks): the entry of line 4 carries `addressed_by: decision-case-815`; the entry of line 11 carries none.
- Ticked by this run in `vault/raw/2026-10-14/1536/spec.md`: 9 boxes, the 9 the handoff's Debt names (5 `update` and 2 `read` by `generate`; the render line by `render` and the `guppi sprint` line by `sprint`). Unticked after the run: none in the Specs of 0101, 0232 or 1536.
- Index check: the yaml holds no `create` entry; the two `lesson` entries were compared with the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 42 lines. None is the same page as an existing lesson; `lesson-shell-bang-commands-given-in-bash-syntax-ran-in-powershell` is marked `near: lesson-bash-tool-heredoc-escapes-interpreted`.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 42 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/`, 4 lines.
  - `lesson-ship-example-file-exempt-whole-left-case-pointers`: none — no index line names `guppi ship` or the example file; it stays `new`. Its entry carries `addressed_by: decision-case-815`, which no Insight takes, since it joined none.
  - `lesson-shell-bang-commands-given-in-bash-syntax-ran-in-powershell`: none — the nearest line, `lesson-bash-tool-heredoc-escapes-interpreted`, names the Bash tool's escape layer before python reads a heredoc, not the `!` prompt running PowerShell 5.1; it stays `new`.

## Readings due

- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: by hand, at Retro, the new Render of rule-work-mode in the Spec; `uv run guppi render --check`; by hand, after the first /work that runs on the rendered `.claude/skills/work/SKILL.md` and in which a Case is ratified in Work Mode.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: by hand, after the session whose Work Mode builds the install skill of rule-morph.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: by hand, after the first /merge-main whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: by hand, after the first pull request from an account other than the owner's is merged into main by /pr-review after the close of plugin.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin.

## Flags

- `near`: `lesson-shell-bang-commands-given-in-bash-syntax-ran-in-powershell` is near `lesson-bash-tool-heredoc-escapes-interpreted` (index check): both are a command that a shell of this Windows machine reads otherwise than it was written; the causes differ.
- No entry is marked `incomplete`, `failed` or `unparsed`. No Estimate is `failed`.
- `make lint`: 0 lines, exit 0.
- Handoff note: the second reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` judged as samples the `origin: raw/2026-09-08/…` values in the `examples` block of the `schema.yaml` files and the id `case 785.1` in a code span of `ratification.md`; the handoff says a stricter reading of "no mention of a session" would make it `failed`.
- Handoff note: the two `－` lines of the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` (ship exits 1; a clean version equal to the last commit) were read from the text of `.github/workflows/prod.yml` both times, never seen in a run.
- Handoff note: the first reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` (`failed`, ledger line 3) was the main agent's judgment; the person did not object and asked for the Case that fixed it (Case 815).
- Handoff observation: `/pre-spec` found that a Case closing a sprint item had no `update` of the sprint page; `case-guppi` had not added one at the first build.
- Handoff observation: the ruleset of `prod` reported "Cannot create ref due to creations being restricted" on the first push and "Cannot update this protected ref" on the second, each under "Bypassed rule violations".

## Next session

### Cases

- The milestone The clean branch is ticked in `vault/wiki/sprint.md` by this run; the next milestone is The plugin — 4 items: the clean version made into a Claude Code plugin, `rule-morph`, the README, the close of `plugin` (handoff, For the next session).

### Work

- none

### Ask the person

- none

## Readings at the close

- `make test`: 1620 passed, 6 skipped.
- `make lint`: 0 lines, exit 0.
- Live pages: rules 84, estimates 281, entities 5, insights 4, lessons 44, decisions 128; `vault/archive/`: 2701 `.md` files after `guppi archive`.
