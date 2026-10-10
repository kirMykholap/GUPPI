# Brief — 2026-10-10, after the librarian run of session 1913

## Where things stand

- Session 1913 of the sprint `plugin` ratified Cases 765, 766, 767, 768, 769 (769.1 to 769.5), 770, 771 (a defer of `rule-skill-sprint-open` and `rule-skill-sprint-close`) and 772 (772.1 to 772.5). Case 764 and its sub-cases are superseded by Case 772 (handoff, What actually got done; Direct instructions).
- Code: `guppi/materialize.py`, `guppi/archive.py`, `guppi/generate.py`, `guppi/cleanup.py`, `guppi/ledger.py`, `guppi/lint.py`, `guppi/prespec.py`, `guppi/sprint.py`, `guppi/sprint_close.py`, `guppi/backlog.py`. `unit_sprint` is the one judgment of a unit's sprint; `SPRINT_PAGE` and `is_sprint_page` in `guppi/ledger.py` are the one judgment of a sprint page. Tests: `tests/test_cleanup.py` 2 new, `tests/test_lint.py` 2 new methods, `tests/test_prespec.py` 2 new (handoff).
- Migration: `decision-case-757` and `decision-case-759` moved from `vault/archive/migration/2026-10-10/1713/decisions/` to `vault/archive/plugin/2026-10-10/1713/decisions/` (handoff).
- Readings of the session: 9 `passed` (ledger lines 35 to 43); lessons on ledger lines 44 and 45 (handoff).
- The yaml `vault/raw/2026-10-10/1913/materialize.yaml`: 43 items under `entries` from a 45-line ledger (line 37 folded into the `create` entry of `estimate-orchestration-acknowledges-the-opening-with-the-frontier`, line 43 into the `create` entry of `estimate-cleanup-files-a-session-by-its-sprint`); the stdout of `guppi materialize` said "written with 45 entries". 34 entries `applied`; entries 1 to 9 (cases 764.1 to 764.5) carry `superseded_by` and are not applied; the two `defer` entries carry `exists: true`; `unparsed: []`. The yamls of 1555 and 1713 were extended with 0 entries. `guppi generate` wrote or changed 52 pages for 1913, 0 for 1555 and 1713.
- Created: decisions 24 (764, 764.1 to 764.5, 765, 766, 767, 768, 769, 769.1 to 769.5, 770, 771, 772, 772.1 to 772.5), of which 18 stay live; estimates 2 (`estimate-orchestration-acknowledges-the-opening-with-the-frontier`, `estimate-cleanup-files-a-session-by-its-sprint`, both `passed`); lessons 2.
- Updated: estimates 13 (7 of them read `passed`); rules 11 (8 by `update`: `rule-skill-sprint-open`, `rule-skill-hi`, `rule-session-start`, `rule-orchestration`, `rule-brief`, `rule-retro`, `rule-handoff`, `rule-case-protocol`; `rule-skill-sprint-open` and `rule-skill-sprint-close` deferred by case 771; `rule-orchestration` and `rule-cleanup` took an Estimate; by the cascade `rule-skill-hi` built → draft and `rule-sprint-close` draft → built).
- Archived by `generate` and moved by `guppi cleanup` (6 pages): `decision-case-764` and `decision-case-764.1` to `764.5`, superseded, to `vault/archive/plugin/2026-10-10/1913/decisions/`.
- Ticked by this run: 39 boxes of `vault/raw/2026-10-10/1913/spec.md` and the `read` box of `estimate-sprint-close-next-session-opens-the-sprint` in `vault/raw/2026-10-10/1555/spec.md`. No unticked line of the session's spec holds `guppi sprint-close --apply`; no close ran.
- Rendered: `.claude/agents/librarian-guppi.md`, `.claude/skills/handoff/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/skills/sprint-open/SKILL.md`, `vault/wiki/orchestration.md`, `vault/wiki/case-schema.md`. `guppi sprint` rewrote `vault/wiki/sprint.md`, `guppi backlog` rewrote `vault/wiki/backlog.md`, `guppi glossary` changed nothing.
- `guppi archive` printed no line and moved nothing: the three units with a ledger, `vault/raw/2026-10-10/1555`, `1713` and `1913`, are dated the day of the run, and 1913 is the session of the run; `vault/raw/2026-10-09/` holds only `event_log.md`.
- Synthesis: Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 29 lines; Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 1 line.
  - `lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page` joined none: no index line names the closing of a sprint item by a Case that does not update the sprint page; it stays `new`.
  - `lesson-hi-brief-line-judged-apart-from-a-broad-milestone-line` joined none: no index line names judging the sameness of a brief line and a milestone line by wording; its cause differs from the other lesson of this run (closing a line vs. judging sameness); it stays `new`.

## Readings due

