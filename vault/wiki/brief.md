# Brief

## Where things stand

Session 1432 of 2026-09-29, sprint `migration`. Slice 4 closed; the round and the Decision page made readable. Ratified: 510, 511.1, 512, 513.1, 513.2, 513.3, 514, 515, 516, 517, 518, 519 (511.2 superseded by 512 in the same session). Commits d2ad75d (code of 513.2, 514, 516, and the deletions of 510: `vault/parked/` and every file under `docs/` but `docs/migration/migration-plan.md`; the commit message names the code only) and 9c8075f (the session folder); `guppi/generate.py`, `tests/test_generate.py`, `tests/test_schemas.py`, `tests/test_materialize.py` changed; readings L1–L5 and L25–L31; lessons L32–L35. `vault/wiki/sprint.md` now opens its milestones at Slice 5 (case 510).

Not done, from the handoff:
- the reading of `estimate-glossary-terms-defined` under Case 515 waits for a session after this run;
- the Render of `rule-estimates-schema` says the frame of a Case stays on its Decision page — short defer, Case 519;
- a repeat of Case 514 ticks its line of the Spec, as an applied entry does, while the task line said "apply nothing";
- lessons L32–L35.

The run over `vault/raw/2026-09-29/1432/materialize.yaml`: 36 entries from 36 ledger lines, plus 7 of the synthesis; 41 applied, 2 superseded (L9, L10, case 511.2), 0 failed, 3 `exists` (the defers of 517, 518, 519, applied). The 0137 and 1134 yaml were extended with 0 entries; L67 of the 1134 yaml, failed in the last run, is now marked applied: `generate: rule-skill-hi: line 67 repeats line 15 of case 508.2; nothing applied` (case 514). `generate` printed 56 pages written or changed for 1432.

- Created: lessons 4 (`lesson-case-build-closes-a-sprint-item-without-the-sprint-page`, `lesson-case-build-quotes-the-person-in-the-chat-language`, `lesson-case-build-writes-a-count-no-command-printed`, `lesson-case-build-splits-a-case-whose-line-stands`), decisions 13 (510, 511.1, 511.2, 512, 513.1–513.3, 514–519).
- Updated by entry: rules 5 (`rule-skill-grill-me`, `rule-case-build`, `rule-decisions-schema`, `rule-case-protocol`, `rule-page-generation`) and 3 defers (`rule-documentation`, `rule-case-protocol`, `rule-estimates-schema`); estimates 7 updates and 12 readings; entities 2 (`entity-glossary`, `entity-sprint-migration`); insights 3 and lessons 4 by the synthesis. The cascade moved 10 rule statuses.
- Deleted: estimates 1 (`estimate-generate-writes-the-given`, case 513.2). `guppi cleanup` moved 2 pages: `estimate-generate-writes-the-given` and `decision-case-511.2`.
- Synthesis: `lesson-case-build-closes-a-sprint-item-without-the-sprint-page` and `lesson-case-build-splits-a-case-whose-line-stands` joined `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (`actioned` → `open`, severity 2); `lesson-case-build-quotes-the-person-in-the-chat-language` joined `insight-case-form-chat-form-read-by-no-script` (`actioned` → `open`, severity 1); `lesson-case-build-writes-a-count-no-command-printed` joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (`actioned` → `open`, severity 1). Each Insight keeps its `addressed_by`.

## Readings due

Failed first:

- `estimate-glossary-terms-defined` — `entity-glossary` — failed: six rows named a `where` page that does not define the term (Plan Mode, Page fields, Category fields, Scripts, Decision, Lesson, Insight (status), Working files). Read by hand in a later session after the librarian's run: the table of `vault/wiki/glossary.md` and `make lint` (spec 1432). This run: `entity-glossary` updated by case 515; `uv run guppi glossary` exit 0, no stderr; the table holds 56 rows; `make lint` prints no finding on `entity-glossary`.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` — failed: after the defer of Case 509, with no Cases line open, the question asked whether to take the W readings, not whether to run /pre-spec. Read by hand, the first defer the person asks for after the render.
- `estimate-documentation-completes` — `rule-documentation` — failed: the run of ff62585 read beyond its list (tail of log.md, head of the old brief.md, git diff of sprint.md and backlog.md, a grep of sprint.md, a count of [x] in the 0137 Spec). Read by `make test-documentation`; the live reading by hand.

Pending:

