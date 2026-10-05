# Brief — 2026-10-05, session 0311: the Spec hook after a refusal, case-guppi writes its own Case file, the schema by example

## Where things stand

- Cases ratified in session 0311: 644 (644.1–644.8), 645 (645.1–645.16), 646 — each built again on the findings of `/pre-spec` and ratified again — and the short-form defers 647, 648, 649 (handoff).
- Code: `guppi/ratified.py` — the Stop run no longer returns at `stop_hook_active`; its reasons and its error pass through `own_refusals` and `untold` of `guppi/ledger.py`; the guard lets `case-guppi` alone write under `cases/`; the Spec hook refuses a Case whose file differs from the store. `guppi/casecheck.py` — `written_case_files`, `file_differences`, `changed_file`, `judge_and_store`; `stored_parents` removed. `guppi/ledger.py` — the docstring of `refusals` (handoff).
- Tests: `tests/test_ratified.py`, `tests/test_casecheck.py` changed; `tests/test_case_schema.py` new. `make test` at the close of the work: 1190 passed, 8 skipped; `make style` clean (handoff).
- Readings: L1 (`estimate-synthesis-clusters`, failed, at `/hi`). Lessons: L31, L40, L41 (handoff).
- This librarian run: `guppi materialize` wrote `vault/raw/2026-10-05/0311/materialize.yaml` with 41 entries from the 41 lines of the ledger and 30 decision blocks, and extended `vault/raw/2026-10-05/0109/materialize.yaml` with 0 entries. The synthesis appended 2 entries; the index check marked 1 entry `near`. All 43 entries marked `applied`; none `failed`; `unparsed: []`. `guppi generate`: 71 pages written or changed for 0311; 0 for 0109; no stderr.
  - decisions: 30 created (644, 644.1–644.8, 645, 645.1–645.16, 646, 647, 648, 649).
  - rules: 7 updated — `rule-spec-write` (644.1 and 645.5, 4 `replace` pairs each, and `purpose`), `rule-case-build` (645.1, 12 `replace` pairs), `rule-case-check` (645.2, 2 pairs), `rule-spec-reconcile` (645.3, 5 pairs), `rule-orchestration` (645.6, 3 pairs), `rule-case-protocol` (646, 6 pairs), `rule-permissions` (645.16, 1 pair); `rule-case-check`, `rule-case-protocol`, `rule-orchestration`, `rule-permissions`, `rule-spec-reconcile` set `built` → `draft` by the cascade. 1 deferred — `rule-prespec-onward` (648, page existed).
  - estimates: 5 created (`estimate-spec-write-answers-a-refusal`, `estimate-case-check-refuses-a-changed-case-file`, `estimate-spec-write-refuses-a-changed-case-file`, `estimate-case-protocol-example-passes-the-check`, `estimate-spec-write-tells-each-reason-once`); 20 updated by decision entries; 1 updated by a reading (`estimate-synthesis-clusters` pending → failed); 2 deferred (`estimate-case-build-checks-the-finished-case` by 647, `estimate-ask-searches-at-prespec` by 649, pages existed); 1 deleted (`estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`, 645.2) and moved to the archive by `cleanup`.
  - insights: 1 updated by the synthesis.
  - lessons: 3 created; 1 of them clustered by the synthesis.
- Spec ticks: this run ticked 37 lines of `vault/raw/2026-10-05/0311/spec.md` — 34 by `generate` (5 `create`, 28 `update`, 1 `delete`) and 3 render lines by `render`. 25 `- [ ] read` lines stay open, and 7 boxes inside the quoted example of Case 646.
- Renders: `.claude/agents/case-guppi.md` (13 lines changed), `vault/wiki/case-schema.md` (100 lines added, 6 removed), `vault/wiki/orchestration.md` (1 line). `vault/wiki/backlog.md` rewritten (`23 items`). `guppi sprint` and `guppi glossary` exit 0, no stderr, no file changed.
- `guppi cleanup`: 1 page moved. `guppi archive`: 0 units moved; `raw/2026-10-05/0109` and `raw/2026-10-05/0311` kept, both dated the day of the run, which the script does not look at, 0311 the session of the run.
- Index check: no `create` outside estimates but the 3 `lesson` entries; each `root_cause` compared with the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 78 lines. None merged. `lesson-agents-sendmessage-to-a-running-subagent-waits-for-its-next-tool-round` marked `near: lesson-sendmessage-answers-open-a-turn-of-their-own`.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 78 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-case-build-replace-pair-value-unpadded-and-paths-off-given` joined `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (open; severity 4 → 5); its 10th child. The lesson entry carries `addressed_by: decision-case-646`; the Insight was `open`, not `actioned`, so its `update` carries `children` alone and its `addressed_by` decision-case-432 stands.
  - `lesson-session-frontier-closer-appended-box-left-open`: none — no index line of either Grep names a closer appended to a Frontier line by an Edit that leaves its box open; `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan` is about an item with no closer. Stays `new`.
  - `lesson-agents-sendmessage-to-a-running-subagent-waits-for-its-next-tool-round`: none — no Insight's pattern names the delivery of a SendMessage to a running subagent; the nearest lesson is about a finished one. Stays `new`.
