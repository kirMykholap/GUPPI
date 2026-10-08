# Brief — 2026-10-08, after the librarian run of session 2352

## Where things stand

- Session 2352 ratified Case 743 (743.1–743.9), Case 744 (744.1, 744.2) and the short-form defer 745. Case 743 was ratified, built again on the findings of `/pre-spec` and ratified again (handoff, What actually got done).
- Code: `guppi/archive.py` (`sweep`, `unit_sprint`); `guppi/sprint_close.py` (`empty_raw`, `old_logs`, `move_logs`, `remove_empty_dates`); `guppi/sprint.py` (`item_statuses`, `is_done`, `closed_heading`, `closed_form`, `closed_id`, `hi_hook`, the `--hi` flag, the closed form of `run` and `--check`, an error on two sprint pages); `guppi/backlog.py` (`item_bodies`, `taken_by`, `finished`); `guppi/casecheck.py` (`AFTER_LINE`, `AFTER_LINES`); `.gitignore` (`vault/archive/*/*/event_log.md`). Tests: `tests/test_archive.py`, `tests/test_sprint_close.py`, `tests/test_sprint.py`, `tests/test_backlog.py`, `tests/test_casecheck.py`. Handoff: `make test` 1466 passed, 6 skipped; `make style` clean.
- Readings of the session: L29–L36 `passed` (`estimate-sprint-close-sweeps-raw`, `estimate-raw-archive-files-a-session-by-its-sprint`, `estimate-sprint-close-moves-old-event-logs`, `estimate-backlog-renders`, `estimate-sprint-marks-a-closed-sprint`, `estimate-sprint-checks-the-file`, `estimate-skill-sprint-open-starts-at-hi`, `estimate-skill-grill-me-asks-in-rounds`); L37–L39 `failed` (`estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-case-check-sends-back-a-faulty-round`). Lessons: L40 `lesson-case-build-rule-create-without-type`, L41 `lesson-ledger-rebuilt-create-keeps-the-stale-ref`.
- The ledger: 41 lines. The yaml: 34 entries from the ledger (11 `create`, 16 `update`, 1 `defer`, 4 `estimate`, 2 `lesson`) for lines 1–28, 32, 34, 36 and 39–41; lines 29, 30, 31, 33, 35, 37 and 38 are folded into the `create` entries of lines 3, 5, 8, 13, 18, 16 and 20, so every ledger line is accounted for. 2 entries added by the synthesis. All 36 entries and 14 decision records carry `applied`; 0 `failed`, 1 `exists` (line 26), 4 `incomplete` (lines 15, 19, 27, 28), 0 `near`, 0 `merged`; `unparsed: []`; no `new_tags`.
- `generate` printed on stdout: `rule-skill-sprint-open: line 27 repeats line 15 of case 743.6; nothing applied` and `rule-skill-sprint-close: line 28 repeats line 19 of case 743.8; nothing applied`. The pages were written from lines 15 and 19.
- Pages created: decisions 14 (743, 743.1–743.9, 744, 744.1, 744.2, 745); rules 2 (`rule-skill-sprint-open`, `rule-skill-sprint-close`, each `draft`, `type: rule` on the page, `parent: "[[rule-session]]"`); estimates 7 (`estimate-sprint-close-sweeps-raw`, `estimate-raw-archive-files-a-session-by-its-sprint`, `estimate-sprint-close-moves-old-event-logs`, `estimate-sprint-marks-a-closed-sprint`, `estimate-skill-sprint-open-starts-at-hi` — each `passed`; `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session` — each `failed`); lessons 2.
- Pages updated: rules 11 (`rule-sprint-close` by 743.1 and 743.3, its defer by `decision-case-718` superseded; `rule-raw-archive` by 743.1, 743.2, 743.3; `rule-backlog` by 743.4, then `draft` → `built` by the cascade; `rule-sprint` and `rule-documentation` by 743.5; `rule-hook-registry` by 743.7; `rule-orchestration` by 743.8; `rule-skill-grill-me` by 744.1; `rule-morph` deferred by 745, `deferred_by` now 239 and 745; `rule-session` — children `rule-skill-sprint-open` and `rule-skill-sprint-close` added; `rule-case-check` `built` → `draft` by the cascade); estimates 4 (`estimate-backlog-renders`, `estimate-sprint-checks-the-file`, `estimate-skill-grill-me-asks-in-rounds` — Criterion replaced, then `passed`; `estimate-case-check-sends-back-a-faulty-round` — Criterion replaced, then `failed`); entities 1 (`entity-sprint-migration` by 743.8); insights 1 (`insight-ledger-ratified-line-never-withdrawn`, synthesis); lessons 1 (`lesson-ledger-rebuilt-create-keeps-the-stale-ref` set `clustered`, synthesis).
- `decision-case-718` stands `superseded` by `decision-case-743.1`; `cleanup` moved it (`cleanup: 1 page(s) moved`) to `vault/archive/migration/2026-10-09/2352/decisions/`.
- The scripts ticked every box of the 2352 Spec; none stays open. No line of the 2352 Spec holds `guppi sprint-close`; none ran.
- `guppi materialize` named the 0050, 0213, 1547 and 2134 yamls of 2026-10-08 ("extended with 0 entries"); `generate` wrote 0 pages from each and 43 from the 2352 yaml.
- `render` wrote `.claude/agents/librarian-guppi.md`, `.claude/settings.json`, `.claude/skills/grill-me/SKILL.md`, `vault/wiki/orchestration.md`, and the new `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/sprint-close/SKILL.md`. `guppi sprint` rewrote `sprint.md` (heading `## migration`, Slice 5 holds `rule-sprint-close` and the close line ``the close of `migration` — `/sprint-close`, a session of its own``). `guppi backlog` rewrote `backlog.md` (6 items → 5: `rule-sprint-close` and the merge line left, `insight-ledger-ratified-line-never-withdrawn` came in). `guppi glossary` left `glossary.md` unchanged. The run added 70 lines to `log.md`. `generate`, `cleanup`, `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- `guppi archive` exit 0, no stderr: it moved the units 0050, 0213, 1547 and 2134 of 2026-10-08 under `vault/archive/migration/2026-10-08/`; the session of the run, 2352, stays in `vault/raw/`.
- Index check: `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 79 lines; `rule-skill-sprint-open` (lines 15, 27) and `rule-skill-sprint-close` (lines 19, 28) match no index line: no `merged`, no `near`. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 74 lines; neither lesson matches an index line: no `merged`, no `near`.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 74 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 36 lines (both run before `generate`).
- `lesson-ledger-rebuilt-create-keeps-the-stale-ref` — joined `insight-ledger-ratified-line-never-withdrawn` (the ledger never withdraws the line of a first ratification of a rebuilt Case). The Insight was `actioned`, `addressed_by` `decision-case-725.1`; it is now `open`, severity 1, children 4; the lesson stands `clustered`.
- `lesson-case-build-rule-create-without-type` — none: no lesson and no Insight names a missing check of the fields `materialize` requires of a `create` item before the Spec; `insight-materialize-lift-loses-a-schema-field` covers a field the parser drops, and `insight-workflow-case-schema-silent-on-what-the-scripts-accept` a schema silent on a form the scripts read. The lesson stays `new`.

