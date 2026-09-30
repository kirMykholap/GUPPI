# Brief — 2026-09-30, session 1306: the check of case-guppi, recommend on the Decision page, the leading indent of a replace pair

## Where things stand

- Ratified and applied (handoff): 541, 542, 543.1, 543.2, 543.3, 543.4, 544.1 to 544.11; 546 defers `rule-orchestration` and supersedes 545, which was superseded in its own session and left the Spec; its ledger line (39) stands, its entry not applied.
- Code (handoff): `guppi/spec.py`, `guppi/ratified.py`, `guppi/materialize.py` (Retro out of the defer texts, the parent record, a sub-case inheriting `context` and `given` alone), `guppi/generate.py` (the leading indent of a `replace` old, `indent_added_twice`, `## Recommend`, the parent page and `parent`), `guppi/prespec.py` (the indent finding), `guppi/casecheck.py` (the titles of the rounds in `recommend`, no `problem` in a sub-case), `guppi/lint.py` (a parent page, the origin of a parent); tests in seven files. `make test` 964 passed, 3 skipped; `make style` clean.
- Yaml: `raw/2026-09-30/1306/materialize.yaml` 48 entries and 5 of the synthesis; 52 applied, 1 not applied (line 39, case 545, `superseded_by: '546'`, `exists`), none `failed`, none `incomplete`, `unparsed` empty; 21 decision records, the parents 543 and 544 among them, none with `recommend` in `case_text`. Its ledger (48 lines) is held whole by the yaml. `raw/2026-09-30/0248/materialize.yaml` extended with 0 entries; `materialize` added 3 parent decision records to it (534, 538, 539), applied. `raw/2026-09-30/0138/materialize.yaml` extended with 0 entries, unchanged.
- Pages, decisions: 24 created — 21 of session 1306 (541, 542, 543, 543.1 to 543.4, 544, 544.1 to 544.11, 545, 546) and 3 parent pages for Cases of session 0248 (534, 538, 539, `generate: 2026-09-30/0248: 3 page(s) written or changed`); 2 archived (480, superseded by 544.1; 545, superseded by 546).
- Pages, rules: 18 updates on 11 pages (`rule-case-build` ×3, `rule-case-protocol` ×3, `rule-spec-write` ×2, `rule-page-generation` ×2, `rule-case-check` ×2, `rule-spec-capture`, `rule-skill-grill-me`, `rule-prespec`, `rule-materialize`, `rule-decisions-schema`, `rule-lint`); 1 deleted and archived (`rule-case-build-checks-its-sub-cases`, its defer by 480 superseded); 1 defer (`rule-orchestration`, `deferred_by` 424 and 546). Cascade draft → built: `rule-backlog`, `rule-settings`, `rule-sprint`.
- Pages, estimates: 6 created (`estimate-generate-replace-takes-the-leading-indent`, `estimate-prespec-catches-an-indent-added-twice`, `estimate-case-build-checks-the-finished-case`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-refuses-a-problem-in-a-sub-case`); 6 readings (4 passed: `estimate-backlog-renders`, `estimate-sprint-items-move-only-by-a-case`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-settings`; 2 failed: `estimate-glossary-terms-defined`, `estimate-hi-takes-its-readings`); 8 updated with the Criterion replaced whole and set `pending`.
- Pages, entities: `entity-glossary` 2 updates (541, 544.8). Insights: 2 set `actioned` by 544.1 (`insight-case-build-promise-lines-compared-by-no-check`, `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`), 1 created and 1 updated by the synthesis. Lessons: 3 created, 3 updated by the synthesis, 5 archived by the cascade of the two actioned Insights (`lesson-case-build-built-case-departs-from-the-chosen-option`, `lesson-case-build-signs-one-criterion-twice-in-a-session`, `lesson-case-build-writes-a-count-no-command-printed`, `lesson-case-build-frame-count-claimed-over-a-partial-search`, `lesson-case-build-context-claims-an-effect-no-check-covers`).
- Synthesis: `lesson-case-build-context-claims-an-effect-no-check-covers` (`addressed_by: decision-case-544.1`) joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, which 544.1 set `actioned` with `addressed_by` 544.1 in this run; 544.1 is not later than 544.1, so the synthesis update carries no `addressed_by`; the cascade archived the lesson. `lesson-prespec-report-questions-still-off-the-shape` and `lesson-prespec-report-decisions-off-the-question-shape` formed the new `insight-prespec-main-agent-question-off-the-grill-me-shape` (open, severity 2). `lesson-hi-opens-estimate-pages-it-does-not-read` stays `new`.
- Render wrote: `.claude/agents/case-guppi.md`, `.claude/skills/grill-me/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/decisions/schema.yaml` — the five the handoff names. `guppi glossary` rewrote two rows of `glossary.md` (`ref`, `slug`, `supersedes`; Decision page). `backlog.md` 20 items (was 22); `sprint.md` unchanged. The run ticked 48 boxes of `raw/2026-09-30/1306/spec.md` and 4 `read` boxes of `raw/2026-09-30/0248/spec.md`.
- Archive: `guppi archive` exit 0, no stdout and no stderr; `raw/2026-09-30/0138`, `raw/2026-09-30/0248` and `raw/2026-09-30/1306` stay under `raw/` — dated the day of the run, and 1306 the session of the run.

