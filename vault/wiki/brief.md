# Brief — 2026-10-11, after the librarian run of session 2350

## Where things stand

- Session 2350 (dated 2026-10-10) of the sprint `plugin` ratified Cases 773, 774 and 775 (775.1, 775.2, 775.3). Case 775.1 and 775.2 supersede Case 771, the defer of `rule-skill-sprint-open` and `rule-skill-sprint-close` (handoff, What actually got done).
- Code: `guppi/generate.py` — one helper, `take_superseded_by`, writes the `superseded by` History line only when it adds the name to `superseded_by`; the step for a page named in `supersedes` and the step for a sub-case call it. Test: `tests/test_generate.py`, one new test (handoff).
- Readings of the session: ledger lines 9 to 12, all `passed`; lesson on ledger line 13 (handoff).
- The yaml `vault/raw/2026-10-10/2350/materialize.yaml`: 12 items under `entries` from a 13-line ledger (line 10, the reading of `estimate-skill-sprint-open-merges-the-closed-sprint-branch`, folded into its `create` entry, line 4); the stdout of `guppi materialize` said "written with 13 entries". All 12 entries and all 6 `decisions` records `applied`; no entry carries `failed`, `exists`, `incomplete`, `near`, `librarian` or `merged`; `unparsed: []`. The yamls of 1555, 1713 and 1913 were extended with 0 entries. `guppi generate` wrote or changed 16 pages for 2350, 0 for the others.
- Created: decisions 6 (773, 774, 775, 775.1, 775.2, 775.3); estimates 1 (`estimate-skill-sprint-open-merges-the-closed-sprint-branch`, `passed`); lessons 1 (`lesson-hi-unread-sprint-reading-made-a-case-line`, `new`).
- Updated: estimates 3 (`estimate-generate-writes-the-decision-page`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-where-to-stop-stops-only-on-its-conditions`: Criterion replaced, set `pending`, read `passed`); entities 1 (`entity-sprint-plugin`: the opening-and-close note removed, the Purpose names only the close); rules 3 (`rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-where-to-stop`); decisions 1 (`decision-case-771`, superseded by 775.1 and 775.2).
- Handoff check (Direct instructions, first line): `deferred_by: ["[[decision-case-771]]"]` is gone from `rule-skill-sprint-open` and `rule-skill-sprint-close`; each History holds `defer by decision-case-771 superseded`; `guppi backlog` went from 5 items to 3 and no longer lists either page.
- Handoff check (second line): the ledger holds 13 lines, each decision line once; 775.3 is lines 7 and 8.
- Handoff check (third line): the render changed `.claude/skills/sprint-open/SKILL.md` (new step 4, the merge tasks of the opening Case, case 775.1), `.claude/skills/sprint-close/SKILL.md` (step 4 holds no merge task line, case 775.2) and `vault/wiki/where-to-stop.md` (condition 6 covers a refused `git merge --ff-only` or `git branch -d` in the merge tasks of the opening Case, case 775.3).
- Handoff check (fourth line): `guppi sprint` rewrote `vault/wiki/sprint.md`; the milestone `The sprint turn and GitHub` holds the GitHub line alone, and the Purpose names only the close.
- Archived by `generate` and moved by `guppi cleanup` (1 page): `decision-case-771`, superseded, to `vault/archive/plugin/2026-10-11/2350/decisions/`.
- Ticked by this run: 16 boxes of `vault/raw/2026-10-10/2350/spec.md`; it holds no unticked box. No unticked line of the session's spec holds `guppi sprint-close --apply`; no close ran.
- `guppi glossary` changed nothing.
- `guppi archive` moved three units: `raw/2026-10-10/1555` → `archive/migration/2026-10-10/1555/raw`, `raw/2026-10-10/1713` → `archive/plugin/2026-10-10/1713/raw`, `raw/2026-10-10/1913` → `archive/plugin/2026-10-10/1913/raw`. It kept `raw/2026-10-10/2350`, the session of the run; `vault/raw/2026-10-09/`, `2026-10-10/` and `2026-10-11/` otherwise hold only `event_log.md`.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 31 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 1 line.
  - `lesson-hi-unread-sprint-reading-made-a-case-line` joined none: no index line names a step of `rule-skill-hi` that keeps an Estimate of the live sprint page in a Cases line; the nearest, `lesson-prespec-method-predicate-misses-a-sprint-session`, has its cause in the wording match of `waits_for_another_session` in `guppi/lint.py`; it stays `new`.

## Readings due

- `estimate-sprint-plugin-close-steps-run-from-the-line` · pending · target `entity-sprint-plugin` (draft) · no read line in the 2350 spec; method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin: its frontier.md, ledger, spec.md and transcript.
- `estimate-sprint-plugin-readme-describes-the-project` · pending · target `entity-sprint-plugin` (draft) · no read line in the 2350 spec; method: by hand, the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` · pending · target `entity-sprint-plugin` (draft) · no read line in the 2350 spec; method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` · pending · target `entity-sprint-plugin` (draft) · no read line in the 2350 spec; method: by hand, a CI run on GitHub and the clean branch it wrote, read in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` · pending · target `entity-sprint-plugin` (draft) · no read line in the 2350 spec; method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-hi-writes-frontier` · pending · target `rule-skill-hi` (draft) · no read line in the 2350 spec; method: by hand, the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py.
- `estimate-brief-written` · pending · target `rule-brief` (draft) · no read line in the 2350 spec; method: by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run and the brief of the run before it. This run ran no `guppi sprint-close --apply`.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`.
- Failed Estimates: none after `generate`.
- MOC candidates: none.
- Stale defer: `rule-morph` — `deferred: 4 times since case 239` (lint).
- Contradiction: the Criterion of `estimate-sprint-close-next-session-opens-the-sprint` names "the refusals of `uv run guppi ledger` in its transcript" in its `When`; its `method` no longer does, by case 769.5 (handoff, For the next session).
- Record: `guppi materialize` marked both `defer` entries of case 771 in the 1913 yaml, now `vault/archive/plugin/2026-10-10/1913/raw/materialize.yaml` (ledger lines 23 and 24) `superseded_by: '775.2'`; the entry of `rule-skill-sprint-open` was superseded by ledger line 3 of 2350, case 775.1. The field is one value per entry, and the `decisions` record of 771 lists both `decision-case-775.1` and `decision-case-775.2`.
- `make lint`, exit 2, 8 lines, the same 8 the handoff saw before the work:
  - `rules/rule-morph: deferred: 4 times since case 239`
  - `estimates/estimate-brief-written: unread: pending`
  - `estimates/estimate-hi-writes-frontier: unread: pending`
  - `estimates/estimate-sprint-plugin-ci-writes-a-clean-branch: unread: pending`
  - `estimates/estimate-sprint-plugin-close-steps-run-from-the-line: unread: pending`
  - `estimates/estimate-sprint-plugin-installs-as-a-plugin: unread: pending`
  - `estimates/estimate-sprint-plugin-pull-requests-reviewed-on-github: unread: pending`
  - `estimates/estimate-sprint-plugin-readme-describes-the-project: unread: pending`
- Read outside the frame: none.

## Next session

**Cases**
- The step of `rule-skill-hi` that makes a Cases line for an open `W` line whose reading cannot run now does not leave out an Estimate of the live sprint page whose work is not done, as `rule-brief` and `rule-retro` do since case 772: the lesson of ledger line 13, `lesson-hi-unread-sprint-reading-made-a-case-line` (handoff, For the next session).
- The milestone line "the repository on GitHub set up so that a pull request from another person is easy to review" was put off untouched; it now holds the current milestone open alone (handoff, For the next session).
- The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` still names "the refusals of `uv run guppi ledger` in its transcript" in its `When`; its `method` no longer does, by case 769.5 (handoff, For the next session).
- The entry-level `superseded_by` of the yaml holds one Case: the `defer` entry of `rule-skill-sprint-open` in the 1913 yaml names 775.2, not 775.1 that superseded it (Flags; `guppi/materialize.py`, the marking of `{supersedes}`).

**Work**
- none

**Ask the person**
- none

## Readings at the close

- `make test`: 1495 passed, 6 skipped.
- `make lint`: exit 2, 8 lines (above).
- Live pages: decisions 41, entities 4, estimates 266, insights 1, lessons 32, rules 79; `vault/archive/` holds 2617 `.md` files.
