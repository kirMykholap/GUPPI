# Brief — 2026-10-09, after the librarian run of session 2049

## Where things stand

- Session 2049 ratified Case 751 (751.1–751.6) and Case 752 (handoff, What actually got done).
- Code: `guppi/casecheck.py` — `round_opening` skips a leading horizontal rule; `outside_the_list` passes over a rule before the first Case heading and reads past a rule that a Case heading follows; both notes allow a rule; the module docstring says so. Tests: `tests/test_casecheck.py` four new tests; `tests/test_orchestration.py` `store_of_showing` reads the `ratification` under each Case heading by `split_cases`. Handoff: `make test` 1490 passed, 6 skipped; `make style` clean.
- Readings of the session: L14–L20 `passed` (`estimate-orchestration-sets-off-each-reply-of-case-guppi`, `estimate-orchestration-marks-each-round-of-a-batch`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-refuses-text-outside-the-list`, `estimate-orchestration-showing-example-passes-the-check`, `estimate-case-build-finds-an-existing-judgment`). Lesson: L21 `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`.
- The ledger: 21 lines. The yaml: 19 entries from the ledger (11 `update`, 2 `create`, 5 `estimate`, 1 `lesson`) for lines 1–13, 15–19 and 21; lines 14 and 20 are folded into the `create` entries of lines 1 and 12, so every ledger line is accounted for. 2 entries added by the synthesis. All 21 entries and 8 decision records carry `applied`; 0 `failed`, 0 `exists`, 0 `incomplete`, 0 `near`, 0 `merged`; `unparsed: []`.
- Pages created: decisions 8 (751, 751.1–751.6, 752); estimates 2 (`estimate-orchestration-sets-off-each-reply-of-case-guppi`, `estimate-case-build-finds-an-existing-judgment`, each `passed`); lessons 1 (`lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`, `clustered` by the synthesis).
- Pages updated: rules 3 (`rule-orchestration` by 751.1, 751.2 and 751.6, estimate added by 751.1; `rule-prespec` by 751.3; `rule-case-build` by 752, estimate added); estimates 5 (`estimate-orchestration-marks-each-round-of-a-batch`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-refuses-text-outside-the-list`, `estimate-orchestration-showing-example-passes-the-check` — Criterion replaced whole, sent `pending`, then `passed` by L15–L19); insights 2 (`insight-workflow-case-written-without-reading-the-pages-it-changes` → `actioned`, `addressed_by` `decision-case-752`, by 752; `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` by the synthesis); lessons 1 (`lesson-case-build-task-copies-an-existing-judgment` `clustered` → `archived` by the cascade of its Insight).
- `generate` printed `2026-10-09/0200: 0 page(s) written or changed` and `2026-10-09/2049: 22 page(s) written or changed`. `cleanup` moved 1 page, `lesson-case-build-task-copies-an-existing-judgment`, to `vault/archive/migration/2026-10-09/2049/lessons/`.
- The scripts ticked every box of the 2049 Spec, the five render lines included; no `- [ ]` line stays open. No line of the 2049 Spec holds `guppi sprint-close`; none ran.
- `guppi materialize` named the 0200 yaml of 2026-10-09 ("extended with 0 entries") and wrote the 2049 yaml with 21 entries.
- `render` wrote `vault/wiki/orchestration.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/case-guppi.md`. `guppi sprint` left `sprint.md` unchanged (heading `## migration`). `guppi backlog` rewrote one line of `backlog.md`: `insight-workflow-case-written-without-reading-the-pages-it-changes` left, `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` came in (severity 1). `guppi glossary` left `glossary.md` unchanged. The run added 35 lines to `log.md`. `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` and `archive` printed nothing on stderr.
- `guppi archive` exit 0, no stdout: no unit of a date before 2026-10-09 stands in `vault/raw/`; the units 0200 and 2049 are of the run day and stay.
- Index check: no `create` entry other than the two Estimates; no Grep of a category run, no `merged`, no `near`.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 76 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 36 lines (both run before `generate`).
- `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper` — joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (the claim that the test accepts the changed example was signed on a narrower check, the check functions alone). The Insight was `actioned`, `addressed_by` `decision-case-690.3`; the lesson carries no `addressed_by`, so it is now `open`, severity 1, children 14, `addressed_by` kept; the lesson stands `clustered`.

## Readings due

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand, the person's answer at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run, sections Where things stand, Readings due, Flags, Next session, Readings at the close.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 2049 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 1 page from `cleanup` under `migration/2026-10-09/2049/lessons/`; `guppi archive` exit 0, no stdout.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` heading `## migration`.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 10 finding lines — 1 `deferred`, 9 `unread: pending`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run (method). This run: `make test` 1490 passed, 6 skipped, on the working tree of this run.

## Flags

- No entry marked `failed`, `incomplete`, `near`, `exists` or `unparsed`.
- Failed Estimates: none.
- Insight `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` reopened by the synthesis: `actioned` (by `decision-case-690.3`) → `open`, severity 1.
- Handoff, Direct instructions: `generate` wrote the second pair of 751.6 as given — the line `---`, a blank line, then `## Case 7 — Members get a reminder before a booking`, inside the block tagged `showing` of `rule-orchestration`; `render` carried it into `vault/wiki/orchestration.md`; `uv run pytest tests/test_orchestration.py` on the rendered page: 6 passed.
- Handoff, Direct instructions: the root cause of `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper` was judged against `insight-workflow-case-written-without-reading-the-pages-it-changes`; the lesson did not join it, and that Insight stands `actioned`, `addressed_by` `decision-case-752`. The lesson joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, which opens again (above).
- Handoff, Direct instructions: Cases 751 and 752 ratified twice; the ledger holds 21 lines, the yaml one entry per decision line, none superseded.
- Handoff, Notes from memory: after Case 752 the agent took the person's "Идём работать" as leaving C1 and C2 (`rule-sprint-close`, the close of `migration`) as items of the sprint, closed `[-] … · sprint · defer`, and went on to `/pre-spec` with no further question.
- Handoff, Notes from memory and Observations: the context of Case 751 said `tests/test_orchestration.py` accepts the example as 751.6 changes it, judged by the check functions alone; the test's helper `store_of_showing` failed on it (`assert 0 >= 2`); Retro fixed the helper as work of 751.6 with no task in the Spec.
- Handoff, Observations: `make lint` was red before the work, exit 2, 10 finding lines; this run's `make lint` gives the same 10 lines.
- Stale defers, from the lint: `rule-morph` deferred 3 times since case 239.
- MOC candidates: the lint names none.
- Contradictions: none found.
- The lint: 10 finding lines — 1 `deferred` (`rules/rule-morph`), 9 `unread: pending`; `make lint` exit 2.

## Next session

Cases:
- `rule-sprint-close` and the close of `migration` stay the items of Slice 5; the close takes a session of its own by `/sprint-close` (handoff, For the next session).
- `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`: when a Case changes a live text that a test reads, nothing has `case-guppi` read the test's own helper code over that text, only the check functions the test runs (case 736.1 covers the tests that read a live file, not their helpers); clustered under the reopened `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (handoff, For the next session).

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

- `make test`: 1490 passed, 6 skipped.
- `make lint`: 10 finding lines — 1 `deferred`, 9 `unread: pending`; exit 2.
- Pages under `vault/wiki/`: rules 79, estimates 262, insights 36, lessons 76, decisions 1333, entities 4.
