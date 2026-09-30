# Brief — 2026-09-30, session 1736: the Frontier after a closed line, the ledger hook that swallowed a parse error, readings taken

## Where things stand

- Ratified (handoff): 547, 548, 549, 550, 552.1 to 552.4; defers 551 (`rule-case-build`) and 553 (`rule-ask`). 547, 548 and 552 were built again after pre-spec and ratified again.
- Code (handoff): `guppi/materialize.py` (`parse_line` reads a space between brackets and gives None for a line it cannot read; the module docstring points to `rule-case-protocol` on `deferred_by`), `guppi/ledger.py` (a line it cannot read is refused; exit 2 on its own error after the payload is read, exit 0 on a payload it cannot read). Tests: `tests/test_materialize.py`, `tests/test_ledger.py`, `tests/test_schemas.py` (three skips became asserts). `make test` 984 passed, 2 skipped; `make style` clean.
- Yaml: `raw/2026-09-30/1736/materialize.yaml` 44 entries and 2 of the synthesis, all 46 applied; 11 decision records, all applied; none `failed`, `incomplete` or `near`; `unparsed` empty. Its ledger has 44 lines, each held by an entry of the yaml. `raw/2026-09-30/0138`, `0248` and `1306` yamls extended with 0 entries; `generate` wrote 0 pages from them.
- Pages, decisions: 11 created (547, 548, 549, 550, 551, 552, 552.1, 552.2, 552.3, 552.4, 553); 3 updated with one History line each by 550 (`decision-case-534`, `decision-case-538`, `decision-case-539`).
- Pages, rules: 9 updates on 8 pages (`rule-ledger-write` ×2 — both `replace` pairs of 552.2 and 552.4 applied —, `rule-case-protocol`, `rule-rules-schema`, `rule-entities-schema`, `rule-insights-schema`, `rule-prespec`, `rule-backlog`, `rule-materialize`); 2 defers (`rule-case-build` `deferred_by` 551, `rule-ask` `deferred_by` 553). Cascade draft → built: `rule-brief`, `rule-lint`, `rule-materialize`, `rule-permissions`, `rule-prespec`, `rule-skill-grill-me`, `rule-skill-hi`; built → draft: `rule-ledger-write`.
- Pages, estimates: 3 created (`estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-ledger-write-exits-2-on-an-error`); 2 updated (`estimate-decisions-schema-checked` its `method` alone, 548; `estimate-ledger-write-lifts` its Criterion replaced whole and set `pending`, 552.3); 22 reading lines on 21 Estimates — 16 lines `passed` on 15 (`estimate-brief-written`, `estimate-generate-writes-the-decision-page`, `estimate-permissions`, `estimate-glossary-terms-defined`, `estimate-hi-takes-its-readings`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-case-check-refuses-a-problem-in-a-sub-case`, `estimate-generate-replace-takes-the-leading-indent`, `estimate-generate-writes`, `estimate-lint-finds-a-broken-link`, `estimate-materialize-assembles`, `estimate-prespec-catches-an-indent-added-twice`, `estimate-spec-write-copies-the-ratified-case` from ledger lines 29 and 30, `estimate-case-protocol-case-form`, `estimate-work-mode-takes-the-work-readings`), 6 `failed`.
- Pages, entities: `entity-glossary` 1 update (549), draft → built. Lessons: 2 created. Insights: 1 updated by the synthesis.
- Synthesis: `lesson-case-protocol-own-text-before-a-round` joined `insight-case-form-chat-form-read-by-no-script`, which was `actioned` (`addressed_by` 537); the lesson carries no `addressed_by`, so the Insight is set `open` again and the lesson `clustered`. `lesson-ledger-hook-swallows-a-parse-error` (`addressed_by` 552.4 in its ledger line) found no lesson or Insight of its cause and stays `new`.
- Render wrote the five files the handoff names: `vault/wiki/case-schema.md`, `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml`, `vault/wiki/insights/schema.yaml`, `.claude/skills/pre-spec/SKILL.md`. `guppi glossary` rewrote the rows `ref`, `slug`, `supersedes` and `deferred_by` of `glossary.md`. `backlog.md` 23 items (was 20: `rule-ask`, `rule-case-build`, `insight-case-form-chat-form-read-by-no-script` added); `sprint.md` unchanged. The run ticked 24 boxes of `raw/2026-09-30/1736/spec.md`, 13 `read` boxes of `raw/2026-09-30/1306/spec.md` and 1 of `raw/2026-09-30/0248/spec.md`; `log.md` 69 lines added.

## Readings due

6 Estimates are `failed`, 35 `pending` (the `unread` lines of `make lint`).

- `estimate-case-build-checks-the-finished-case` — `rule-case-build` — failed: the report of ask-guppi at `/pre-spec` of 1736 held 1 frame hit found by meaning and missed (547 against `rule-skill-hi`) and 2 claims of context not borne out by their search (548, 552); method: by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case case-guppi built
- `estimate-case-build-records-the-rounds-in-recommend` — `rule-case-build` — failed: the item of Q2 of Case 549 gives the first recommendation, which Q3 replaced; method: by hand, the Case files of a later session after the render against the rounds in the chat
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: the sentence on what the round decides runs parallel clauses in one sentence on 548 and 550, and the Context of 547 names five examples in one sentence; method: by hand in a session after the render, one first round and one later round of case-guppi
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` — failed: the main agent wrote a line of its own before the first question of each round; method: by hand, the Cases of a session at its close against the transcript
- `estimate-documentation-completes` — `rule-documentation` — failed: the librarian's run of 070d8e6 read beyond its list (git status over `vault/wiki/decisions/`, a grep of git status for `vault/archive`, the target, status and method of 52 Estimate pages, a grep over every Decision page for a count); method: `make test-documentation`; the live reading by hand
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` — failed: at the first showing of Case 551 the hook raised on a malformed line, caught the error and exited 0, so nothing of 551 was written; method: `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi read against the event log
- `estimate-carry-over-writes` — `rule-carry-over` — spec 0248: at the first `/carry` after the render, and at the `/hi` after it
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` — spec 1306; method: `pytest tests/test_casecheck.py -k rounds`, then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — `rule-case-protocol` — spec 1736; method: by hand in a later session, the first reply in Plan Mode after the first reply of `/hi` that closes a Frontier line with no ratification and no defer
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-decisions-schema-checked` — `rule-decisions-schema` — spec 1306; method: `pytest tests/test_schemas.py -k decision` on the live `decisions/schema.yaml`; the live reading `make lint`, no schema finding on `wiki/decisions/`
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, then by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading, the librarian's run that applies the first reword. This run: no entry of the four yamls carries `reword`
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, then by hand one refused Edit of a governed file
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-ledger-write-exits-2-on-an-error` — `rule-ledger-write` — spec 1736: in a later session; method: `uv run pytest tests/test_ledger.py`, a function of the hook patched to raise
- `estimate-ledger-write-lifts` — `rule-ledger-write` — spec 1736: in a later session; method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; the live reading once by hand
- `estimate-ledger-write-refuses-a-line-it-cannot-read` — `rule-ledger-write` — spec 1736: in a later session; method: `uv run pytest tests/test_ledger.py`
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-python-utf8-output-intact` — `rule-python-utf8` — spec 0248: at a later session start
- `estimate-retro-commit-gates` — `rule-retro-commit` — method: pytest in `tests/test_gate.py`; the live reading once by hand
- `estimate-retro-loads` — `rule-retro` — method: by hand at the first `/retro`
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — method: `uv run pytest tests/test_onward.py`; by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` names a check under Expected red
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` Baseline holds a failing test or a lint finding line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-phases-in-order` — `rule-session` — method: by hand at the close of a session, the marks of each phase read in order
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi`
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — spec 1306; method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: by hand on the tree at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of `migration`, then git log of `main` after the merge
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types

## Flags

- No entry `failed`, `incomplete`, `near` or `unparsed` in the four yamls.
- Failed Estimates: `estimate-case-build-checks-the-finished-case`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-build-writes-a-plain-round`, `estimate-case-protocol-shows-the-built-case`, `estimate-documentation-completes`, `estimate-spec-write-writes-a-defer`.
- `insight-case-form-chat-form-read-by-no-script` set `open` again by the synthesis (was `actioned` by 537).
- Handoff, Observations: five readings whose moment was this Retro, "to read from this file and transcript" (`estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-loads`, `estimate-retro-runs-on-to-the-handoff`, `estimate-handoff-holds-each-fact-once`, `estimate-where-to-stop-stops-only-on-its-conditions`), have no line in the ledger of 1736; all five stand `pending`.
- Handoff, Observations: the code of 552.1 was built before the Spec and the Baseline, by the person's choice; `guppi ratified`, `guppi casecheck`, `guppi context` and `guppi onward` still catch their own errors and exit 0, and `guppi ratified` lost the first showing of Case 551 that way; the method of `estimate-estimates-schema-checked` runs `-k estimates`, which does not select the test of `method` on an Estimate page.
- MOC candidates: none. Contradictions: none found by this run. Stale defer: `rule-subagent-guppi` 31 times since case 29.
- `make lint`: exit 2, 50 finding lines — `rule-spec-box` schema: missing field `kind`, missing field `estimates`, and orphan; `decision-case-13` fence open at the end of `## When`; deferred: `rule-complaint-becomes-a-lesson` 1 time since case 504, `rule-morph` 1 since 239, `rule-orchestration` 2 times since 424, `rule-prespec-script-skips-code-spans` 1 since 481, `rule-subagent-guppi` 31 since 29; unread: 35 `pending` and 6 `failed`, the Estimates of Readings due. Handoff: 61 lines before and after the work.

## Next session

Cases
- The other `Stop` hooks swallow their errors with exit 0, as the ledger hook did: give them the exit 2 of case 552.4, or keep them as they are? (handoff, For the next session; Observations name `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward`)
- `estimate-estimates-schema-checked`: its method selects no test of `method`; set it to a command that runs that test (handoff, For the next session)
- `estimate-case-build-checks-the-finished-case` failed: a frame hit found by meaning missed, Grep claims misreported — its fix to decide (handoff, For the next session)
- `estimate-case-protocol-shows-the-built-case` failed: own text before a round — its fix to decide (handoff, For the next session; `insight-case-form-chat-form-read-by-no-script` reopened)
- `estimate-case-build-records-the-rounds-in-recommend` failed: an item keeps a replaced recommendation — its fix to decide (handoff, For the next session)
- `estimate-documentation-completes` failed: the librarian read beyond its list — its fix to decide (handoff, For the next session)
- `estimate-spec-write-writes-a-defer` failed: the hook swallowed an error — its fix to decide (handoff, For the next session)
- `estimate-case-build-writes-a-plain-round` failed; its target `rule-case-build` stands deferred by 551 (ledger line 19, backlog)

Work
- `estimate-ask-finds`
- `estimate-carry-over-writes` (spec 0248, unticked `read` box)
- `estimate-case-build-writes-the-case`
- `estimate-case-check-requires-each-question-of-the-rounds` (spec 1306, unticked `read` box)
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-ledger-line-form`
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` (spec 1736, unticked `read` box)
- `estimate-compact-recall-reloads`
- `estimate-decisions-schema-checked` (spec 1306, unticked `read` box)
- `estimate-end-of-work-order`
- `estimate-event-log-records`
- `estimate-generate-rewords`
- `estimate-governed-files-hook-refuses`
- `estimate-handoff-dispatches`
- `estimate-handoff-holds-each-fact-once`
- `estimate-ledger-write-exits-2-on-an-error` (spec 1736, unticked `read` box)
- `estimate-ledger-write-lifts` (spec 1736, unticked `read` box)
- `estimate-ledger-write-refuses-a-line-it-cannot-read` (spec 1736, unticked `read` box)
- `estimate-plan-mode-verified`
- `estimate-python-utf8-output-intact` (spec 0248, unticked `read` box)
- `estimate-retro-commit-gates`
- `estimate-retro-loads`
- `estimate-retro-onward-sends-the-agent-to-the-handoff`
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- `estimate-retro-red-in-the-baseline-is-not-charged`
- `estimate-retro-runs-on-to-the-handoff`
- `estimate-session-phases-in-order`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec` (spec 1306, unticked `read` box)
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-where-to-stop-stops-only-on-its-conditions`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

Ask the person
none

## Readings at the close

- `make test`: 984 passed, 2 skipped.
- `make lint`: exit 2, 50 finding lines (Flags).
- Pages in `vault/wiki/`: rules 74, estimates 170, lessons 71, insights 27, entities 4; decisions not counted (the librarian does not read `wiki/decisions/`).
