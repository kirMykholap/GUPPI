# Brief — 2026-10-01, session 1237: the readings of session 2356, cases 567 to 569, the defers 570 to 576

## Where things stand

- Ratified (handoff): 567.1, 567.2, 568, 569.1, 569.2, and the defers 570 to 576. Cases 567 and 569 were ratified, built again on the findings of `/pre-spec` and ratified again; the ledger holds each decision line once.
- Code and tests (handoff): none changed. `make test` 1034 passed, 2 skipped; `make style` clean.
- Readings (handoff): at `/hi`, ledger lines 1 to 8 — 6 passed, 2 failed (`estimate-documentation-completes`, `estimate-retro-runs-on-to-the-handoff`); in Work Mode, ledger lines 28 to 41 — 11 passed, 3 failed. No lesson.
- Yaml: `raw/2026-10-01/1237/materialize.yaml` 41 entries — 22 `estimate`, 12 `update`, 7 `defer` (all 7 `exists`), 0 `create`, 0 `lesson`; 14 decision records; all 41 entries and all 14 records `applied`. None `failed` or `incomplete`; no `near`, `librarian` or `merged` mark; `unparsed` empty. Its ledger has 41 lines, each held by an entry of the yaml. `raw/2026-09-30/2356/materialize.yaml` was extended with 0 entries; `generate` wrote 0 pages from it and 56 from the 1237 yaml.
- Index check: the yaml holds no `create` other than an Estimate, so no Grep was run. Synthesis: the yaml holds no `lesson` entry, so no Grep was run and no entry was added.
- Pages, decisions: 14 created (567, 567.1, 567.2, 568, 569, 569.1, 569.2, 570 to 576). `cleanup` moved 0 pages.
- Pages, rules: 14 updated — 5 by Cases (`rule-documentation` 567.1, `rule-brief` 567.1 and 567.2, `rule-case-build` and `rule-case-protocol` 568, `rule-retro` 569.1 and 569.2); 3 by defers (`rule-case-rebuild-cost` 570, `rule-orchestration` 574, `rule-prespec-onward` 575); cascade draft → built: `rule-context-size`, `rule-prespec-hook`, `rule-prespec-onward`, `rule-python-utf8`, `rule-retro-onward`, `rule-session`, `rule-where-to-stop`.
- Pages, estimates: 28 updated — 22 readings from ledger lines 1 to 8 and 28 to 41 (17 `passed`, 5 `failed`); 5 by Cases, each set `pending` with its Criterion replaced (`estimate-documentation-completes` 567.1, `estimate-brief-written` 567.2, `estimate-case-build-records-the-rounds-in-recommend` 568 with a new `purpose`, `estimate-retro-runs-on-to-the-handoff` 569.1, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` 569.2); 4 by defers (`estimate-case-build-checks-the-finished-case` 571, `estimate-case-build-writes-a-plain-round` 572, `estimate-spec-write-writes-a-defer` 573, `estimate-estimates-schema-checked` 576). Three of the readings were replaced by a later line of the same run: `estimate-brief-written` (passed, line 1), `estimate-documentation-completes` (failed, line 2) and `estimate-retro-runs-on-to-the-handoff` (failed, line 5) end `pending`.
- Pages, lessons and insights: 0 created, 0 updated.
- Render wrote `.claude/agents/librarian-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/skills/retro/SKILL.md` and `vault/wiki/case-schema.md`. `backlog.md`: 23 → 24 items, `rule-prespec-onward` added (put off in 0 sessions), `rule-case-rebuild-cost` put off in 2 sessions, `rule-orchestration` in 7. `sprint.md` and `glossary.md` unchanged. The run ticked 18 boxes of `raw/2026-10-01/1237/spec.md` and 13 `read` boxes of `raw/2026-09-30/2356/spec.md`; `log.md` 62 lines added.
- Archive: `guppi archive` moved `raw/2026-09-30/2356` to `archive/migration/2026-09-30/2356/raw`; `raw/2026-10-01/1237`, the session of the run, stays. The Spec cited below as spec 2356 now stands under `archive/migration/2026-09-30/2356/raw/spec.md`.

## Readings due

6 Estimates are `failed`, 28 `pending` (the 34 `unread` lines of `make lint`). Every target rule named below stands `draft`; `entity-sprint-migration` stands `draft`.

- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — failed: the Changes paragraph of 567 holds four sentences and those of 568 and 569 three, against one or two, and the Frontier folds 38 open W lines into one line (ledger line 30); method: one reading by hand of the first acknowledging reply of a session
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — `rule-case-protocol` — failed: the reply closing A1 folded the open W lines into one line, against one line per open item (ledger line 35); method: by hand, in a later session, the first Plan Mode reply after the first reply of `/hi` that closes a line of `frontier.md`
- `estimate-prespec-gathers-the-answers-after-findings` — `rule-prespec` — failed: the main agent wrote in the chat twice while answers of `case-guppi` were out (ledger line 37); method: by hand at the `/pre-spec` of a later session whose report sends findings to two or more `case-guppi`
- `estimate-case-build-checks-the-finished-case` — `rule-case-build` — failed: at the `/pre-spec` of session 2356, 2 pages made false and 1 rule acting at the same moment that the Case missed; `deferred_by` 571 (this run); method: by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: parallel clauses in one sentence on Cases 548 and 550 and five examples in one sentence on Case 547 (session 1736); `deferred_by` 572 (this run); method: by hand, in a session after the render, one first round and one later round of `case-guppi`
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` — failed: at the first showing of Case 551 the hook raised on a malformed line, caught the error and exited 0, so nothing of 551 was written (session 1736); `deferred_by` 573 (this run); method: `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule
- `estimate-brief-written` — `rule-brief` — spec 1237: by hand, the brief of the first librarian run whose agent file holds this Render — this run: its frame was the agent file loaded at its start; this run's `render` rewrote `.claude/agents/librarian-guppi.md` from the pages of 567.1 and 567.2
- `estimate-carry-over-writes` — `rule-carry-over` — method: `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode
- `estimate-case-build-records-the-rounds-in-recommend` — `rule-case-build` — spec 1237: by hand, the Case files of a later session after the render, each `recommend` read against the rounds of its Case in the chat
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a create without a ref, one that changes a hook
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` — method: `pytest tests/test_casecheck.py -k rounds`, then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses (spec 2356: in a later session)
- `estimate-case-protocol-asks-in-the-grill-me-shape` — `rule-case-protocol` — method: by hand at the close of a later session, each question of the main agent's own read in the transcript (spec 2356: in a later session)
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the first session where a lesson and the Case that closes its cause stand together, and the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-documentation-completes` — `rule-documentation` — spec 1237: at the first librarian run whose agent file holds this Render: its event log against the Flags of its brief and its report
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, plus by hand at the close of a later session: its folder, the day's event log and git log
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — method: `pytest tests/test_schemas.py -k estimate`; the live reading `make lint`, no schema finding on `wiki/estimates/`; deferred by 576 (this run)
- `estimate-event-log-records` — `rule-event-log` — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading the librarian's run that applies the first reword — this run: the 1237 yaml holds no entry with `reword`; `generate` printed 56 pages written or changed for 1237 and 0 for 2356
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, plus by hand in a later session one Edit of a governed file refused
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session: the event log, `handoff.md`, the dispatch line and git log
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: one reading by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — spec 1237: in a later session
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — spec 1237: in a later session
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi` whose reply carries a LEDGER block, and the ledger of the next working session after its first ratification
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of migration, then git log of main after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` — method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the 1237 yaml holds 0 lesson entries; the 2356 yaml was extended with 0 entries
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types

## Flags

- Entries marked `incomplete`, `failed`, `near` or `unparsed`: none.
- `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no line on stderr.
- Failed Estimates: 6 — `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-prespec-gathers-the-answers-after-findings` (this run); `estimate-case-build-checks-the-finished-case`, `estimate-case-build-writes-a-plain-round`, `estimate-spec-write-writes-a-defer` (earlier, deferred by 571, 572, 573 in this run).
- MOC candidates: none.
- Stale defers (`make lint`): `rule-subagent-guppi` 31 times since case 29; `rule-orchestration` 3 times since case 424; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 since 504; `rule-morph` 1 since 239; `rule-prespec-script-skips-code-spans` 1 since 481.
- `rule-prespec-onward`: deferred by case 575 and moved draft → built by the cascade in the same run; `backlog.md` lists it, put off in 0 sessions.
- The defers 571, 572, 573 and 576 target Estimates, which carry no `deferred_by` (handoff, Direct instructions).
- Contradictions: none found.
- `make lint` (before the brief): `render --check`, `sprint --check`, `backlog --check` and `glossary --check` passed; `guppi lint` exit 1 with 44 lines — `rules/rule-spec-box` schema: missing field `kind`, missing field `estimates`; `decisions/decision-case-13` fence: an open code fence at the end of `## When`; `rules/rule-spec-box` orphan; 6 `deferred` lines (above); 34 `unread` lines (the Estimates of Readings due).
- Handoff, Direct instructions: no instruction to repair a yaml entry.
- Reads beyond the reads the frame names: none.

## Next session

Cases
- `estimate-case-protocol-acknowledging-reply` failed: the Changes paragraph held three or four sentences against one or two, and the Frontier folded the open `W` lines into one line (handoff, For the next session).
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` failed: whether a later Frontier may fold the open `W` lines as the first reply of `/hi` does (handoff, For the next session).
- `estimate-prespec-gathers-the-answers-after-findings` failed: whether the clause should allow one short line per notification turn (handoff, For the next session).
- The silent `Stop` after the reply that ended Retro: whether it needs a check or a fallback (handoff, For the next session).
- `estimate-case-build-checks-the-finished-case` failed, deferred by 571 (Readings due).
- `estimate-case-build-writes-a-plain-round` failed, deferred by 572 (Readings due).
- `estimate-spec-write-writes-a-defer` failed, deferred by 573 (Readings due).
- The close of a sprint and a sprint item left for later, put off by the person (handoff, Notes from memory).

Work
- `estimate-ask-finds`
- `estimate-brief-written` (box in spec 1237)
- `estimate-carry-over-writes`
- `estimate-case-build-records-the-rounds-in-recommend` (box in spec 1237)
- `estimate-case-build-writes-the-case`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-shows-only-the-checked-case` (box in spec 2356)
- `estimate-case-protocol-asks-in-the-grill-me-shape` (box in spec 2356)
- `estimate-case-protocol-ledger-line-form`
- `estimate-compact-recall-reloads`
- `estimate-documentation-completes` (box in spec 1237)
- `estimate-end-of-work-order`
- `estimate-estimates-schema-checked`
- `estimate-event-log-records`
- `estimate-generate-rewords`
- `estimate-governed-files-hook-refuses`
- `estimate-handoff-dispatches`
- `estimate-handoff-holds-each-fact-once`
- `estimate-plan-mode-verified`
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` (box in spec 1237)
- `estimate-retro-runs-on-to-the-handoff` (box in spec 1237)
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-synthesis-clusters`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

Ask the person
- none

## Readings at the close

- `make test`: 1034 passed, 2 skipped.
- `make lint`: exit 2 at `guppi lint`, 44 lines (2 schema, 1 fence, 1 orphan, 6 deferred, 34 unread); the four `--check` steps passed.
- Pages under `vault/wiki/`: decisions 914, rules 76, estimates 182, lessons 74, insights 28, entities 4.
