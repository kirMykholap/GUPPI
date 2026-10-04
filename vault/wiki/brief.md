# Brief — 2026-10-04, session 2245: Slice 5 — the readings that wait: the check of a cited search, and seven methods that no longer wait for a rare live event

## Where things stand

- Cases ratified in session 2245: 636, 637 (637.1–637.4).
- Code: `tests/test_lint.py`, two tests whose names hold `every_step` (637.3). `make test` at the close of the work: 1168 passed, 6 skipped; `make style` clean (handoff).
- Readings: L1 (`estimate-insights-schema-checked`) and L2 (`estimate-handoff-holds-each-fact-once`) passed in Plan Mode; Work readings L14, L15, L17 passed (`estimate-orchestration-asks-in-the-grill-me-shape`, `estimate-prespec-reconciles`, `estimate-orchestration-shows-the-built-case`); L16 failed (`estimate-prespec-confirms-the-findings-once`). One lesson, L18.
- This librarian run, one yaml applied: `vault/raw/2026-10-04/2245/materialize.yaml`, 18 entries from 18 ledger lines, 2 synthesis entries, 6 decision blocks; 26 marked `applied`, none `failed`, `exists`, `incomplete`. `guppi generate`: 32 pages written or changed for 2245; 0 for 0004, 0112, 1439, 1934, 2041.
  - decisions: 6 created (636, 637, 637.1–637.4); `decision-case-631` superseded by 637.3 and archived.
  - rules: 4 changed — `rule-case-build` by 2 `replace` entries (636, 637.2); `rule-handoff`, `rule-insights-schema`, `rule-orchestration` to `built` by the cascade.
  - estimates: 14 updated — 6 readings applied (5 passed, 1 failed), 8 by decision entries (636: 1; 637.1: 4; 637.2, 637.3, 637.4: 1 each).
  - insights: 2 updated — `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` set `actioned`, `addressed_by` decision-case-636 (636); `insight-prespec-after-findings-loop-unruled` took a child (synthesis).
  - lessons: 1 created, then clustered (`lesson-prespec-confirmation-prompt-invites-a-new-finding`); 4 archived by the cascade of the actioned Insight (`lesson-case-build-a-count-in-context-not-from-a-run`, `lesson-case-build-a-grep-cited-for-files-it-did-not-print`, `lesson-case-build-a-page-judged-true-by-its-mark-not-its-moment`, `lesson-case-build-hits-counted-as-lines`).
- Spec ticks: this run ticked 13 lines of `vault/raw/2026-10-04/2245/spec.md` (3 `- [ ] read` lines stay open) and 5 `read` lines of `vault/raw/2026-10-04/2041/spec.md`.
- Renders: `.claude/agents/case-guppi.md`; `vault/wiki/backlog.md` rewritten (19 items); `guppi sprint` and `guppi glossary` exit 0.
- `guppi cleanup`: 5 pages moved to `vault/archive/migration/2026-10-05/2245/` (1 decision, 4 lessons). `guppi archive`: 5 session units moved (0004, 0112, 1439, 1934, 2041 of 2026-10-04); 2245 kept, the session of this run.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 78 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-prespec-confirmation-prompt-invites-a-new-finding` joined `insight-prespec-after-findings-loop-unruled` (open, `addressed_by` decision-case-561.1 kept; severity 1 → 2); its 4th child.
- Index check: the yaml holds no `create` outside estimates but the lesson entry, compared by the lessons Grep above (78 lines). No entry merged; one `near`.
- No `guppi sprint-close` line in the session's `spec.md`; no sprint closed. `entity-sprint-migration` stays live (`draft`).

## Readings due

- `estimate-prespec-confirms-the-findings-once` — failed — `rule-prespec` (draft) — method: by hand at the `/pre-spec` of a later session whose findings send a Case back, after the render by case 634.2. Result (L16): the ask-guppi answers at the confirmation did not hold one line per finding with one sentence, and the main agent's SendMessage invited "a new defect the rebuild itself brought in".
- `estimate-case-build-checks-the-finished-case` — pending — `rule-case-build` (draft) — spec.md L81; method: by hand at `/pre-spec` of a later session after the render, the answers of the ask-guppi runs, one per top-level Case.
- `estimate-case-check-sends-back-a-clash-with-another-case` — pending — `rule-case-check` (draft) — spec.md L229; method: `uv run pytest tests/test_casecheck.py -k session_clash`.
- `estimate-lint-runs-every-step` — pending — `rule-lint` (draft) — spec.md L267; method: `uv run pytest tests/test_lint.py -k every_step`.
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — pending — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k lone`.
- `estimate-case-check-requires-each-question-of-the-rounds` — pending — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds` over a temp agent transcript.
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k subagent_clash`.
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k shape`.
- `estimate-session-start-context` — pending — `rule-session-start` (draft) — method: `make test-session-start`.
- `estimate-ask-finds` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, the answer of ask-guppi at a `/pre-spec` after the render by case 633.1.
- `estimate-ask-searches-at-prespec` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, the calls of ask-guppi at a `/pre-spec` after the render by case 633.2.
- `estimate-ask-query-before-a-create` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, a case-guppi that built a Case with a `create` without a `ref`.
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` (draft) — method: by hand, live dispatches after the render — a fork, a `create` without a `ref`, a change of a hook, a change on one sub-case.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` (draft) — method: by hand at the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` (draft) — method: `uv run guppi render --check`; a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand a Case ratified in Work Mode.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand a `/work` at the fork, one `/box` calls, and the `/work` of a session that closes a sprint.
- `estimate-brief-written` — pending — `rule-brief` (draft) — method: by hand at the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — pending — `rule-backlog` (draft) — method: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint. This run: `guppi backlog` exit 0, no stderr; `backlog.md` heads `19 items`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` (draft) — method: pytest `-k sprint` of `tests/test_ledger.py` and `tests/test_materialize.py`; by hand at the librarian's run of the session after the close of a sprint. This run: the yaml carries `sprint: migration`; `guppi sprint` exit 0, no stderr; `entity-sprint-migration` live.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` (draft) — method: `pytest tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint, its ledger, spec.md, handoff.md, event log, report and `vault/archive/`. This run: the session's `spec.md` holds no unticked task line with `guppi sprint-close` and `--apply`; no close ran. `guppi archive`, exit 0, no stderr: `archive: raw/2026-10-04/0004 → archive/migration/2026-10-04/0004/raw`; `archive: raw/2026-10-04/0112 → archive/migration/2026-10-04/0112/raw`; `archive: raw/2026-10-04/1439 → archive/migration/2026-10-04/1439/raw`; `archive: raw/2026-10-04/1934 → archive/migration/2026-10-04/1934/raw`; `archive: raw/2026-10-04/2041 → archive/migration/2026-10-04/2041/raw`.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` (draft) — method: by hand after the Work Mode of the session that closes a sprint.
- `estimate-synthesis-clusters` — pending — `rule-synthesis` (draft) — method: by hand, the yaml and the report after a live librarian run whose yaml holds at least two lesson entries. This run: the yaml holds 1 lesson entry; 2 synthesis entries appended.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` (draft) — method: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run. This run: `make lint` printed 31 finding lines, 4 `deferred`, 26 `unread`, 1 `method`, exit 2.
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` (draft) — method: one reading of the tree by hand in the Work Mode of the session that closes the sprint, before the librarian's run.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run. This run: `make test` 1168 passed, 6 skipped, on the uncommitted tree of branch `migration`.

