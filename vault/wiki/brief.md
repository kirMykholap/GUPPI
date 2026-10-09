# Brief — 2026-10-09, after the librarian run of session 0200

## Where things stand

- Session 0200 ratified Case 746 (746.1, 746.2, 746.3), Case 747, Case 748 (748.1, 748.2), Case 749 and the short-form defer Case 750 (handoff, What actually got done).
- Code: `guppi/materialize.py` (`SINGULAR` moved here, `fill_type`, `create_lacks`, `create_fields`); `guppi/generate.py` and `guppi/prespec.py` import `SINGULAR` from it; `guppi/prespec.py` (`check_required` in `judge`); `guppi/casecheck.py` (`changed_create_findings`, `create_line`). Tests: `tests/test_materialize.py` (`type_from_the_category`), `tests/test_prespec.py` (`required_field`, five fixtures given the fields the new check requires), `tests/test_casecheck.py` (`changed_create_line`). Handoff: `make test` 1486 passed, 6 skipped; `make style` clean.
- Readings of the session: L16–L22 `passed` (`estimate-session-phases-in-order`, `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-materialize-fills-the-type-from-the-category`, `estimate-prespec-hook-reports-a-create-without-a-required-field`, `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`). Lesson: L23 `lesson-case-build-task-copies-an-existing-judgment`.
- The handoff closes the `W` line of the four unticked code boxes of Case 733 as work: Case 738 keeps them unticked, and the code landed in its session.
- The ledger: 23 lines. The yaml: 20 entries from the ledger (11 `update`, 3 `create`, 1 `defer`, 4 `estimate`, 1 `lesson`) for lines 1–19 and 23; lines 20, 21 and 22 are folded into the `create` entries of lines 10, 11 and 12, so every ledger line is accounted for. 2 entries added by the synthesis. All 22 entries and 10 decision records carry `applied`; 0 `failed`, 1 `exists` (line 15), 0 `incomplete`, 0 `near`, 0 `merged`; `unparsed: []`; no `new_tags`.
- Pages created: decisions 10 (746, 746.1, 746.2, 746.3, 747, 748, 748.1, 748.2, 749, 750); estimates 3 (`estimate-materialize-fills-the-type-from-the-category`, `estimate-prespec-hook-reports-a-create-without-a-required-field`, `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`, each `passed`); lessons 1 (`lesson-case-build-task-copies-an-existing-judgment`, `clustered` by the synthesis).
- Pages updated: rules 10 (`rule-skill-sprint-open` parent `rule-session-start` and `draft` → `built` by the cascade; `rule-skill-sprint-close` parent `rule-plan-mode` and `draft` → `built` by the cascade; `rule-session` children the five phases alone; `rule-session-start` child `rule-skill-sprint-open` added last; `rule-plan-mode` child `rule-skill-sprint-close` added last; `rule-case-protocol` by 749; `rule-case-check` estimate added by 749, `draft` → `built` by the cascade; `rule-materialize` estimate added by 748.1; `rule-prespec-hook` estimate added by 748.2; `rule-morph` deferred by 750, `deferred_by` now 239, 745 and 750); estimates 4 (`estimate-session-phases-in-order`, `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-case-check-sends-back-a-faulty-round` — sent back `pending`, then `passed`; the last with its Criterion replaced by 747); insights 2 (`insight-ledger-ratified-line-never-withdrawn` `open` → `actioned`, `addressed_by` `decision-case-749`, by 749; `insight-workflow-case-written-without-reading-the-pages-it-changes` by the synthesis); lessons 1 (`lesson-ledger-rebuilt-create-keeps-the-stale-ref` `clustered` → `archived` by the cascade of its Insight).
- `generate` printed `2026-10-08/2352: 0 page(s) written or changed` and `2026-10-09/0200: 31 page(s) written or changed`. `cleanup` moved 1 page, `lesson-ledger-rebuilt-create-keeps-the-stale-ref`, to `vault/archive/migration/2026-10-09/0200/lessons/`.
- The scripts ticked 22 boxes of the 0200 Spec, the render line included; no `- [ ]` line stays open. No line of the 0200 Spec holds `guppi sprint-close`; none ran.
- `guppi materialize` named the 2352 yaml of 2026-10-08 ("extended with 0 entries") and wrote the 0200 yaml with 23 entries.
- `render` wrote `vault/wiki/case-schema.md` (one line, the rebuilt-Case sentence of 749). `guppi sprint` left `sprint.md` unchanged (heading `## migration`). `guppi backlog` rewrote `backlog.md`: `insight-ledger-ratified-line-never-withdrawn` left, `insight-workflow-case-written-without-reading-the-pages-it-changes` came in (severity 1), `rule-morph` put off in 6 sessions. `guppi glossary` left `glossary.md` unchanged. The run added 43 lines to `log.md`. `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` and `archive` printed nothing on stderr.
- `guppi archive` exit 0: it moved the unit 2352 of 2026-10-08 under `vault/archive/migration/2026-10-08/2352/raw`; the session of the run, 0200, stays in `vault/raw/`.
- Index check: no `create` entry other than the three Estimates. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 75 lines; `lesson-case-build-task-copies-an-existing-judgment` matches no index line: no `merged`, no `near`.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 75 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 36 lines (both run before `generate`).
- `lesson-case-build-task-copies-an-existing-judgment` — joined `insight-workflow-case-written-without-reading-the-pages-it-changes` (a Case composed without reading what it runs beside, found only by a later check, pre-spec). The Insight was `actioned`, `addressed_by` `decision-case-734`; it is now `open`, severity 1, children 6; the lesson stands `clustered`.