## Readings due

4 Estimates are `failed`, 48 `pending`; each target stands `draft`.

- `estimate-hi-takes-its-readings` — `rule-skill-hi` — failed: at `/hi` of session 1306 the agent opened the pages of five Estimates it did not read; method: by hand at the first `/hi` after the render
- `estimate-glossary-terms-defined` — `entity-glossary` — failed: the row `ref`, `slug`, `supersedes` said each supersede clears the `deferred_by` of its Case; method: one reading of the table by hand after the librarian's run, plus `make lint`. This run: case 541 and 544.8 applied to `entity-glossary`; `guppi glossary` exit 0, no stderr; the diff of `glossary.md` rewrites the rows `ref`, `slug`, `supersedes` and Decision page; `make lint` prints no line on `entity-glossary`
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: the first round on Case 534 ended with a "Files checked:" list; spec 1306: in a later session after the render, one first round and one later round of `case-guppi` read in the chat against the Criterion
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` — failed: the label `**Options:**` stood indented by four spaces in most rounds; spec 1306: in a later session after the render, `uv run guppi render --check`, then one round of `case-guppi` read in the chat against the Criterion
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi read against the event log
- `estimate-brief-written` — `rule-brief` — spec 0248: at the librarian's run after the render. This run: the render did not rewrite `.claude/agents/librarian-guppi.md`; this brief was written under the frame loaded at the start of the run
- `estimate-carry-over-writes` — `rule-carry-over` — spec 0248: at the first `/carry` after the render, and at the `/hi` after it
- `estimate-case-build-checks-the-finished-case` — `rule-case-build` — spec 1306; method: by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case case-guppi built
- `estimate-case-build-records-the-rounds-in-recommend` — `rule-case-build` — spec 1306; method: by hand, the Case files of a later session after the render against the rounds in the chat
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render
- `estimate-case-check-refuses-a-problem-in-a-sub-case` — `rule-case-check` — spec 1306; method: `pytest tests/test_casecheck.py -k problem`
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` — spec 1306; method: `pytest tests/test_casecheck.py -k rounds`, then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-case-form` — `rule-case-protocol` — spec 1306; method: one reading by hand of the Cases of a session, at its close
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` — method: by hand, the Cases of a session at its close against the transcript
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-decisions-schema-checked` — `rule-decisions-schema` — spec 1306; method: `pytest tests/test_schemas.py -k decisions` on the live `decisions/schema.yaml`; the live reading `make lint`
- `estimate-documentation-completes` — `rule-documentation` — method: `make test-documentation`; the live reading by hand
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, then by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-replace-takes-the-leading-indent` — `rule-page-generation` — spec 1306; method: pytest in `tests/test_generate.py` against a temp vault
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading, the librarian's run that applies the first reword. This run: no entry of the three yamls carries `reword`
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` — spec 1306; method: `pytest tests/test_generate.py`, the tests of the decision page; the live reading in the librarian's run. This run: `generate` printed `2026-09-30/1306: 70 page(s) written or changed` and `2026-09-30/0248: 3 page(s) written or changed`, no stderr; 21 Decision pages new for session 1306, `decision-case-543` and `decision-case-544` the records with `children`, 3 new for session 0248 (`decision-case-534`, `decision-case-538`, `decision-case-539`); no `case_text` carries `recommend`; `decision-case-480`, changed by the supersede of 544.1, and `decision-case-545` moved to the archive by cleanup
- `estimate-generate-writes` — `rule-page-generation` — method: pytest in `tests/test_generate.py`; the live reading once by hand
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, then by hand one refused Edit of a governed file
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-lint-finds-a-broken-link` — `rule-lint` — spec 1306; method: `uv run pytest tests/test_lint.py`
- `estimate-materialize-assembles` — `rule-materialize` — spec 1306; method: pytest in `tests/test_materialize.py`; the live reading once by hand
- `estimate-permissions` — `rule-permissions` — method: the person's word on the client's prompt at a Write of `work.md` in Work Mode (Ask the person)
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-prespec-catches-an-indent-added-twice` — `rule-prespec` — spec 1306; method: `pytest tests/test_prespec.py` on a temp plan over temp pages
- `estimate-python-utf8-output-intact` — `rule-python-utf8` — spec 0248: at a later session start; method `uv run guppi render --check`, `json.load` of `.claude/settings.json`, then a Python script through the Bash tool and the Stop line of `guppi context`
- `estimate-retro-commit-gates` — `rule-retro-commit` — method: pytest in `tests/test_gate.py`; the live reading once by hand
- `estimate-retro-loads` — `rule-retro` — method: by hand at the first `/retro`
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — method: `uv run pytest tests/test_onward.py`; by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` names a check under Expected red
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` Baseline holds a failing test or a lint finding line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-phases-in-order` — `rule-session` — method: by hand at the close of a session, the marks of each phase read in order
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi`
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` — spec 1306; method: `uv run pytest tests/test_ratified.py -k write`; by hand, the plan file after the first ratification of a session
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — spec 1306; method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` — spec 1306: `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change, in a later session
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: by hand on the tree at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of `migration`, then git log of `main` after the merge
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` — method: by hand at the first `/work` after the render

## Flags

- `near`: `lesson-case-build-context-claims-an-effect-no-check-covers` near `lesson-case-build-writes-a-count-no-command-printed` (both archived by the cascade this run); `lesson-prespec-report-questions-still-off-the-shape` near `lesson-prespec-report-decisions-off-the-question-shape` (now clustered together).
- No entry `failed`, `incomplete` or `unparsed`. Entry of line 39 (case 545, `defer` of `rule-skill-grill-me`) not applied: `superseded_by: '546'`.
- Failed Estimates: `estimate-hi-takes-its-readings`, `estimate-glossary-terms-defined`, `estimate-case-build-writes-a-plain-round`, `estimate-skill-grill-me-asks-in-rounds`.
- `make test` after the render: 1 failed, 964 passed, 2 skipped. `tests/test_schemas.py::test_a_decision_page_without_context_has_no_finding` (case 513.1) asserts `## Problem` among the sections of the page in shape; the render of `vault/wiki/decisions/schema.yaml` (544.8) made `## Problem` optional, so the page in shape holds `## History` alone. The skipped test of 544.8 now runs.
- Parent Decision pages for Cases of session 0248: `decision-case-534`, `decision-case-538`, `decision-case-539` written by this run (handoff asked to report them).
- Contradiction (handoff): the row `deferred_by` of the glossary and the field texts of `rule-rules-schema` and `rule-entities-schema` say a `supersedes` clears `deferred_by`, without the condition that the superseding Case names the page.
- The root cause of `lesson-prespec-report-questions-still-off-the-shape` also says the lesson of session 0248 does not reach the session that needs it, the pattern of `insight-session-vault-knowledge-not-loaded`; the lesson joined the new Insight of its first cause.
- MOC candidates: none. Stale defer: `rule-subagent-guppi` 31 times since case 29.
- Handoff observations: the indent of `**Options:**` came in most rounds of the session; `work.md` was written through Bash again, and its `## Expected red` by Edit; the Case file of 541 carries a typo in its `context`, left by the person's choice; no dispatch of case-guppi ran between the build of 544.3 and the render of its frame.
- `make lint`: exit 2, 61 finding lines — `rule-spec-box` schema: missing field `kind`, missing field `estimates`, and orphan; `decision-case-13` fence open at the end of `## When`; deferred: `rule-complaint-becomes-a-lesson` 1 time since case 504, `rule-morph` 1 since 239, `rule-orchestration` 2 times since 424, `rule-prespec-script-skips-code-spans` 1 since 481, `rule-subagent-guppi` 31 since 29; unread: 48 `pending` and 4 `failed`, the Estimates of Readings due. Handoff: 85 lines before and after the work; the findings "missing section ## Problem" are gone after the render of `decisions/schema.yaml`.