## Flags

- `near`: the lesson entry `lesson-prespec-confirmation-prompt-invites-a-new-finding` is marked `near: lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary` — both a main-agent dispatch to ask-guppi that departs from the text of its rule. No entry marked `incomplete`, `failed` or `unparsed` (`unparsed: []`).
- Failed Estimate: `estimate-prespec-confirms-the-findings-once` (L16).
- Contradiction (lint): `estimates/estimate-session-phases-in-order: method: says by hand while estimate-session-start-context names a test file` — new since 637.4 set the method of `estimate-session-start-context` to `make test-session-start`.
- Stale defers (lint): `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239; `rule-subagent-guppi` 31 times since case 29.
- Lint: 31 finding lines — 4 `deferred`, 26 `unread` (25 pending, 1 failed), 1 `method`; exit 2. The handoff gives 35 lines before the work.
- Handoff instruction 1: both `replace` entries of `rule-case-build` (636, 637.2) landed, each on its own sentence; `guppi render` ran once and changed 2 lines of `.claude/agents/case-guppi.md`.
- Handoff instruction 2: the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` holds no line on what `case-guppi` does after a clash; a Grep of `should change` over the page printed nothing.
- Handoff instruction 3: `estimate-lint-runs-every-step` holds no `deferred_by`; `decision-case-631` carries `superseded_by` decision-case-637.3 and was archived.
- Handoff instruction 4: the cascade archived the four `clustered` lessons of the actioned Insight; the synthesis put the new lesson under `insight-prespec-after-findings-loop-unruled`.
- Handoff observation: whether the two changes of `rule-case-build` meet in meaning was not judged at the session; the run of 637 saw only that their anchors stand in two different sentences.
- MOC candidates: none raised.
- Read outside the frame's list: the `git diff` of `vault/wiki/decisions/decision-case-631.md`, which shows the text of a Decision page, for the check of handoff instruction 3 (the `deferred_by` of `estimate-lint-runs-every-step`); the handoff asked for that check, not for this read.

## Next session

### Cases

- `estimate-prespec-confirms-the-findings-once` failed: decide whether the form of the ask-guppi answer at the confirmation is enforced or the Criterion allows a short paragraph per finding (handoff, For the next session).
- The close of migration, when the person is ready: a session of its own, case 628.9 (handoff, For the next session).
- Lint contradiction: the `method` of `estimate-session-phases-in-order` says by hand while `estimate-session-start-context` names a test file (`make lint`, after 637.4).

### Work

- `estimate-case-build-checks-the-finished-case`
- `estimate-case-check-sends-back-a-clash-with-another-case`
- `estimate-lint-runs-every-step`
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-session-start-context`
- `estimate-ask-finds`
- `estimate-ask-searches-at-prespec`
- `estimate-ask-query-before-a-create`
- `estimate-case-build-writes-the-case`
- `estimate-hi-writes-frontier`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-synthesis-clusters`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-merges`

### Ask the person

none

## Readings at the close

- `make test`: 1168 passed, 6 skipped.
- `make lint`: 31 finding lines (4 `deferred`, 26 `unread`, 1 `method`), exit 2.
- Pages under `vault/wiki/`: decisions 1078, entities 4, estimates 209, insights 30, lessons 75, rules 77. Under `vault/archive/`: 830 `.md` files; `guppi archive` moved 5 session units.