## Readings due

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand, the person's answer at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run, sections Where things stand, Readings due, Flags, Next session, Readings at the close.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 0200 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 1 page from `cleanup` under `migration/2026-10-09/0200/lessons/`; `guppi archive` exit 0: `archive: raw/2026-10-08/2352 → archive/migration/2026-10-08/2352/raw`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` heading `## migration`.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 10 finding lines — 1 `deferred`, 9 `unread: pending`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run (method). This run: `make test` 1486 passed, 6 skipped, on the working tree of this run.

## Flags

- `exists` on line 15: the `defer` of `rule-morph` by 750, applied to the live page.
- No entry marked `failed`, `incomplete`, `near` or `unparsed`.
- Failed Estimates: none.
- Insight `insight-workflow-case-written-without-reading-the-pages-it-changes` reopened by the synthesis: `actioned` (by `decision-case-734`) → `open`, severity 1.
- Handoff, Direct instructions: `generate` wrote the `set` of 746.1 as the Spec gives it — `rule-skill-sprint-open` parent `rule-session-start`, `rule-skill-sprint-close` parent `rule-plan-mode`; `rule-session-start` and `rule-plan-mode` list the skill last among their children; `rule-session` lists the five phases alone.
- Handoff, Direct instructions: `insight-ledger-ratified-line-never-withdrawn` stands `actioned`, `addressed_by` `decision-case-749`; `lesson-ledger-rebuilt-create-keeps-the-stale-ref` was archived by the cascade and moved by `cleanup`.
- Handoff, Direct instructions: the render changed `vault/wiki/case-schema.md` (one line).
- Handoff, Notes from memory: Case 746 was built as one Case for four Frontier items at the person's word, against the batch form of case 684.1; ledger lines 15 and 19 of session 2352 stand with their stale `{ref:rule-session}`; `ask-guppi` did not check that `generate` writes a `set` of `parent` and `children` as given on an `update` (this run: it did, see above), nor the Spec of case 39.
- Handoff, Notes from memory: the person put off C1 and C2 (`rule-sprint-close`, the close of `migration`) as items of the sprint, and `rule-morph` by the short Case 750.
- Handoff, Observations: `make lint` was red before the work, exit 2, 14 finding lines, `backlog: vault/wiki/backlog.md differs from its sources` among them; this run's `make lint` has no `backlog` line. The staged run of the round check needs a script that sets its stdout to UTF-8; under `python -I` the encoding variable is ignored on this machine.
- Stale defers, from the lint: `rule-morph` deferred 3 times since case 239.
- MOC candidates: the lint names none.
- Contradictions: none found.
- The lint: 10 finding lines — 1 `deferred` (`rules/rule-morph`), 9 `unread: pending`; `make lint` exit 2.

## Next session

Cases:
- `rule-sprint-close` and the close of `migration` stay the items of Slice 5; the close takes a session of its own by `/sprint-close` (handoff, For the next session).
- `lesson-case-build-task-copies-an-existing-judgment`: nothing before `/pre-spec` checks that a task of a Case adds no second copy of a judgment the code already holds; clustered under the reopened `insight-workflow-case-written-without-reading-the-pages-it-changes` (handoff, For the next session).

Work:
- `estimate-hi-takes-a-conserved-spec`
- `estimate-brief-written`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`

Ask the person:
- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?

## Readings at the close

- `make test`: 1486 passed, 6 skipped.
- `make lint`: 10 finding lines — 1 `deferred`, 9 `unread: pending`; exit 2.
- Pages under `vault/wiki/`: rules 79, estimates 260, insights 36, lessons 76, decisions 1325, entities 4.
