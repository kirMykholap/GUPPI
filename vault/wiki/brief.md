# Brief — 2026-10-12, after the librarian run of session 1449

## Where things stand

- Session 1449 (dated 2026-10-12) of the sprint `plugin` ratified Cases 776, 778 and 779; Case 779 supersedes Case 777, which was ratified in the same session (handoff, What actually got done; Notes from memory).
- Code: `guppi/materialize.py` — `mark_superseded` reads the entry's `superseded_by` through `cases_of` and appends the Case when the list does not hold it. Tests: `tests/test_materialize.py`, the entry assertions compare to a list; two new tests (handoff).
- Readings of the session: ledger lines 7, 8 and 9, all `passed`; lesson on ledger line 10 (handoff).
- The yaml `vault/raw/2026-10-12/1449/materialize.yaml`: 10 entries from a 10-line ledger, one per line. 9 entries and the 3 `decisions` records of 776, 778 and 779 are `applied`; the entry of line 3 (case 777) carries `superseded_by: ['779']` and no `applied`, and the record of 777 carries `superseded_by: [decision-case-779]`. No entry carries `failed`, `exists`, `incomplete`, `near`, `librarian` or `merged`; `unparsed: []`. The yaml of 2350 was extended with 0 entries. `guppi generate` wrote or changed 10 pages for 1449, 0 for 2350.
- Created: decisions 4 (776, 777, 778, 779); lessons 1 (`lesson-case-build-recommended-a-trigger-that-keeps-the-defect`, `new`).
- Updated: rules 2 (`rule-materialize`: the one-off migration sets `superseded_by` to a list, case 776; `rule-skill-hi`: two `replace` pairs, case 778); estimates 3 (`estimate-materialize-marks-superseded`, `estimate-hi-takes-its-readings`, `estimate-sprint-close-next-session-opens-the-sprint`: Criterion replaced, set `pending`, read `passed`); decisions 1 (`decision-case-777`, superseded by 779).
- Handoff check (Direct instructions, first line): the `## Criterion` of `estimate-sprint-close-next-session-opens-the-sprint` holds the `When` of Case 779 ("Someone reads `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of the Render of `rule-brief` …"); its method names the Retro of the session of case 779. `vault/wiki/log.md` holds `decisions/decision-case-777 superseded by decision-case-779` and `decision-case-777 archived · superseded`.
- Handoff check (third line): both `replace` pairs of case 778 stand on `rule-skill-hi`; the render changed one line of `.claude/skills/hi/SKILL.md`, which now holds both new sentences (case 778).
- Archived by `generate` and moved by `guppi cleanup` (1 page): `decision-case-777`, superseded, to `vault/archive/plugin/2026-10-12/1449/decisions/`.
- Ticked by this run: 9 boxes of `vault/raw/2026-10-12/1449/spec.md` (8 by `generate`, the render line of `.claude/skills/hi/SKILL.md` by `render`); it holds no unticked box. No unticked line of the spec holds `guppi sprint-close --apply`; no close ran.
- `guppi sprint`, `guppi backlog` and `guppi glossary` changed nothing.
- `guppi archive` moved one unit: `raw/2026-10-10/2350` → `archive/plugin/2026-10-10/2350/raw`. It kept `raw/2026-10-12/1449`, the session of the run; `vault/raw/2026-10-10/` now holds only `event_log.md`.
- Index check: the one `create`-kind entry other than an Estimate is the lesson of line 10; Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 32 lines; none has the same cause, none near.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 32 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 1 line.
  - `lesson-case-build-recommended-a-trigger-that-keeps-the-defect` joined none: no index line names a Criterion judged against the item's own words instead of the rule its defect breaks; `lesson-case-reading-moment-before-the-render-it-reads` has its cause in a reading moment set from the end state, and `lesson-hi-brief-line-judged-apart-from-a-broad-milestone-line` in sameness judged by wording at `/hi`; the one Insight is about code live before its page. It stays `new`.

## Readings due

- `estimate-sprint-plugin-close-steps-run-from-the-line` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1449 spec; method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin: its frontier.md, ledger, spec.md and transcript.
- `estimate-sprint-plugin-readme-describes-the-project` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1449 spec; method: by hand, the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1449 spec; method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1449 spec; method: by hand, a CI run on GitHub and the clean branch it wrote, read in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1449 spec; method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-hi-writes-frontier` · pending · target `rule-skill-hi` (draft) · no read line in the 1449 spec; method: by hand, the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py.
- `estimate-brief-written` · pending · target `rule-brief` (draft) · no read line in the 1449 spec; method: by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run and the brief of the run before it. This run ran no `guppi sprint-close --apply`.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`.
- Failed Estimates: none after `generate`.
- MOC candidates: none.
- Stale defer: `rule-morph` — `deferred: 4 times since case 239` (lint).
- Contradictions: none found.
- Record: `lesson-hi-unread-sprint-reading-made-a-case-line` (ledger line 13 of 2350) names as its root cause the step of `rule-skill-hi` that case 778 changed; no decision line of case 778 carries `{addresses:…}`, so the lesson stays `new` with no `addressed_by`.
- `make lint`, exit 2, 8 lines, the same 8 the handoff saw in the baseline:
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
- Estimates that wait for an event other than the close of a sprint — a moment that `rule-case-protocol` (case 670.4) has pre-spec report — and the path the person proposed for a reading `/hi` cannot take: Work, a flag of the librarian, a defer into the backlog at the next `/hi`; Case 778 left both out (handoff, For the next session).
- The cause of the lesson of ledger line 10, `lesson-case-build-recommended-a-trigger-that-keeps-the-defect`: `case-guppi` judged a Criterion against the item's own words and not against `rule-case-protocol` (case 670.4), so its recommended option kept the defect (handoff, For the next session).
- The milestone line "the repository on GitHub set up so that a pull request from another person is easy to review" still holds the current milestone open alone (handoff, For the next session).

**Work**
- none

**Ask the person**
- none

## Readings at the close

- `make test`: 1497 passed, 6 skipped.
- `make lint`: exit 2, 8 lines (above).
- Live pages: decisions 44, entities 4, estimates 266, insights 1, lessons 33, rules 79; `vault/archive/` holds 2626 `.md` files after `guppi archive`.