- `estimate-agent-writing-followed` — `rule-agent-writing` — by hand in a later session, the person's messages of one session against the section in CLAUDE.md.
- `estimate-ask-finds` — `rule-ask` — by hand on three dispatches in a later session (spec 0137).
- `estimate-brief-carries-the-run-facts` — `rule-brief` — by hand, at the `/hi` after the first librarian run on the new frame (spec 1134). This run's frame holds the Render; the brief is written before `uv run guppi archive`; no `pending` Estimate's `method` names the archive step.
- `estimate-carry-over-writes` — `rule-carry-over` — `uv run guppi render --check`; by hand, the first /carry after the fork of ExitPlanMode.
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — in a later session after the render: one first round and one later round of `case-guppi` read in the chat against the Criterion (spec 1432).
- `estimate-case-build-writes-the-case` — `rule-case-build` — by hand: live dispatches in a session after the render.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — by hand, the reading its `method` names, in a later session (spec 0137).
- `estimate-compact-recall-reloads` — `rule-compact-recall` — `pytest tests/test_recall.py`; live, the first compaction of a working session.
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` — `uv run pytest tests/test_context.py -k limit`; live at the first prompt past 400 000 tokens.
- `estimate-decisions-schema-checked` — `rule-decisions-schema` — `pytest tests/test_schemas.py -k decisions`, then `make lint` with no `schema` finding on `vault/wiki/decisions/` but the pages of Cases 1–28, at a later session (spec 1432).
- `estimate-end-of-work-order` — `rule-end-of-work` — `make test-end-of-work`, then by hand at the close of a later session (spec 0137).
- `estimate-event-log-records` — `rule-event-log` — pytest in tests/test_event.py and tests/test_gate.py; by hand, one /hi outside plan mode and one in it.
- `estimate-generate-fails-alone` — `rule-page-generation` — `pytest tests/test_generate.py`, at a later session (spec 1134).
- `estimate-generate-renames` — `rule-page-generation` — pytest in tests/test_generate.py; live, the librarian's run on a real rename. This run: no entry carries `rename`.
- `estimate-generate-rewords` — `rule-page-generation` — pytest in tests/test_generate.py; live, the librarian's run that applies the first reword. This run: no entry carries `reword`.
- `estimate-generate-writes` — `rule-page-generation` — `pytest tests/test_generate.py`, then by hand at a later librarian's run (spec 1134).
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` — `pytest tests/test_generate.py`, the tests of the Decision page, and the pages of the librarian's run, at a later session (spec 1432). This run: 13 Decision pages written; `decision-case-510`, `511.1`, `512`, `513.1`, `513.2`, `513.3`, `514`, `515`, `516` carry `## Problem` and `## History`; `517`, `518`, `519`, short-form defers, carry `## Context`, `## Problem`, `## Deferred` and `## History`; `decision-case-511.2` went `superseded` by 512 and was archived by `generate` and moved by `cleanup`; the `## Deferred` of `decision-case-519` holds "Correct the description of".
- `estimate-git-context-current` — `rule-git-context` — by hand at the /hi of the next session on the current remote, and its event_log.md at its close.
- `estimate-glossary-ticks-the-spec` — `rule-glossary` — `pytest tests/test_glossary.py`, plus one reading of this session's spec.md after the librarian's run. This run: `uv run guppi glossary` exit 0, no stderr; the line `` - [x] `uv run guppi glossary` `` of the 1432 spec.md stands ticked after the run.
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — `pytest tests/test_guard.py`, then by hand on one refused `Edit` in a later session (spec 0137).
- `estimate-handoff-dispatches` — `rule-handoff` — by hand at the `/handoff` of a later session (spec 0137).
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — by hand at the first /handoff after the render.
- `estimate-permissions` — `rule-permissions` — the allow list of .claude/settings.json and tests/test_render.py; live, the person's word on the prompt at a Write of work.md.
- `estimate-plan-mode-verified` — `rule-plan-mode` — `make test-plan-mode`; one live reading by hand.
- `estimate-retro-commit-gates` — `rule-retro-commit` — pytest in tests/test_gate.py; the live reading once by hand.
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — by hand at the first /retro after the render whose work.md names a check under Expected red.
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — by hand at the first /retro after the render whose Baseline holds a failing test or a lint finding.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` — by hand at the first /retro after the render.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-session-start-context` — `rule-session-start` — `make test-session-start`; by hand, one session opened without /hi.
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` — in a later session after the render: one round of `case-guppi` or of the person's `/grill-me`, read in the chat (spec 1432).
- `estimate-skill-wait-what-re-pitches` — `rule-skill-wait-what` — `uv run guppi render --check`; by hand, one run of the skill read in the chat in a later session (spec 0137).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by hand on the tree at the close of the sprint (spec 1432).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only unread lines on the sprint's Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit of migration, then git log of main after the merge.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — `uv run guppi render --check`; by hand, the first /work at the fork and the first /work the person types.
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` — by hand, at the first `/work` of a session after the render (spec 1134).