- No `guppi sprint-close` line in the session's `spec.md`; no sprint closed. `entity-sprint-migration` stays live.

## Readings due

- `estimate-synthesis-clusters` — failed — `rule-synthesis` (draft) — method: by hand, the yaml and the report after a live librarian run whose yaml holds at least two lesson entries. Result (L1): failed on one clause — the librarian of 0109 printed the frontmatter of six lesson pages at synthesis, and neither its report nor its brief named them with an outcome. This run: the yaml holds 3 lesson entries; the Greps printed 78 (lessons) and 31 (insights) lines; 2 entries appended, each `librarian: synthesis` — 1 `update` of an Insight with the lesson added to `children`, 1 `update` of a lesson with `status: clustered` and `insight`; 2 lessons joined none; no Insight created; one page read at synthesis, the Insight `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, no lesson page.
- `estimate-ask-searches-at-prespec` — failed — `rule-ask` (draft) — deferred by 649 — method: by hand at the `/hi` of a later session, the calls of ask-guppi at a `/pre-spec` after the render by case 633.2 and of `.claude/rules/search-leaves-out-decisions.md` by case 640. Result: call 16 of agent a390781c7f1241c18, a Grep over `vault/wiki` with the glob `!decisions/**`, printed 29 lines of files under `vault/wiki/decisions/`.
- `estimate-case-build-checks-the-finished-case` — failed — `rule-case-build` (draft) — deferred by 647 — method: by hand at `/pre-spec` of a later session after the render, the answers of the ask-guppi runs, one per top-level Case. Result: the four case-guppi of session 0109 missed 1 page made false, 4 rules and 1 lesson of the same moment, 1 clash with a Case of the prompt and 4 claims of context.
- `estimate-spec-write-answers-a-refusal` — pending — `rule-spec-write` (draft) — `vault/raw/2026-10-05/0311/spec.md` L123; method: `uv run pytest tests/test_ratified.py -k answers_a_refusal`; by hand at the `/hi` of a later session.
- `estimate-spec-write-copies-the-ratified-case` — pending — `rule-spec-write` (draft) — spec.md L163; method: `uv run pytest tests/test_ratified.py -k write`; by hand the plan file after the first ratification of a session.
- `estimate-spec-write-checks-the-written-case` — pending — `rule-spec-write` (draft) — spec.md L199; method: `uv run pytest tests/test_ratified.py -k checks_the_written`; by hand a ratification of a session.
- `estimate-spec-write-writes-a-defer` — pending — `rule-spec-write` (draft) — spec.md L235; method: `uv run pytest tests/test_ratified.py -k defer`, then by hand a defer the person asks for.
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` (draft) — spec.md L269; method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand a Case ratified in Work Mode.
- `estimate-spec-write-removes-a-superseded-case` — pending — `rule-spec-write` (draft) — spec.md L303; method: `uv run pytest tests/test_ratified.py -k superseded`; by hand a supersedes of a Case of the same session.
- `estimate-spec-write-exits-2-on-an-error` — pending — `rule-spec-write` (draft) — spec.md L339; method: `uv run pytest tests/test_ratified.py`.
- `estimate-spec-write-tells-each-reason-once` — pending — `rule-spec-write` (draft) — spec.md L379; method: `uv run pytest tests/test_ratified.py -k tells_each_reason_once`.
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` (draft) — spec.md L551; method: by hand, live dispatches in a session after the render, the file written in Plan Mode with no prompt.
- `estimate-case-check-sends-back-a-faulty-case` — pending — `rule-case-check` (draft) — spec.md L610; method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand in a session after the render.
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — pending — `rule-spec-reconcile` (draft) — spec.md L670; method: `uv run pytest tests/test_ratified.py -k guard`; by hand in a later session, a probe Write under `cases/`.
- `estimate-case-check-refuses-a-changed-case-file` — pending — `rule-case-check` (draft) — spec.md L711; method: `uv run pytest tests/test_casecheck.py -k changed_file`.
- `estimate-spec-write-refuses-a-changed-case-file` — pending — `rule-spec-write` (draft) — spec.md L769; method: `uv run pytest tests/test_ratified.py -k changed_file`.
- `estimate-orchestration-shows-the-built-case` — pending — `rule-orchestration` (draft) — spec.md L822; method: by hand, the Cases of a session at its close against the transcript.
- `estimate-case-check-refuses-a-letter-outside-the-script` — pending — `rule-case-check` (draft) — spec.md L862; method: `uv run pytest tests/test_casecheck.py -k script`.
- `estimate-case-check-notes-a-criterion-line-not-carried` — pending — `rule-case-check` (draft) — spec.md L900; method: `uv run pytest tests/test_casecheck.py tests/test_prespec.py -k note`, then by hand the first note.
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending — `rule-case-check` (draft) — spec.md L935; method: `uv run pytest tests/test_casecheck.py -k subagent_clash`.
- `estimate-case-protocol-case-form` — pending — `rule-case-protocol` (draft) — spec.md L974; method: one reading by hand of the Cases of a session, at its close.
- `estimate-case-check-shows-only-the-checked-case` — pending — `rule-case-check` (draft) — spec.md L1012; method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses.
- `estimate-case-build-answers-what-done-means` — pending — `rule-case-build` (draft) — spec.md L1042; method: by hand at the close of a later session.
- `estimate-case-build-records-the-rounds-in-recommend` — pending — `rule-case-build` (draft) — spec.md L1081; method: by hand, the Case files of a later session after the render.
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — pending — `rule-case-check` (draft) — spec.md L1113; method: `uv run pytest tests/test_casecheck.py -k backlog`, then by hand.
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending — `rule-case-check` (draft) — spec.md L1149; method: `uv run pytest tests/test_casecheck.py -k shape`.
- `estimate-permissions` — pending — `rule-permissions` (draft) — spec.md L1193; method: the allow list of the rendered `.claude/settings.json` and `tests/test_render.py`; the live probe is the person's word on the client's prompt.
- `estimate-case-protocol-example-passes-the-check` — pending — `rule-case-protocol` (draft) — spec.md L1392; method: `uv run pytest tests/test_case_schema.py`, passed and not skipped.
- `estimate-prespec-confirms-the-findings-once` — pending — `rule-prespec` (draft) — method: by hand at the `/pre-spec` of a later session whose findings send a Case back, after the render by case 638.
- `estimate-ask-finds` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, the answer of ask-guppi at a `/pre-spec` after the render by case 639.
- `estimate-search-leaves-out-decisions-in-every-agent` — pending — `rule-search-leaves-out-decisions` (draft) — method: by hand at the `/hi` of a later session, the transcripts after the render by case 640.
- `estimate-ask-query-before-a-create` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, a case-guppi that built a Case with a `create` without a `ref`.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` (draft) — method: by hand at the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` (draft) — method: `uv run guppi render --check`; a session that takes a conserved Spec, and the `/hi` after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand a `/work` at the fork, one `/box` calls, and the `/work` of a session that closes a sprint.
- `estimate-brief-written` — pending — `rule-brief` (draft) — method: by hand at the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — pending — `rule-backlog` (draft) — method: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint. This run: `guppi backlog` exit 0, no stderr; `backlog.md` heads `23 items`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` (draft) — method: pytest `-k sprint` of `tests/test_ledger.py` and `tests/test_materialize.py`; by hand at the librarian's run of the session after the close of a sprint. This run: the yaml carries `sprint: migration`; `guppi sprint` exit 0, no stderr; `entity-sprint-migration` live.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` (draft) — method: `pytest tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint, its ledger, spec.md, handoff.md, event log, report and `vault/archive/`. This run: the session's `spec.md` holds no unticked task line with `guppi sprint-close` and `--apply`; no close ran. `guppi archive`: exit 0, no stdout, no stderr.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` (draft) — method: by hand after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` (draft) — method: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run. This run: `make lint` printed 48 finding lines, 5 `deferred`, 43 `unread`, exit 2.
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` (draft) — method: one reading of the tree by hand in the Work Mode of the session that closes the sprint, before the librarian's run.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run. This run: `make test` 1192 passed, 6 skipped, on the uncommitted tree of branch `migration`.

## Flags

- `incomplete`: none. `failed`: none. `unparsed: []`.
- `exists`: the defers of `estimate-case-build-checks-the-finished-case` (647), `rule-prespec-onward` (648) and `estimate-ask-searches-at-prespec` (649) found their pages.
- `near`: `lesson-agents-sendmessage-to-a-running-subagent-waits-for-its-next-tool-round` is marked `near: lesson-sendmessage-answers-open-a-turn-of-their-own` — both are about when a SendMessage reaches a case-guppi, one running, one finished.
- Failed Estimates: `estimate-synthesis-clusters` (L1), `estimate-ask-searches-at-prespec` (deferred by 649), `estimate-case-build-checks-the-finished-case` (deferred by 647).
- Stale defers (lint): `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239; `rule-prespec-judges-the-spec-whole` 1 time since case 643; `rule-subagent-guppi` 31 times since case 29.
- Lint: 48 finding lines — 5 `deferred`, 43 `unread` (40 pending, 3 failed); exit 2. The handoff gives 25 finding lines before the work.
- Handoff instruction 1: the 4 `replace` pairs of 644.1 and the 4 of 645.5 on `rule-spec-write` each hit their anchor once on the page before `generate`, and once in sequence in either order of the two Cases; both entries applied.
- Handoff instruction 2: the handoff counts eleven pairs in 645.1 on `rule-case-build`; the yaml entry holds 12 `replace` pairs, each anchor hit once, applied. After the render, `.claude/agents/case-guppi.md` carries `tools: Read, Grep, Glob, Write, Edit` and `permissionMode: acceptEdits`.
- Handoff instruction 3: `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` deleted and moved to `vault/archive/migration/2026-10-05/0311/`; its slug stands in `rule-case-check` only in History lines.
- Handoff instruction 4: the six Estimates of `rule-spec-write` took their Criteria from the entries of 644.2–644.7; no entry of 645.5 names them.
- Handoff instruction 5: after the render `vault/wiki/case-schema.md` holds one four-backtick block tagged `case`; `uv run pytest tests/test_case_schema.py` printed 2 passed, none skipped.
- `vault/raw/2026-10-05/0311/spec.md` L1319–L1367 hold 7 unticked boxes inside the quoted example of Case 646 (`entity-cart`, `entity-checkout`, `estimate-checkout-orders-the-steps`, `estimate-cart-renders-in-time`, `src/cart/view.py`); they are example text.
- Read beyond the frame: a Grep of `vault/raw/2026-10-05/0311/ledger.md` printed its lines 2–6 (decision lines of 644.1–644.4) beside the count of its lines; the `Work` line needed only the count and the lines the yaml does not account for. The handoff did not ask for it.
- MOC candidates: none raised. Contradictions: none found.

## Next session

### Cases

- Remove the old path of `guppi casecheck --subagent` (the answer text, `write_case_files`) once `estimate-case-build-writes-the-case` passes live (handoff, For the next session).
- Remove the skip of `tests/test_case_schema.py` after `estimate-case-protocol-example-passes-the-check` passes (handoff, For the next session).
- `orchestration.md` still calls the reply of `case-guppi` "the answer"; two lessons of `insight-workflow-case-schema-silent-on-what-the-scripts-accept` are about forms the main agent writes there (handoff, For the next session).
- Whether a guard stops a second agent from overwriting the file of a Case another agent holds (handoff, For the next session).
- `estimate-synthesis-clusters` failed (L1).
- `estimate-ask-searches-at-prespec` failed, deferred by 649.
- `estimate-case-build-checks-the-finished-case` failed, deferred by 647.

### Work

- `estimate-spec-write-answers-a-refusal`
- `estimate-spec-write-copies-the-ratified-case`
- `estimate-spec-write-checks-the-written-case`
- `estimate-spec-write-writes-a-defer`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-spec-write-removes-a-superseded-case`
- `estimate-spec-write-exits-2-on-an-error`
- `estimate-spec-write-tells-each-reason-once`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- `estimate-case-check-refuses-a-changed-case-file`
- `estimate-spec-write-refuses-a-changed-case-file`
- `estimate-orchestration-shows-the-built-case`
- `estimate-case-check-refuses-a-letter-outside-the-script`
- `estimate-case-check-notes-a-criterion-line-not-carried`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-protocol-case-form`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-build-answers-what-done-means`
- `estimate-case-build-records-the-rounds-in-recommend`
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-permissions`
- `estimate-case-protocol-example-passes-the-check`
- `estimate-prespec-confirms-the-findings-once`
- `estimate-ask-finds`
- `estimate-search-leaves-out-decisions-in-every-agent`
- `estimate-ask-query-before-a-create`
- `estimate-hi-writes-frontier`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-merges`

### Ask the person

none

## Readings at the close

- `make test`: 1192 passed, 6 skipped.
- `make lint`: 48 finding lines (5 `deferred`, 43 `unread`), exit 2.
- Pages under `vault/wiki/`: decisions 1114, entities 4, estimates 214, insights 30, lessons 81, rules 79. Under `vault/archive/`: 838 `.md` files before `guppi archive`.