- `estimate-sprint-plugin-close-steps-run-from-the-line` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1913 spec; method: by hand, at the end of Work Mode of the session that closes entity-sprint-plugin: its frontier.md, ledger, spec.md and transcript.
- `estimate-sprint-plugin-readme-describes-the-project` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1913 spec; method: by hand, the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 89 of `vault/raw/2026-10-10/1913/spec.md`; method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` · pending · target `entity-sprint-plugin` (draft) · `- [ ] read` line 134 of the 1913 spec; method: by hand, a CI run on GitHub and the clean branch it wrote, read in a session of the sprint plugin before its close.
- `estimate-sprint-plugin-installs-as-a-plugin` · pending · target `entity-sprint-plugin` (draft) · no read line in the 1913 spec; method: by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close.
- `estimate-hi-writes-frontier` · pending · target `rule-skill-hi` (draft) · `- [ ] read` line 315 of the 1913 spec; method: by hand, the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py.
- `estimate-brief-written` · pending · target `rule-brief` (draft) · `- [ ] read` line 603 of the 1913 spec; method: by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run and the brief of the run before it. This run ran no `guppi sprint-close --apply`.

## Flags

- `incomplete`: the parent entry of case 764 (`decision-case-764`, under `decisions` of the yaml) lacks `context` and `problem`; it is `superseded_by: decision-case-772.1` and its page is archived. No entry is marked `failed`, `near` or `unparsed`.
- Failed Estimates: none after `generate`.
- MOC candidates: none.
- Stale defer: `rule-morph` — `deferred: 4 times since case 239` (lint).
- Contradictions: none found.
- Defect: `vault/wiki/log.md` holds the line `decisions/decision-case-764.1 superseded by decision-case-772.1` twice from this run's `generate`: once among the sub-cases of 764 superseded with their parent, once for the explicit `{supersedes:case 764.1}` of ledger line 25.
- Handoff check (Direct instructions, fourth line): the seven files it names were rewritten by this run's render, and each holds its new Case: `.claude/skills/retro/SKILL.md` (772.2), `.claude/skills/handoff/SKILL.md` (772.3), `.claude/agents/librarian-guppi.md` (772.1), `.claude/skills/hi/SKILL.md` (769.2), `.claude/skills/sprint-open/SKILL.md` (769.1), `vault/wiki/orchestration.md` (769.4), `vault/wiki/case-schema.md` (772.4).
- Handoff note: this brief is written from the text of `rule-brief` before Case 772.1, so the readings of `entity-sprint-plugin` and their `read` boxes stand under `Work`; the new text is rendered into `.claude/agents/librarian-guppi.md` for the next run.
- `make lint`, exit 2, 8 lines:
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
- The milestone line "the opening and the close of a sprint run with no fix by hand and each flaw found in them is fixed" stays open: its open flaw is the merge step at the opening of a sprint, deferred by Case 771, and the close of `plugin` is not yet run (handoff, For the next session).
- The milestone line "the repository on GitHub set up so that a pull request from another person is easy to review" was put off untouched (handoff, For the next session).
- The method of `estimate-sprint-close-next-session-opens-the-sprint` no longer names a transcript, by Case 769.5; the person's earlier wish to fix that method before the close of `plugin` is settled by that Case (handoff, For the next session).
- Defect: a doubled `superseded by` line for `decision-case-764.1` in `vault/wiki/log.md`, written by `guppi generate` (Flags).

**Work**
- `estimate-sprint-plugin-close-steps-run-from-the-line`.
- `estimate-sprint-plugin-readme-describes-the-project`.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (its `- [ ] read` line 89 of the 1913 spec).
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (its `- [ ] read` line 134 of the 1913 spec).
- `estimate-sprint-plugin-installs-as-a-plugin`.
- Ledger lines 1 to 9 of `vault/raw/2026-10-10/1913/ledger.md` (cases 764.1 to 764.5) not applied to their pages: superseded by Case 772; their Decision pages were written and archived.

**Ask the person**
- `estimate-hi-writes-frontier` — needs the person — in the session after the close of `plugin`, at the reply that acknowledges the opening Case of `/sprint-open`: did the Frontier come out as the Criterion says, with the opening line first and closed by the opening Case, and the items of the first milestone taken from the opening Case? (its `- [ ] read` line 315 of the 1913 spec)
- `estimate-brief-written` — needs the person — at the `/hi` after the librarian's run of the session that closes `plugin`, on that brief and the one before it: does `Cases` of Next session hold each contradiction of Flags once, and do `Work` and `Ask the person` leave out a reading of the live sprint page whose work is not done, and one whose method names the close of a sprint, except in the brief of the closing run? (its `- [ ] read` line 603 of the 1913 spec)

## Readings at the close

- `make test`: 1494 passed, 6 skipped.
- `make lint`: exit 2, 8 lines (above).
- Live pages: decisions 36, entities 4, estimates 265, insights 1, lessons 31, rules 79; `vault/archive/` holds 2585 `.md` files.