## Flags

- failed: none. unparsed: none.
- incomplete: L10 (case 511.2, `estimate-case-build-writes-a-plain-round`) lacks `criterion`; superseded by 512, not applied.
- near: L32 `lesson-case-build-closes-a-sprint-item-without-the-sprint-page` near `lesson-defer-to-a-milestone-leaves-the-sprint-page-silent`; L34 `lesson-case-build-writes-a-count-no-command-printed` near `lesson-case-check-command-signed-without-a-run`; L35 `lesson-case-build-splits-a-case-whose-line-stands` near `lesson-ledger-a-dropped-item-needs-a-superseding-sub-case`.
- Defect: L36, the defer of case 519 on `rule-estimates-schema`, carries `purpose: Correct the description of`, cut mid-sentence; the `## Deferred` of `decision-case-519` holds that text. The entry stays as it is.
- Failed Estimates: `estimate-glossary-terms-defined`, `estimate-case-protocol-defers-in-one-reply`, `estimate-documentation-completes`.
- Contradiction, from the handoff: a repeat of Case 514 ticks its line of the Spec, as an applied entry does, while the task line said "apply nothing".
- The `schema: missing section ## Context` the handoff expected before the render did not appear; `make lint` prints no `## Context` finding.
- MOC candidates: none reported by any step.
- Stale defers, from lint: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-build-checks-its-sub-cases` (case 480), `rule-complaint-becomes-a-lesson` (case 504), `rule-morph` (case 239), `rule-orchestration` (case 424), `rule-prespec-script-skips-code-spans` (case 481) once each.
- `generate` moved no item to the Backlog and dropped no milestone in this run.
- Lint (`make lint`, exit 2), 84 finding lines: `rules/rule-spec-box` schema: missing field `kind`, missing field `estimates`, and orphan; 31 Decision pages of Cases 1–28 missing `## Problem`; `decisions/decision-case-13` fence: a code fence open at the end of `## When`; 6 deferred lines (above); 3 unread: failed and 40 unread: pending.

## Next session

Cases:
- `estimate-glossary-terms-defined` failed; the table was rewritten by case 515 in this run and its reading waits for a later session — from the Estimate page and the handoff.
- `estimate-case-protocol-defers-in-one-reply` failed; put off by case 518 — from the Estimate page.
- `estimate-documentation-completes` failed; put off by case 517 — from the Estimate page.
- The defer entry of case 519 wrote the purpose "Correct the description of", cut mid-sentence, into `decision-case-519` — from `vault/raw/2026-09-29/1432/materialize.yaml` L36.
- A repeat of Case 514 ticks its Spec line while the task line said "apply nothing" — from the handoff.

Work:
- the pending readings of Readings due: `estimate-agent-writing-followed`, `estimate-ask-finds`, `estimate-brief-carries-the-run-facts`, `estimate-carry-over-writes`, `estimate-case-build-writes-a-plain-round`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-ledger-line-form`, `estimate-compact-recall-reloads`, `estimate-context-size-warns-past-the-limit`, `estimate-decisions-schema-checked`, `estimate-end-of-work-order`, `estimate-event-log-records`, `estimate-generate-fails-alone`, `estimate-generate-renames`, `estimate-generate-rewords`, `estimate-generate-writes`, `estimate-generate-writes-the-decision-page`, `estimate-git-context-current`, `estimate-glossary-ticks-the-spec`, `estimate-governed-files-hook-refuses`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-permissions`, `estimate-plan-mode-verified`, `estimate-retro-commit-gates`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-report-holds-each-fact-once`, `estimate-session-phases-in-order`, `estimate-session-start-context`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-skill-wait-what-re-pitches`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-work-mode-takes-the-work-readings`.
- the unticked boxes of the Specs: 17 `- [ ] read` lines — 0137: 6, 1134: 4, 1432: 7; each names an Estimate of the list above.
- ledger lines this run did not apply: none; the 1432 ledger holds 36 lines, each with an entry, and L9, L10 are superseded by case 512.
- dirty tree: none after the close commit.

## Readings at the close

- `make test`: 906 passed, 2 skipped.
- `make lint`: exit 2, 84 finding lines (above).
- Pages in `vault/wiki/`: rules 73, entities 4, estimates 158, decisions 793, lessons 66, insights 26 (6 open, 20 actioned).
