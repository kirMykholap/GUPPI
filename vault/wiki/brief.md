# Brief — 2026-10-05, session 0109: the form and the searches of ask-guppi, the session's make target

## Where things stand

- Cases ratified in session 0109: 638, 639, 640, 641 — each built again on the findings of `/pre-spec` and ratified again — and the short-form defers 642 and 643 (handoff).
- Code: `Makefile`, the target `test-session` over `test-session-start`, `test-plan-mode`, `test-end-of-work` and `test-documentation` (641). No test changed. `make test` at the close of the work: 1168 passed, 6 skipped; `make style` clean; `make test-session` ran the four pipelines and passed (handoff).
- Readings: L1–L7 passed, L8 (`estimate-ask-finds`) and L9 (`estimate-ask-searches-at-prespec`) failed, all at `/hi`; L22 failed (`estimate-case-build-checks-the-finished-case`, in Work Mode). Lessons: L23, L24, L25.
- This librarian run: `guppi materialize` wrote `vault/raw/2026-10-05/0109/materialize.yaml` with 25 entries from 25 ledger lines and 6 decision blocks, and extended `vault/raw/2026-10-04/2245/materialize.yaml` with 0 entries. The synthesis appended 4 entries. All 29 entries and 6 decision blocks marked `applied`; none `failed`. `guppi generate`: 33 pages written or changed for 0109; 0 for 2245.
  - decisions: 6 created (638–643).
  - rules: 2 created — `rule-search-leaves-out-decisions` (640), `rule-prespec-judges-the-spec-whole` (placeholder of the defer 643); 6 changed — `rule-prespec` (638), `rule-ask` (638 and 639, 3 `replace` pairs), `rule-harness` (640, 2 `replace` pairs and a child); `rule-case-check`, `rule-lint`, `rule-session-start` to `built` by the cascade.
  - estimates: 1 created (`estimate-search-leaves-out-decisions-in-every-agent`); 12 updated — 10 readings applied (7 passed, 3 failed), and one decision entry each of 638, 639, 640 and 641; `estimate-ask-finds` and `estimate-ask-searches-at-prespec` take both a reading and an update.
  - entities: 1 deferred — `entity-sprint-migration` (642), `deferred_by` decision-case-642, `status: draft`.
  - insights: 2 updated by the synthesis.
  - lessons: 3 created; 2 of them clustered by the synthesis.