## Readings due

Failed:
- `estimate-skill-sprint-open-asks-the-opening-questions` — failed — `rule-skill-sprint-open` stands `draft` — read: by hand, at the Retro of the session that creates it, the new Render of `rule-skill-sprint-open` in the Spec read against the Criterion (method). Result: Retro, not read; both `create` entries of `rule-skill-sprint-open` marked `incomplete: [type]`, the then block of 743.6 holds no `type: rule`.
- `estimate-skill-sprint-close-leads-the-closing-session` — failed — `rule-skill-sprint-close` stands `draft` — read: by hand, at the Retro of the session that creates it, the new Renders of `rule-skill-sprint-close` and `rule-orchestration` and the update of `entity-sprint-migration` in the Spec read against the Criterion (method). Result: Retro, not read; both `create` entries of `rule-skill-sprint-close` marked `incomplete: [type]`, the then block of 743.8 holds no `type: rule`.
- `estimate-case-check-sends-back-a-faulty-round` — failed — `rule-case-check` stands `draft` — read: `uv run pytest tests/test_casecheck.py -k round_form`, then by hand a round the hook sends back live (method). Result: Retro, not read; the pytest part 13 passed, the by-hand part did not occur after the change.

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: the unticked `- [ ] read` line of the 0050 Spec, now `vault/archive/migration/2026-10-08/0050/raw/spec.md`; the method: by hand, the person's answer at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run, sections Where things stand, Readings due, Flags, Next session, Readings at the close.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 2352 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 1 page from `cleanup` under `migration/2026-10-09/2352/decisions/`; `guppi archive` exit 0: `archive: raw/2026-10-08/0050 → archive/migration/2026-10-08/0050/raw`, `archive: raw/2026-10-08/0213 → archive/migration/2026-10-08/0213/raw`, `archive: raw/2026-10-08/1547 → archive/migration/2026-10-08/1547/raw`, `archive: raw/2026-10-08/2134 → archive/migration/2026-10-08/2134/raw`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` heading `## migration`.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 13 finding lines — 1 `deferred`, 3 `unread: failed`, 9 `unread: pending`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run (method). This run: `make test` 1466 passed, 6 skipped, on the working tree of this run.

## Flags