## Next session

Cases
- `estimate-hi-takes-its-readings` failed: does `/hi` decide the moment of a reading from the method line of the brief alone, or may it open the page to decide? (handoff, For the next session; `lesson-hi-opens-estimate-pages-it-does-not-read`)
- `estimate-glossary-terms-defined` stays failed until its table is read again after this run wrote the row of Case 541 (handoff, For the next session)
- The parent Decision pages this run wrote for Cases of session 0248 (534, 538, 539): keep them, or limit the parent record to the Cases of the unit's own session? (handoff, For the next session)
- The row `deferred_by` of the glossary and the field texts of `rule-rules-schema` and `rule-entities-schema` say a `supersedes` clears `deferred_by` without the condition that the superseding Case names the page (handoff, For the next session)
- `estimate-case-build-writes-a-plain-round` failed; its reading is due in a later session after the render (spec 1306, unticked `read` box)
- `estimate-skill-grill-me-asks-in-rounds` failed; its reading is due in a later session after the render (spec 1306, unticked `read` box)
- `tests/test_schemas.py::test_a_decision_page_without_context_has_no_finding` fails after the render of `vault/wiki/decisions/schema.yaml` of 544.8 (`make test` of this run)

Work
- `estimate-ask-finds`
- `estimate-brief-written` (spec 0248, unticked `read` box)
- `estimate-carry-over-writes` (spec 0248, unticked `read` box)
- `estimate-case-build-checks-the-finished-case` (spec 1306, unticked `read` box)
- `estimate-case-build-records-the-rounds-in-recommend` (spec 1306, unticked `read` box)
- `estimate-case-build-writes-the-case`
- `estimate-case-check-refuses-a-problem-in-a-sub-case` (spec 1306, unticked `read` box)
- `estimate-case-check-requires-each-question-of-the-rounds` (spec 1306, unticked `read` box)
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-case-form` (spec 1306, unticked `read` box)
- `estimate-case-protocol-ledger-line-form`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-compact-recall-reloads`
- `estimate-decisions-schema-checked` (spec 1306, unticked `read` box)
- `estimate-documentation-completes`
- `estimate-end-of-work-order`
- `estimate-event-log-records`
- `estimate-generate-replace-takes-the-leading-indent` (spec 1306, unticked `read` box)
- `estimate-generate-rewords`
- `estimate-generate-writes-the-decision-page` (spec 1306, unticked `read` box)
- `estimate-generate-writes`
- `estimate-governed-files-hook-refuses`
- `estimate-handoff-dispatches`
- `estimate-handoff-holds-each-fact-once`
- `estimate-lint-finds-a-broken-link` (spec 1306, unticked `read` box)
- `estimate-materialize-assembles` (spec 1306, unticked `read` box)
- `estimate-plan-mode-verified`
- `estimate-prespec-catches-an-indent-added-twice` (spec 1306, unticked `read` box)
- `estimate-python-utf8-output-intact` (spec 0248, unticked `read` box)
- `estimate-retro-commit-gates`
- `estimate-retro-loads`
- `estimate-retro-onward-sends-the-agent-to-the-handoff`
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- `estimate-retro-red-in-the-baseline-is-not-charged`
- `estimate-retro-runs-on-to-the-handoff`
- `estimate-session-phases-in-order`
- `estimate-session-start-context`
- `estimate-spec-write-copies-the-ratified-case` (spec 1306, unticked `read` box)
- `estimate-spec-write-reaches-the-approved-spec` (spec 1306, unticked `read` box)
- `estimate-spec-write-writes-a-defer` (spec 1306, unticked `read` box)
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-where-to-stop-stops-only-on-its-conditions`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-work-mode-takes-the-work-readings`
- Ledger line 39 of `raw/2026-09-30/1306/ledger.md` (case 545) not applied: superseded by 546 in its own session

Ask the person
- `estimate-permissions` — needs the person — When the agent changed `vault/raw/2026-09-30/1306/work.md` in Work Mode with the Edit tool, did Claude Code ask you for permission?

## Readings at the close

- `make test`: 1 failed, 964 passed, 2 skipped (Flags).
- `make lint`: exit 2, 61 finding lines (Flags).
- Pages in `vault/wiki/`: rules 74, estimates 167, lessons 69, insights 27, entities 4, decisions 856.