- Spec ticks: this run ticked 14 lines of `vault/raw/2026-10-05/0109/spec.md` (10 by `generate`, 4 `render` lines by `render`); 3 `- [ ] read` lines stay open. It ticked 3 `read` lines of `vault/raw/2026-10-04/2245/spec.md`.
- Renders: `.claude/agents/ask-guppi.md` (4 lines changed), `.claude/skills/pre-spec/SKILL.md` (2 lines), `.claude/rules/search-leaves-out-decisions.md` (new; the folder `.claude/rules/` is new). `vault/wiki/backlog.md` rewritten (22 items). `guppi sprint` and `guppi glossary` exit 0 and changed no file.
- `guppi cleanup`: 0 pages moved. `guppi archive`: 1 session unit moved (2026-10-04/2245); 0109 kept, the session of this run.
- Index check: one `create` outside estimates, `rule-search-leaves-out-decisions`, compared with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, 83 lines. Not merged; marked `near: rule-page-read`.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 75 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-orchestration-short-defer-then-block-written-as-a-mapping` joined `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (open; severity 3 → 4); its 9th child.
  - `lesson-orchestration-dispatch-prompt-carried-counts-not-from-a-run` joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`; the Insight was `actioned` (`addressed_by` decision-case-636) and is set `open`, `addressed_by` kept; severity 1; its 12th child.
  - `lesson-spec-write-skips-the-reply-that-answers-a-refusal`: none — no index line of either Grep names the Stop hook `guppi ratified` returning at once on `stop_hook_active`; stays `new`.
- No `guppi sprint-close` line in the session's `spec.md`; no sprint closed. `entity-sprint-migration` stays live, now deferred.

## Readings due

- `estimate-ask-searches-at-prespec` — failed — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, the calls of ask-guppi at a `/pre-spec` after the render by case 633.2 and of `.claude/rules/search-leaves-out-decisions.md` by case 640. Result (L9): call 16 of agent a390781c7f1241c18, a Grep over `vault/wiki` with the glob `!decisions/**`, printed 29 lines of files under `vault/wiki/decisions/`.
- `estimate-case-build-checks-the-finished-case` — failed — `rule-case-build` (draft) — method: by hand at `/pre-spec` of a later session after the render, the answers of the ask-guppi runs, one per top-level Case. Result (L22): the four case-guppi of session 0109 missed 1 page made false, 4 rules and 1 lesson of the same moment, 1 clash with a Case of the prompt and 4 claims of context.
- `estimate-prespec-confirms-the-findings-once` — pending — `rule-prespec` (draft) — `vault/raw/2026-10-05/0109/spec.md` L110; method: by hand at the `/pre-spec` of a later session whose findings send a Case back, after the render by case 638.
- `estimate-ask-finds` — pending — `rule-ask` (draft) — `vault/raw/2026-10-05/0109/spec.md` L196; method: by hand at the `/hi` of a later session, the answer of ask-guppi at a `/pre-spec` after the render by case 639.
- `estimate-search-leaves-out-decisions-in-every-agent` — pending — `rule-search-leaves-out-decisions` (draft) — `vault/raw/2026-10-05/0109/spec.md` L355; method: by hand at the `/hi` of a later session, the transcripts of the main agent, ask-guppi and case-guppi after the render by case 640.
- `estimate-ask-query-before-a-create` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, a case-guppi that built a Case with a `create` without a `ref`, after the render by case 626.1.
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` (draft) — method: by hand, live dispatches after the render — a fork, a `create` without a `ref`, a change of a hook, a change on one sub-case.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` (draft) — method: by hand at the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` (draft) — method: `uv run guppi render --check`; a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand a Case ratified in Work Mode.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand a `/work` at the fork, one `/box` calls, and the `/work` of a session that closes a sprint.
- `estimate-brief-written` — pending — `rule-brief` (draft) — method: by hand at the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — pending — `rule-backlog` (draft) — method: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint. This run: `guppi backlog` exit 0, no stderr; `backlog.md` heads `22 items`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` (draft) — method: pytest `-k sprint` of `tests/test_ledger.py` and `tests/test_materialize.py`; by hand at the librarian's run of the session after the close of a sprint. This run: the yaml carries `sprint: migration`; `guppi sprint` exit 0, no stderr; `entity-sprint-migration` live.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` (draft) — method: `pytest tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint, its ledger, spec.md, handoff.md, event log, report and `vault/archive/`. This run: the session's `spec.md` holds no unticked task line with `guppi sprint-close` and `--apply`; no close ran. `guppi archive`, exit 0, no stderr: `archive: raw/2026-10-04/2245 → archive/migration/2026-10-04/2245/raw`.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` (draft) — method: by hand after the Work Mode of the session that closes a sprint.
- `estimate-synthesis-clusters` — pending — `rule-synthesis` (draft) — method: by hand, the yaml and the report after a live librarian run whose yaml holds at least two lesson entries. This run: the yaml holds 3 lesson entries; the Greps printed 75 (lessons) and 31 (insights) lines; 4 entries appended, each `librarian: synthesis` — 2 `update` of an Insight with the lesson added to `children`, 2 `update` of a lesson with `status: clustered`; 1 lesson joined none.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` (draft) — method: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run. This run: `make lint` printed 25 finding lines, 5 `deferred`, 20 `unread`, exit 2.
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` (draft) — method: one reading of the tree by hand in the Work Mode of the session that closes the sprint, before the librarian's run.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run. This run: `make test` 1168 passed, 6 skipped, on the uncommitted tree of branch `migration`.

## Flags

- `incomplete`: the entry `rule-search-leaves-out-decisions` (line 15) lacked `type`; the page carries `type: rule`. The decision blocks of 642 and 643 lacked `context` and `problem` (short-form defers). No entry `failed`; `unparsed: []`.
- `exists`: the defer of `entity-sprint-migration` (642) found its page; the defer of `rule-prespec-judges-the-spec-whole` (643) wrote a placeholder.
- `near`: `rule-search-leaves-out-decisions` is marked `near: rule-page-read` — both keep vault text an agent did not need out of its context, one the History of a page, one the text of Decision pages through a search.
- The defer target `rule-prespec-judges-the-spec-whole` was not index-checked, since a defer is not a `create`; the purposes of `rule-prespec` and `rule-prespec-hook` also speak of a contradiction between the decisions of a Spec.
- Failed Estimates: `estimate-ask-searches-at-prespec` (L9), `estimate-case-build-checks-the-finished-case` (L22). `estimate-ask-finds` failed at L8 and stands `pending` after `generate`, set by the update of 639. `estimate-ask-searches-at-prespec` stands `failed` after `generate`; the update of 640 set its `method` alone.
- Stale defers (lint): `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239; `rule-prespec-judges-the-spec-whole` 1 time since case 643; `rule-subagent-guppi` 31 times since case 29.
- Lint: 25 finding lines — 5 `deferred`, 20 `unread` (18 pending, 2 failed); exit 2. The handoff gives 31 lines before the work, 1 of them `method` on `estimate-session-phases-in-order`; that line is gone.
- Handoff instruction 1: the three `replace` pairs of `rule-ask` (638: 1, 639: 2) landed; each anchor stood once before `generate`. `.claude/agents/ask-guppi.md` holds `(case 638)` once and `(case 639)` twice after the render.
- Handoff instruction 2: `.claude/rules/search-leaves-out-decisions.md` written by the render; the folder `.claude/rules/` was created.
- Handoff instruction 3: after `generate`, `estimate-ask-finds` is `pending`, `estimate-ask-searches-at-prespec` is `failed`.
- Handoff instruction 4: `rule-prespec-judges-the-spec-whole` written as a placeholder, `deferred_by` decision-case-643, `status: draft`.
- Handoff instruction 5: `entity-sprint-migration` carries `deferred_by` decision-case-642 and stands in the Deferred list of `backlog.md`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- Handoff observations: the hook `guppi onward --plan` judged the loop after the findings ended before it started; the ledger hook did not append the decision lines of 638–641 again at their second ratification.
- MOC candidates: none raised.

## Next session

### Cases

- `estimate-case-build-checks-the-finished-case` failed: decide what the frame of `case-guppi` changes, or whether the Criterion asks too much of one build (handoff, For the next session).
- The Stop hook `guppi ratified` writes nothing on the reply that answers a refusal (`stop_hook_active`), and `orchestration.md` does not say so: decide whether the rule says it or the hook writes there too (handoff, For the next session; `lesson-spec-write-skips-the-reply-that-answers-a-refusal`).
- The hook `guppi onward --plan` sent the agent to the check and the exit while the loop after the findings had not started: decide whether it is a bug of the hook (handoff, For the next session).
- `estimate-ask-searches-at-prespec` failed (L9), and stands `failed` after the update of 640.

### Work

- `estimate-prespec-confirms-the-findings-once`
- `estimate-ask-finds`
- `estimate-search-leaves-out-decisions-in-every-agent`
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
- `make lint`: 25 finding lines (5 `deferred`, 20 `unread`), exit 2.
- Pages under `vault/wiki/`: decisions 1084, entities 4, estimates 210, insights 30, lessons 78, rules 79. Under `vault/archive/`: 830 `.md` files before `guppi archive`.