- `incomplete: [type]` on lines 15 and 27 (`create` of `rule-skill-sprint-open`) and lines 19 and 28 (`create` of `rule-skill-sprint-close`). The pages were written from lines 15 and 19 and hold `type: rule`.
- Lines 15 and 19 carry `ref: rule-session`; lines 27 and 28 (`rule-session-start`, `rule-plan-mode`) were not applied as repeats. Both rule pages stand with `parent: "[[rule-session]]"`, and `rule-session` lists them among its children, against Case 743, which hangs them under `rule-session-start` and `rule-plan-mode`. The handoff says such a backlink breaks `estimate-session-phases-in-order`; that Estimate stands `passed`, and this run did not read it.
- `exists` on line 26: the `defer` of `rule-morph` by 745, applied to the live page.
- No entry marked `failed`, `near` or `unparsed`.
- Failed Estimates: `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-case-check-sends-back-a-faulty-round` (Readings due).
- Handoff, Direct instructions: the new Estimates of `rule-skill-sprint-open` and `rule-skill-sprint-close` were expected to miss their backlink; the two rule pages were created from lines 15 and 19 and list them in `estimates`, so no backlink is missing.
- Handoff, Direct instructions: `rule-orchestration` lost the paragraph on the closing session; the render wrote `.claude/skills/sprint-close/SKILL.md` from `rule-skill-sprint-close`, so the steps stand in that skill.
- Handoff, Direct instructions: `vault/wiki/backlog.md` was written in Work Mode; this run wrote it again (5 items).
- Handoff, Notes from memory: the person went against the recommendation on the Backlog of a closed sprint (the opening only gives the count of `backlog.md`); the person replaced a `sprint` key in `guppi.toml` with the closed mark in `sprint.md`; the person asked for two skills and a hook on `/hi`.
- Handoff, Notes from memory: at `/pre-spec` `estimate-sprint-migration-leftovers-gone` and `estimate-sprint-migration-merges` keep a reason the change makes out of date; their Criteria change only in the session that reads them.
- Handoff, Observations: `make lint` was red before the work, exit 2, 12 finding lines; the line `backlog: vault/wiki/backlog.md differs from its sources` is gone. The method `-k hi` of `estimate-skill-sprint-open-starts-at-hi` selects 7 tests, two of them the tests of the hook. The hook `guppi sprint --hi` runs once the render writes its registration into `.claude/settings.json`; this run's render rewrote that file.
- Insight `insight-ledger-ratified-line-never-withdrawn` reopened by the synthesis: `actioned` (by `decision-case-725.1`) → `open`, severity 1.
- Contradictions: the parent of the two new skill rules (above).
- Stale defers, from the lint: `rule-morph` deferred 2 times since case 239.
- MOC candidates: the lint names none.
- The lint: 13 finding lines — 1 `deferred` (`rules/rule-morph`), 3 `unread: failed`, 9 `unread: pending`; `make lint` exit 2.

## Next session

Cases:
- Build 743.6 and 743.8 again with `type: rule` on the `create` items of `rule-skill-sprint-open` and `rule-skill-sprint-close`, and with marks that retire ledger lines 15 and 19, whose `{ref:rule-session}` is stale (handoff, For the next session).
- The two skill rules stand under `rule-session`, not under `rule-session-start` and `rule-plan-mode` as Case 743 says; `estimate-session-phases-in-order` stands `passed` (defect found by this run).
- `estimate-skill-sprint-open-asks-the-opening-questions` — failed (Readings due).
- `estimate-skill-sprint-close-leads-the-closing-session` — failed (Readings due).
- `estimate-case-check-sends-back-a-faulty-round` — failed: its method asks for a round the hook sends back live, which did not occur after the change (handoff, For the next session).
- `lesson-case-build-rule-create-without-type`: no check before the Spec judges the fields `materialize` requires of a `create` item (handoff, For the next session).
- `lesson-ledger-rebuilt-create-keeps-the-stale-ref`: a rebuilt Case that changes the `ref` of a `create` line leaves the first line, with its stale ref, as an entry of the yaml; clustered under the reopened `insight-ledger-ratified-line-never-withdrawn` (handoff, For the next session).
- The close of `migration` and its session of its own stay open (handoff, For the next session).
- `rules/rule-morph: deferred` 2 times since case 239 stays a lint finding until a Case decides `rule-morph` (lint).

Work:
- `estimate-hi-takes-a-conserved-spec`
- `estimate-brief-written`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- The 4 unticked code boxes of Case 733 in the 0213 Spec, moved by `guppi archive` to `vault/archive/migration/2026-10-08/0213/raw/spec.md` (`guppi/lint.py`, `guppi/prespec.py`, `tests/test_prespec.py`, `tests/test_lint.py`); Case 738 keeps them unticked.

Ask the person:
- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?

## Readings at the close

- `make test`: 1466 passed, 6 skipped.
- `make lint`: 13 finding lines — 1 `deferred`, 3 `unread: failed`, 9 `unread: pending`; exit 2.
- Pages under `vault/wiki/`: rules 79, estimates 257, insights 36, lessons 76, decisions 1315, entities 4.
